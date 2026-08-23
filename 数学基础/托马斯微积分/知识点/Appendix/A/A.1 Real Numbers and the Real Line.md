---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Appendix A Real Numbers and the Real Line
section: A.1 Real Numbers and the Real Line（实数与直线）
tags: [微积分, 实数, 数轴, 不等式, 区间, 绝对值, 绝对值性质, 三角不等式, 托马斯微积分]
prerequisites: []
aliases: [实数与直线, Real Numbers and the Real Line, A.1 实数与直线]
---

# A.1 Real Numbers and the Real Line（实数与直线）

> [!info] 📘 **本节引言**
> 本节复习微积分所需要的实数、不等式、区间与绝对值等预备知识。

## 实数（Real Numbers）

微积分在很大程度上建立在实数系的性质之上。**实数（real numbers）**是可以用小数表示的数，例如

$$ -\frac{3}{4}=-0.75000\dots $$

$$ \frac{1}{3}=0.33333\dots $$

$$ \sqrt{2}=1.4142\dots $$

每种情形中的省略号 $\dots$ 都表示数字序列无限延续下去。每一个可以设想的小数展开都表示一个实数；不过，某些数有两种表示。例如，无限小数 $.999\dots$ 与 $1.000\dots$ 表示同一个实数 $1$。对任何具有无限个 $9$ 的尾数的数，类似的结论也成立。

实数在几何上可以表示为一条直线（称为**实数轴（real line）**）上的点。（教材在正文旁给出了一条带刻度、并标出如 $-2,-1,0,1,2,3,4$ 及 $\sqrt{2},\frac13$ 等点位置的实数轴示意图。）

> [!definition] 📐 RULES FOR INEQUALITIES（不等式运算法则）
> 若 $a,b,c$ 为实数，则：
> 1. $a<b \Rightarrow a+c<b+c$
> 2. $a<b \Rightarrow a-c<b-c$
> 3. $a<b$ 且 $c>0 \Rightarrow ac<bc$
> 4. $a<b$ 且 $c<0 \Rightarrow bc<ac$  
>    特例：$a<b \Rightarrow -b<-a$
> 5. $a>0 \Rightarrow \dfrac{1}{a}>0$
> 6. 若 $a$ 与 $b$ 同号（同为正或同为负），则 $a<b \Rightarrow \dfrac{1}{b}<\dfrac{1}{a}$

符号 $\mathbb{R}$ 表示实数系，或者等价地表示实数轴。

实数系的性质分为三类：代数性质、序性质与完备性。代数性质说明实数在通常的算术规则下可以加、减、乘、除（除数不能为 $0$）而得到更多实数。**绝不可除以 $0$。**

序性质在附录 A.6 中给出。左侧这些有用的法则都可以由它们推导出来，其中符号 $\Rightarrow$ 表示"推出（implies）"。

注意不等式乘以一个数的法则：乘以正数保持不等号方向；乘以负数则反转不等号方向。此外，对同号的数取倒数会反转不等号方向。例如 $2<5$，但 $-2>-5$，且 $\dfrac12>\dfrac15$。

实数系的完备性更为深刻，也更难精确定义。不过，这一性质对极限（第 2 章）的概念至关重要。粗略地说，它表明实数"足够多"以至于能"填满"实数轴，即实数轴上没有"洞"或"空隙"。若实数系不完备，微积分的许多定理都将失效。附录 A.6 将介绍相关的思想并讨论实数是如何构造出来的。

我们区分实数的三个特殊子集：

1. **自然数（natural numbers）**：$1,2,3,4,\dots$
2. **整数（integers）**：$0,\pm1,\pm2,\pm3,\dots$
3. **有理数（rational numbers）**：可以表示为分数 $\dfrac{m}{n}$ 的数，其中 $m,n$ 为整数且 $n\ne0$。例如

$$ \frac{1}{3},\quad -\frac{4}{9}=\frac{-4}{9}=\frac{4}{-9},\quad \frac{200}{13},\quad \text{以及}\quad 57=\frac{57}{1}. $$

有理数恰好是那些小数展开要么

a. **有限（terminating）**（以无限串零结尾）的实数，例如

