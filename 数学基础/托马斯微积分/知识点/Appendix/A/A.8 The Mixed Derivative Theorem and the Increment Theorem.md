---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Appendix A Real Numbers and the Real Line
section: A.8 The Mixed Derivative Theorem and the Increment Theorem（混合偏导定理与增量定理）
tags: [微积分, 偏导数, 混合偏导数, 增量定理, 中值定理, 全微分, 托马斯微积分]
prerequisites:
  - "[[14.03 Partial Derivatives]]"
  - "[[4.2 The Mean Value Theorem]]"
aliases: [混合偏导定理与增量定理, The Mixed Derivative Theorem and the Increment Theorem, A.8 混合偏导定理与增量定理]
---

# A.8 The Mixed Derivative Theorem and the Increment Theorem（混合偏导定理与增量定理）

> [!info] 📘 本节引言
> 本节推导混合偏导定理（14.3 节定理 2）与二元函数的增量定理（14.3 节定理 3）。欧拉于 1734 年在他关于流体动力学的系列论文中首次发表混合偏导定理。

## 混合偏导定理（The Mixed Derivative Theorem）

> [!theorem] 📐 THEOREM 2 — The Mixed Derivative Theorem（混合偏导定理）
> 若 $f(x,y)$ 及其偏导数 $f_x,\,f_y,\,f_{xy}$ 与 $f_{yx}$ 在包含点 $(a,b)$ 的开区域内处处有定义，且在 $(a,b)$ 处均连续，则
> $$f_{xy}(a,b) = f_{yx}(a,b).$$
>
> **Proof.** $f_{xy}(a,b)$ 与 $f_{yx}(a,b)$ 的相等可以通过四次应用中值定理（4.2 节定理 4）来建立。由假设，点 $(a,b)$ 位于 xy 平面上一个矩形 $R$ 的内部，在 $R$ 上 $f,\,f_x,\,f_y,\,f_{xy}$ 与 $f_{yx}$ 均有定义。我们取数 $h$ 与 $k$，使得点 $(a+h, b+k)$ 也在 $R$ 内，并考虑差
> $$\Delta = F(a+h) - F(a), \tag{1}$$
> 其中
> $$F(x) = f(x, b+k) - f(x, b). \tag{2}$$
> 对 $F$ 应用中值定理（$F$ 可微因而是连续的）。则方程 (1) 变为
> $$\Delta = hF'(c_1), \tag{3}$$
> 其中 $c_1$ 介于 $a$ 与 $a+h$ 之间。由方程 (2)，
> $$F'(x) = f_x(x, b+k) - f_x(x, b),$$
> 所以方程 (3) 变为
> $$\Delta = h\bigl[f_x(c_1, b+k) - f_x(c_1, b)\bigr]. \tag{4}$$
> 现在对函数 $g(y) = f_x(c_1, y)$ 应用中值定理，有
> $$g(b+k) - g(b) = kg'(d_1),$$
> 即
> $$f_x(c_1, b+k) - f_x(c_1, b) = k\,f_{xy}(c_1, d_1)$$
> 对某个介于 $b$ 与 $b+k$ 之间的 $d_1$。把此式代入方程 (4)，得
> $$\Delta = hk\,f_{xy}(c_1, d_1) \tag{5}$$
> 对矩形 $R'$（顶点为 $(a,b)$、$(a+h,b)$、$(a+h,b+k)$ 与 $(a,b+k)$）中的某个点 $(c_1,d_1)$（Figure A.27）。
>
> 把方程 (2) 代入方程 (1)，我们也可以写
> $$\Delta = f(a+h,b+k) - f(a+h,b) - f(a,b+k) + f(a,b) = \varphi(b+k) - \varphi(b), \tag{6}$$
> 其中
> $$\varphi(y) = f(a+h, y) - f(a, y). \tag{7}$$
> 对方程 (6) 应用中值定理，得
> $$\Delta = k\varphi'(d_2) \tag{8}$$
> 对某个介于 $b$ 与 $b+k$ 之间的 $d_2$。由方程 (7)，
> $$\varphi'(y) = f_y(a+h, y) - f_y(a, y). \tag{9}$$
> 把方程 (9) 代入方程 (8)，得
> $$\Delta = k\bigl[f_y(a+h, d_2) - f_y(a, d_2)\bigr].$$
> 最后，对括号中的表达式应用中值定理，得
> $$\Delta = kh\,f_{yx}(c_2, d_2) \tag{10}$$
> 对某个介于 $a$ 与 $a+h$ 之间的 $c_2$。
>
> 合并方程 (5) 与 (10) 表明
> $$f_{xy}(c_1, d_1) = f_{yx}(c_2, d_2), \tag{11}$$
> 其中 $(c_1,d_1)$ 与 $(c_2,d_2)$ 都在矩形 $R'$ 内（Figure A.27）。方程 (11) 还不是我们想要的结果，因为它只说明 $f_{xy}$ 在 $(c_1,d_1)$ 的值等于 $f_{yx}$ 在 $(c_2,d_2)$ 的值。然而，讨论中的数 $h$ 与 $k$ 可以随意取小。$f_{xy}$ 与 $f_{yx}$ 都在 $(a,b)$ 连续的假设意味着
> $$f_{xy}(c_1,d_1) = f_{xy}(a,b) + \varepsilon_1, \qquad f_{yx}(c_2,d_2) = f_{yx}(a,b) + \varepsilon_2,$$
> 其中 $\varepsilon_1,\varepsilon_2 \to 0$ 当 $h,k \to 0$。于是，若令 $h,k \to 0$，我们便得到
> $$f_{xy}(a,b) = f_{yx}(a,b).$$
>
> ![[Pasted image 20260823214056.png|300]]

