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
| Reference audio | `--audio-upload-id ID` | Supported; total ≤30 seconds |

```bash
python3 {baseDir}/scripts/create_model_generation.py "扩展镜头并保持人物一致" \
  --model doubao-seedance-2.5 --duration -1 --resolution 720p \
  --reference-video-id upl_video
```

## 不可用能力

The Gateway cannot explicitly choose `reference`/`edit`/`extend`, set `generate_audio`, assign first/last-frame roles, select MOV output, use web search, or send provider callback controls. For a request that depends on a specific task type, stop rather than infer it.

