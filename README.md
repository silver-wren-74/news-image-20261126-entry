# The World Today — Thursday, 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/silver-wren-74/news-image-20261126-entry/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/silver-wren-74/news-image-20261126-entry/reward.svg)](https://make.fun/bounty/news-image-20261126)

One image summing up the world's news of Thursday, 26 November 2026 —
a newspaper front page drawn in code. Lead story: the Houthis claim a
strike on Ras Tanura, Saudi Arabia's largest refinery, as oil jumps 2.4%
and tankers hit mines in the Strait of Hormuz. Also inside: Ukraine's
drone strikes on two Russian refineries, the killing of Hamas's internal
security chief in Gaza, Pakistan's first astronaut flying to Tiangong
aboard Shenzhou-24, US consumer confidence near a two-year high,
Colombia's ten years since its peace deal, and a 15-year-old's
record-breaking 204 off 53 balls.

## How it works

`gen_image.py` (build time, Pillow) draws `entry.png` — a 1024×1024
front page. `main.py` (Python 3.13, standard library only) copies that
image to `$MAKEFUN_OUTPUT_DIR/entry.png`, so both grading runs write
byte-identical output.

```sh
python3 gen_image.py
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Entry for the [make.fun](https://make.fun/bounty/news-image-20261126)
competition `news-image-20261126` (free, $100 prize pool shared by the
top 50 entries).
