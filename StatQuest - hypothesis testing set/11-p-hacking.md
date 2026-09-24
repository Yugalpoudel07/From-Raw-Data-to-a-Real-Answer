[⏮️ **Previous: 10 — Power Analysis**](10-power-analysis.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 12 — False Discovery Rate** ⏭️](12-false-discovery-rate.md)

---

# 11: p-hacking — What It Is and How to Avoid It

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> **p-hacking is any way of giving yourself extra chances to get p < 0.05** and then reporting only the chance that worked. Test 20 things on pure noise and one will probably look "significant". Peek at the results and add data until p dips under 0.05. Try five ways of removing outliers and keep the one that works. Each trick is small; together they make "significant" results out of nothing. Nobody has to be dishonest for this to happen — it's the default outcome of flexible analysis.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Why It Works: Many Chances

With α = 0.05 each test on a true null has a 5% chance of a false positive. Give yourself $m$ chances:

$$ P(\text{at least one } p < 0.05) = 1 - 0.95^{m} $$

```text
   20 tests on pure random noise, alpha = 0.05

   test:   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
   p<.05?  .  .  .  .  .  .  .  .  .  .  .  .  *  .  .  .  .  .  .  .
                                             ^
                              "Drug 13 works! p = 0.03"

   P(at least one star) = 1 - 0.95^20 = 0.64
```

On average you get one false "discovery" per 20 null tests — and a 64% chance of at least one.

---

### 2. The Many Forms of p-hacking

| Form | What it looks like |
| :--- | :--- |
| **Testing many, reporting one** | 20 drugs / features / segments tested; only the significant one reaches the slide deck |
| **Adding data until significant** | p = 0.06 → "let's collect a few more" → p = 0.04 → stop |
| **Flexible analysis** | Trying different outlier rules, transformations, covariates, or tests until one crosses 0.05 |
| **Subgroup fishing** | "No effect overall… but it works for women over 40 on mobile!" |
| **Switching tails or metrics** | Two-sided p = 0.08 becomes one-sided p = 0.04; or the primary metric is quietly swapped |
| **HARKing** | *Hypothesising After the Results are Known* — presenting a post-hoc pattern as if it were predicted |

---

### 3. How to Avoid It

| Defence | How it helps |
| :--- | :--- |
| **Decide the plan before the data** — hypothesis, metric, test, α | Removes the forks in the road (pre-registration) |
| **Power analysis first** (topic 10) | Fixes $n$ in advance, so there's no "add a few more" |
| **Correct for multiple testing** | Bonferroni (below) or FDR (topics 12–13) |
| **Report everything you tested** | Readers can judge how many chances you had |
| **Treat surprising subgroup results as hypotheses** | Confirm them in a new, independent experiment |

**Bonferroni correction.** The simplest fix, and not given its own video in this set: divide the threshold by the number of tests.

$$ \alpha_{\text{per test}} = \frac{\alpha}{m} \qquad \text{20 tests: } \frac{0.05}{20} = 0.0025 $$

That brings the chance of *any* false positive across all 20 back down to about 5%. It's easy and very safe, but conservative — with many tests it also throws away real effects, which is what FDR methods improve on.

---

### 4. The Simulation to Build This Week

The roadmap's second build task. Aim to show, with your own code:

1. Generate two groups of **pure random noise** (same distribution) 20 times and run a t-test each time.
2. Record which, if any, come out with p < 0.05 — your "discovery".
3. Repeat the whole 20-test experiment many times: the fraction with at least one "discovery" should be close to **0.64**.
4. Apply Bonferroni (and Benjamini–Hochberg, topic 13) and watch the discoveries disappear.
5. Write ~200 words on what this means for every dashboard and paper you read.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Many metrics per experiment** | Dashboards track 30+ metrics | Expect 1–2 to move "significantly" by chance in every A/B test |
| **Hyperparameter search** | Trying 200 configs and reporting the best | The best validation score is optimistically biased — confirm on an untouched test set |
| **Test-set reuse** | Every look at the test set is another chance | "Tuning on the test set" is p-hacking for models (roadmap Week 10) |
| **Feature fishing** | Screening thousands of features for correlation with the target | Some correlate strongly by chance; validate on held-out data |
| **Segment slicing** | "Works for iOS users in Canada" | Treat as a new hypothesis, not a finding |

---

### 6. Check Your Understanding

**Q1: A marketing analyst tests 12 email subject lines against a control and reports "subject line 7 significantly increased opens (p = 0.04)". What should you ask?**
<details>
<summary><b>Reveal Answer</b></summary>

"How many did you test, and was there a correction?" With 12 comparisons, one p = 0.04 is quite likely by chance ($1 - 0.95^{12} \approx 0.46$). With Bonferroni the threshold would be $0.05/12 \approx 0.004$, which p = 0.04 doesn't meet.
</details>

**Q2: An experiment ends at p = 0.07. The PM proposes running it another week. Is that p-hacking?**
<details>
<summary><b>Reveal Answer</b></summary>

Yes, if the decision to extend depends on the p-value — it gives the test a second chance to cross 0.05 and inflates the false-positive rate. The clean approach: accept the planned result, and if the effect still matters, run a new experiment sized by a power analysis (topic 14).
</details>

**Q3: Is running many tests itself the problem?**
<details>
<summary><b>Reveal Answer</b></summary>

No. Exploring is fine. The problem is running many tests **and reporting them as if only one was run**, without a correction. Report the number of tests and adjust for it.
</details>

---

### 📺 Source

* **Video:** [p-hacking: What it is and how to avoid it](https://youtu.be/HDCOUXE3HMM)

---

[⏮️ **Previous: 10 — Power Analysis**](10-power-analysis.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 12 — False Discovery Rate** ⏭️](12-false-discovery-rate.md)
