#!/usr/bin/env python3
"""Create a doubao-seedream-4.5 image through baoliangxia Agent Gateway."""

import argparse

from _common import GatewayError, fail
from _generation import add_transport_args, append_if_present, bounded_int, submit, upload_refs


RATIOS = ("1:1", "4:3", "3:4", "16:9", "9:16", "3:2", "2:3", "21:9")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", help="Prompt text; forwarded unchanged")
    parser.add_argument("--aspect-ratio", choices=RATIOS)
    parser.add_argument("--resolution", choices=("2K", "4K"))
    parser.add_argument("--n", type=bounded_int(1, 15))
    parser.add_argument("--input-upload-id", action="append", default=[])
    add_transport_args(parser)
    return parser.parse_args()


def main():
    args = parse_args()
    output_count = args.n or 1
    if len(args.input_upload_id) > 14 or len(args.input_upload_id) + output_count > 15:
        raise ValueError("reference image count + output image count must be at most 15")
    payload = {"model": "doubao-seedream-4.5", "prompt": args.prompt}
    append_if_present(payload, "aspectRatio", args.aspect_ratio)
    append_if_present(payload, "resolution", args.resolution)
    append_if_present(payload, "n", args.n)
    append_if_present(payload, "inputImages", upload_refs(args.input_upload_id))
    submit("images", payload, args)


if __name__ == "__main__":
    try:
        main()
    except (GatewayError, ValueError) as exc:
        fail(str(exc))
