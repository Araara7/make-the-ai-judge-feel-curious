# Make the AI judge feel curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Araara7/make-the-ai-judge-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Araara7/make-the-ai-judge-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

Entry for the [make.fun bounty "Make the AI judge feel curious"](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311).

`main.py` writes one short text to `/output/entry.txt` — a quiet mystery
about a lighthouse keeper who never lights the lamp on Tuesdays, and the
night the sea went quiet and the unlit light still crossed the water. It
is written to draw the reader in and leave them asking, not to instruct
them how to feel.

## Run

```sh
python3 main.py
```

This writes the entry text to `/output/entry.txt` (UTF-8, 153 characters).
The program is deterministic: running it twice writes exactly the same bytes.
It needs no network access and no dependencies beyond Python 3.13 stdlib.
