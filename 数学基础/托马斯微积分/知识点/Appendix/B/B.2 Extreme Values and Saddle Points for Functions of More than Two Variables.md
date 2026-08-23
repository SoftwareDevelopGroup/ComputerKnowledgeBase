---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Appendix B Determinants
section: B.2 Extreme Values and Saddle Points for Functions of More than Two Variables（多于两个变量的函数的极值与鞍点）
tags: [微积分, 多元函数, 极值, 鞍点, Hessian矩阵, 主子式, 临界点, 开球, 托马斯微积分]
prerequisites:
  - "[[14.07 Extreme Values and Saddle Points]]"
  - "[[14.03 Partial Derivatives]]"
  - "[[B.1 Determinants]]"
aliases: [多于两个变量的函数的极值与鞍点, Extreme Values and Saddle Points for Functions of More than Two Variables, B.2 极值与鞍点]
---

# B.2 Extreme Values and Saddle Points for Functions of More than Two Variables（多于两个变量的函数的极值与鞍点）

> [!info] 📘 本节引言
> 14.7 节讨论了二元函数的极值与鞍点，本节把它推广到三个或更多变量的函数，使用 Hessian 矩阵的主子式行列式进行判定。

许多应用涉及多个自变量的函数。例如，为预测美国的能源趋势，一个计量经济学模型可能使用五十个自变量的函数 $f(p_1, p_2, \ldots, p_{50})$，表示五十个州的汽油平均价格。

确定这类函数的极值常常很重要。在 14.1 节我们定义了 $n$ 元函数，其定义域是实数 $n$ 元组 $(x_1, x_2, \ldots, x_n)$ 的集合。定义域是 $n$ 维空间中的一个区域。

## 开球与区域（Open Balls and Regions）

我们将用开球来定义一些重要概念，例如内点与边界点。以 $(a_1, a_2, \ldots, a_n)$ 为中心、半径为 $r$ 的 $n$ 维开球（或开 $n$ 球）是满足
$$(x_1 - a_1)^2 + (x_2 - a_2)^2 + \cdots + (x_n - a_n)^2 < r^2$$
的点 $(x_1, x_2, \ldots, x_n)$ 组成的集合。

> [!example] ✏️ EXAMPLE 1
> 判断 4 维空间中的下列点是否在以 $(-2, 0, 3, 1)$ 为中心、半径为 $5$ 的开 4 球内。
> **(a)** $(1, -2, 1, 0)$
> **(b)** $(0, 1, -1, 5)$
>
> **解答.**
> **(a)** $(1 - (-2))^2 + (-2 - 0)^2 + (1 - 3)^2 + (0 - 1)^2 = 9 + 4 + 4 + 1 = 18 < 25 = 5^2$；因此，$(1, -2, 1, 0)$ 在开 4 球内。
> **(b)** $(0 - (-2))^2 + (1 - 0)^2 + (-1 - 3)^2 + (5 - 1)^2 = 4 + 1 + 16 + 16 = 37 \ge 25 = 5^2$；因此，$(0, 1, -1, 5)$ 不在开 4 球内。

利用开 $n$ 球，我们可以把 14.1 节的定义推广到 $n$ 维空间中的区域。

> [!definition] 📐 DEFINITIONS — Interior and Boundary Points（内点与边界点）
> $n$ 维空间中区域 $D$ 内的点 $(x_1, x_2, \ldots, x_n)$ 若是一个完全位于 $D$ 内的正半径开 $n$ 球的中心，则称为 $D$ 的**内点（interior point）**。若以 $(x_1, x_2, \ldots, x_n)$ 为中心的每个开 $n$ 球既包含位于 $D$ 之外的点，也包含位于 $D$ 之内的点，则 $(x_1, x_2, \ldots, x_n)$ 是 $D$ 的**边界点（boundary point）**。
> $D$ 的**内部（interior）**是 $D$ 的内点的集合。$D$ 的**边界（boundary）**是 $D$ 的边界点的集合。
> 若一个区域完全由内点组成，则它是**开**的（open）。若一个区域包含其全部边界，则它是**闭**的（closed）。
> 若一个区域位于某个有限半径的开 $n$ 球内，则它是**有界**的（bounded）。若它不是有界的，则是**无界**的（unbounded）。

