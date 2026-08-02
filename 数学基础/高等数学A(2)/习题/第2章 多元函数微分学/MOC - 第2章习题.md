---
domain: 数学基础
subject: 高等数学A(2)
type: exercise
chapter: 第2章 多元函数微分学
tags: [高等数学,习题,偏导数,全微分,梯度,拉格朗日乘数法]
prerequisites: ["高等数学A(1)"]
aliases: [第2章习题, 多元微分学习题]
---

# MOC - 第2章习题

> [!info] 习题集说明
> 本文件汇集第2章"多元函数微分学"30 道精选习题，覆盖填空、选择、计算、证明四种题型，对应 [[MOC - 第2章]] 八个小节的全部核心考点。答案与提示以 `<details>` 折叠呈现，计算题给出完整步骤。

## 一、填空题（8 题）

### T1
设 $z=\mathrm{e}^{xy}\sin(x+y)$，则 $z_x=$ ________。

<details>
<summary>答案</summary>

$z_x=y\mathrm{e}^{xy}\sin(x+y)+\mathrm{e}^{xy}\cos(x+y)=\mathrm{e}^{xy}[y\sin(x+y)+\cos(x+y)]$。
</details>

### T2
设 $z=f(x^2-y^2,\mathrm{e}^{xy})$，$f$ 有连续偏导，则 $\dfrac{\partial z}{\partial y}=$ ________。

<details>
<summary>答案</summary>

设 $u=x^2-y^2, v=\mathrm{e}^{xy}$，则 $\dfrac{\partial z}{\partial y}=f_1\cdot(-2y)+f_2\cdot x\mathrm{e}^{xy}$。
</details>

### T3
函数 $u=\ln(x^2+y^2+z^2)$ 在点 $M(1,1,1)$ 处的梯度 $\mathrm{grad}\,u=$ ________。

<details>
<summary>答案</summary>

$u_x=\dfrac{2x}{x^2+y^2+z^2}$，在 $M$ 处 $\mathrm{grad}\,u=\dfrac{2}{3}(1,1,1)=\left(\dfrac{2}{3},\dfrac{2}{3},\dfrac{2}{3}\right)$。
</details>

### T4
设 $z=x^3-3xy+y^3$，则其全部驻点为 ________。

<details>
<summary>答案</summary>

解 $\begin{cases}3x^2-3y=0\\ -3x+3y^2=0\end{cases}$，由 $y=x^2$ 代入第二式 $-3x+3x^4=0\Rightarrow x(x^3-1)=0$，故驻点为 $(0,0)$ 与 $(1,1)$。
</details>

### T5
设 $x^2+y^2+z^2-xyz=4$ 确定 $z=z(x,y)$，则 $\dfrac{\partial z}{\partial x}=$ ________。

<details>
<summary>答案</summary>

$F=x^2+y^2+z^2-xyz-4$，$F_x=2x-yz$，$F_z=2z-xy$，故 $\dfrac{\partial z}{\partial x}=-\dfrac{2x-yz}{2z-xy}=\dfrac{yz-2x}{2z-xy}$。
</details>

### T6
设 $f(x,y)=\arctan\dfrac{y}{x}$，则 $\mathrm{d}f=$ ________。

<details>
<summary>答案</summary>

$f_x=\dfrac{-y}{x^2+y^2}, f_y=\dfrac{x}{x^2+y^2}$，故 $\mathrm{d}f=\dfrac{-y\mathrm{d}x+x\mathrm{d}y}{x^2+y^2}$。
</details>

### T7
函数 $u=xy+2yz+3zx$ 在点 $(1,1,1)$ 处沿方向 $\vec{\ell}=(1,2,2)$ 的方向导数为 ________。

<details>
<summary>答案</summary>

$\mathrm{grad}\,u=(y+3z, x+2z, 2y+3x)\big|_{(1,1,1)}=(4,3,5)$，$\vec{e}_\ell=\dfrac{1}{3}(1,2,2)$。
$\dfrac{\partial u}{\partial \ell}=\dfrac{4\times 1+3\times 2+5\times 2}{3}=\dfrac{4+6+10}{3}=\dfrac{20}{3}$。
</details>

### T8
设 $z=x^2 y^3$，则 $\mathrm{d}z\big|_{(1,2)}=$ ________。

<details>
<summary>答案</summary>

$z_x=2xy^3\big|_{(1,2)}=16$，$z_y=3x^2 y^2\big|_{(1,2)}=12$，故 $\mathrm{d}z=16\mathrm{d}x+12\mathrm{d}y$。
</details>

