---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Appendix A Real Numbers and the Real Line
section: A.4 Proofs of Limit Theorems（极限定理的证明）
tags: [微积分, 极限, 极限法则, 极限定理证明, 极限乘积法则, 极限商法则, 夹逼定理, 三角不等式, 托马斯微积分]
prerequisites:
  - "[[2.2 Limit of a Function and Limit Laws]]"
  - "[[2.3 The Precise Definition of a Limit]]"
  - "[[2.4 One-Sided Limits]]"
aliases: [极限定理的证明, Proofs of Limit Theorems, A.4 极限定理的证明]
---

# A.4 Proofs of Limit Theorems（极限定理的证明）

> [!info] 📘 本节引言
> 本附录证明 2.2 节的定理 1（极限法则）中的第 2–5 条，以及定理 4（夹逼定理）。

> [!theorem] 📐 THEOREM 1 — Limit Laws（极限法则）
> 若 $L,\,M,\,c,\,k$ 为实数，且
> $$\lim_{x\to c} f(x) = L \quad \text{且} \quad \lim_{x\to c} g(x) = M,\quad \text{则}$$
>
> 1. **Sum Rule（和法则）**：$\displaystyle\lim_{x\to c}\bigl(f(x) + g(x)\bigr) = L + M$
> 2. **Difference Rule（差法则）**：$\displaystyle\lim_{x\to c}\bigl(f(x) - g(x)\bigr) = L - M$
> 3. **Constant Multiple Rule（常数倍法则）**：$\displaystyle\lim_{x\to c}\bigl(k\,f(x)\bigr) = kL$
> 4. **Product Rule（乘积法则）**：$\displaystyle\lim_{x\to c}\bigl(f(x)\,g(x)\bigr) = LM$
> 5. **Quotient Rule（商法则）**：$\displaystyle\lim_{x\to c}\frac{f(x)}{g(x)} = \frac{L}{M},\quad M \neq 0$
> 6. **Power Rule（幂法则）**：$\displaystyle\lim_{x\to c}[f(x)]^n = L^n$，$n$ 为正整数
> 7. **Root Rule（根式法则）**：$\displaystyle\lim_{x\to c}\sqrt[n]{f(x)} = \sqrt[n]{L} = L^{1/n}$，$n$ 为正整数
>
> （若 $n$ 为偶数，我们假设 $\lim_{x\to c} f(x) = L > 0$。）
>
> 和法则已在 2.3 节证明，幂法则与根式法则在更高级的教材中证明。将 $g(x)$ 替换为 $-g(x)$、$M$ 替换为 $-M$，由和法则可得**差法则**。**常数倍法则**是乘积法则在 $g(x) = k$ 时的特殊情形。于是只剩乘积法则与商法则需要证明。
>
> **Proof of the Limit Product Rule（极限乘积法则的证明）** 我们证明：对任意 $\varepsilon > 0$，存在 $\delta > 0$，使得对 $f$ 与 $g$ 定义域的交集 $D$ 中的一切 $x$，
> $$\lvert f(x)\,g(x) - LM\rvert < \varepsilon \quad \text{当} \quad 0 < \lvert x - c\rvert < \delta.$$
>
> 设 $\varepsilon$ 为一正数，将 $f(x)$ 与 $g(x)$ 写成
> $$f(x) = L + \bigl(f(x) - L\bigr), \qquad g(x) = M + \bigl(g(x) - M\bigr).$$
>
> 将两式相乘并减去 $LM$：
> $$
> \begin{aligned}
> f(x)\,g(x) - LM &= \bigl(L + (f(x) - L)\bigr)\bigl(M + (g(x) - M)\bigr) - LM \\
> &= LM + L\bigl(g(x) - M\bigr) + M\bigl(f(x) - L\bigr) \\
> &\quad + \bigl(f(x) - L\bigr)\bigl(g(x) - M\bigr) - LM \\
> &= L\bigl(g(x) - M\bigr) + M\bigl(f(x) - L\bigr) + \bigl(f(x) - L\bigr)\bigl(g(x) - M\bigr).
> \end{aligned}
> \qquad \text{(1)}
> $$
> 因为 $f$ 与 $g$ 在 $x \to c$ 时极限分别为 $L$ 与 $M$，存在正数 $\delta_1,\,\delta_2,\,\delta_3,\,\delta_4$ 使得
> $$
> \begin{aligned}
> \lvert f(x) - L\rvert < \sqrt{\varepsilon/3} \quad & \text{当} \quad 0 < \lvert x - c\rvert < \delta_1, \\
> \lvert g(x) - M\rvert < \sqrt{\varepsilon/3} \quad & \text{当} \quad 0 < \lvert x - c\rvert < \delta_2, \\
> \lvert f(x) - L\rvert < \dfrac{\varepsilon}{3(1 + \lvert M\rvert)} \quad & \text{当} \quad 0 < \lvert x - c\rvert < \delta_3, \\
> \lvert g(x) - M\rvert < \dfrac{\varepsilon}{3(1 + \lvert L\rvert)} \quad & \text{当} \quad 0 < \lvert x - c\rvert < \delta_4.
> \end{aligned}
> \qquad \text{(2)}
> $$
> 取 $\delta$ 为 $\delta_1,\,\delta_2,\,\delta_3,\,\delta_4$ 中最小者，则当 $0 < \lvert x - c\rvert < \delta$ 时，(2) 中的右端四个不等式同时成立。因此，对 $D$ 中的一切 $x$，若 $0 < \lvert x - c\rvert < \delta$，则
> $$
> \begin{aligned}
> \lvert f(x)\,g(x) - LM\rvert \quad & \text{对 (1) 应用三角不等式} \\
> &\le \lvert L\rvert\,\lvert g(x) - M\rvert + \lvert M\rvert\,\lvert f(x) - L\rvert + \lvert f(x) - L\rvert\,\lvert g(x) - M\rvert \\
> &\le (1 + \lvert L\rvert)\,\lvert g(x) - M\rvert + (1 + \lvert M\rvert)\,\lvert f(x) - L\rvert + \lvert f(x) - L\rvert\,\lvert g(x) - M\rvert \\
> &< \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \sqrt{\frac{\varepsilon}{3}}\,\sqrt{\frac{\varepsilon}{3}} = \varepsilon. \quad \text{由 (2)}
> \end{aligned}
> $$
> （最后一步中用到 $\lvert L\rvert \le 1 + \lvert L\rvert$、$\lvert M\rvert \le 1 + \lvert M\rvert$，再结合 (2) 中四个右端不等式。）至此完成极限乘积法则的证明。
>
> **Proof of the Limit Quotient Rule（极限商法则的证明）** 我们先证
> $$\lim_{x\to c}\frac{1}{g(x)} = \frac{1}{M}.$$
> 由此可由极限乘积法则得
> $$\lim_{x\to c}\frac{f(x)}{g(x)} = \lim_{x\to c}\left(f(x) \cdot \frac{1}{g(x)}\right) = \lim_{x\to c} f(x) \cdot \lim_{x\to c}\frac{1}{g(x)} = L \cdot \frac{1}{M} = \frac{L}{M}.$$
>
> 设给定 $\varepsilon > 0$。要证 $\lim_{x\to c}\dfrac{1}{g(x)} = \dfrac{1}{M}$，即须找到 $\delta > 0$ 使得
> $$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert < \varepsilon \quad \text{当} \quad 0 < \lvert x - c\rvert < \delta.$$
>
> 因为 $g$ 在 $x \to c$ 时极限为 $M$，且 $\lvert M\rvert > 0$，故存在正数 $\delta_1$ 使得
> $$\lvert g(x) - M\rvert < \frac{\lvert M\rvert}{2} \quad \text{当} \quad 0 < \lvert x - c\rvert < \delta_1. \qquad \text{(3)}$$
>
> 对任意实数 $A,\,B$，由三角不等式可得 $\lvert A\rvert - \lvert B\rvert \le \lvert A - B\rvert$ 与 $\lvert B\rvert - \lvert A\rvert \le \lvert A - B\rvert$，从而
> $$\bigl\lvert\,\lvert A\rvert - \lvert B\rvert\,\bigr\rvert \le \lvert A - B\rvert.$$
> 取 $A = g(x)$、$B = M$，即
> $$\bigl\lvert\,\lvert g(x)\rvert - \lvert M\rvert\,\bigr\rvert \le \lvert g(x) - M\rvert.$$
> 与 (3) 右端结合，依次得
> $$
> \begin{aligned}
> \bigl\lvert\,\lvert g(x)\rvert - \lvert M\rvert\,\bigr\rvert &< \frac{\lvert M\rvert}{2}, \\
> -\frac{\lvert M\rvert}{2} < \lvert g(x)\rvert - \lvert M\rvert &< \frac{\lvert M\rvert}{2}, \\
> \frac{\lvert M\rvert}{2} < \lvert g(x)\rvert &< \frac{3\lvert M\rvert}{2}, \\
> \lvert M\rvert < 2\,\lvert g(x)\rvert &< 3\,\lvert M\rvert, \\
> \frac{1}{\lvert g(x)\rvert} < \frac{2}{\lvert M\rvert} &< \frac{3}{\lvert g(x)\rvert}.
> \end{aligned}
> \qquad \text{(4)}
> $$
> 因此，$0 < \lvert x - c\rvert < \delta_1$ 蕴含
> $$
> \begin{aligned}
> \left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert 
> &= \left\lvert \frac{M - g(x)}{M\,g(x)}\right\rvert \le \frac{1}{\lvert M\rvert} \cdot \frac{1}{\lvert g(x)\rvert} \cdot \lvert M - g(x)\rvert \\
> &< \frac{1}{\lvert M\rvert} \cdot \frac{2}{\lvert M\rvert} \cdot \lvert M - g(x)\rvert. \quad \text{由 (4)}
> \end{aligned}
> \qquad \text{(5)}
> $$
> 因为 $\dfrac{1}{2}\lvert M\rvert^2 \varepsilon > 0$，故存在 $\delta_2 > 0$ 使得
> $$\lvert M - g(x)\rvert < \frac{\varepsilon}{2}\,\lvert M\rvert^2 \quad \text{当} \quad 0 < \lvert x - c\rvert < \delta_2. \qquad \text{(6)}$$
>
> 取 $\delta$ 为 $\delta_1,\,\delta_2$ 中较小者，则 (5) 与 (6) 中的结论在 $0 < \lvert x - c\rvert < \delta$ 时同时成立；二者合起来给出
> $$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert < \varepsilon \quad \text{当} \quad 0 < \lvert x - c\rvert < \delta.$$
> 至此完成极限商法则的证明。