## 极值与鞍点（Extreme Values and Saddle Points）

> [!definition] 📐 DEFINITIONS — Local Maximum and Local Minimum（局部极大值与局部极小值）
> 设 $f(x_1, x_2, \ldots, x_n)$ 定义在实数 $n$ 元组 $(x_1, x_2, \ldots, x_n)$ 的集合 $D$ 上，$D$ 包含点 $(a_1, a_2, \ldots, a_n)$。
> 若对位于以 $(a_1, a_2, \ldots, a_n)$ 为中心的开 $n$ 球内的所有定义域点 $(x_1, x_2, \ldots, x_n)$，都有 $f(a_1, a_2, \ldots, a_n) \ge f(x_1, x_2, \ldots, x_n)$，则 $f(a_1, a_2, \ldots, a_n)$ 是 $f$ 的一个**局部极大值（local maximum）**。
> 若对位于以 $(a_1, a_2, \ldots, a_n)$ 为中心的开 $n$ 球内的所有定义域点 $(x_1, x_2, \ldots, x_n)$，都有 $f(a_1, a_2, \ldots, a_n) \le f(x_1, x_2, \ldots, x_n)$，则 $f(a_1, a_2, \ldots, a_n)$ 是 $f$ 的一个**局部极小值（local minimum）**。

> [!example] ✏️ EXAMPLE 2
> 函数 $f(x, y, z) = 10 - x^2 - y^2 - z^2$ 定义在整个三维空间上。Figure B.1 展示了这个函数的一族等值面。水平集 $f(x, y, z) = 10$ 是单点，即原点。在每一点 $(x, y, z)$ 处都有 $f(x, y, z) = 10 - x^2 - y^2 - z^2 \le 10 = f(0, 0, 0)$；因此，$f$ 在 $(0, 0, 0)$ 处有局部（且绝对）极大值 $10$。这个函数没有局部极小值。

![[Pasted image 20260823215436.png]]

假设 $f(x_1, x_2, \ldots, x_n)$ 在其定义域的内点 $(a_1, a_2, \ldots, a_n)$ 处有局部极大值或局部极小值，且它的一阶偏导数在该点都有定义。则函数 $g_1(t) = f(t, a_2, \ldots, a_n)$ 必在 $t = a_1$ 处有局部极值。因此，$g_1'(a_1) = 0$，从而
$$\frac{\partial f}{\partial x_1}(a_1, a_2, \ldots, a_n) = 0.$$
同样，我们可以用函数 $g_2(t) = f(a_1, t, a_3, \ldots, a_n)$ 证明
$$\frac{\partial f}{\partial x_2}(a_1, a_2, \ldots, a_n) = 0,$$
并以同样的方式继续，得出结论
$$\frac{\partial f}{\partial x_i}(a_1, a_2, \ldots, a_n) = 0$$
对所有 $i = 1, 2, \ldots, n$ 成立。

上面的讨论把 14.7 节的定理 10 推广到 $n$ 元函数。我们用梯度记号更简洁地表述它：
$$\nabla f = \left\langle \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n} \right\rangle.$$

> [!theorem] 📐 THEOREM 3 — First Derivative Theorem for Local Extreme Values (General Version)（局部极值的一阶导数定理·一般形式）
> 若 $f(x_1, x_2, \ldots, x_n)$ 在其定义域的内点 $(a_1, a_2, \ldots, a_n)$ 处有局部极大值或局部极小值，且 $\nabla f$ 在该点存在，则 $\nabla f(a_1, a_2, \ldots, a_n) = \mathbf{0}$，其中 $\mathbf{0} = \langle 0, 0, \ldots, 0 \rangle$ 表示 $n$ 维空间中的零向量。

