[⏮️ **Previous: 02 — The Alternative Hypothesis**](02-alternative-hypothesis.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 04 — How to Calculate p-values** ⏭️](04-how-to-calculate-p-values.md)

---

# 03: p-values — What They Are and How to Interpret Them

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> A p-value answers exactly one question: **"If there were really no effect at all, how surprising would data like mine be?"** It is a number between 0 and 1. Close to 0 means "this would be very unusual if the null were true," so you become more confident the groups really differ. It does **not** tell you the probability that your theory is right, and it does **not** tell you how big or important the effect is. Almost everyone gets this backwards — including people with doctorates.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Definition

$$ \boxed{\; p = P\big(\text{data at least this extreme} \;\big|\; H_0 \text{ is true}\big) \;} $$

Read the bar "|" as **"assuming"**. The p-value is calculated in a world where the null is true. It is a statement about the **data**, given the hypothesis — never about the hypothesis, given the data.

```text
   Imagine re-running the experiment many times in a world where
   Drug A and Drug B are IDENTICAL.  Plot the difference in means each time.

                    ___
                  /     \
                /         \
             __/           \__
     _______/                 \_______
   ----------------------------|----------
                 0          observed
                             difference
                               |######|  <- this area is the p-value
                                          (both tails, for a two-sided test)
```

---

### 2. Reading a p-value

| p-value | Plain reading |
| :--- | :--- |
| 0.50 | Data like these are completely ordinary under "no effect". |
| 0.05 | Only 5% of no-effect experiments would look this extreme. |
| 0.001 | Only 1 in 1,000 no-effect experiments would look this extreme. |

The **threshold** (usually 0.05) is covered in topic 05. The key idea: with a 0.05 threshold, **if the null is true, you'll wrongly call a result "significant" about 5% of the time.** That wrong call is a **false positive** (topic 15).

---

### 3. The Four Things a p-value Is Not

| ❌ Common belief | ✅ Reality |
| :--- | :--- |
| **1. "p = 0.03 means a 3% chance the null is true."** | p is computed *assuming* the null is true. $P(\text{data} \mid H_0) \neq P(H_0 \mid \text{data})$ — the same mix-up as the base-rate fallacy in Bayes' theorem. |
| **2. "p = 0.03 means a 97% chance my effect is real."** | Same mistake from the other side. Whether the effect is real depends on the prior plausibility and the power too (topic 12 shows how many "significant" results can be false). |
| **3. "A smaller p-value means a bigger, more important effect."** | p mixes effect size **and** sample size. A trivial effect with a huge sample gives a tiny p-value. |
| **4. "p > 0.05 means there is no effect."** | It means you didn't detect one. Small samples miss real effects all the time (topic 09, power). |

> **Bonus mistake:** "p = 0.03 means there's a 3% chance the result was due to random chance." This sounds right but is belief #1 in disguise.

---

### 4. Why p Is Not Effect Size

Two experiments, same p-value, very different meaning:

| | Experiment 1 | Experiment 2 |
| :--- | :--- | :--- |
| Sample size | 40 per group | 1,000,000 per group |
| Difference in means | 0.8 SD (large) | 0.01 SD (tiny) |
| p-value | < 0.001 | < 0.001 |
| Worth acting on? | Probably | Probably not |

With a million users per group, a difference of 0.01 standard deviations gives $z \approx 7$ and $p < 10^{-11}$ — "extremely significant" and practically meaningless. **Always report the effect size and its confidence interval next to the p-value.**

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **$P(\text{data} \mid H_0)$** | The only thing an A/B test p-value tells you | "If the new ranker changed nothing, a lift this big would appear 2% of the time" |
| **Not effect size** | Big-data experiments are almost always "significant" | At 10M users, report the lift and its CI; the p-value alone is uninformative |
| **Not $P(H_0)$** | Stops over-confident launch decisions | A p = 0.04 on an implausible idea is still probably a false positive |
| **Regression output** | p-values next to coefficients | A tiny p on a feature doesn't make it important for prediction |
| **Interview staple** | The most asked stats question in DS interviews | "Explain a p-value to a product manager" |

---

### 6. Check Your Understanding

**Q1: Explain p = 0.02 to a product manager in one sentence, correctly.**
<details>
<summary><b>Reveal Answer</b></summary>

"If the new design truly made no difference, we'd see a gap this large (or larger) only about 2% of the time — so it's unlikely to be pure noise." Avoid "there's a 2% chance we're wrong" or "98% chance it works".
</details>

**Q2: Test A has p = 0.001, test B has p = 0.04. Does test A show the bigger effect?**
<details>
<summary><b>Reveal Answer</b></summary>

Not necessarily. Test A may simply have a much larger sample. Compare the estimated effect sizes (with their confidence intervals), not the p-values.
</details>

**Q3: Name the four misconceptions from memory.**
<details>
<summary><b>Reveal Answer</b></summary>

1. p is the probability the null is true. 2. 1 − p is the probability the effect is real. 3. Smaller p means a bigger or more important effect. 4. p > 0.05 means no effect exists.
</details>

---

### 📺 Source

* **Video:** [p-values: What they are and how to interpret them](https://youtu.be/vemZtEM63GY)

---

[⏮️ **Previous: 02 — The Alternative Hypothesis**](02-alternative-hypothesis.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 04 — How to Calculate p-values** ⏭️](04-how-to-calculate-p-values.md)
