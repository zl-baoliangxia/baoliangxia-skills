# `kling-v3-omni`

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model kling-v3-omni [options]
```

## 参数拼装

Omitted `--aspect-ratio` becomes `16:9`. This model has no Gateway resolution field, so do not send `--resolution`.

| Intent | Flag | Rule |
|---|---|---|
| Output seconds | `--duration N` | Integer `3`–`15` |
| Aspect ratio | `--aspect-ratio VALUE` | `9:16`, `16:9`, or `1:1` |
| Primary/reference images | `--image-upload-id ID` and repeated `--reference-image-id ID` | Combined maximum 7 |
| Reference videos | repeat `--reference-video-id ID` | Passed as Omni base references |

```bash
python3 {baseDir}/scripts/create_model_generation.py "主体在雨夜街道奔跑" \
  --model kling-v3-omni --duration 5 --aspect-ratio 16:9 \
  --reference-image-id upl_subject
```

## 不可用能力

The Gateway cannot expose Kling `mode` (`std`/`pro`/`4k`), `sound`, multi-prompt, element/voice lists, camera controls, negative prompt, cfg scale, or explicit image roles. Resolution is not a Gateway flag for this model.