$f_{xy}(a,b)$ 与 $f_{yx}(a,b)$ 的相等可以在比我们所假设的更弱的假设下证明。例如，只要 $f_x$ 与 $f_y$ 在 $R$ 内存在、且 $f_{xy}$ 在 $(a,b)$ 连续就够了。则 $f_{yx}$ 将在 $(a,b)$ 存在，并等于该点的 $f_{xy}$。

## 增量定理（The Increment Theorem for Functions of Two Variables）

> [!theorem] 📐 THEOREM 3 — The Increment Theorem for Functions of Two Variables（二元函数的增量定理）
> 假设 $f(x,y)$ 的一阶偏导数在包含点 $(x_0,y_0)$ 的开区域 $R$ 内处处有定义，且 $f_x$ 与 $f_y$ 在 $(x_0,y_0)$ 连续。则从 $(x_0,y_0)$ 移到 $R$ 中另一点 $(x_0+\Delta x, y_0+\Delta y)$ 所引起的 $f$ 值的变化
> $$\Delta z = f(x_0+\Delta x, y_0+\Delta y) - f(x_0, y_0)$$
> 满足形如
> $$\Delta z = f_x(x_0,y_0)\Delta x + f_y(x_0,y_0)\Delta y + \varepsilon_1\Delta x + \varepsilon_2\Delta y$$
> 的方程，其中 $\varepsilon_1,\varepsilon_2 \to 0$ 当 $\Delta x,\Delta y \to 0$。
>
> **Proof.** 我们在以 $A(x_0,y_0)$ 为中心、位于 $R$ 内的矩形 $T$ 中工作，并假设 $\Delta x$ 与 $\Delta y$ 已经小到连接 $A$ 与 $B(x_0+\Delta x, y_0)$ 的线段、以及连接 $B$ 与 $C(x_0+\Delta x, y_0+\Delta y)$ 的线段都在 $T$ 的内部（Figure A.28）。
>
> 我们可以把 $\Delta z$ 看作两个增量之和 $\Delta z = \Delta z_1 + \Delta z_2$，其中
> $$\Delta z_1 = f(x_0+\Delta x, y_0) - f(x_0, y_0)$$
> 是从 $A$ 到 $B$ 的 $f$ 值变化，而
> $$\Delta z_2 = f(x_0+\Delta x, y_0+\Delta y) - f(x_0+\Delta x, y_0)$$
> 是从 $B$ 到 $C$ 的 $f$ 值变化（Figure A.29）。
>
> 在连接 $x_0$ 与 $x_0+\Delta x$ 的闭 $x$ 区间上，函数 $F(x) = f(x, y_0)$ 是 $x$ 的可微（因而是连续的）函数，导数为 $F'(x) = f_x(x, y_0)$。由中值定理（4.2 节定理 4），存在介于 $x_0$ 与 $x_0+\Delta x$ 之间的 $x$ 值 $c$，使
> $$\Delta z_1 = f_x(c, y_0)\Delta x. \tag{12}$$
> 类似地，$G(y) = f(x_0+\Delta x, y)$ 在连接 $y_0$ 与 $y_0+\Delta y$ 的闭 $y$ 区间上是 $y$ 的可微（因而是连续的）函数，导数为 $G'(y) = f_y(x_0+\Delta x, y)$。因此，存在介于 $y_0$ 与 $y_0+\Delta y$ 之间的 $y$ 值 $d$，使
> $$\Delta z_2 = f_y(x_0+\Delta x, d)\Delta y. \tag{13}$$
>
> 现在，当 $\Delta x$ 与 $\Delta y$ 都趋近 $0$ 时，我们知道 $c \to x_0$ 且 $d \to y_0$。因此，由于 $f_x$ 与 $f_y$ 在 $(x_0,y_0)$ 连续，量
> $$\varepsilon_1 = f_x(c, y_0) - f_x(x_0, y_0), \qquad \varepsilon_2 = f_y(x_0+\Delta x, d) - f_y(x_0, y_0) \tag{14}$$
> 当 $\Delta x$ 与 $\Delta y$ 都趋近 $0$ 时都趋近 $0$。
>
> 最后，
> $$
> \begin{aligned}
> \Delta z &= \Delta z_1 + \Delta z_2 = f_x(c,y_0)\Delta x + f_y(x_0+\Delta x, d)\Delta y \\
> &= \bigl[f_x(x_0,y_0) + \varepsilon_1\bigr]\Delta x + \bigl[f_y(x_0,y_0) + \varepsilon_2\bigr]\Delta y \\
> &= f_x(x_0,y_0)\Delta x + f_y(x_0,y_0)\Delta y + \varepsilon_1\Delta x + \varepsilon_2\Delta y.
> \end{aligned}
> $$
>
> ![[Pasted image 20260823214117.png|300]]
>
> ![[Pasted image 20260823214155.png]]

