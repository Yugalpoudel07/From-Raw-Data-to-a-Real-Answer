[⏮️ **Previous: 14 — p-hacking and Power Calculations**](14-p-hacking-and-power-calculations.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 16 — Type II Errors** ⏭️](16-type-2-errors.md)

---

# 15: Type I Errors (False Positives) — *Optional Refresher*

**StatQuest with Josh Starmer · Hypothesis Testing Set** · *YouTube Short, under a minute*

> [!TIP]
> **Core Intuition:**
> A **Type I error** is a **false positive**: you reject the null hypothesis when it was actually true — you "discover" an effect that isn't there. Its probability, when the null is true, is exactly your threshold $\alpha$. Pick α = 0.05 and you've agreed to be fooled this way about 1 time in 20 on null experiments.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Where It Sits

```text
                              REALITY
                     H0 true              H0 false
                  (no effect)          (real effect)
               +--------------------+--------------------+
   Reject H0   |  TYPE I ERROR      |  Correct           |
   DECISION    |  false positive    |  true positive     |
               |  prob = alpha      |  prob = power      |
               +--------------------+--------------------+
   Fail to     |  Correct           |  TYPE II ERROR     |
   reject H0   |  true negative     |  false negative    |
               |  prob = 1 - alpha  |  prob = beta       |
               +--------------------+--------------------+
```

---

### 2. Key Facts

| Fact | Detail |
| :--- | :--- |
| Probability | $P(\text{Type I}) = \alpha$, **given** the null is true |
| How to lower it | Stricter α (0.01), corrections for multiple tests (topics 11–13), no peeking (topic 14) |
| The cost of lowering it | Lower power → more Type II errors (topic 16) |
| What inflates it in practice | Many tests, flexible analysis, topping up data — i.e. p-hacking |

**Examples:** launching a feature that doesn't actually help; a medical test flagging a healthy patient; announcing a "winning" model that only won by seed luck.

---

### 3. Connection to Machine Learning

| Hypothesis testing | Classifier evaluation |
| :--- | :--- |
| Type I error | False positive (FP) |
| α (Type I rate on true nulls) | False-positive rate, FPR |
| Share of discoveries that are false (FDR) | 1 − precision |

---

### 4. Check Your Understanding

**Q: A spam filter moves a real email from your boss into spam. Which error type, if $H_0$ = "this email is not spam"?**
<details>
<summary><b>Reveal Answer</b></summary>

Type I error: the filter rejected $H_0$ ("not spam") when it was true — a false positive for the "spam" class.
</details>

---

### 📺 Source

* **Video (Short):** [Type 1 Errors (False Positive)](https://youtube.com/shorts/P4aYC1kS4d0)

---

[⏮️ **Previous: 14 — p-hacking and Power Calculations**](14-p-hacking-and-power-calculations.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 16 — Type II Errors** ⏭️](16-type-2-errors.md)
