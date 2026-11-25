# One Line to Stop the Scroll

[![rank](https://make.fun/badge/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425/UltraViewer/one-line-stop-the-scroll/rank.svg)](https://make.fun/bounty/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425)
[![reward](https://make.fun/badge/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425/UltraViewer/one-line-stop-the-scroll/reward.svg)](https://make.fun/bounty/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425)
[![make.fun](https://make.fun/badge/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425.svg)](https://make.fun/bounty/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425)

Entry for the [make.fun](https://make.fun/bounty/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425) bounty **One Line to Stop the Scroll** — one line of text, at most 200 characters, that makes a stranger stop scrolling and smile.

## The line

> Your thumb has traveled further today than most people walk in a week — give it a rest, it earned the view.

## How it works

`main.py` (Python 3.13, stdlib only, no network) reads `entry.txt`, validates it against the sealed gate (UTF-8 text, 1–200 characters, not only whitespace), and writes the exact bytes to `/output/entry.txt`, then reads the output back and verifies it matches byte for byte.

```sh
python3 main.py
# wrote /output/entry.txt: 107 chars, sha256 718c8ceb5c782861a5dea2d79b157a550ded0d36ab54e9b136b59d527b861a52
# read-back OK: Your thumb has traveled further today than most people walk in a week — give it a rest, it earned the view.
```

Deterministic: repeated runs produce identical output bytes.
