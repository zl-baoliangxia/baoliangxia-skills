#!/usr/bin/env python3
"""Create an image generation through the baoliangxia REST API."""

import argparse
import uuid

from _common import GatewayError, api_headers, base_url, fail, generation_result, print_json, request_json, upload_ref


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", help="Prompt text; forwarded unchanged")
    parser.add_argument("--model", default="doubao-seedream-4.5")
    parser.add_argument("--aspect-ratio", default="1:1")
    parser.add_argument("--resolution", default="2k")
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--output-format", default="png")
    parser.add_argument("--input-upload-id", action="append", default=[])
    parser.add_argument("--idempotency-key", default=None)
    parser.add_argument("--base-url", default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    payload = {
        "model": args.model,
        "prompt": args.prompt,
        "aspectRatio": args.aspect_ratio,
        "resolution": args.resolution,
        "n": args.n,
        "outputFormat": args.output_format,
    }
    if args.input_upload_id:
        payload["inputImages"] = [upload_ref(value) for value in args.input_upload_id]
    idempotency_key = args.idempotency_key or str(uuid.uuid4())
    response = request_json(
        "POST",
        base_url(args.base_url) + "/api/v1/images/generations",
        body=payload,
        headers=api_headers(idempotency_key),
    )
    result = generation_result(response)
    result["idempotencyKey"] = idempotency_key
    print_json(result)


if __name__ == "__main__":
    try:
        main()
    except (GatewayError, ValueError) as exc:
        fail(str(exc))