## 二、选择题（6 题）

### T9
下列命题正确的是（  ）。

A. 若 $f(x,y)$ 在 $(x_0,y_0)$ 处偏导数存在，则 $f$ 在该点连续
B. 若 $f$ 在 $(x_0,y_0)$ 处可微，则 $f$ 在该点偏导数连续
C. 若 $f$ 在 $(x_0,y_0)$ 处偏导数连续，则 $f$ 在该点可微
D. 若 $f$ 在 $(x_0,y_0)$ 处连续，则 $f$ 在该点可微

<details>
<summary>答案</summary>

**C**。由 [[2.3 全微分]] 可微充分条件。A、D 反例见 [[2.1 多元函数、极限与连续]]；B 偏导连续是充分非必要条件。
</details>

### T10
设 $f(x,y)=\dfrac{xy}{x^2+y^2}$（$(x,y)\neq(0,0)$，$f(0,0)=0$），则（  ）。

A. $f$ 在 $(0,0)$ 处连续
B. $f$ 在 $(0,0)$ 处偏导数不存在
C. $f$ 在 $(0,0)$ 处偏导数存在但不连续
D. $f$ 在 $(0,0)$ 处可微

<details>
<summary>答案</summary>

**C**。沿 $y=kx$ 路径 $f\to\dfrac{k}{1+k^2}$ 依赖 $k$，故不连续（A 错）。$f_x(0,0)=\lim_{\Delta x}\dfrac{f(\Delta x,0)-0}{\Delta x}=0$，同理 $f_y(0,0)=0$，偏导存在（B 错）。但 $\dfrac{\Delta z-(f_x\Delta x+f_y\Delta y)}{\rho}=\dfrac{xy}{x^2+y^2}\cdot\dfrac{1}{\rho}$，沿 $y=x$ 趋于 $\dfrac{1}{2}\neq 0$，不可微（D 错）。
</details>

### T11
设 $z=f(u,v)$，$u=\varphi(x), v=\psi(x)$ 均可微，则 $\dfrac{\mathrm{d}z}{\mathrm{d}x}=$（  ）。

A. $f_u+f_v$
B. $f_u\varphi'+f_v\psi'$
C. $f_u\mathrm{d}u+f_v\mathrm{d}v$
D. $f_x+f_u\varphi'+f_v\psi'$

<details>
<summary>答案</summary>

**B**。由 [[2.4 复合函数求导法则]] 情形 2（全导数公式）。
</details>

### T12
设 $F(x,y,z)=0$ 确定隐函数 $z=z(x,y)$，则 $\dfrac{\partial z}{\partial x}=$（  ）。

A. $-\dfrac{F_x}{F_y}$
B. $\dfrac{F_x}{F_z}$
C. $-\dfrac{F_x}{F_z}$
D. $\dfrac{F_y}{F_z}$

<details>
<summary>答案</summary>

**C**。由 [[2.5 隐函数求导公式]] 三元情形公式。
</details>

### T13
$f(x,y)=x^2+y^2$ 在 $(1,1)$ 处沿方向 $\vec{\ell}=(\cos\theta,\sin\theta)$ 的方向导数最大时 $\theta=$（  ）。

A. $0$
B. $\dfrac{\pi}{4}$
C. $\dfrac{\pi}{2}$
D. $\pi$

<details>
<summary>答案</summary>

**B**。$\mathrm{grad}\,f=(2,2)$，方向 $\dfrac{1}{\sqrt{2}}(1,1)$，即 $\theta=\dfrac{\pi}{4}$。
</details>

### T14
设 $f(x,y)$ 在 $(0,0)$ 处取得极大值，则（  ）。

A. $f_x(0,0)=f_y(0,0)=0$
B. $f_{xx}(0,0)>0$
C. $f_{xy}(0,0)=0$
D. $AC-B^2<0$

<details>
<summary>答案</summary>

**A**。极值必要条件（[[2.7 多元函数极值与最值]]）。
</details>

## 三、计算题（10 题）

### T15
设 $z=\mathrm{e}^{x^2 y}$，求 $\dfrac{\partial z}{\partial x}, \dfrac{\partial z}{\partial y}, \dfrac{\partial^2 z}{\partial x\partial y}$。

<details>
<summary>解答</summary>

$$\dfrac{\partial z}{\partial x}=2xy\,\mathrm{e}^{x^2 y},\quad \dfrac{\partial z}{\partial y}=x^2\,\mathrm{e}^{x^2 y}$$

