[⏮️ **Previous: 11 — p-hacking**](11-p-hacking.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 13 — FDR and Benjamini–Hochberg** ⏭️](13-fdr-benjamini-hochberg.md)

---

# 12: False Discovery Rate (FDR), Clearly Explained

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> When you run thousands of tests, asking "what's the chance of **any** false positive?" becomes hopeless — the answer is basically 100%. The **false discovery rate** asks a more useful question: **"Of all the results I'm calling significant, what fraction are false?"** Controlling FDR at 5% means you accept that about 1 in 20 of your discoveries may be wrong, in exchange for keeping far more of the real ones than a strict correction like Bonferroni would.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Problem at Scale

Test 10,000 genes (or features, or segments). Suppose 1,000 genuinely differ, 9,000 don't, you use α = 0.05, and your tests have power 0.80.

```text
                        called significant     not significant
   truly different           800  (TP)             200  (FN)
   no real difference        450  (FP)           8,550  (TN)
                            -----
                            1,250 "discoveries"

   False discovery rate = 450 / 1,250 = 36%
```

Every one of the 9,000 null tests had only a 5% false-positive rate — and still **more than a third of the discoveries are false**. α controls errors per test; it says nothing about how trustworthy your *list of hits* is.

---

### 2. Two Error Rates, Two Questions

| | Family-wise error rate (FWER) | False discovery rate (FDR) |
| :--- | :--- | :--- |
| Question | P(**at least one** false positive)? | Expected **fraction** of discoveries that are false |
| Typical method | Bonferroni: $\alpha / m$ | Benjamini–Hochberg (topic 13) |
| Strictness | Very strict | More lenient |
| Best when | Any single false positive is costly; few tests | Many tests; you'll follow up the hits anyway |

---

### 3. The Key Picture: Histograms of p-values

What do p-values look like when the null is true?

```text
   p-values from NULL tests               p-values from REAL effects
   (no difference)                        (a true difference)

   |####|####|####|####|####|             |##########|
   |####|####|####|####|####|             |########|
   |####|####|####|####|####|             |#####|
   |####|####|####|####|####|             |###|##|#|.|.|
   0                        1             0                        1

   FLAT (uniform): every value            PILED UP near 0
   equally likely
```

Mix them together and you get a flat floor (the nulls) plus a spike near 0 (the real effects):

```text
   |###|
   |###|
   |###|##|
   |###|##|#|#|#|#|#|#|#|#|   <- spike near 0 = real effects + some nulls
   |###|##|#|#|#|#|#|#|#|#|   <- flat floor    = nulls
   0                        1
```

The height of the flat floor tells you roughly how many nulls there are — and therefore how many of the small p-values near 0 are probably nulls too. That's the intuition FDR methods exploit.

---

### 4. What "FDR = 5%" Means

If you call a set of results significant while controlling FDR at 0.05:

* ✅ On average, about 5% of the results **in that list** are false positives.
* ❌ It does **not** tell you which ones.
* ❌ It is **not** the probability that any particular result is false.

Related quantity: a **q-value** is the FDR-adjusted version of a p-value — the smallest FDR at which that result would be called significant.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **FDR = 1 − precision** | Same quantity as a classifier's false-discovery share | Of the alerts your anomaly detector fires, what fraction are false? |
| **Mass testing** | Screening many metrics, segments or features | Which of 500 product metrics moved after a release? |
| **Uniform null p-values** | A diagnostic for your pipeline | Run an A/A test many times: p-values should be flat; if not, the pipeline is broken |
| **Base rates matter** | When true effects are rare, FDR is high | Most product ideas don't work → many "wins" at α = 0.05 are false |

---

### 6. Check Your Understanding

**Q1: 2,000 tests, all truly null, α = 0.05. How many discoveries and what FDR?**
<details>
<summary><b>Reveal Answer</b></summary>

About 100 discoveries, and all of them are false: FDR = 100%. With no real effects, every "hit" is a false positive.
</details>

**Q2: Why is FWER control usually too strict for 20,000-gene studies?**
<details>
<summary><b>Reveal Answer</b></summary>

Bonferroni would require $p < 0.05/20{,}000 = 2.5 \times 10^{-6}$. Most real but moderate effects can't reach that, so you'd miss nearly everything. Controlling the fraction of false discoveries is a better trade when you plan to validate the hits.
</details>

**Q3: A histogram of your p-values is completely flat. What does that suggest?**
<details>
<summary><b>Reveal Answer</b></summary>

That essentially all tests are null — there's no pile-up near 0 from real effects. Any "significant" results are probably false positives.
</details>

---

### 📺 Source

* **Video:** [False Discovery Rate (FDR), Clearly Explained](https://youtu.be/L3nlGfSyHV0)

---

[⏮️ **Previous: 11 — p-hacking**](11-p-hacking.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 13 — FDR and Benjamini–Hochberg** ⏭️](13-fdr-benjamini-hochberg.md)