$$ \frac{3}{4}=0.75000\dots=0.75, $$

要么

b. **最终循环（eventually repeating）**（以一个不断重复的数字块结尾）的实数，例如

$$ \frac{23}{11}=2.090909\dots=2.\overline{09} \quad \text{横线表示循环的数字块}. $$

有限小数展开是循环小数的一种特殊情形，因为末尾的零不断重复。

有理数集合具有实数的全部代数性质与序性质，但缺少完备性。例如，不存在平方为 $2$ 的有理数；在有理轴上 $\sqrt{2}$ 本应所在之处有一个"洞"。

不是有理数的实数称为**无理数（irrational numbers）**。它们的特征是非有限且非循环的小数展开。例如 $\pi,\ \sqrt{2},\ \sqrt[3]{5},$ 以及 $\log_{10}3$。由于每个小数展开都表示一个实数，所以有无穷多个无理数。有理数与无理数在实数轴上任意给定点的任意近旁都能找到。

集合记号对描述实数集合非常有用。**集合（set）**是一些对象的总体，这些对象称为集合的**元素（elements）**。若 $S$ 是一个集合，记号 $a\in S$ 表示 $a$ 是 $S$ 的元素，$a\notin S$ 表示 $a$ 不是 $S$ 的元素。若 $S$ 与 $T$ 是集合，则 $S\cup T$ 是它们的**并集（union）**，由属于 $S$ 或 $T$（或两者）的所有元素组成。**交集（intersection）** $S\cap T$ 由同时属于 $S$ 与 $T$ 的所有元素组成。**空集（empty set）** $\emptyset$ 是不含任何元素的集合。例如，有理数与无理数的交集是空集。

有些集合可以通过在花括号内**列举**元素来描述。例如，由小于 $6$ 的自然数（或正整数）组成的集合 $A$ 可写为

$$ A=\{1,2,3,4,5\}. $$

全体整数集合写作

$$ \{0,\pm1,\pm2,\pm3,\dots\}. $$

另一种描述集合的方法是在花括号内写入一条能生成该集合全部元素的**规则**。例如，集合

$$ A=\{x\mid x\text{ 是整数且 }0<x<6\} $$

就是小于 $6$ 的正整数集。

## 区间（Intervals）

实数轴的一个子集如果至少包含两个数，并且包含其任意两个元素之间的所有实数，就称为一个**区间（interval）**。例如，所有满足 $x>6$ 的实数 $x$ 组成的集合是一个区间，所有满足 $-2\le x\le5$ 的 $x$ 组成的集合也是。所有非零实数的集合不是一个区间，因为缺少了 $0$，它就没有包含 $-1$ 与 $1$ 之间的每一个实数（例如）。

在几何上，区间对应于实数轴上的射线与线段，以及实数轴本身。对应于线段的区间称为**有限区间（finite intervals）**；对应于射线与实数轴的区间称为**无限区间（infinite intervals）**。

一个有限区间若包含两个端点，则称为**闭（closed）**区间；若包含一个端点而不包含另一个，则称为**半开（half-open）**区间；若两个端点都不包含，则称为**开（open）**区间。端点也称为**边界点（boundary points）**，它们构成区间的**边界（boundary）**。区间的其余点称为**内点（interior points）**，它们共同组成区间的**内部（interior）**。无限区间若包含某个有限端点则为闭，否则为开。整个实数轴 $\mathbb{R}$ 是一个既开又闭的无限区间。表 A.1 总结了各类区间。

**表 A.1 区间的类型（Table A.1 Types of intervals）**