$$\dfrac{\partial^2 z}{\partial x\partial y}=\dfrac{\partial}{\partial y}(2xy\,\mathrm{e}^{x^2 y})=2x\,\mathrm{e}^{x^2 y}+2xy\cdot x^2\,\mathrm{e}^{x^2 y}=2x(1+x^2 y)\,\mathrm{e}^{x^2 y}$$
</details>

### T16
设 $z=f(x+y, x-y)$，$f$ 有二阶连续偏导，求 $\dfrac{\partial^2 z}{\partial x^2}-\dfrac{\partial^2 z}{\partial y^2}$。

<details>
<summary>解答</summary>

设 $u=x+y, v=x-y$。
$$z_x=f_1+f_2,\quad z_y=f_1-f_2$$
$$z_{xx}=f_{11}+f_{12}+f_{21}+f_{22}=f_{11}+2f_{12}+f_{22}$$
$$z_{yy}=f_{11}-f_{12}-f_{21}+f_{22}=f_{11}-2f_{12}+f_{22}$$
故 $z_{xx}-z_{yy}=4f_{12}$。
</details>

### T17
设 $z=z(x,y)$ 由方程 $\mathrm{e}^z-xyz=0$ 确定，求 $\dfrac{\partial z}{\partial x}, \dfrac{\partial z}{\partial y}, \dfrac{\partial^2 z}{\partial x^2}$。

<details>
<summary>解答</summary>

$F=\mathrm{e}^z-xyz$，$F_x=-yz$，$F_y=-xz$，$F_z=\mathrm{e}^z-xy$。

$$\dfrac{\partial z}{\partial x}=-\dfrac{F_x}{F_z}=\dfrac{yz}{\mathrm{e}^z-xy}=\dfrac{z}{xz-xy}=\dfrac{z}{x(z-1)}$$

（用 $\mathrm{e}^z=xyz$ 代换）同理 $\dfrac{\partial z}{\partial y}=\dfrac{xz}{\mathrm{e}^z-xy}=\dfrac{z}{y(z-1)}$。

求 $z_{xx}$：对 $z_x=\dfrac{z}{x(z-1)}$ 关于 $x$ 再求偏导（视 $z$ 为 $x$ 的函数）：
$$z_{xx}=\dfrac{x(z-1)z_x-z[1+(z-1)+xz_x]}{x^2(z-1)^2}$$

化简较繁，通常用隐函数求导法对原方程二次求导（略）。
</details>

### T18
求函数 $u=\ln(x+y+z)$ 在点 $(1,2,3)$ 处沿方向 $\vec{\ell}=(1,1,1)$ 的方向导数。

<details>
<summary>解答</summary>

$\vec{e}_\ell=\dfrac{1}{\sqrt{3}}(1,1,1)$。$u_x=u_y=u_z=\dfrac{1}{x+y+z}$，在 $(1,2,3)$ 处为 $\dfrac{1}{6}$。

$$\dfrac{\partial u}{\partial \ell}=\dfrac{1}{6}\cdot\dfrac{1+1+1}{\sqrt{3}}=\dfrac{3}{6\sqrt{3}}=\dfrac{1}{2\sqrt{3}}=\dfrac{\sqrt{3}}{6}$$
</details>

### T19
求 $f(x,y)=x^3+y^3-3x^2-3y^2$ 的极值。

<details>
<summary>解答</summary>

解 $\begin{cases}f_x=3x^2-6x=0\\ f_y=3y^2-6y=0\end{cases}\Rightarrow x=0,2; y=0,2$。
驻点：$(0,0), (0,2), (2,0), (2,2)$。
$A=f_{xx}=6x-6, B=f_{xy}=0, C=f_{yy}=6y-6$，$\Delta=AC$。

| 驻点 | $A$ | $C$ | $\Delta$ | 结论 |
| ---- | --- | --- | -------- | ---- |
| $(0,0)$ | $-6$ | $-6$ | $36>0, A<0$ | 极大值 $0$ |
| $(0,2)$ | $-6$ | $6$ | $-36<0$ | 鞍点 |
| $(2,0)$ | $6$ | $-6$ | $-36<0$ | 鞍点 |
| $(2,2)$ | $6$ | $6$ | $36>0, A>0$ | 极小值 $-8$ |
</details>

### T20
在平面 $3x+2y+z=1$ 上求一点，使其与原点距离最近。

<details>
<summary>解答</summary>

