# Vidu digital-human and lip-sync solutions

Use `viduq2-pro` or `viduq2-turbo` for text-driven digital humans and `vidu` for text-driven lip sync.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model viduq2-turbo --image-upload-id upl_portrait [options]
```

## 参数拼装

Omitted `--resolution` becomes `720p` for `viduq2-pro` and `viduq2-turbo`. Those models have no aspect-ratio field. `vidu` has neither field; do not send `--aspect-ratio` or `--resolution` for it. Explicit flags win.

| Model | Required media | Optional flags | Rule |
|---|---|---|---|
| `viduq2-pro` / `viduq2-turbo` | one portrait via `--image-upload-id ID` | `--resolution 540p|720p|1080p` | Prompt is the text-driven speech; default voice is applied server-side |
| `vidu` | one source video via `--reference-video-id ID` | none | Prompt is the text-driven speech |

```bash
python3 {baseDir}/scripts/create_model_generation.py "欢迎使用我们的新品" \
  --model viduq2-turbo --resolution 720p --image-upload-id upl_portrait
```

## 不可用能力

The Gateway cannot carry Vidu `requestExtras`, so audio-driven speech, custom voice ID, speed, volume, language, ref-photo URL, and separate visual prompt are unavailable. Supplying `--audio-upload-id` would not populate Vidu's required `audio_url`, so the script rejects it.

