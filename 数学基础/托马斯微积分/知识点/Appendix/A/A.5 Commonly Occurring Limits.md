---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Appendix A Real Numbers and the Real Line
section: A.5 Commonly Occurring Limits（常见极限）
tags: [微积分, 数列极限, 常见极限, 夹逼定理, 洛必达法则, 指数函数, 阶乘, 托马斯微积分]
prerequisites:
  - "[[10.01 Sequences]]"
  - "[[7.5 Indeterminate Forms and L'Hôpital's Rule]]"
aliases: [常见极限, Commonly Occurring Limits, A.5 常见极限]
---

# A.5 Commonly Occurring Limits（常见极限）

> [!info] 📘 本节引言
> 本附录验证 10.1 节定理 5 中的极限 (4)–(6)。

## Limit 4：若 $\lvert x\rvert < 1$，则 $\lim_{n\to\infty} x^n = 0$

我们需要证明：对每个 $\varepsilon > 0$，都存在足够大的整数 $N$，使得对所有大于 $N$ 的 $n$，都有 $\lvert x\rvert^n < \varepsilon$。由于 $\varepsilon^{1/n} \to 1$（当 $n \to \infty$）而 $\lvert x\rvert < 1$，故存在整数 $N$ 使得 $\lvert x\rvert < \varepsilon^{1/N}$。换言之，
$$\lvert x\rvert^N < \varepsilon. \tag{1}$$
这正是我们所需的整数，因为若 $\lvert x\rvert < 1$，则
$$\lvert x\rvert^n < \lvert x\rvert^N \quad \text{对所有 } n > N. \tag{2}$$
结合 (1) 与 (2) 得：对所有 $n > N$，$\lvert x\rvert^n < \varepsilon$，证明完毕。

## Limit 5：对任意数 $x$，$\lim_{n\to\infty}\left(1+\frac{x}{n}\right)^n = e^x$

令
$$a_n = \left(1+\frac{x}{n}\right)^n.$$
则
$$\ln a_n = \ln\left(1+\frac{x}{n}\right)^n = n\ln\left(1+\frac{x}{n}\right) \to x,$$
如下面的洛必达法则应用所示（对 $n$ 求导）：
$$\lim_{n\to\infty} n\ln\left(1+\frac{x}{n}\right) = \lim_{n\to\infty}\frac{\ln(1+x/n)}{1/n} = \lim_{n\to\infty}\frac{-\dfrac{x}{n^2\left(1+\dfrac{x}{n}\right)}}{-\dfrac{1}{n^2}} = \lim_{n\to\infty}\frac{x}{1+\dfrac{x}{n}} = x.$$
对 10.1 节的定理 3 应用 $f(x) = e^x$，可得
$$\left(1+\frac{x}{n}\right)^n = e^{\ln a_n} \to e^x.$$

## Limit 6：对任意数 $x$，$\lim_{n\to\infty}\frac{x^n}{n!} = 0$

由于
$$-\frac{\lvert x\rvert^n}{n!} \le \frac{x^n}{n!} \le \frac{\lvert x\rvert^n}{n!},$$
我们只需证明 $\dfrac{\lvert x\rvert^n}{n!} \to 0$。然后即可应用数列的夹逼定理（10.1 节定理 2）得出 $\dfrac{x^n}{n!} \to 0$。

证明 $\dfrac{\lvert x\rvert^n}{n!} \to 0$ 的第一步是选取整数 $M > \lvert x\rvert$，使得 $\dfrac{\lvert x\rvert}{M} < 1$。由刚证过的 Limit 4，我们便得到 $\left(\dfrac{\lvert x\rvert}{M}\right)^n \to 0$。然后我们把注意力限制在 $n > M$ 的取值上。对这些 $n$，可以写出
$$
\frac{\lvert x\rvert^n}{n!} = \frac{\lvert x\rvert^n}{1\cdot2\cdots M\cdot(M+1)\cdots n} \le \frac{\lvert x\rvert^n}{M!\,M^{n-M}} = \frac{\lvert x\rvert^M}{M!}\left(\frac{\lvert x\rvert}{M}\right)^{n-M},
$$
其中分母 $1\cdot2\cdots M\cdot(M+1)\cdots n$ 中的 $1\cdot2\cdots M$ 共有 $M$ 个因子（即 $M!$），而 $(M+1)\cdots n$ 的每个因子都不小于 $M$。因此，
$$0 \le \frac{\lvert x\rvert^n}{n!} \le \frac{\lvert x\rvert^M}{M!}\left(\frac{\lvert x\rvert}{M}\right)^{n-M}.$$
现在，常数 $\dfrac{\lvert x\rvert^M}{M!}$ 不随 $n$ 的增大而改变。于是夹逼定理告诉我们 $\dfrac{\lvert x\rvert^n}{n!} \to 0$，因为 $\left(\dfrac{\lvert x\rvert}{M}\right)^n \to 0$。
