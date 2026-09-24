[⏮️ **Previous: 08 — t-tests and ANOVA as Linear Models**](08-t-tests-and-anova-linear-models.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 10 — Power Analysis** ⏭️](10-power-analysis.md)

---

# 09: Statistical Power, Clearly Explained

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> **Power is the probability that your test catches a real effect when there is one.** If the two groups truly differ, a well-powered experiment will usually give a small p-value; an underpowered one will often shrug and say "not significant" — not because there's nothing there, but because the experiment was too small to see it. Power depends on four things: **how big the effect is, how noisy the data are, how many samples you have, and how strict your threshold is.**

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Definition

$$ \text{Power} = P(\text{reject } H_0 \mid H_0 \text{ is false}) = 1 - \beta $$

where $\beta$ is the probability of a **Type II error** (missing a real effect, topic 16). The conventional target is **power = 0.80**: if the effect is real, you catch it 4 times out of 5.

---

### 2. The Picture: Two Overlapping Distributions

```text
   Distribution of the test statistic...

      ...if H0 is true            ...if the real effect exists
            ___                          ___
          /     \                      /     \
        /         \                  /         \
     __/     beta   \__          __/             \__
   _/     ::::::::::::|\#########/####  POWER  ######\_
   -------------------|-------------------------------
                  threshold
                      ^
   left of threshold: fail to reject     right: reject H0
   ':' under the right curve = beta (missed)
   '#' under the right curve = power (caught)
```

Power is the part of the "effect is real" distribution that lands beyond the threshold. Anything that **pushes the two curves apart** or **makes them narrower** increases power.

---

### 3. The Four Levers

| Lever | Change | Effect on power | Why |
| :--- | :--- | :--- | :--- |
| **Effect size** | Bigger true difference | ⬆️ | Curves further apart |
| **Noise** ($\sigma$) | Less variable data | ⬆️ | Curves narrower |
| **Sample size** ($n$) | More data | ⬆️ | Curves narrower (SE $= \sigma/\sqrt{n}$) |
| **Threshold** ($\alpha$) | Looser (0.10 vs 0.05) | ⬆️ | Threshold moves left — but more false positives |

You rarely control the effect size. You sometimes control noise (better measurement, paired designs — topic 07). You almost always control **sample size**, which is why topic 10 is about choosing it.

---

### 4. Power in Numbers

Two-sample t-test, α = 0.05, standardised effect size $d = 0.5$ (a "medium" effect — the groups differ by half a standard deviation):

| Samples per group | Power |
| :-: | :-: |
| 20 | 0.34 |
| 64 | **0.80** |
| 100 | 0.94 |

A study with 20 per group would **miss this real, medium-sized effect two times out of three.**

A handy approximation for a two-sided, two-sample test with $n$ per group:

$$ \text{Power} \approx \Phi\!\left(d\sqrt{\tfrac{n}{2}} - z_{1-\alpha/2}\right) $$

With $d = 0.5$, $n = 64$: $\;0.5\sqrt{32} - 1.96 = 0.87 \Rightarrow \Phi(0.87) \approx 0.81$.

---

### 5. Why Low Power Is Worse Than It Sounds

* **Wasted experiments.** Most underpowered tests say "not significant" even when the idea works.
* **Misleading successes.** When an underpowered test *does* come out significant, the estimated effect is usually **exaggerated** — only the lucky overestimates cross the threshold (topic 14).
* **"No effect" claims.** A non-significant result from a low-power test is almost no evidence of absence.

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Power = recall** | Of the real effects out there, what fraction do you detect? | Same idea as a classifier's true-positive rate |
| **Sample size lever** | Why A/B tests need so much traffic | Detecting a lift from 5.0% to 5.5% conversion at 80% power needs about 31,000 users per arm |
| **Noise lever** | Variance reduction techniques | Paired designs, CUPED, stratification — all raise power without more users |
| **Model comparison** | 3 seeds is rarely enough | Small differences between models need many seeds or folds to detect reliably |

---

### 7. Check Your Understanding

**Q1: A test has power 0.80. The effect is real. What's the probability the test says "not significant"?**
<details>
<summary><b>Reveal Answer</b></summary>

$\beta = 1 - 0.80 = 0.20$. One in five experiments would miss it.
</details>

**Q2: Name two ways to increase power without collecting more data.**
<details>
<summary><b>Reveal Answer</b></summary>

Reduce noise (a paired design, better measurement, controlling for a covariate) or loosen α (at the cost of more false positives). A one-sided test also raises power, but only if the direction was fixed in advance for good reason.
</details>

**Q3: A colleague's pilot (10 per group) finds p = 0.30 and concludes "the feature has no effect." Respond.**
<details>
<summary><b>Reveal Answer</b></summary>

With 10 per group, power to detect even a medium effect is roughly 0.2, so a non-significant result is expected whether or not the feature works. The pilot can't distinguish "no effect" from "too small to see". Report the confidence interval for the difference, and run a power analysis to size a real test.
</details>

---

### 📺 Source

* **Video:** [Statistical Power, Clearly Explained](https://youtu.be/Rsc5znwR5FA)

---

[⏮️ **Previous: 08 — t-tests and ANOVA as Linear Models**](08-t-tests-and-anova-linear-models.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 10 — Power Analysis** ⏭️](10-power-analysis.md)