| 记号 Notation | 集合描述 Set description | 类型 Type | 图形 Picture |
| :--- | :--- | :--- | :--- |
| $(a,b)$ | $\{x\mid a<x<b\}$ | 开 Open | ○────○ 两端开 |
| $[a,b]$ | $\{x\mid a\le x\le b\}$ | 闭 Closed | ●────● 两端闭 |
| $[a,b)$ | $\{x\mid a\le x<b\}$ | 半开 Half-open | ●────○ 左闭右开 |
| $(a,b]$ | $\{x\mid a<x\le b\}$ | 半开 Half-open | ○────● 左开右闭 |
| $(a,\infty)$ | $\{x\mid x>a\}$ | 开 Open | ○────→ |
| $[a,\infty)$ | $\{x\mid x\ge a\}$ | 闭 Closed | ●────→ |
| $(-\infty,b)$ | $\{x\mid x<b\}$ | 开 Open | ←────○ |
| $(-\infty,b]$ | $\{x\mid x\le b\}$ | 闭 Closed | ←────● |
| $(-\infty,\infty)$ | $\mathbb{R}$（全体实数集） | 既开又闭 Both open and closed | ←────→ |

## 解不等式（Solving Inequalities）

寻找满足关于 $x$ 的不等式的区间或区间组的过程，称为**解不等式（solving the inequality）**。

> [!example] ✏️ EXAMPLE 1 — Solving Inequalities（解不等式并表示解集）
> 解下列不等式，并在实数轴上表示它们的解集。
> 
> (a) $2x-1<x+3$  
> (b) $\dfrac{6}{x-1}\ge 5$
> 
> **Solution.**  
> (a)
> $$ 2x-1<x+3 $$
> $$ 2x<x+4 \quad \text{两边加 }1 $$
> $$ x<4 \quad \text{两边减 }x $$
> 
> 解集是开区间 $(-\infty,4)$（见图 A.1a）。
> 
> (b) 不等式 $\dfrac{6}{x-1}\ge5$ 只有在 $x>1$ 时才可能成立，否则 $\dfrac{6}{x-1}$ 无定义或为负。因此 $x-1$ 为正，两边同乘 $x-1$ 时不等号方向保持不变：
> $$ \frac{6}{x-1}\ge 5 $$
> $$ 6\ge 5x-5 \quad \text{两边同乘 }x-1 $$
> $$ 11\ge 5x \quad \text{两边加 }5 $$
> $$ \frac{11}{5}\ge x \quad \text{即 }x\le\frac{11}{5} $$
> 
> 解集是半开区间 $\left(1,\dfrac{11}{5}\right]$（见图 A.1b）。
> 
> ![[Pasted image 20260823203234.png|300]]

## 绝对值（Absolute Value）

数 $x$ 的**绝对值（absolute value）**，记作 $\lvert x\rvert$，由下式定义：

$$ \lvert x\rvert = \begin{cases} x, & x\ge0, \\ -x, & x<0. \end{cases} $$

> [!example] ✏️ EXAMPLE 2 — Evaluating Absolute Values（绝对值求值）
> $$ \lvert 3\rvert=3,\quad \lvert 0\rvert=0,\quad \lvert -5\rvert=-(-5)=5,\quad \lvert -\lvert a\rvert\rvert=\lvert a\rvert. $$

在几何上，$x$ 的绝对值就是 $x$ 到实数轴上 $0$ 的距离。由于距离总是非负，可见对每个实数 $x$ 都有 $\lvert x\rvert\ge0$，且 $\lvert x\rvert=0$ 当且仅当 $x=0$。此外，

$$ \lvert x-y\rvert=\text{实数轴上 }x\text{ 与 }y\text{ 之间的距离}. $$

![[Pasted image 20260823203249.png|384]]

由于符号 $\sqrt{a}$ 总表示 $a$ 的**非负**平方根，绝对值还有一个等价定义：

$$ \lvert x\rvert=\sqrt{x^2}. $$

务必记住 $\sqrt{a^2}=\lvert a\rvert$。除非已经知道 $a\ge0$，否则不要写成 $\sqrt{a^2}=a$。

> [!definition] 📐 Absolute Value Properties（绝对值的性质）
> 1. $\lvert -a\rvert=\lvert a\rvert$　　一个数与其相反数具有相同的绝对值。
> 2. $\lvert ab\rvert=\lvert a\rvert\,\lvert b\rvert$　　乘积的绝对值等于绝对值的乘积。
> 3. $\left\lvert\dfrac{a}{b}\right\rvert=\dfrac{\lvert a\rvert}{\lvert b\rvert}$　　商的绝对值等于绝对值的商。
> 4. $\lvert a+b\rvert\le\lvert a\rvert+\lvert b\rvert$　　**三角不等式（triangle inequality）**。两数之和的绝对值不大于它们绝对值之和。

