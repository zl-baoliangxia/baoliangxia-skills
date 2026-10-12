#!/usr/bin/env python3
"""Query a generation once or wait for a terminal state and download outputs."""

import argparse
import time
from pathlib import Path

from _common import GatewayError, api_headers, base_url, download_outputs, fail, output_urls, print_json, request_json, unwrap_data


TERMINAL_STATES = {"completed", "failed", "stopped"}


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("generation_id")
    parser.add_argument("--wait", action="store_true")
    parser.add_argument("--interval", type=float, default=20)
    parser.add_argument("--timeout", type=float, default=1200)
    parser.add_argument("--output-dir")
    parser.add_argument("--base-url", default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    if args.interval < 0 or args.timeout < 0:
        raise GatewayError("--interval and --timeout must be non-negative")
    url = base_url(args.base_url) + f"/api/v1/generations/{args.generation_id}"
    deadline = time.monotonic() + args.timeout
    while True:
        response = unwrap_data(request_json("GET", url, headers=api_headers()))
        if not isinstance(response, dict):
            raise GatewayError("Generation response must be a JSON object")
        status = str(response.get("status", "")).lower()
        if not args.wait or status in TERMINAL_STATES:
            break
        if time.monotonic() >= deadline:
            response = dict(response)
            response["timedOut"] = True
            break
        time.sleep(min(args.interval, max(0, deadline - time.monotonic())))

    result = dict(response)
    if result.get("status", "").lower() == "completed" and args.output_dir:
        urls = output_urls(result.get("outputs"))
        result["downloaded"] = download_outputs(urls, Path(args.output_dir).expanduser())
    print_json(result)


if __name__ == "__main__":
    try:
        main()
    except GatewayError as exc:
        fail(str(exc))
