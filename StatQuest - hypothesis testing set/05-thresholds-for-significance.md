[⏮️ **Previous: 04 — How to Calculate p-values**](04-how-to-calculate-p-values.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 06 — The CLT and the t-test** ⏭️](06-central-limit-theorem-and-the-t-test.md)

---

# 05: Thresholds for Significance

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> The significance threshold $\alpha$ is **the false-positive rate you agree to live with** when the null is true. Pick 0.05 and, across many experiments where nothing is really going on, about 1 in 20 will still come out "significant". There is nothing magic about 0.05 — it's a convention. The right threshold depends on **what a false positive costs you** compared with a false negative, and it must be chosen **before** you see the data.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. What $\alpha$ Controls

$$ \alpha = P(\text{reject } H_0 \mid H_0 \text{ is true}) = P(\text{Type I error}) $$

```text
   Null distribution of the test statistic

                         ___
                       /     \
                     /         \
                  __/           \__
      #####_____/                   \_____#####
      alpha/2          "fail to reject"      alpha/2
      reject H0                              reject H0

   The shaded tails ARE alpha.  Land there and you reject H0.
   If H0 is true, you land there alpha of the time -> false positive.
```

---

### 2. The Trade-Off

Lowering $\alpha$ makes false positives rarer but makes real effects **harder to detect** (lower power, more false negatives). You can't shrink both for free — only more data does that.

| Threshold | False positives (when $H_0$ true) | Ability to detect real effects |
| :--- | :--- | :--- |
| 0.10 | 1 in 10 | Higher |
| **0.05** | **1 in 20** | Moderate (the usual default) |
| 0.01 | 1 in 100 | Lower |
| 0.001 | 1 in 1,000 | Much lower (needs far more data) |

---

### 3. Choosing a Threshold by Cost

| Situation | A false positive means… | Typical choice |
| :--- | :--- | :--- |
| Low-stakes product tweak (button colour) | Shipping something harmless that doesn't help | 0.05, sometimes 0.10 |
| Drug approval | Patients take a drug that doesn't work | 0.05 or stricter, plus replication |
| Genome-wide association studies (~1M tests) | Chasing a gene that isn't involved | $5 \times 10^{-8}$ |
| Particle physics discovery | Announcing a particle that doesn't exist | "5 sigma" ≈ $3 \times 10^{-7}$ (one-sided) |

> **Rule:** decide $\alpha$ before collecting data. Choosing it afterwards ("0.07 is close enough") makes it meaningless.

---

### 4. What 0.05 Does *Not* Mean

* It does **not** mean 5% of your significant results are false. That fraction is the **false discovery rate** (topic 12), and it can be far higher than 5% when true effects are rare.
* "Significant" does **not** mean "important". It means "unlikely under the null at the level I chose."
* p = 0.049 and p = 0.051 are practically identical evidence. Treat the threshold as a decision rule, not a cliff between truth and falsehood.

---

### 5. Many Tests, One Threshold

$\alpha$ is the error rate **per test**. Run many tests and the errors add up:

$$ P(\text{at least one false positive in } m \text{ independent null tests}) = 1 - (1 - \alpha)^m $$

| Tests $m$ | Chance of ≥ 1 false positive at $\alpha = 0.05$ |
| :-: | :-: |
| 1 | 5% |
| 5 | 23% |
| 20 | **64%** |
| 100 | 99.4% |

That's the whole reason topics 11–14 exist.

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **$\alpha$ as FPR** | Same idea as a classifier's false-positive rate | $\alpha$ is the FPR of your "significant / not significant" classifier on null experiments |
| **Cost-based threshold** | Same logic as picking a classification threshold | Don't default to 0.5 for a model or 0.05 for a test — derive it from costs (roadmap Week 12) |
| **Decided in advance** | Part of every experiment design doc | Metric, $\alpha$, power and sample size fixed before launch |
| **Many metrics** | Dashboards with 30 metrics per A/B test | Expect ~1–2 "significant" moves by chance alone |

---

### 7. Check Your Understanding

**Q1: You run 1,000 A/B tests where the change truly does nothing, each at α = 0.05. About how many come out significant?**
<details>
<summary><b>Reveal Answer</b></summary>

About $1{,}000 \times 0.05 = 50$. Every one of them is a false positive.
</details>

**Q2: Your team uses α = 0.05 and a result comes in at p = 0.06. Someone suggests using α = 0.10 "for this one". Why not?**
<details>
<summary><b>Reveal Answer</b></summary>

Moving the threshold after seeing the p-value guarantees you'll call more things significant than your stated error rate allows. The threshold only controls false positives if it was fixed in advance. Report p = 0.06 as not significant at 0.05 and, if the effect matters, plan a properly powered follow-up (topic 10).
</details>

**Q3: When would you deliberately choose a stricter threshold than 0.05?**
<details>
<summary><b>Reveal Answer</b></summary>

When a false positive is expensive (costly launch, medical or financial decisions) or when you're running many tests at once, so that per-test errors would otherwise pile up.
</details>

---

### 📺 Source

* **Video:** [Thresholds for Significance](https://youtu.be/KEofcJ1tfkI)

---

[⏮️ **Previous: 04 — How to Calculate p-values**](04-how-to-calculate-p-values.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 06 — The CLT and the t-test** ⏭️](06-central-limit-theorem-and-the-t-test.md)
