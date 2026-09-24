[🏠 **Repository Home**](../README.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 02 — The Alternative Hypothesis** ⏭️](02-alternative-hypothesis.md)

---

# 01: Hypothesis Testing and the Null Hypothesis

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> A hypothesis test is a **structured way of asking "could this just be noise?"** You start from a boring default — the **null hypothesis**, "there is no difference" — and ask whether your data are surprising enough to throw that default out. You never *prove* the null true; you either **reject** it (the data are too weird for it) or **fail to reject** it (the data are compatible with it). Everything else in this set — p-values, t-tests, power, FDR — is machinery for making that one decision well.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Setup

You give Drug A to one group and Drug B to another, then measure recovery time. Drug A's group recovers a bit faster on average. Is Drug A actually better, or did you just happen to get faster healers in group A?

```text
   Recovery time (days)

   Drug A:   o  o o  oo o   o                 mean = 13.2
   Drug B:        o  o oo  o o  o   o         mean = 15.1
           |----|----|----|----|----|----|
          10   12   14   16   18   20   22

   The means differ.  But the points overlap a lot.
   Would we see a gap this big even if the drugs were identical?
```

Hypothesis testing turns that vague worry into a procedure.

---

### 2. The Null Hypothesis

$$ H_0 : \mu_A = \mu_B \qquad \text{("no difference")} $$

The null is chosen because it is **specific enough to calculate with**. "The drugs are identical" tells you exactly what the data *should* look like if nothing is going on — so you can measure how far your real data sit from that picture.

| Question | Typical null hypothesis |
| :--- | :--- |
| Does the new checkout page change conversion? | Conversion rate is the same on both pages |
| Is this coin fair? | $P(\text{heads}) = 0.5$ |
| Does feature X predict churn? | The coefficient on X is 0 |
| Did model B beat model A? | Mean accuracy is the same for both |

> The null doesn't have to be "zero difference" — it can be any specific value ("the drug lowers blood pressure by exactly 5"). Zero is just the most common because it is the most useful default.

---

### 3. The Procedure

```text
   1. State H0 (and H1)                 BEFORE looking at the data
   2. Choose a threshold alpha          BEFORE looking at the data
   3. Collect data
   4. Compute a test statistic          (how far is the data from H0?)
   5. Convert it to a p-value           (how surprising is that distance under H0?)
   6. Decide:
          p <= alpha  ->  reject H0
          p >  alpha  ->  fail to reject H0
```

The **test statistic** is just a number that measures "distance from the null" in standard units — a difference in means divided by its standard error, for example. Topics 03–08 fill in steps 4–5.

---

### 4. "Fail to Reject" Is Not "Accept"

This is the part everyone gets wrong. A test can only **reject** the null or **fail to reject** it. It can never prove the null.

```text
   Courtroom analogy

   H0 = "the defendant is innocent"

   Strong evidence    ->  "guilty"          (reject H0)
   Weak evidence      ->  "not guilty"      (fail to reject H0)

   "Not guilty" does NOT mean "proven innocent".
   It means "not enough evidence to convict".
```

A large p-value can happen because (a) there really is no effect, **or** (b) there is an effect but your sample was too small to see it. Topic 09 (power) is about telling those two apart.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Null hypothesis** | The default every A/B test starts from | "The new recommendation model does not change click-through" |
| **Reject vs fail to reject** | Honest reporting of experiments | "No significant difference detected" ≠ "the two models are equivalent" |
| **Test statistic** | Distance from the null in standard-error units | Difference in mean validation loss ÷ its standard error across seeds |
| **Deciding before looking** | Protects against fooling yourself | Choose the metric and threshold before the experiment starts (roadmap Week 17) |
| **Model comparison** | Is model B really better or just a lucky seed? | Paired test on per-fold CV scores |

---

### 6. Check Your Understanding

**Q1: You want to know whether a new onboarding email changes 7-day retention. Write the null hypothesis.**
<details>
<summary><b>Reveal Answer</b></summary>

$H_0$: 7-day retention is the same for users who get the new email and users who get the old one ($p_{\text{new}} = p_{\text{old}}$). It is specific enough to calculate what the data should look like if the email does nothing.
</details>

**Q2: A colleague runs a test, gets p = 0.40, and writes "the two versions perform the same." What's wrong?**
<details>
<summary><b>Reveal Answer</b></summary>

p = 0.40 means the data are **compatible** with no difference — it does not prove there is no difference. The test may simply have been too small (low power) to detect a real effect. The correct wording is "we did not detect a difference," ideally with a confidence interval showing how large a difference is still plausible.
</details>

**Q3: Why do we test the null hypothesis instead of testing "Drug A is better" directly?**
<details>
<summary><b>Reveal Answer</b></summary>

"Drug A is better" doesn't say *how much* better, so it doesn't pin down what the data should look like. "No difference" is a single, precise claim, so you can calculate exactly how likely your observed data would be under it — which is what a p-value needs.
</details>

---

### 📺 Source

* **Video:** [Hypothesis Testing and the Null Hypothesis](https://youtu.be/0oc49DyA3hU)

---

[🏠 **Repository Home**](../README.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 02 — The Alternative Hypothesis** ⏭️](02-alternative-hypothesis.md)
