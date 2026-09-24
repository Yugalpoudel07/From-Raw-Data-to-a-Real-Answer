[⏮️ **Previous: 05 — Thresholds for Significance**](05-thresholds-for-significance.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 07 — Which t-test to Use** ⏭️](07-which-t-test-to-use.md)

---

# 06: The Central Limit Theorem — or "How I Learned to Stop Worrying and Love the t-test"

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> A t-test compares **means**, and the Central Limit Theorem says that **means are approximately normal** even when the raw data are not. That's the whole reason you can run a t-test on skewed, lumpy, real-world data without worrying (much) about its shape. The "t" part handles one extra problem: you don't know the true standard deviation, you estimate it — so for small samples the distribution of the test statistic has **heavier tails** than a normal, and the t-distribution accounts for that.

> ✍️ **My one line (write after watching, no peeking):**

> 📎 **Already covered in Month 1:** the CLT itself is written up in [Mathematics-for-Data-Science → StatQuest topic 11](https://github.com/Yugalpoudel07/Mathematics-for-Data-Science/blob/main/StatQuest%20with%20Josh%20Starmer/11-central-limit-theorem.md) (same video). This note focuses on what the CLT buys you for **hypothesis testing**.

---

### 1. The Worry, and Why It Goes Away

A t-test's maths assumes the thing being tested is normally distributed. Real data rarely are.

```text
   Raw data: order values (skewed)          Sample MEANS (n = 40 each)

   #                                                  _-_
   ###                                               /   \
   #####                                            /     \
   ########_______                               __/       \__
   $0                $500                            mean

   NOT normal                                  approximately NORMAL  <- CLT
```

The t-test doesn't look at the raw data's shape; it looks at the **difference in means**. By the CLT that difference is close to normal once the samples are moderately large, so the test is valid.

| Raw data shape | Rough sample size for the t-test to behave |
| :--- | :--- |
| Already normal | Any |
| Mildly skewed | ~15–30 per group |
| Heavily skewed, outliers | Larger — or use a permutation test instead |
| Infinite variance (e.g. Cauchy) | Never — the CLT doesn't apply |

---

### 2. The Test Statistic

For a one-sample test of $H_0: \mu = \mu_0$:

$$ \boxed{\; t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} \;} \qquad \text{df} = n - 1 $$

It's "how far is the sample mean from the null value, measured in standard errors". The standard error $s/\sqrt{n}$ is exactly the spread of the sampling distribution that the CLT describes.

---

### 3. Why "t" and Not "z"

If you knew the true $\sigma$, the statistic would be exactly standard normal (a z-test). You don't — you plug in the sample estimate $s$, which is itself noisy. That extra noise fattens the tails:

```text
        normal (z)       t with df = 4
           _-_                _-_
          /   \              /   \
         /     \            /     \
      __/       \__     ___/       \___       <- more area far out
                           more "surprising" values happen by chance
```

| Degrees of freedom | 95% two-sided critical value $t^*$ |
| :-: | :-: |
| 4 | 2.78 |
| 9 | 2.26 |
| 15 | 2.13 |
| 29 | 2.05 |
| ∞ (normal) | 1.96 |

**Worked example:** $n = 16$, $\bar{x} = 52$, $s = 8$, $H_0: \mu = 48$.
SE $= 8/4 = 2$, so $t = (52 - 48)/2 = 2.0$ with 15 df → two-sided **p ≈ 0.064**.
A z-test would have said p ≈ 0.046 — the t-test is (correctly) more cautious because $s$ was estimated from only 16 points.

---

### 4. What the CLT Does *Not* Rescue

* **Independence.** The CLT needs independent observations. Repeated measurements of the same user, or time-series rows, break it (and break the t-test).
* **Tiny samples of skewed data.** With $n = 5$ from a skewed distribution, the mean isn't normal yet.
* **The wrong question.** A t-test compares means. If the groups differ in spread or shape but not in mean, a t-test won't notice.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Means are normal** | Justifies t-tests on skewed business metrics | Revenue per user is heavily skewed, but mean revenue per group is ~normal at large n |
| **t vs z** | Small-sample honesty | Comparing two models over 5 seeds: use t with 4 df, not z |
| **Independence** | The assumption most often broken in practice | Randomise and analyse by user, not by session (roadmap Week 17) |
| **Permutation fallback** | When the CLT hasn't kicked in | Small, skewed samples → permutation test (build task 1) |

---

### 6. Check Your Understanding

**Q1: Session durations are strongly right-skewed. You have 500 sessions per group. Can you use a t-test to compare mean duration?**
<details>
<summary><b>Reveal Answer</b></summary>

Yes, as long as the sessions are independent. With 500 per group the CLT makes the difference in means approximately normal even though individual durations are skewed. (If many sessions come from the same users, aggregate to one value per user first.)
</details>

**Q2: Why does the t-distribution have heavier tails than the normal?**
<details>
<summary><b>Reveal Answer</b></summary>

Because the standard error uses the estimated $s$, not the true $\sigma$. When $s$ happens to come out small, $t$ comes out large, so extreme values occur more often than a normal would predict. As $n$ grows, $s$ becomes accurate and $t$ approaches the normal.
</details>

**Q3: $n = 10$, $\bar{x} = 105$, $s = 6$, $H_0: \mu = 100$. Compute t and decide at α = 0.05.**
<details>
<summary><b>Reveal Answer</b></summary>

SE $= 6/\sqrt{10} \approx 1.90$, $t = 5/1.90 \approx 2.64$ with 9 df. The critical value is 2.26, so reject $H_0$ (p ≈ 0.027).
</details>

---

### 📺 Source

* **Video:** [The Central Limit Theorem (or "How I Learned to Stop Worrying and Love the t-test")](https://youtu.be/YAlJCEDH2uY)

---

[⏮️ **Previous: 05 — Thresholds for Significance**](05-thresholds-for-significance.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 07 — Which t-test to Use** ⏭️](07-which-t-test-to-use.md)
