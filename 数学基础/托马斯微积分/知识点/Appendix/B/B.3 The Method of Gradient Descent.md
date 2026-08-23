---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Appendix B Determinants
section: B.3 The Method of Gradient Descent（梯度下降法）
tags: [微积分, 梯度下降, 最速下降法, 学习率, 数值优化, 局部极小值, 梯度上升, 托马斯微积分]
prerequisites:
  - "[[14.05 Directional Derivatives and Gradient Vectors]]"
  - "[[B.2 Extreme Values and Saddle Points for Functions of More than Two Variables]]"
aliases: [梯度下降法, The Method of Gradient Descent, B.3 梯度下降法]
---

# B.3 The Method of Gradient Descent（梯度下降法）

> [!info] 📘 本节引言
> 本节介绍梯度下降法（又称最速下降法），用于数值逼近 $n$ 元函数的局部极小值，并讨论步长（学习率）的选择。

在 14.7 节和附录 B.2 中，我们讨论了使我们能够解析地确定可微函数 $f$（$n$ 元）的局部极大值、局部极小值与鞍点的方法。虽然这些方法适用于任何整数 $n \ge 2$，但当 $n$ 非常大时它们可能不实用。此外，有些重要应用里我们可以在没有 $f$ 的显式公式的情况下求（或近似）$f$ 及其偏导数的值。这些是数值搜索 $n$ 元函数局部极值的部分原因。

在本附录中，我们用记号 $f(\mathbf{x})$ 表示 $n$ 元函数 $f(x_1, x_2, \ldots, x_n)$ 的值，其中 $\mathbf{x} = \langle x_1, x_2, \ldots, x_n \rangle$ 是点 $(x_1, x_2, \ldots, x_n)$ 的位置向量。$f$ 在该点沿单位向量 $\mathbf{u}$ 方向的方向导数可以表示为
$$D_{\mathbf{u}}f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u}.$$

在引入方向导数概念的 14.5 节中，我们注意到函数 $f$ 沿 $\nabla f$ 方向增加最快，而沿 $-\nabla f$ 方向减小最快。这引出**梯度下降法（method of gradient descent）**（又称**最速下降法（method of steepest descent）**），用于数值逼近 $n$ 元函数 $f$ 的局部极小值。

初始近似 $\mathbf{x}_0$ 可以选择为对极小值可能出现位置的最佳猜测。（或者可以用随机选择的点作为 $\mathbf{x}_0$。）然后我们沿 $-\nabla f(\mathbf{x}_0)$ 方向迈出一步，得到下一个近似
$$\mathbf{x}_1 = \mathbf{x}_0 - h_0 \nabla f(\mathbf{x}_0),$$
其中正的量 $h_0$ 控制步长的大小。我们以同样的方式得到后续近似 $\mathbf{x}_2, \mathbf{x}_3, \ldots$。

## 梯度下降法（The Method of Gradient Descent）

1. 从一个局部极小值的第一近似 $f(\mathbf{x}_0)$ 出发。
2. 用第一近似得到第二近似、用第二近似得到第三近似，依此类推，使用公式
$$\mathbf{x}_{k+1} = \mathbf{x}_k - h_k \nabla f(\mathbf{x}_k), \tag{1}$$
其中 $h_k > 0$。

在应用中，包括机器学习领域中的应用，梯度下降法可以用于逼近含大量自变量的函数的局部极小值。为洞察这一方法，考虑 Figure B.2，其中展示了把该方法应用于二元函数 $f(\mathbf{x}) = f(x, y)$ 的情形（我们把 $\mathbf{x} = \langle x, y \rangle$ 取作点 $(x, y)$ 的位置向量）。注意向量 $-\nabla f(\mathbf{x}_0)$ 垂直于过点 $\mathbf{x}_0$ 的 $f$ 的等值线，该等值线由平面中满足方程 $f(\mathbf{x}) = f(\mathbf{x}_0)$ 的所有点 $\mathbf{x}$ 组成。把 $-\nabla f(\mathbf{x}_0)$ 加到 $\mathbf{x}_0$ 上就给出下一个近似 $\mathbf{x}_1$。同样，$-\nabla f(\mathbf{x}_1)$ 垂直于过该点的等值线。这个过程以类似的方式继续。除了等值线，Figure B.2 还展示了曲面 $z = f(\mathbf{x})$，它有助于直观看到值 $f(\mathbf{x}_0), f(\mathbf{x}_1), f(\mathbf{x}_2), \ldots$ 的下降。这些值看起来正在趋近 $f$ 的一个极小值。

![[Pasted image 20260823215909.png]]

## 学习率的选择（Choosing the Learning Rate）