## 更多自变量的增量定理（The Increment Theorem for More Variables）

对任何有限个自变量的函数有类似的结果。假设 $w = f(x,y,z)$ 的一阶偏导数在包含点 $(x_0,y_0,z_0)$ 的开区域内处处有定义，且 $f_x,\,f_y$ 与 $f_z$ 在 $(x_0,y_0,z_0)$ 连续。则
$$\Delta w = f(x_0+\Delta x, y_0+\Delta y, z_0+\Delta z) - f(x_0, y_0, z_0) = f_x\Delta x + f_y\Delta y + f_z\Delta z + \varepsilon_1\Delta x + \varepsilon_2\Delta y + \varepsilon_3\Delta z, \tag{15}$$
其中 $\varepsilon_1,\varepsilon_2,\varepsilon_3 \to 0$ 当 $\Delta x,\Delta y,\Delta z \to 0$。

方程 (15) 中的偏导数 $f_x,\,f_y,\,f_z$ 在点 $(x_0,y_0,z_0)$ 处取值。

方程 (15) 可以通过把 $\Delta w$ 看作三个增量之和来证明，
$$\Delta w_1 = f(x_0+\Delta x, y_0, z_0) - f(x_0, y_0, z_0), \tag{16}$$
$$\Delta w_2 = f(x_0+\Delta x, y_0+\Delta y, z_0) - f(x_0+\Delta x, y_0, z_0), \tag{17}$$
$$\Delta w_3 = f(x_0+\Delta x, y_0+\Delta y, z_0+\Delta z) - f(x_0+\Delta x, y_0+\Delta y, z_0), \tag{18}$$
并分别对其中每一个应用中值定理。在这些部分增量 $\Delta w_1,\,\Delta w_2,\,\Delta w_3$ 的每一个中，两个坐标保持不变，只有一个坐标变化。例如在方程 (17) 中，只有 $y$ 变化，因为 $x$ 保持等于 $x_0+\Delta x$，$z$ 保持等于 $z_0$。由于 $f(x_0+\Delta x, y, z_0)$ 是 $y$ 的连续函数、导数为 $f_y$，它满足中值定理的条件，于是
$$\Delta w_2 = f_y(x_0+\Delta x, y_1, z_0)\Delta y$$
对某个介于 $y_0$ 与 $y_0+\Delta y$ 之间的 $y_1$。
