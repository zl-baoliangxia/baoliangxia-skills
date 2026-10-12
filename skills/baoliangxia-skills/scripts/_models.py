#!/usr/bin/env python3
"""Static CanvasMind media-model catalog used by the skill scripts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelSpec:
    kind: str
    reference: str
    ratios: tuple[str, ...] = ()
    resolutions: tuple[str, ...] = ()
    duration_min: int | None = None
    duration_max: int | None = None
    duration_values: tuple[int, ...] = ()
    duration_required: bool = False
    allow_adaptive_duration: bool = False
    max_outputs: int | None = None
    output_formats: tuple[str, ...] = ()
    max_input_images: int | None = None
    max_reference_images: int | None = None
    max_reference_videos: int | None = None
    allow_audio: bool = False
    unavailable_reason: str | None = None
    # Applied only when the caller omits the flag. A value stated in the model
    # document wins. Otherwise the ratio is 16:9, and the resolution is the
    # supported tier nearest 720p, spelled exactly as that model requires.
    default_ratio: str | None = None
    default_resolution: str | None = None
    # Used instead of default_ratio when an image or video is attached.
    default_ratio_with_media: str | None = None
    # Some image-driven routes cannot accept a ratio. Leave it unset then.
    omit_default_ratio_with_media: bool = False


IMAGE_RATIOS = ("9:16", "16:9", "3:4", "4:3", "1:1", "21:9", "3:2", "2:3")
IMAGE_2_RATIOS = IMAGE_RATIOS + ("5:4", "4:5", "9:21", "2:1", "1:2", "1:3", "3:1")
VIDEO_RATIOS = ("9:16", "16:9", "3:4", "4:3", "1:1")
WAN_RATIOS = ("adaptive", "9:16", "16:9", "4:3", "3:4", "1:1")


MODELS: dict[str, ModelSpec] = {
    "doubao-seedream-4.5": ModelSpec(
        "images", "references/models/doubao-seedream-4.5.md",
        ratios=IMAGE_RATIOS, resolutions=("2K", "4K"), max_outputs=15, max_input_images=14,
        default_ratio="1:1", default_resolution="2K",
    ),
    "doubao-seedream-5.0-lite": ModelSpec(
        "images", "references/models/doubao-seedream-5.0-lite.md",
        ratios=IMAGE_RATIOS, resolutions=("2K", "3K", "4K"), max_outputs=15,
        output_formats=("png", "jpeg"), max_input_images=14,
        default_ratio="1:1", default_resolution="2K",
    ),
    "doubao-seedream-5.0-pro": ModelSpec(
        "images", "references/models/doubao-seedream-5.0-pro.md",
        ratios=IMAGE_RATIOS, resolutions=("1K", "2K"), output_formats=("png", "jpeg"),
        max_input_images=10, default_ratio="1:1", default_resolution="2K",
    ),
    "zl-ooe-3.1-flash-image": ModelSpec(
        "images", "references/models/nanobanana-2.md",
        ratios=("1:1", "3:4", "4:3", "16:9", "9:16", "21:9", "3:2", "2:3", "5:4", "4:5"),
        max_input_images=3, default_ratio="16:9",
    ),
    "zl-pep-image-2": ModelSpec(
        "images", "references/models/zl-pep-image-2.md",
        ratios=IMAGE_2_RATIOS, resolutions=("1K", "2K", "4K"), max_outputs=10,
        max_input_images=3, default_ratio="16:9", default_resolution="1K",
    ),
    "zl-pep-image-2-async": ModelSpec(
        "images", "references/models/zl-pep-image-2.md",
        ratios=IMAGE_2_RATIOS, resolutions=("1K", "2K", "4K"), max_outputs=10,
        max_input_images=3, default_ratio="16:9", default_resolution="1K",
    ),
    "doubao-seedance-2.0": ModelSpec(
        "videos", "references/models/doubao-seedance-2.0.md",
        ratios=VIDEO_RATIOS, resolutions=("480p", "720p", "1080p"), duration_min=1,
        max_reference_images=30, max_reference_videos=10, allow_audio=True,
        default_ratio="16:9", default_resolution="720p",
    ),
    "doubao-seedance-2.0-fast": ModelSpec(
        "videos", "references/models/doubao-seedance-2.0.md",
        ratios=VIDEO_RATIOS, resolutions=("480p", "720p"), duration_min=1,
        max_reference_images=30, max_reference_videos=10, allow_audio=True,
        default_ratio="16:9", default_resolution="720p",
    ),
    "doubao-seedance-2.0-mini": ModelSpec(
        "videos", "references/models/doubao-seedance-2.0.md",
        ratios=VIDEO_RATIOS, resolutions=("480p", "720p"), duration_min=1,
        max_reference_images=30, max_reference_videos=10, allow_audio=True,
        default_ratio="16:9", default_resolution="720p",
    ),
    "doubao-seedance-2.5": ModelSpec(
        "videos", "references/models/doubao-seedance-2.5.md",
        ratios=VIDEO_RATIOS + ("adaptive",), resolutions=("480p", "720p", "1080p"),
        duration_min=4, duration_max=30, allow_adaptive_duration=True,
        max_reference_images=30, max_reference_videos=10, allow_audio=True,
        default_ratio="adaptive", default_resolution="720p",
    ),
    "happyhorse-1.1": ModelSpec(
        "videos", "references/models/happyhorse-1.1.md",
        ratios=("9:16", "16:9", "1:1"), resolutions=("720P", "1080P"),
        duration_min=1, max_reference_images=20, max_reference_videos=20,
        default_ratio="16:9", default_resolution="720P", omit_default_ratio_with_media=True,
    ),
    "jielan-video": ModelSpec(
        "videos", "references/models/jielan-video.md",
        ratios=VIDEO_RATIOS, resolutions=("720p", "1080p", "2k", "4k"), duration_min=1,
        max_reference_images=30, max_reference_videos=10, allow_audio=True,
        default_ratio="16:9", default_resolution="720p",
    ),
    "jielan-video-lite": ModelSpec(
        "videos", "references/models/jielan-video.md",
        ratios=VIDEO_RATIOS, resolutions=("720p", "1080p"), duration_min=1,
        max_reference_images=30, max_reference_videos=10, allow_audio=True,
        default_ratio="16:9", default_resolution="720p",
    ),
    "jielan-video-mini": ModelSpec(
        "videos", "references/models/jielan-video.md",
        ratios=VIDEO_RATIOS, resolutions=("720p", "1080p"), duration_min=1,
        max_reference_images=30, max_reference_videos=10, allow_audio=True,
        default_ratio="16:9", default_resolution="720p",
    ),
    "kling-v3-omni": ModelSpec(
        "videos", "references/models/kling-v3-omni.md",
        ratios=("9:16", "16:9", "1:1"), duration_min=3, duration_max=15,
        max_reference_images=7, max_reference_videos=7, default_ratio="16:9",
    ),
    "MiniMax-H3": ModelSpec(
        "videos", "references/models/minimax-h3.md",
        ratios=("adaptive", "9:16", "16:9", "4:3", "3:4", "1:1", "21:9"),
        resolutions=("768P", "2K"), duration_min=4, duration_max=15, duration_required=True,
        max_reference_images=30, max_reference_videos=10, allow_audio=True,
        default_ratio="16:9", default_resolution="768P", default_ratio_with_media="adaptive",
    ),
    "video-sr": ModelSpec(
        "videos", "references/models/video-sr.md", resolutions=("720p", "1080p", "2k", "4k"),
        max_reference_videos=1, default_resolution="720p",
        unavailable_reason=(
            "Agent Gateway 的通用视频创建接口尚不能传递 video-sr 所需的 superResolution 元数据；"
            "直接提交会在执行阶段失败"
        ),
    ),
    "vidu": ModelSpec(
        "videos", "references/models/vidu-solutions.md", max_reference_videos=1,
    ),
    "vidu-short_drama_ads_fast": ModelSpec(
        "videos", "references/models/vidu-short-ads.md",
        ratios=("16:9", "9:16", "3:4", "4:3"), resolutions=("720p",),
        duration_values=tuple(range(4, 16)) + (20, 25, 30), max_reference_images=20,
        max_reference_videos=1, default_ratio="16:9", default_resolution="720p",
    ),
    "viduq2-pro": ModelSpec(
        "videos", "references/models/vidu-solutions.md",
        resolutions=("540p", "720p", "1080p"), max_reference_images=1,
        default_resolution="720p",
    ),
    "viduq2-turbo": ModelSpec(
        "videos", "references/models/vidu-solutions.md",
        resolutions=("540p", "720p", "1080p"), max_reference_images=1,
        default_resolution="720p",
    ),
    "viduq3-ad": ModelSpec(
        "videos", "references/models/vidu-q3.md", ratios=VIDEO_RATIOS,
        resolutions=("720p", "1080p"), duration_min=1, duration_max=16,
        max_reference_images=7, default_ratio="16:9", default_resolution="1080p",
    ),
    "viduq3-mix": ModelSpec(
        "videos", "references/models/vidu-q3.md", ratios=VIDEO_RATIOS,
        resolutions=("540p", "720p", "1080p"), duration_min=1, duration_max=16,
        max_reference_images=7, default_ratio="16:9", default_resolution="1080p",
    ),
    "wan3.0-video": ModelSpec(
        "videos", "references/models/wan3.0-video.md", ratios=WAN_RATIOS,
        resolutions=("480P", "720P", "1080P"), duration_min=2, duration_max=30,
        allow_adaptive_duration=True, max_reference_images=10, max_reference_videos=5,
        allow_audio=True, default_ratio="adaptive", default_resolution="1080P",
    ),
    "wan3.0-video-prime": ModelSpec(
        "videos", "references/models/wan3.0-video.md", ratios=WAN_RATIOS,
        resolutions=("480P", "720P", "1080P"), duration_min=2, duration_max=30,
        allow_adaptive_duration=True, max_reference_images=10, max_reference_videos=5,
        allow_audio=True, default_ratio="adaptive", default_resolution="1080P",
    ),
}


def catalog_rows() -> list[dict[str, str | bool | None]]:
    return [
        {
            "model": model,
            "kind": spec.kind,
            "reference": spec.reference,
            "available": spec.unavailable_reason is None,
            "defaultAspectRatio": spec.default_ratio,
            "defaultResolution": spec.default_resolution,
        }
        for model, spec in MODELS.items()
    ]