目标 $f=x^2+y^2+z^2$，约束 $3x+2y+z-1=0$。
构造 $L=x^2+y^2+z^2+\lambda(3x+2y+z-1)$。
$$\begin{cases}2x+3\lambda=0\\ 2y+2\lambda=0\\ 2z+\lambda=0\\ 3x+2y+z=1\end{cases}$$
由前三式 $x=-\dfrac{3\lambda}{2}, y=-\lambda, z=-\dfrac{\lambda}{2}$。代入第四式：
$$-\dfrac{9\lambda}{2}-2\lambda-\dfrac{\lambda}{2}=1\Rightarrow -7\lambda=1\Rightarrow \lambda=-\dfrac{1}{7}$$
故 $x=\dfrac{3}{14}, y=\dfrac{1}{7}, z=\dfrac{1}{14}$，最近点为 $\left(\dfrac{3}{14}, \dfrac{1}{7}, \dfrac{1}{14}\right)$。
距离 $\dfrac{1}{\sqrt{14}}$。
</details>

### T21
求函数 $z=x^2+y^2$ 在条件 $x+y=1$ 下的极小值。

<details>
<summary>解答</summary>

构造 $L=x^2+y^2+\lambda(x+y-1)$。
$$\begin{cases}2x+\lambda=0\\ 2y+\lambda=0\\ x+y=1\end{cases}$$
由前两式 $x=y$，代入第三式 $x=y=\dfrac{1}{2}$。$z=\dfrac{1}{4}+\dfrac{1}{4}=\dfrac{1}{2}$。
</details>

### T22
设 $z=f(u,v)$，$u=x-y, v=\mathrm{e}^{xy}$，$f$ 有二阶连续偏导，求 $\dfrac{\partial z}{\partial x}, \dfrac{\partial^2 z}{\partial x\partial y}$。

<details>
<summary>解答</summary>

$$z_x=f_1\cdot 1+f_2\cdot y\mathrm{e}^{xy}=f_1+y\mathrm{e}^{xy}f_2$$

$$z_{xy}=\dfrac{\partial}{\partial y}(f_1+y\mathrm{e}^{xy}f_2)$$
$$=f_{11}\cdot(-1)+f_{12}\cdot x\mathrm{e}^{xy}+\mathrm{e}^{xy}f_2+xy\mathrm{e}^{xy}f_2+y\mathrm{e}^{xy}[f_{21}\cdot(-1)+f_{22}\cdot x\mathrm{e}^{xy}]$$
$$=-f_{11}+(x-y)\mathrm{e}^{xy}f_{12}+xy\mathrm{e}^{2xy}f_{22}+(1+xy)\mathrm{e}^{xy}f_2$$
（用了 $f_{12}=f_{21}$）
</details>

### T23
求 $f(x,y)=xy$ 在圆 $x^2+y^2\leq 1$ 上的最值。

<details>
<summary>解答</summary>

内部驻点：$f_x=y=0, f_y=x=0\Rightarrow (0,0)$，$f(0,0)=0$。
边界 $x^2+y^2=1$ 上令 $x=\cos t, y=\sin t$，$f=\cos t\sin t=\dfrac{1}{2}\sin 2t$，最大 $\dfrac{1}{2}$，最小 $-\dfrac{1}{2}$。
比较：最大值 $\dfrac{1}{2}$（$t=\dfrac{\pi}{4}$），最小值 $-\dfrac{1}{2}$（$t=\dfrac{3\pi}{4}$）。
</details>

### T24
证明：函数 $u=\dfrac{1}{r}$，$r=\sqrt{x^2+y^2+z^2}$ 满足 Laplace 方程 $\Delta u=0$（$r\neq 0$）。

<details>
<summary>解答</summary>

参见 [[2.2 偏导数]] 例 3。

$u_x=-\dfrac{x}{r^3}$，$u_{xx}=-\dfrac{1}{r^3}+\dfrac{3x^2}{r^5}=\dfrac{3x^2-r^2}{r^5}$。同理 $u_{yy},u_{zz}$。求和
$$\Delta u=\dfrac{3(x^2+y^2+z^2)-3r^2}{r^5}=0$$
</details>

## 四、证明题（6 题）

### T25
证明 $\lim_{(x,y)\to(0,0)}\dfrac{x^2 y^2}{x^2+y^2}=0$。

<details>
<summary>证明</summary>

由 $x^2\leq x^2+y^2, y^2\leq x^2+y^2$，故 $x^2 y^2\leq (x^2+y^2)^2$，于是
$$\left|\dfrac{x^2 y^2}{x^2+y^2}\right|\leq x^2+y^2\to 0$$
由夹逼准则极限为 $0$。
</details>

### T26
证明 $\lim_{(x,y)\to(0,0)}\dfrac{x^2-y^2}{x^2+y^2}$ 不存在。

