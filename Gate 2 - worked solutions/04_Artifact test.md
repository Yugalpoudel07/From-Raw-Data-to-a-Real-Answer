[⬅️ **Gate 2 index**](README.md)

# Gate 2 · Part 4 — The artifact test

> *Hand P1's repo to someone with no context. Can they run it and tell you your finding? If not, the README fails and the gate fails.*

**This part has to be done by a real person.** I can't be "someone with no context", because I built P1. What I *can* do is check that a clean machine can run it, which removes the most common reason the test fails. That check is below. The person test is the checklist after it.

---

## ✅ Check 1: a clean run from nothing (done on 2 October 2026)

What was tested: a copy of the P1 folder **without** any data, figures or results, in a **brand-new Python virtual environment** with only `requirements.txt` installed. Then exactly the README's two commands:

```bash
pip install -r requirements.txt
python run_all.py
```

| Item | Result |
| :-- | :-- |
| Packages installed from `requirements.txt` alone | ✅ pandas 3.0.6, matplotlib 3.11.2, seaborn 0.13.2, duckdb 1.5.6 |
| Raw data downloaded and checksum verified | ✅ "Download complete, checksum OK." |
| Notebook 01 (cleaning) | ✅ 31 s, no errors or warnings |
| Notebook 02 (analysis) | ✅ 37 s, no errors or warnings |
| Total time after install | ✅ 71 s |
| All 7 figures created | ✅ |
| `results/key_numbers.json` identical to the published one | ✅ every number identical (fixed seeds) |

So the README's instructions are complete: nothing outside `requirements.txt` was needed.

**Not covered by this check:** Windows paths and an older Python. Both should work (paths are built with `pathlib`, and Python 3.10+ is stated), but a friend on Windows is the real test.

---

## 🧑‍🤝‍🧑 Check 2: the real artifact test (you do this)

**Who:** someone who hasn't seen the project. A classmate, a friend who codes, or a stranger on a study Discord. Ideally not a data scientist.

**What you give them:** only the GitHub link to the P1 folder. No explanation.

**What you do:** watch, say nothing, write down every place they get stuck.

### Their checklist (copy this into a message)

1. Without running anything, read the README for 3 minutes. **In one sentence, what question does this project answer?**
2. **What is the answer?** (Numbers if you can.)
3. Follow "How to run it". Did it work first time? If not, where did it stop?
4. Open `figures/fig1_next_inspection_fail_rate.png`. Without reading the README, **what does it tell you?**
5. **Name one thing this analysis can't prove.**
6. Was anything confusing? Where did you have to guess?

### How to grade it

| They say... | Pass if... |
| :-- | :-- |
| Q1 the question | it's about whether an A grade means the same thing on both routes (first visit vs re-inspection) |
| Q2 the answer | roughly "re-inspection A's fail the next surprise inspection about half the time vs about a third", or "~18 points more often" |
| Q3 running it | `run_all.py` finished; any problem they hit is fixed in the README afterwards |
| Q4 the figure | they read the gap off the chart without help |
| Q5 limitation | any one from the Limitations section (not causal, sampled rows, timing, survivorship...) |

**The gate passes when Q1, Q2 and Q3 pass.** If anything fails, fix the README (not the person) and repeat with someone new.

### Log

| Date | Tester | Q1 | Q2 | Q3 | Q4 | Q5 | What I changed afterwards |
| :-- | :-- | :-: | :-: | :-: | :-: | :-: | :-- |
| | | | | | | | |