下面的临界点定义使用梯度记号。

> [!definition] 📐 DEFINITION — Critical Point（临界点）
> $f$ 的定义域中使 $\nabla f = \mathbf{0}$ 或 $\nabla f$ 不存在的内点称为 $f$ 的**临界点（critical point）**。

注意：当一个向量的一个或多个分量不存在时，该向量不存在。

鞍点的概念可以推广到 $n$ 元函数 $f$。

> [!definition] 📐 DEFINITION — Saddle Point（鞍点）
> 可微函数 $f(x_1, x_2, \ldots, x_n)$ 的临界点 $(a_1, a_2, \ldots, a_n)$ 称为**鞍点（saddle point）**，若以该点为中心的每个开 $n$ 球都既包含满足 $f(a_1, a_2, \ldots, a_n) > f(x_1, x_2, \ldots, x_n)$ 的点 $(x_1, x_2, \ldots, x_n)$，也包含满足 $f(a_1, a_2, \ldots, a_n) < f(y_1, y_2, \ldots, y_n)$ 的点 $(y_1, y_2, \ldots, y_n)$。

## Hessian 矩阵与二阶导数检验（The Hessian Matrix and the Second Derivative Test）

二元函数的 Hessian 矩阵在 14.7 节引入。我们现在把这个概念推广到 $n$ 元函数。

> [!definition] 📐 DEFINITIONS — Hessian Matrix and Principal Minor Determinants（Hessian 矩阵与主子式行列式）
> $f(x_1, x_2, \ldots, x_n)$ 的 **Hessian 矩阵（Hessian matrix）**是 $n\times n$ 矩阵（含 $n$ 行 $n$ 列）
> $$Hf = \begin{bmatrix} f_{x_1x_1} & f_{x_1x_2} & \cdots & f_{x_1x_n} \\ f_{x_2x_1} & f_{x_2x_2} & \cdots & f_{x_2x_n} \\ \vdots & \vdots & \ddots & \vdots \\ f_{x_nx_1} & f_{x_nx_2} & \cdots & f_{x_nx_n} \end{bmatrix}$$
> Hessian 矩阵的**主子式行列式（principal minor determinants）**为
> $$\Delta_1 = f_{x_1x_1},$$
> $$\Delta_2 = \begin{vmatrix} f_{x_1x_1} & f_{x_1x_2} \\ f_{x_2x_1} & f_{x_2x_2} \end{vmatrix},$$
> $$\Delta_3 = \begin{vmatrix} f_{x_1x_1} & f_{x_1x_2} & f_{x_1x_3} \\ f_{x_2x_1} & f_{x_2x_2} & f_{x_2x_3} \\ f_{x_3x_1} & f_{x_3x_2} & f_{x_3x_3} \end{vmatrix},$$
> $$\vdots$$
> $$\Delta_n = \lvert Hf\rvert = \begin{vmatrix} f_{x_1x_1} & f_{x_1x_2} & \cdots & f_{x_1x_n} \\ f_{x_2x_1} & f_{x_2x_2} & \cdots & f_{x_2x_n} \\ \vdots & \vdots & \ddots & \vdots \\ f_{x_nx_1} & f_{x_nx_2} & \cdots & f_{x_nx_n} \end{vmatrix}.$$

14.7 节的定理 11 给了我们判定函数 $f(x_1, x_2)$ 的临界点是局部极大、局部极小还是鞍点的工具。多于两个变量的函数的临界点的性质可以用 Hessian 矩阵的主子式行列式类似地判定。