<details>
<summary>证明</summary>

沿 $y=0$：$\lim_{x\to 0}\dfrac{x^2}{x^2}=1$。
沿 $x=0$：$\lim_{y\to 0}\dfrac{-y^2}{y^2}=-1$。
两路径极限不同，故原极限不存在。
</details>

### T27
设 $f$ 具有二阶连续偏导数，证明 $z=f(x+y)+g(x-y)$ 满足方程 $\dfrac{\partial^2 z}{\partial x^2}=\dfrac{\partial^2 z}{\partial y^2}$。

<details>
<summary>证明</summary>

设 $u=x+y, v=x-y$，$z=f(u)+g(v)$。
$z_x=f'+g', z_{xx}=f''+g''$；
$z_y=f'-g', z_{yy}=f''+g''$。
故 $z_{xx}=z_{yy}$。
</details>

### T28
设 $z=\varphi(x^2+y^2)$，证明 $y\dfrac{\partial z}{\partial x}-x\dfrac{\partial z}{\partial y}=0$。

<details>
<summary>证明</summary>

设 $u=x^2+y^2$，$z_x=2x\varphi'(u), z_y=2y\varphi'(u)$。
$$y z_x-x z_y=2xy\varphi'(u)-2xy\varphi'(u)=0$$
</details>

### T29
设 $F(x,y,z)$ 满足 $F_x, F_y, F_z$ 一次齐次（即 $F_x, F_y, F_z$ 各自为齐一次），且 $F$ 有连续偏导。证明由 $F(x,y,z)=0$ 确定的隐函数 $z=z(x,y)$ 满足 $x\dfrac{\partial z}{\partial x}+y\dfrac{\partial z}{\partial y}=z$。

<details>
<summary>证明</summary>

由 $F(x,y,z)=0$ 对 $t$ 求导（视 $x,y,z$ 同乘 $t$）并由齐次性（Euler 定理）：$F_x\cdot x+F_y\cdot y+F_z\cdot z=kF=0$（$k=1$ 次，且 $F=0$），即
$$xF_x+yF_y+zF_z=0$$
又 $z_x=-\dfrac{F_x}{F_z}, z_y=-\dfrac{F_y}{F_z}$，故
$$x z_x+y z_y=-\dfrac{xF_x+yF_y}{F_z}=\dfrac{zF_z}{F_z}=z$$
</details>

### T30
设函数 $f(x,y)$ 在凸区域 $D$ 上偏导数恒为零，证明 $f$ 在 $D$ 上为常数。

<details>
<summary>证明</summary>

任取 $P_1, P_2\in D$，由 $D$ 凸性，线段 $\overline{P_1P_2}\subset D$。沿该线段参数化 $P(t)=P_1+t(P_2-P_1), t\in[0,1]$，则 $g(t)=f(P(t))$。
$$g'(t)=f_x\cdot (x_2-x_1)+f_y\cdot (y_2-y_1)=0$$
故 $g$ 为常数，$f(P_1)=f(P_2)$，由 $P_1,P_2$ 任意性，$f$ 在 $D$ 上为常数。
</details>

## 五、考点统计

| 考点 | 题号 | 难度 | 备注 |
| ---- | ---- | ---- | ---- |
| 偏导数与高阶偏导计算 | T1, T2, T15, T22, T28 | 易-中 | 链式法则重点 |
| 全微分 | T6, T8, T24 | 易 | 公式记忆 |
| 复合函数求导 | T2, T11, T16, T22, T27 | 中 | 树状图法 |
| 隐函数求导 | T5, T12, T17, T29 | 中-难 | 雅可比方法 |
| 方向导数与梯度 | T3, T7, T13, T18 | 易-中 | 投影公式 |
| 极值与无条件极值 | T4, T14, T19, T23 | 中 | 判别式法 |
| 拉格朗日乘数法 | T20, T21, T23 | 中-难 | 多约束情形 |
| 极限存在性 | T9, T10, T25, T26 | 中 | 路径法 |
| 可微性判定 | T9, T10 | 中 | 定义法 |
| 函数恒等式证明 | T27, T28, T29, T30 | 难 | 齐次函数、Euler 定理 |

## 章节导航

- 上一级：[[MOC - 第2章]]
- 上一章习题：[[MOC - 第1章习题]]（占位）
- 下一章习题：[[MOC - 第3章习题]]（占位）
- 返回：[[MOC - 高等数学A(2)]]

## 相关标签

#高等数学 #习题 #偏导数 #全微分 #梯度 #拉格朗日乘数法 #多元微积分