在 Figure B.2 中，我们对所有 $h_k$ 使用常数 $h = 1$。Figure B.3 说明 $h$ 值的不同选择会如何影响方法的性能。当 $h$ 较小时（Figure B.3a），方法被迫迈更多的步。通常取更大的步长更有效（Figure B.3b，与 Figure B.2 中相同的 $h$）。若 $h$ 的值太大（Figure B.3c），则方法可能不收敛。为理解当 $h$ 太大时方法为何可能失效，回想一下：虽然在 $\mathbf{x}_k$ 处函数 $f$ 沿 $-\nabla f(\mathbf{x}_k)$ 方向减小最快，但若我们继续沿这个方向并离开 $\mathbf{x}_k$ 太远，函数可能开始增大。

![[Pasted image 20260823215921.png]]

为量 $h$（在机器学习中有时称为**学习率（learning rate）**）选择既不太小也不太大的合适值可能很有挑战性。这里我们只考虑梯度下降法使用常数、预先选定的值 $h_k = h$ 的情形。更高级的方法专注于识别合适的 $h_k$ 值（这些值可能不是常数）——其中之一涉及执行**线搜索（line search）**（见习题 5）。

## 梯度下降法的应用（An Application of Gradient Descent）

> [!example] ✏️ EXAMPLE 1
> 对函数 $f(x, y, z) = 2x^3y + 3y^2 + 6yz + 6z^2 - 6xy$ 应用梯度下降法，初始近似 $\mathbf{x}_0 = \langle 2, 1, -1 \rangle$，取 $h_k = h = 0.1$。列出 $k = 0, 1, 2, \ldots, 10$ 时 $\mathbf{x}_k$ 的分量与 $f(\mathbf{x}_k)$。
>
> **解答.** 在初始近似 $\mathbf{x}_0 = \langle 2, 1, -1 \rangle$ 处，有 $f(\mathbf{x}_0) = f(2, 1, -1) = 7$。
> 函数 $f$ 的梯度为
> $$\nabla f = \langle 6x^2y - 6y, \; 2x^3 + 6y + 6z - 6x, \; 6y + 12z \rangle.$$
> 在初始近似处求梯度值，得到 $\nabla f(\mathbf{x}_0) = \langle 18, 4, -6 \rangle$。
> 我们现在应用方程 (1) 得到第二近似
> $$
> \begin{aligned}
> \mathbf{x}_1 &= \mathbf{x}_0 - h_0 \nabla f(\mathbf{x}_0) \\
> &= \langle 2, 1, -1 \rangle - (0.1)\langle 18, 4, -6 \rangle \\
> &= \langle 0.2, 0.6, -0.4 \rangle.
> \end{aligned}
> $$
> 此时 $f(\mathbf{x}_1) \approx -0.11$。
> 随后用技术手段反复应用方程 (1) 得到近似 $\mathbf{x}_2, \mathbf{x}_3, \ldots$。这些近似以及相应的 $f$ 值列于下表。
>
> | $k$ | $\mathbf{x}_k$ 的 $x$ 分量 | $\mathbf{x}_k$ 的 $y$ 分量 | $\mathbf{x}_k$ 的 $z$ 分量 | $f(\mathbf{x}_k)$ |
> | :--- | :--- | :--- | :--- | :--- |
> | 0 | 2 | 1 | -1 | 7 |
> | 1 | 0.200000000000001 | 0.600000000000001 | -0.399999999999999 | -0.110400000000005 |
> | 2 | 0.545600000000001 | 0.598400000000001 | -0.280000000000001 | -1.22520965376901 |
> | 3 | 0.7977612025856 | 0.702237228236801 | -0.30304 | -1.8946600083389 |
> | 4 | 0.950951612242085 | 0.839832907434822 | -0.360734336942082 | -2.26841318086511 |
> | 5 | 0.999170298397954 | 0.95095391811045 | -0.431752877072477 | -2.43587094205513 |
> | 6 | 1.00011671520043 | 1.03943288055905 | -0.484221775451776 | -2.5295411401069 |
> | 7 | 0.999971125564279 | 1.1063062093209 | -0.526815373245074 | -2.58519263199985 |
> | 8 | 1.0000094577719 | 1.15861170717517 | -0.558420650943528 | -2.61825804593691 |
> | 9 | 0.999996308247422 | 1.19849707338251 | -0.583482894116396 | -2.63790410815758 |
> | 10 | 1.00000161770321 | 1.22948856581467 | -0.602401665206229 | -2.64957702176556 |

例 1 中的函数 $f$ 曾在附录 B.2 的例 3 中分析过，并已证明它有局部极小值 $f\left(1, \frac{4}{3}, -\frac{2}{3}\right) = -\frac{8}{3}$。例 1 中生成的近似序列看起来收敛到这个局部极小值。

梯度下降法旨在逼近多变量函数的局部极小值。若我们想逼近局部**极大值**，则应用**梯度上升（gradient ascent）**法
$$\mathbf{x}_{k+1} = \mathbf{x}_k + h_k \nabla f(\mathbf{x}_k),$$
即沿梯度 $\nabla f$ 的方向而非 $-\nabla f$ 的方向行进。
