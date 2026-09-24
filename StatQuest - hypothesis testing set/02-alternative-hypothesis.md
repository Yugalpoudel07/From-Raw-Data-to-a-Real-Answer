[⏮️ **Previous: 01 — Hypothesis Testing & the Null Hypothesis**](01-hypothesis-testing-and-the-null-hypothesis.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 03 — p-values: What They Are** ⏭️](03-p-values-what-they-are.md)

---

# 02: The Alternative Hypothesis — Main Ideas

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> The **alternative hypothesis** ($H_1$ or $H_a$) is simply "the null is wrong." If the null says *the drugs are the same*, the alternative says *the drugs are different*. You never test the alternative directly — you test the null, and if you reject it, the alternative is what you're left with. Its real job is to fix **what counts as "extreme"** before you look at the data: a difference in *either* direction (two-sided), or only in one direction (one-sided).

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Pair

Every test is a pair of statements that cover every possibility between them:

| | Null $H_0$ | Alternative $H_1$ |
| :--- | :--- | :--- |
| Drug comparison | $\mu_A = \mu_B$ | $\mu_A \neq \mu_B$ |
| Coin | $p = 0.5$ | $p \neq 0.5$ |
| Regression coefficient | $\beta = 0$ | $\beta \neq 0$ |

```text
   All possible truths about the drugs
   +----------------------------------------------+
   |  H0: no difference  |  H1: some difference     |
   +----------------------------------------------+
            ^                       ^
     what we TEST              what we CONCLUDE
                               if H0 is rejected
```

---

### 2. Why You Don't Test $H_1$ Directly

"The drugs are different" covers infinitely many possibilities — different by 0.1 days, by 3 days, by 30 days. You can't compute *one* distribution for "different". You can compute one for "identical". So the logic runs through the null:

1. Assume $H_0$.
2. Ask how surprising the data are under $H_0$ (the p-value).
3. If very surprising → reject $H_0$ → accept $H_1$.
4. If not surprising → fail to reject $H_0$. $H_1$ is **not** disproved either.

---

### 3. Two-Sided vs One-Sided Alternatives

```text
   Two-sided   H1: mu_A != mu_B          One-sided   H1: mu_A < mu_B

   extreme = far out in EITHER tail       extreme = far out in ONE tail

      ###                    ###                                    ###
     ####         ___        ####                   ___             ####
    _____________/   \______________      _________/   \______________
                  H0                                H0
    2.5%                        2.5%                              5%
```

| | Two-sided | One-sided |
| :--- | :--- | :--- |
| Detects | A difference in either direction | A difference in the stated direction only |
| p-value (symmetric test) | Twice the one-sided value | Half the two-sided value |
| When to use | **Almost always** | Only if an effect in the other direction is genuinely impossible or irrelevant, *and* you decided before seeing data |

> **The trap:** running a two-sided test, getting p = 0.08, then "switching" to one-sided to get p = 0.04. Choosing the direction after seeing which way the data went is a form of p-hacking (topic 11). Pick the alternative **before** you look.

---

### 4. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Two-sided default** | A new model could be worse, not just better | Test "model B ≠ model A", not "model B > model A" |
| **One-sided with a reason** | Non-inferiority checks | "The faster model is no more than 1 point worse" |
| **Pre-registration** | Fixing $H_1$ before the experiment | Written into the experiment design doc (roadmap Week 17) |
| **Rejecting $H_0$ ≠ size of effect** | Accepting $H_1$ tells you *there is* a difference, not how big | Always report the estimated difference with a confidence interval |

---

### 5. Check Your Understanding

**Q1: A product team says "we only care if the new page *increases* sign-ups, so let's use a one-sided test." What's the risk?**
<details>
<summary><b>Reveal Answer</b></summary>

If the new page actually **hurts** sign-ups, a one-sided test for "increase" can't flag it — a big drop just looks like "fail to reject". For product changes a decrease is usually very relevant, so a two-sided test (or a separate guardrail check) is the safer choice.
</details>

**Q2: A two-sided t-test gives p = 0.07. The effect is in the direction you hoped. Can you now report a one-sided p = 0.035?**
<details>
<summary><b>Reveal Answer</b></summary>

No. The direction was chosen after seeing the data, which doubles your real false-positive rate. Report p = 0.07 (two-sided), as planned.
</details>

---

### 📺 Source

* **Video:** [Alternative Hypothesis: Main Ideas](https://youtu.be/5koKb5B_YWo)

---

[⏮️ **Previous: 01 — Hypothesis Testing & the Null Hypothesis**](01-hypothesis-testing-and-the-null-hypothesis.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 03 — p-values: What They Are** ⏭️](03-p-values-what-they-are.md)