> [!theorem] 📐 THEOREM 4 — Second Derivative Test for Local Extreme Values (General Version)（局部极值的二阶导数检验·一般形式）
> 假设 $f(x_1, x_2, \ldots, x_n)$ 及其一阶、二阶偏导数在以 $(a_1, a_2, \ldots, a_n)$ 为中心的开 $n$ 球内处处连续，且假设 $\nabla f(a_1, a_2, \ldots, a_n) = \mathbf{0}$。则
> **(i)** 若在点 $(a_1, a_2, \ldots, a_n)$ 处对 $i = 1, 2, \ldots, n$ 都有 $(-1)^i \Delta_i > 0$，则 $f$ 在 $(a_1, a_2, \ldots, a_n)$ 处有局部极大值；
> **(ii)** 若在 $(a_1, a_2, \ldots, a_n)$ 处对 $i = 1, 2, \ldots, n$ 都有 $\Delta_i > 0$，则 $f$ 在 $(a_1, a_2, \ldots, a_n)$ 处有局部极小值；
> **(iii)** 若在 $(a_1, a_2, \ldots, a_n)$ 处 $\Delta_n \neq 0$ 且条件 (i)、(ii) 都不满足，则 $f$ 在 $(a_1, a_2, \ldots, a_n)$ 处有鞍点；
> **(iv)** 若在 $(a_1, a_2, \ldots, a_n)$ 处 $\Delta_n = 0$，则检验失效。

对 $n = 2$，定理 4 归结为 14.7 节的定理 11（见习题 11）。主子式行列式 $\Delta_i$ 记录 $f$ 沿哪些方向有局部极大、沿哪些方向有局部极小。若 $f$ 沿 $n$ 个可能的坐标轴方向中的每一个都取局部极大（或局部极小），则 $f$ 在某个开 $n$ 球内取局部极大（或局部极小）。

