---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Appendix A Real Numbers and the Real Line
section: A.7 The Distributive Law for Vector Cross Products（向量叉积分配律）
tags: [微积分, 向量, 叉积, 分配律, 正交投影, 旋转, 托马斯微积分]
prerequisites:
  - "[[12.4 The Cross Product]]"
aliases: [向量叉积分配律, The Distributive Law for Vector Cross Products, A.7 向量叉积分配律]
---

# A.7 The Distributive Law for Vector Cross Products（向量叉积分配律）

> [!info] 📘 本节引言
> 本节证明向量叉积的分配律，即 12.4 节的性质 2。

在本附录中我们证明分配律
$$\mathbf{u} \times (\mathbf{v} + \mathbf{w}) = \mathbf{u} \times \mathbf{v} + \mathbf{u} \times \mathbf{w},$$
即 12.4 节的性质 2。

**Proof（证明）** 为推导分配律，我们以一种新的方式构造 $\mathbf{u}\times\mathbf{v}$。从公共点 $O$ 画出 $\mathbf{u}$ 与 $\mathbf{v}$，并在 $O$ 处构造垂直于 $\mathbf{u}$ 的平面 $M$（Figure A.25）。然后把 $\mathbf{v}$ 正交投影到 $M$ 上，得到长度为 $\lvert\mathbf{v}\rvert\sin\theta$ 的向量 $\mathbf{v}_1$。把 $\mathbf{v}_1$ 绕 $\mathbf{u}$ 按正向旋转 $90^\circ$ 得到向量 $\mathbf{v}_2$。最后把 $\mathbf{v}_2$ 乘以 $\mathbf{u}$ 的长度。所得向量 $\lvert\mathbf{u}\rvert\,\mathbf{v}_2$ 等于 $\mathbf{u}\times\mathbf{v}$，因为 $\mathbf{v}_2$ 由构造具有与 $\mathbf{u}\times\mathbf{v}$ 相同的方向（Figure A.25），且
$$\lvert\mathbf{u}\rvert\,\lvert\mathbf{v}_2\rvert = \lvert\mathbf{u}\rvert\,\lvert\mathbf{v}_1\rvert = \lvert\mathbf{u}\rvert\,\lvert\mathbf{v}\rvert\sin\theta = \lvert\mathbf{u}\times\mathbf{v}\rvert.$$

![[Pasted image 20260823213503.png]]

现在这三个操作，即
1. 向 $M$ 的投影（projection onto $M$）
2. 绕 $\mathbf{u}$ 旋转 $90^\circ$（rotation about $\mathbf{u}$ through $90^\circ$）
3. 乘以标量 $\lvert\mathbf{u}\rvert$（multiplication by the scalar $\lvert\mathbf{u}\rvert$）
当应用于平面不平行于 $\mathbf{u}$ 的三角形时，都会产生另一个三角形。若从边为 $\mathbf{v}$、$\mathbf{w}$ 与 $\mathbf{s} = \mathbf{v} + \mathbf{w}$ 的三角形开始（Figure A.26），并依次应用这三步，我们依次得到：

1. 边为 $\mathbf{v}_1$、$\mathbf{w}_1$ 与 $\mathbf{s}_1$ 的三角形，满足向量方程 $\mathbf{v}_1 + \mathbf{w}_1 = \mathbf{s}_1$；
2. 边为 $\mathbf{v}_2$、$\mathbf{w}_2$ 与 $\mathbf{s}_2$ 的三角形，满足向量方程 $\mathbf{v}_2 + \mathbf{w}_2 = \mathbf{s}_2$；
3. 边为 $\lvert\mathbf{u}\rvert\mathbf{v}_2$、$\lvert\mathbf{u}\rvert\mathbf{w}_2$ 与 $\lvert\mathbf{u}\rvert\mathbf{s}_2$ 的三角形，满足向量方程 $\lvert\mathbf{u}\rvert\mathbf{v}_2 + \lvert\mathbf{u}\rvert\mathbf{w}_2 = \lvert\mathbf{u}\rvert\mathbf{s}_2$。

![[Pasted image 20260823213511.png]]

把上面讨论中的 $\lvert\mathbf{u}\rvert\mathbf{v}_2 = \mathbf{u}\times\mathbf{v}$、$\lvert\mathbf{u}\rvert\mathbf{w}_2 = \mathbf{u}\times\mathbf{w}$ 与 $\lvert\mathbf{u}\rvert\mathbf{s}_2 = \mathbf{u}\times(\mathbf{v}+\mathbf{w})$ 代入最后一个方程，得到
$$\mathbf{u}\times\mathbf{v} + \mathbf{u}\times\mathbf{w} = \mathbf{u}\times(\mathbf{v}+\mathbf{w}),$$
即我们要建立的分配律。
