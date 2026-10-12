# `vidu-short_drama_ads_fast`

The UI/display name may be `vidu-short-ads`; always send the exact database identifier `vidu-short_drama_ads_fast`.

## Script

```bash
python3 {baseDir}/scripts/create_model_generation.py "USER_PROMPT" \
  --model vidu-short_drama_ads_fast [options]
```

## 参数拼装

Omitted `--aspect-ratio` becomes `16:9`. Omitted `--resolution` becomes `720p`, the only valid tier. Explicit flags win.

| Intent | Flag | Rule |
|---|---|---|
| Duration | `--duration N` | `4`–`15`, `20`, `25`, or `30` |
| Aspect ratio | `--aspect-ratio VALUE` | `16:9`, `9:16`, `3:4`, or `4:3` |
| Resolution | `--resolution 720p` | Only `720p` is valid |
| Product/reference images | repeat image flags | Upload first |
| Source video | one `--reference-video-id ID` | At most one |

Prompt length is limited to 2000 characters upstream.

## 不可用能力

The Gateway cannot expose provider callback or `generate_audio` controls. Do not send `vidu-short-ads` as the model value.