> [!theorem] 📐 THEOREM 4 — The Sandwich Theorem（夹逼定理）
> 设 $g(x) \le f(x) \le h(x)$ 对包含 $c$ 的某开区间 $I$ 中的一切 $x$ 成立（$x = c$ 本身可能除外），且
> $$\lim_{x\to c} g(x) = \lim_{x\to c} h(x) = L.$$
> 则
> $$\lim_{x\to c} f(x) = L.$$
>
> **Proof for Right-Hand Limits（右极限情形的证明）** 设
> $$\lim_{x\to c^+} g(x) = \lim_{x\to c^+} h(x) = L.$$
> 则对任意 $\varepsilon > 0$，存在 $\delta > 0$ 使区间 $(c,\,c + \delta) \subset I$，且
> $$L - \varepsilon < g(x) < L + \varepsilon \quad \text{且} \quad L - \varepsilon < h(x) < L + \varepsilon$$
> 当 $c < x < c + \delta$ 时成立。因为总有 $g(x) \le f(x) \le h(x)$，当 $c < x < c + \delta$ 时便有
> $$
> \begin{aligned}
> L - \varepsilon < g(x) \le f(x) \le h(x) &< L + \varepsilon, \\
> L - \varepsilon < f(x) &< L + \varepsilon, \\
> -\varepsilon < f(x) - L &< \varepsilon.
> \end{aligned}
> $$
> 因此，当 $c < x < c + \delta$ 时，$\lvert f(x) - L\rvert < \varepsilon$。
>
> **Proof for Left-Hand Limits（左极限情形的证明）** 设
> $$\lim_{x\to c^-} g(x) = \lim_{x\to c^-} h(x) = L.$$
> 则对任意 $\varepsilon > 0$，存在 $\delta > 0$ 使区间 $(c - \delta,\,c) \subset I$，且
> $$L - \varepsilon < g(x) < L + \varepsilon \quad \text{且} \quad L - \varepsilon < h(x) < L + \varepsilon$$
> 当 $c - \delta < x < c$ 时成立。仿前同样可得：当 $c - \delta < x < c$ 时，$\lvert f(x) - L\rvert < \varepsilon$。
>
> **Proof for Two-Sided Limits（双侧极限情形的证明）** 若
> $$\lim_{x\to c} g(x) = \lim_{x\to c} h(x) = L,$$
> 则 $g(x)$ 与 $h(x)$ 在 $x \to c^+$ 与 $x \to c^-$ 时均趋近 $L$；故
> $$\lim_{x\to c^+} f(x) = L, \qquad \lim_{x\to c^-} f(x) = L.$$
> 因而 $\lim_{x\to c} f(x)$ 存在且等于 $L$。