把定理 4 应用于例 2 的函数 $f(x, y, z) = 10 - x^2 - y^2 - z^2$，我们得到 Hessian 矩阵 $Hf = \begin{bmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{bmatrix}$。它的主子式行列式为
$$\Delta_1 = -2,$$
$$\Delta_2 = \begin{vmatrix} -2 & 0 \\ 0 & -2 \end{vmatrix} = 4,$$
$$\Delta_3 = \begin{vmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{vmatrix} = -2 \begin{vmatrix} -2 & 0 \\ 0 & -2 \end{vmatrix} - 0 \begin{vmatrix} 0 & 0 \\ 0 & -2 \end{vmatrix} + 0 \begin{vmatrix} 0 & -2 \\ 0 & 0 \end{vmatrix} = -8.$$
在临界点 $(0, 0, 0)$ 处，有 $\Delta_1 < 0$、$\Delta_2 > 0$、$\Delta_3 < 0$，所以定理 4 证实了我们在例 2 中得出的结论：$f$ 在 $(0, 0, 0)$ 处有局部极大值。

> [!example] ✏️ EXAMPLE 3
> 求函数
> $$f(x, y, z) = 2x^3y + 3y^2 + 6yz + 6z^2 - 6xy$$
> 的局部极值与鞍点。
>
> **解答.** 函数 $f$ 可微，因此它的临界点是使 $\nabla f = \mathbf{0}$ 的点。令梯度的每个分量等于零，得到如下方程：
> $$f_x = 6x^2y - 6y = 6y(x^2 - 1) = 0,$$
> $$f_y = 2x^3 + 6y + 6z - 6x = 0,$$
> $$f_z = 6y + 12z = 0.$$
> 方程 $f_x = 0$ 可以以三种方式满足：(i) $y = 0$，(ii) $x = 1$，或 (iii) $x = -1$。我们逐一考虑这些可能性。
> **(i)** 若 $y = 0$，则方程 $f_z = 0$ 给出 $z = 0$，然后方程 $f_y = 0$ 导出
> $$2x^3 - 6x = 2x(x^2 - 3) = 0.$$
> 这个方程有三个解：$x = 0, \pm\sqrt{3}$，所以我们得到临界点 $(0, 0, 0)$、$(\sqrt{3}, 0, 0)$ 与 $(-\sqrt{3}, 0, 0)$。
> **(ii)** 若 $x = 1$，则方程 $f_y = 0$ 变为 $6y + 6z - 4 = 0$。与方程 $f_z = 6y + 12z = 0$ 一起，构成二元线性方程组，可解得 $y = \frac{4}{3}$、$z = -\frac{2}{3}$。所得临界点为 $\left(1, \frac{4}{3}, -\frac{2}{3}\right)$。
> **(iii)** 若 $x = -1$，则与情形 (ii) 类似地解余下的两个方程，得到 $y = -\frac{4}{3}$、$z = \frac{2}{3}$，最后的临界点是 $\left(-1, -\frac{4}{3}, \frac{2}{3}\right)$。
>
> $f$ 的 Hessian 矩阵为
> $$Hf = \begin{bmatrix} f_{xx} & f_{xy} & f_{xz} \\ f_{yx} & f_{yy} & f_{yz} \\ f_{zx} & f_{zy} & f_{zz} \end{bmatrix} = \begin{bmatrix} 12xy & 6x^2 - 6 & 0 \\ 6x^2 - 6 & 6 & 6 \\ 0 & 6 & 12 \end{bmatrix},$$
> 主子式行列式为
> $$\Delta_1 = 12xy,$$
> $$\Delta_2 = \begin{vmatrix} 12xy & 6x^2 - 6 \\ 6x^2 - 6 & 6 \end{vmatrix} = 72xy - (6x^2 - 6)^2,$$
> $$\Delta_3 = \begin{vmatrix} 12xy & 6x^2 - 6 & 0 \\ 6x^2 - 6 & 6 & 6 \\ 0 & 6 & 12 \end{vmatrix} = 12xy \begin{vmatrix} 6 & 6 \\ 6 & 12 \end{vmatrix} - (6x^2 - 6) \begin{vmatrix} 6x^2 - 6 & 6 \\ 0 & 12 \end{vmatrix} + 0$$
> $$= 12xy \cdot 36 - (6x^2 - 6)^2(12).$$
> 我们把这些行列式在各临界点处的值列在下表中。
>
> | 临界点 | $\Delta_1$ | $\Delta_2$ | $\Delta_3$ |
> | :--- | :--- | :--- | :--- |
> | $(0, 0, 0)$ | $0$ | $-36$ | $-432$ |
> | $(\sqrt{3}, 0, 0)$ | $0$ | $-144$ | $-1728$ |
> | $(-\sqrt{3}, 0, 0)$ | $0$ | $-144$ | $-1728$ |
> | $\left(1, \frac{4}{3}, -\frac{2}{3}\right)$ | $16$ | $96$ | $576$ |
> | $\left(-1, -\frac{4}{3}, \frac{2}{3}\right)$ | $16$ | $96$ | $576$ |
>
> 根据定理 4，
> **(i)** 若 $\Delta_1 < 0$、$\Delta_2 > 0$、$\Delta_3 < 0$，则 $f$ 在临界点处有局部极大值。这个模式在我们的任何临界点处都没有出现；因此，$f$ 没有局部极大值。
> **(ii)** 若 $\Delta_1 > 0$、$\Delta_2 > 0$、$\Delta_3 > 0$，则 $f$ 在临界点处有局部极小值。表中列出的主子式行列式的符号对最后两个临界点符合这个模式，所以 $f$ 在 $\left(1, \frac{4}{3}, -\frac{2}{3}\right)$ 与 $\left(-1, -\frac{4}{3}, \frac{2}{3}\right)$ 处有局部极小值。
> **(iii)** 若 $\Delta_3 \neq 0$ 但条件 (i)、(ii) 都不满足，则 $f$ 在临界点处有鞍点。根据我们的表，前三个临界点都是这种情况。我们得出结论：$f$ 在 $(0, 0, 0)$、$(\sqrt{3}, 0, 0)$ 与 $(-\sqrt{3}, 0, 0)$ 处有鞍点。
