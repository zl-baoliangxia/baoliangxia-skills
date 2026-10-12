#!/usr/bin/env python3
"""Create the Image 2 async task using its CanvasMind database model identifier."""

import argparse

from _common import GatewayError, fail
from _generation import add_transport_args, append_if_present, bounded_int, submit, upload_refs


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", help="Prompt text; forwarded unchanged")
    parser.add_argument("--n", type=bounded_int(1, 10))
    parser.add_argument("--input-upload-id", action="append", default=[])
    add_transport_args(parser)
    return parser.parse_args()


def main():
    args = parse_args()
    payload = {"model": "zl-pep-image-2-async", "prompt": args.prompt}
    append_if_present(payload, "n", args.n)
    append_if_present(payload, "inputImages", upload_refs(args.input_upload_id))
    submit("images", payload, args)


if __name__ == "__main__":
    try:
        main()
    except (GatewayError, ValueError) as exc:
        fail(str(exc))
