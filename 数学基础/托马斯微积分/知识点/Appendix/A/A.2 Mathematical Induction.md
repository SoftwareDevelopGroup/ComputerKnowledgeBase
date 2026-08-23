---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Appendix A Real Numbers and the Real Line
section: A.2 Mathematical Induction（数学归纳法）
tags: [微积分, 数学归纳法, 归纳证明, 正整数, 导数和法则, 阶乘, 托马斯微积分]
prerequisites: []
aliases: [数学归纳法, 归纳法, Mathematical Induction, A.2 数学归纳法]
---

# A.2 Mathematical Induction（数学归纳法）

> [!info] 📘 **本节引言**
> 本节介绍数学归纳法原理，并用它证明求和公式、不等式以及有限个函数之和的导数和法则等结论。

## 数学归纳法原理（The Principle of Mathematical Induction）

许多公式，例如

$$ 1+2+\cdots+n=\frac{n(n+1)}{2}, $$

都可以通过运用一个称为**数学归纳法原理（mathematical induction principle）**的公理，证明它们对每个正整数 $n$ 都成立。运用这一公理的证明称为**数学归纳法证明（proof by mathematical induction）**，或简称**归纳法证明（proof by induction）**。

用归纳法证明一个公式的步骤如下：

1. 验证该公式对 $n=1$ 成立。
2. 证明：若该公式对某个正整数 $n=k$ 成立，**那么**它对下一个整数 $n=k+1$ 也成立。

归纳法公理指出：一旦完成这两步，该公式就对所有正整数 $n$ 都成立。由第 1 步，它对 $n=1$ 成立；由第 2 步，它对 $n=2$ 成立，从而再由第 2 步对 $n=3$ 成立，再由第 2 步对 $n=4$ 成立，依此类推。这就像多米诺骨牌：如果第一张倒下，并且第 $k$ 张倒下时总能把第 $(k+1)$ 张也撞倒，那么所有的骨牌都会倒下。

> [!example] ✏️ EXAMPLE 1 — Sum of the First $n$ Positive Integers（前 $n$ 个正整数之和）
> 用数学归纳法证明：对每个正整数 $n$，
> $$ 1+2+\cdots+n=\frac{n(n+1)}{2}. $$
> 
> **Solution.** 我们通过完成上述两步来完成证明。
> 
> 1. 公式对 $n=1$ 成立，因为
>    $$ 1=\frac{1(1+1)}{2}. $$
> 2. 若公式对 $n=k$ 成立，它是否也对 $n=k+1$ 成立？答案是肯定的，证明如下。若
>    $$ 1+2+\cdots+k=\frac{k(k+1)}{2}, $$
>    则由此可得
>    $$ \begin{aligned} 1+2+\cdots+k+(k+1) &= \frac{k(k+1)}{2}+(k+1)=\frac{k^2+k+2k+2}{2} \\ &= \frac{(k+1)(k+2)}{2}=\frac{(k+1)\bigl((k+1)+1\bigr)}{2}. \end{aligned} $$
> 
> 这串等式中的最后一个表达式，正是 $\frac{n(n+1)}{2}$ 在 $n=k+1$ 时的情形。
> 
> 数学归纳法原理现在保证了原公式对所有正整数 $n$ 都成立。

在第 5.2 节的例 4 中，我们曾给出前 $n$ 个正整数之和公式的另一种证明。不过，数学归纳法证明也可用于求前 $n$ 个正整数的平方和与立方和（习题 9 和 10）。下面是另一个归纳法证明的例子。

