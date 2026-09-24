[⏮️ **Previous: 15 — Type I Errors**](15-type-1-errors.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [🏠 **Repository Home**](../README.md)

---

# 16: Type II Errors (False Negatives) — *Optional Refresher*

**StatQuest with Josh Starmer · Hypothesis Testing Set** · *YouTube Short, under a minute*

> [!TIP]
> **Core Intuition:**
> A **Type II error** is a **false negative**: there really is an effect, but your test fails to reject the null — you miss it. Its probability is written $\beta$, and **power $= 1 - \beta$**. Type II errors are the quiet ones: nobody announces a result they didn't find, so an underpowered experiment just looks like "the idea didn't work."

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Where It Sits

```text
                              REALITY
                     H0 true              H0 false
                  (no effect)          (real effect)
               +--------------------+--------------------+
   Reject H0   |  Type I error      |  Correct           |
               |  prob = alpha      |  prob = power      |
               +--------------------+--------------------+
   Fail to     |  Correct           |  TYPE II ERROR     |
   reject H0   |  prob = 1 - alpha  |  false negative    |
               |                    |  prob = beta       |
               +--------------------+--------------------+
```

---

### 2. Key Facts

| Fact | Detail |
| :--- | :--- |
| Probability | $\beta = P(\text{fail to reject} \mid \text{effect is real})$ |
| Relationship to power | Power $= 1 - \beta$; the usual target is β = 0.20 (power 0.80) |
| How to lower it | More data, less noise (paired designs), larger true effect, looser α (topic 09) |
| Why it's dangerous | A non-significant result gets read as "no effect" (topic 01) |

**Examples:** abandoning a feature that actually helps because the test was too small; a medical screen missing a sick patient; concluding two models are "the same" from 3 seeds.

---

### 3. The α–β Trade-Off

```text
   Stricter alpha (move threshold right)  ->  fewer Type I, MORE Type II
   Looser alpha   (move threshold left)   ->  more Type I,  FEWER Type II

   The only way to reduce BOTH:  more data / less noise
   (narrower distributions, less overlap)
```

---

### 4. Connection to Machine Learning

| Hypothesis testing | Classifier evaluation |
| :--- | :--- |
| Type II error | False negative (FN) |
| β | False-negative rate, FNR = 1 − recall |
| Power | Recall / true-positive rate |

---

### 5. Check Your Understanding

**Q: A fraud model lets a fraudulent transaction through. With $H_0$ = "this transaction is legitimate", which error is it — and what's the fix at the model level?**
<details>
<summary><b>Reveal Answer</b></summary>

Type II error (false negative): the transaction was fraud but $H_0$ wasn't rejected. Lowering the decision threshold raises recall (fewer Type II errors) at the cost of more false alarms (Type I errors) — the same trade-off as α vs β.
</details>

---

### 📺 Source

* **Video (Short):** [Type 2 Errors (False Negative)](https://youtube.com/shorts/qioNUZGVH1A)

---

[⏮️ **Previous: 15 — Type I Errors**](15-type-1-errors.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [🏠 **Repository Home**](../README.md)
