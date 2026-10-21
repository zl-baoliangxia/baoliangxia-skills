# `doubao-seedance-2.5`

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model doubao-seedance-2.5 [options]
```

## 参数拼装

Omitted `--aspect-ratio` becomes `adaptive`, the documented default. Omitted `--resolution` becomes `720p`, also the documented default. Text and reference video may still use an explicit ratio. First-frame, multimodal, edit, and extend tasks only accept `adaptive`. Explicit flags win.

| Intent | Flag | Rule |
|---|---|---|
| Output seconds | `--duration N` | `4`–`30`, or `-1` for adaptive |
| Aspect ratio | `--aspect-ratio VALUE` | `adaptive`, `9:16`, `16:9`, `3:4`, `4:3`, or `1:1` |
| Resolution | `--resolution VALUE` | Database values: `480p`, `720p`, `1080p` |
| Primary image | `--image-upload-id ID` | General driving image |
| Reference images | repeat `--reference-image-id ID` | At most 30 uploads |
| Reference videos | repeat `--reference-video-id ID` | At most 10; total ≤30 seconds |
| Reference audio | repeat `--reference-audio-id ID` | Up to 10 audio uploads; legacy `--audio-upload-id` remains supported for one |
| Generated audio | `--option generate_audio=true|false` | Defaults to `true`; controls generated sound, not reference audio |
| Reference task type | `--option omni_reference_task_type=reference|edit|extend` | Defaults to `reference` when media is attached; omit for text-only |
| Watermark | `--watermark true|false` | Defaults to `false` |

```bash
python3 {baseDir}/scripts/create_model_generation.py "扩展镜头并保持人物一致" \
  --model doubao-seedance-2.5 --duration -1 --resolution 720p \
  --reference-video-id upl_video
```

## 不可用能力

The Gateway supports the listed task type and audio controls. First/last-frame roles, MOV output, web search, and provider callback controls remain unavailable. For an edit or extend task, pass its task type explicitly.

