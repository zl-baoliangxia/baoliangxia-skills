#!/usr/bin/env python3
"""Create a wan3.0-video generation through CanvasMind Agent Gateway."""

import argparse

from _common import GatewayError, fail, upload_ref
from _generation import add_transport_args, append_if_present, submit, upload_refs, wan_duration


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", help="Prompt text; forwarded unchanged")
    parser.add_argument("--duration", type=wan_duration)
    parser.add_argument("--aspect-ratio", choices=("adaptive", "16:9", "4:3", "1:1", "3:4", "9:16"))
    parser.add_argument("--resolution", choices=("480P", "720P", "1080P"))
    parser.add_argument("--image-upload-id", help="General guide image; not an explicit first/last-frame role")
    parser.add_argument("--reference-image-id", action="append", default=[])
    parser.add_argument("--reference-video-id", action="append", default=[])
    parser.add_argument("--audio-upload-id", help="One uploaded reference audio")
    add_transport_args(parser)
    return parser.parse_args()


def main():
    args = parse_args()
    if len(args.reference_image_id) > 10:
        raise ValueError("wan3.0-video accepts at most 10 reference images")
    if len(args.reference_video_id) > 5:
        raise ValueError("wan3.0-video accepts at most 5 reference videos")
    payload = {"model": "wan3.0-video", "prompt": args.prompt}
    append_if_present(payload, "duration", args.duration)
    append_if_present(payload, "aspectRatio", args.aspect_ratio)
    append_if_present(payload, "resolution", args.resolution)
    if args.image_upload_id:
        payload["imageUrl"] = upload_ref(args.image_upload_id)
    append_if_present(payload, "referenceImages", upload_refs(args.reference_image_id))
    append_if_present(payload, "referenceVideos", upload_refs(args.reference_video_id))
    if args.audio_upload_id:
        payload["audio"] = upload_ref(args.audio_upload_id)
    submit("videos", payload, args)


if __name__ == "__main__":
    try:
        main()
    except (GatewayError, ValueError) as exc:
        fail(str(exc))