> [!example] ✏️ EXAMPLE 2 — Sum of a Finite Geometric Series（有限等比数列之和）
> 用数学归纳法证明：对所有正整数 $n$，
> $$ \frac{1}{2^1}+\frac{1}{2^2}+\cdots+\frac{1}{2^n}=1-\frac{1}{2^n}. $$
> 
> **Solution.** 我们通过完成数学归纳法的两步来完成证明。
> 
> 1. 公式对 $n=1$ 成立，因为
>    $$ \frac{1}{2^1}=1-\frac{1}{2^1}. $$
> 2. 若
>    $$ \frac{1}{2^1}+\frac{1}{2^2}+\cdots+\frac{1}{2^k}=1-\frac{1}{2^k}, $$
>    则由此可得
>    $$ \begin{aligned} \frac{1}{2^1}+\frac{1}{2^2}+\cdots+\frac{1}{2^k}+\frac{1}{2^{k+1}} &= 1-\frac{1}{2^k}+\frac{1}{2^{k+1}}=1-\frac{1\cdot2}{2^k\cdot2}+\frac{1}{2^{k+1}} \\ &= 1-\frac{2}{2^{k+1}}+\frac{1}{2^{k+1}}=1-\frac{1}{2^{k+1}}. \end{aligned} $$
> 
> 于是，只要公式对 $n=k$ 成立，它便对 $n=k+1$ 成立。
> 
> 这两步验证完毕后，数学归纳法原理就保证了该公式对每个正整数 $n$ 都成立。

## 从其他整数开始（Other Starting Integers）

有些归纳论证不是从 $n=1$ 开始，而是从另一个整数开始。这类论证的步骤如下：

1. 验证公式对 $n=n_1$（第一个适当的整数）成立。
2. 证明：若公式对任意整数 $n=k\ge n_1$ 成立，则它也对 $n=k+1$ 成立。

一旦完成这两步，数学归纳法原理就保证了该公式对所有 $n\ge n_1$ 都成立。

> [!example] ✏️ EXAMPLE 3 — $n!>3^n$ for Large Enough $n$（足够大时 $n!>3^n$）
> 证明：当 $n$ 足够大时，$n!>3^n$。
> 
> **Solution.** 多"大"才算足够大？我们先试验一下：
> 
> | $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
> | $n!$ | 1 | 2 | 6 | 24 | 120 | 720 | 5040 |
> | $3^n$ | 3 | 9 | 27 | 81 | 243 | 729 | 2187 |
> 
> 看起来当 $n\ge7$ 时有 $n!>3^n$。为确认这一点，我们运用数学归纳法。在第 1 步取 $n_1=7$，并完成第 2 步。
> 
> 假设对某个 $k\ge7$ 有 $k!>3^k$。则
> $$ (k+1)!=(k+1)(k!)>(k+1)3^k>7\cdot3^k>3^{k+1}. $$
> 
> 因此，对 $k\ge7$，
> $$ k!>3^k \quad \text{推出} \quad (k+1)!>3^{k+1}. $$
> 
> 数学归纳法原理现在保证了 $n!>3^n$ 对所有 $n\ge7$ 都成立。

## 有限个函数之和的导数和法则的证明（Proof of the Derivative Sum Rule for Sums of Finitely Many Functions）

我们用数学归纳法证明如下命题：

$$ \frac{d}{dx}(u_1+u_2+\cdots+u_n)=\frac{du_1}{dx}+\frac{du_2}{dx}+\cdots+\frac{du_n}{dx}. $$

当 $n=2$ 时该命题成立，这已在第 3.3 节中证明。这是归纳证明的第 1 步。

第 2 步是证明：若该命题对某个正整数 $n=k$（其中 $k\ge n_0=2$）成立，则它对 $n=k+1$ 也成立。于是假设

$$ \frac{d}{dx}(u_1+u_2+\cdots+u_k)=\frac{du_1}{dx}+\frac{du_2}{dx}+\cdots+\frac{du_k}{dx}. \tag{1} $$

那么

$$ \begin{aligned} \frac{d}{dx}(u_1+u_2+\cdots+u_k+u_{k+1}) \\ &\quad \text{（把这个和定义的函数记作 }u\text{，把 }u_{k+1}\text{ 记作 }v\text{）} \\ &= \frac{d}{dx}(u_1+u_2+\cdots+u_k)+\frac{du_{k+1}}{dx} \quad \text{和的导数法则 }\frac{d}{dx}(u+v) \\ &= \frac{du_1}{dx}+\frac{du_2}{dx}+\cdots+\frac{du_k}{dx}+\frac{du_{k+1}}{dx} \quad \text{式 (1)} \end{aligned} $$

这两步验证完毕后，数学归纳法原理就保证了该和法则对每个整数 $n\ge2$ 都成立。
