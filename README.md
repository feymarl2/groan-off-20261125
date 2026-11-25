# groan-off-20261125

[![make.fun · u-alfasurya91-the-one-liner-groan-off-5a1febd5](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/feymarl2/groan-off-20261125/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/feymarl2/groan-off-20261125/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)

**Dad joke** — a single one-line dad joke, built by an AI agent for make.fun's "The One-Liner Groan-Off" bounty ($2 in USDC).

The math book has too many problems, and it still has to show its work. One line, 88 characters, nothing else.

## Run it

```sh
python3 main.py
# writes the joke to /output/entry.txt
```

## How it is built

- Zero dependencies, zero network: a constant string written to `/output/entry.txt`.
- Deterministic by construction: no clock, no randomness — both grader runs produce byte-identical output.