注意 $\lvert -a\rvert\ne-\lvert a\rvert$。例如 $\lvert -3\rvert=3$，而 $-\lvert 3\rvert=-3$。若 $a$ 与 $b$ 异号，则 $\lvert a+b\rvert$ 严格小于 $\lvert a\rvert+\lvert b\rvert$；在其他所有情形下，$\lvert a+b\rvert$ 等于 $\lvert a\rvert+\lvert b\rvert$。在诸如 $\lvert -3+5\rvert$ 这样的式子中，绝对值号的作用如同括号：我们先做括号内的运算，再取绝对值。

> [!definition] 📐 FURTHER PROPERTIES: ABSOLUTE VALUES AND INTERVALS（绝对值与区间的进一步性质）
> 若 $a$ 为任意正数，则：
> 5. $\lvert x\rvert=a \iff x=\pm a$
> 6. $\lvert x\rvert<a \iff -a<x<a$
> 7. $\lvert x\rvert>a \iff x>a\text{ 或 }x<-a$
> 8. $\lvert x\rvert\le a \iff -a\le x\le a$
> 9. $\lvert x\rvert\ge a \iff x\ge a\text{ 或 }x\le -a$

> [!example] ✏️ EXAMPLE 3 — Evaluating Absolute Values（绝对值求值）
> $$ \lvert -3+5\rvert=\lvert 2\rvert=2<\lvert -3\rvert+\lvert 5\rvert=8 $$
> $$ \lvert 3+5\rvert=\lvert 8\rvert=\lvert 3\rvert+\lvert 5\rvert $$
> $$ \lvert -3-5\rvert=\lvert -8\rvert=8=\lvert -3\rvert+\lvert -5\rvert $$

不等式 $\lvert x\rvert<a$ 表示 $x$ 到 $0$ 的距离小于正数 $a$。这意味着 $x$ 必须落在 $-a$ 与 $a$ 之间，正如图 A.3 所示。

![[Pasted image 20260823203302.png|406]]

表中第 5–9 条都是绝对值定义的直接推论，在解涉及绝对值的方程或不等式时常常很有用。表中出现的符号 $\iff$ 常被数学家用来表示"当且仅当（if and only if）"的逻辑关系，它也表示"推出且被推出"。

> [!example] ✏️ EXAMPLE 4 — Solving an Absolute Value Equation（解绝对值方程）
> 解方程 $\lvert 2x-3\rvert=7$。
> 
> **Solution.** 由性质 5，$2x-3=\pm7$，因此有两种可能：
> $$ 2x-3=7 \qquad 2x-3=-7 \qquad \text{去掉绝对值后的等价方程} $$
> $$ 2x=10 \qquad 2x=-4 \qquad \text{按通常方法求解} $$
> $$ x=5 \qquad x=-2 $$
> 
> 方程 $\lvert 2x-3\rvert=7$ 的解为 $x=5$ 与 $x=-2$。

> [!example] ✏️ EXAMPLE 5 — Solving an Absolute Value Inequality（解绝对值不等式）
> 解不等式 $\left\lvert 5-\dfrac{2}{x}\right\rvert<1$。
> 
> **Solution.** 我们有
> $$ \left\lvert 5-\frac{2}{x}\right\rvert<1 $$
> $$ \iff -1<5-\frac{2}{x}<1 \quad \text{性质 6} $$
> $$ \iff -6<-\frac{2}{x}<-4 \quad \text{两边减 }5 $$
> $$ \iff 3>\frac{1}{x}>2 \quad \text{两边同乘 }-\frac{1}{2} $$
> $$ \iff \frac{1}{3}<x<\frac{1}{2} \quad \text{取倒数} $$
> 
> 注意这里如何运用了各种不等式法则：乘以负数会反转不等号方向，对两边都为正的不等式取倒数也会反转方向。原不等式成立当且仅当 $\dfrac{1}{3}<x<\dfrac{1}{2}$。解集是开区间 $\left(\dfrac{1}{3},\dfrac{1}{2}\right)$。
