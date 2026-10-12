#!/usr/bin/env python3
"""Shared submission helpers for model-specific generation scripts."""

from __future__ import annotations

import argparse
import uuid
from typing import Any

from _common import api_headers, base_url, generation_result, print_json, request_json, upload_ref


def add_transport_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--idempotency-key", default=None)
    parser.add_argument("--base-url", default=None)


def append_if_present(payload: dict[str, Any], key: str, value: Any) -> None:
    if value is not None and value != []:
        payload[key] = value


def upload_refs(values: list[str]) -> list[dict[str, str]]:
    return [upload_ref(value) for value in values]


def bounded_int(minimum: int, maximum: int):
    def parse(value: str) -> int:
        parsed = int(value)
        if not minimum <= parsed <= maximum:
            raise argparse.ArgumentTypeError(f"must be between {minimum} and {maximum}")
        return parsed
    return parse


def wan_duration(value: str) -> int:
    parsed = int(value)
    if parsed != -1 and not 2 <= parsed <= 30:
        raise argparse.ArgumentTypeError("must be -1 or between 2 and 30")
    return parsed


def submit(kind: str, payload: dict[str, Any], args: argparse.Namespace) -> None:
    idempotency_key = args.idempotency_key or str(uuid.uuid4())
    response = request_json(
        "POST",
        base_url(args.base_url) + f"/api/v1/{kind}/generations",
        body=payload,
        headers=api_headers(idempotency_key),
    )
    result = generation_result(response)
    result["idempotencyKey"] = idempotency_key
    print_json(result)
