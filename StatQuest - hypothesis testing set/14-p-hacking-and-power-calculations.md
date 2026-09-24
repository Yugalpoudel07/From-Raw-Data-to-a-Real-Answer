[⏮️ **Previous: 13 — FDR and Benjamini–Hochberg**](13-fdr-benjamini-hochberg.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 15 — Type I Errors** ⏭️](15-type-1-errors.md)

---

# 14: p-hacking and Power Calculations

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> The most tempting kind of p-hacking is the innocent-looking one: **p = 0.06, so "let's just add a few more samples."** It feels like being thorough, but you've given the test a second chance to cross 0.05 — and it only ever gets extra chances in one direction. The cure is to **decide the sample size before you start, with a power analysis, and then stick to it.** If the result misses, you don't top up the old experiment; you design a new, properly powered one.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Trap: Topping Up

```text
   Planned: 30 per group.   Result: p = 0.06   "so close!"

   add 5 more  ->  p = 0.07
   add 5 more  ->  p = 0.052
   add 5 more  ->  p = 0.048   STOP.  "Significant!"

   You stopped BECAUSE it crossed 0.05.
   If it had stayed above, you would have kept going.
```

Under the null, p-values wander randomly as data arrive. Keep checking and stop the first time it dips below 0.05, and you'll "win" far more often than 5% of the time.

**Simulated, with no real effect at all:** checking a two-sample t-test after every 10 users per group, up to 100 per group (10 looks), and stopping at the first p < 0.05 gives a false-positive rate of about **19–20%** — roughly four times the 5% you think you're running.

---

### 2. The Fix: Fix n in Advance

```text
   1. Choose the smallest effect worth detecting    (e.g. d = 0.5)
   2. Choose alpha and power                         (0.05, 0.80)
   3. Power analysis -> n                            (64 per group)
   4. Collect exactly n.  Test once.
   5. p <= 0.05 -> reject.   p > 0.05 -> fail to reject.  Done.

   Want to follow up a near miss?
   -> new experiment, new power analysis, FRESH data.
```

A near miss is useful information for designing the next experiment (it gives you a rough effect-size estimate), not a reason to extend the current one.

---

### 3. Low Power + Significance Filter = Exaggerated Effects

Power calculations aren't only about missing effects. When an **underpowered** study does reach p < 0.05, it almost always **overestimates** the effect, because only the lucky high draws make it over the line.

```text
   true effect d = 0.2, n = 20 per group (power ~ 9%)

   estimates from many repeats:
       |          ___
       |        /     \
       |      /    |    \
       |   __/     |     \__ |###      <- only these cross p < 0.05
       +-----------+---------+------
                  0.2       ~0.64
                 truth    significance threshold for d-hat

   Average estimate among the "significant" ones: d ≈ 0.8  (4x too big)
```

This is sometimes called the **winner's curse**. It's why exciting results from small studies often shrink or vanish when someone repeats them — and why a power analysis is also a defence against believing your own lucky result.

---

### 4. The Honest Workflow

| Step | Why |
| :--- | :--- |
| Write the plan (metric, test, α, effect size) | Removes forks in the road |
| Power analysis → $n$ | Enough data to detect what matters; no topping up |
| Collect $n$, test once | α means what it says |
| Report effect size + CI, not just p | Readers see magnitude and uncertainty |
| Near miss → new powered study | Keeps the new test's error rates clean |
| Genuinely need to monitor continuously? | Use a method designed for it (sequential tests, alpha spending) — roadmap Month 4 |

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Peeking** | The #1 A/B testing mistake in industry | Checking the dashboard daily and stopping on the first green day (roadmap Week 17 simulation) |
| **Fixed horizon** | Standard experiment design | "Run for 14 days / 60,000 users, then analyse once" |
| **Winner's curse** | Launched features underperform their test | The measured +4% lift becomes +1% after launch |
| **Early stopping (training)** | Different thing, same flavour of bias | Picking the best epoch on validation makes the validation score optimistic |

---

### 6. Check Your Understanding

**Q1: Your test was planned for 2,000 users per arm and ended at p = 0.058. What's the right next step?**
<details>
<summary><b>Reveal Answer</b></summary>

Report it as not significant at 0.05, along with the estimated effect and its confidence interval. If the effect would still matter, use it to plan a new experiment with a power analysis and fresh users — don't extend the current one.
</details>

**Q2: Why does stopping as soon as p < 0.05 inflate false positives, even if every individual test is valid?**
<details>
<summary><b>Reveal Answer</b></summary>

Each look is another chance for noise to cross the threshold, and you only stop on crossings — never on non-crossings. With 10 looks the chance that *some* look crosses 0.05 under the null is about 20%, not 5%.
</details>

**Q3: A small pilot (n = 15 per group) finds a large, significant effect. Why be cautious?**
<details>
<summary><b>Reveal Answer</b></summary>

With low power, results that reach significance are biased toward overestimates (winner's curse). The true effect is probably smaller. Plan the confirmation study assuming a smaller effect than the pilot suggests.
</details>

---

### 📺 Source

* **Video:** [p-hacking and power calculations](https://www.youtube.com/watch?v=UFhJefdVCjE)

---

[⏮️ **Previous: 13 — FDR and Benjamini–Hochberg**](13-fdr-benjamini-hochberg.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 15 — Type I Errors** ⏭️](15-type-1-errors.md)
