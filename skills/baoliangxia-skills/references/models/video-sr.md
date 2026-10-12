# `video-sr`

The model exists and is enabled, but the current Agent Gateway contract cannot create a valid super-resolution task.

## 参数拼装

The configured resolution default would be `720p`, but this model stays fail-closed and must not be submitted.

The upstream operation needs one source video plus target resolution `720p`, `1080p`, `2k`, or `4k`. CanvasMind's internal SR executor additionally requires a structured `superResolution` payload containing source URL and source-duration metadata.

## 不可用能力

`scripts/create_model_generation.py` deliberately fails before network submission for `video-sr`. The public Agent Gateway video request currently has no `superResolution` field, so forwarding only `referenceVideos` would create an invalid task. Do not use the generic video script as a workaround.

