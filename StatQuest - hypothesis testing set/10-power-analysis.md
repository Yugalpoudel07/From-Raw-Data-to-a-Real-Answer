[⏮️ **Previous: 09 — Statistical Power**](09-statistical-power.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 11 — p-hacking** ⏭️](11-p-hacking.md)

---

# 10: Power Analysis, Clearly Explained

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> A power analysis answers **"how many samples do I need?"** — and it's done **before** you collect any data. You state three things: the threshold ($\alpha$, usually 0.05), the power you want (usually 0.80), and the **smallest effect you care about detecting**. Out comes a sample size. Doing it first is what turns an experiment from "let's see what happens" into a test that can actually answer the question — and it's your main protection against p-hacking.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Inputs and the Output

```text
   alpha (e.g. 0.05)         ---+
   power (e.g. 0.80)         ---+--->  POWER ANALYSIS  --->  n per group
   effect size (e.g. d=0.5)  ---+
```

Any three of {α, power, effect size, n} determine the fourth. The usual use is solving for $n$.

---

### 2. Effect Size: Cohen's d

For comparing two means, the effect size is the difference in **standard-deviation units**:

$$ d = \frac{\mu_1 - \mu_2}{\sigma_{\text{pooled}}} \qquad \sigma_{\text{pooled}} = \sqrt{\frac{s_1^2 + s_2^2}{2}} \;\;(\text{equal } n) $$

Standardising means one table works for any units — days, dollars, clicks.

| $d$ | Common label | What it looks like |
| :-: | :--- | :--- |
| 0.2 | Small | Distributions overlap almost entirely |
| 0.5 | Medium | Visible to a careful observer |
| 0.8 | Large | Obvious in a plot |

> **Where the effect size comes from:** the **smallest effect worth acting on** (a business or clinical judgement), previous studies, or a pilot. **Not** the effect you're hoping for — that's usually too optimistic, which makes $n$ too small.

---

### 3. The Formula (Normal Approximation)

For a two-sided, two-sample test with $n$ per group:

$$ \boxed{\; n \approx \frac{2\,\big(z_{1-\alpha/2} + z_{\text{power}}\big)^2}{d^2} \;} $$

With α = 0.05 ($z = 1.96$) and power = 0.80 ($z = 0.84$): $\;n \approx \dfrac{15.7}{d^2}$.

| Effect size $d$ | $n$ per group (formula) | $n$ per group (exact t-test) |
| :-: | :-: | :-: |
| 0.2 | 393 | 394 |
| 0.5 | 63 | 64 |
| 0.8 | 25 | 26 |

The key shape: **$n$ grows with $1/d^2$.** Halve the effect you want to detect and you need **four times** the data.

**Worked example:** recovery times have SD ≈ 4 days, and a drug is only worth using if it shortens recovery by at least 2 days. $d = 2/4 = 0.5$ → about **64 patients per group**.

---

### 4. Doing It in Code, Then Checking by Simulation

```python
from statsmodels.stats.power import TTestIndPower

n = TTestIndPower().solve_power(effect_size=0.5, alpha=0.05, power=0.80)
# n ≈ 63.8 → round UP to 64 per group
```

**Verify by simulation** (build task 3 of the week): generate many fake experiments with the true effect $d = 0.5$ and 64 per group, run the t-test on each, and count how often $p < 0.05$. The fraction should come out close to 0.80. If it doesn't, something in your reasoning is off.

---

### 5. Common Mistakes

| ❌ Mistake | ✅ Instead |
| :--- | :--- |
| Choosing $n$ by what's convenient, then hoping | Run the power analysis first |
| Using the effect size you *observed* in the same study ("post-hoc power") | Post-hoc power is just a restatement of the p-value; it tells you nothing new |
| Using an optimistic effect size | Use the smallest effect that would change your decision |
| Forgetting units: 64 **per group** | Total sample is 128 |
| Ignoring dropouts or data loss | Inflate $n$ for expected attrition |

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Sample size before launch** | The heart of experiment design | "We need 31,000 users per arm to detect 5.0% → 5.5% conversion" |
| **Minimum detectable effect (MDE)** | Industry's name for the effect-size input | A/B platforms report the MDE for your available traffic |
| **$n \propto 1/d^2$** | Why small lifts are expensive to prove | Detecting a 1% relative lift can need millions of users |
| **Simulation check** | Validates your stats code | Same habit as checking a from-scratch model against sklearn |

---

### 7. Check Your Understanding

**Q1: With α = 0.05 and power 0.80, roughly how many per group to detect $d = 0.25$?**
<details>
<summary><b>Reveal Answer</b></summary>

$n \approx 15.7 / 0.25^2 = 15.7 / 0.0625 \approx 251$ per group (the exact t-test answer is 253). Note it's 4× the 63 needed for $d = 0.5$.
</details>

**Q2: Your budget allows only 30 per group. What can you do with a power analysis?**
<details>
<summary><b>Reveal Answer</b></summary>

Flip it around: fix $n = 30$, α and power, and solve for the **minimum detectable effect** (about $d = 0.74$ here). If realistic effects are smaller than that, the experiment is likely to miss them and may not be worth running as designed.
</details>

**Q3: Why should the power analysis happen before data collection?**
<details>
<summary><b>Reveal Answer</b></summary>

Because it fixes the sample size in advance. Without a fixed $n$ it's tempting to keep adding data until p drops below 0.05 — which inflates false positives (topic 14).
</details>

---

### 📺 Source

* **Video:** [Power Analysis, Clearly Explained](https://youtu.be/VX_M3tIyiYk)

---

[⏮️ **Previous: 09 — Statistical Power**](09-statistical-power.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 11 — p-hacking** ⏭️](11-p-hacking.md)
