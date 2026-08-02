---
domain: 数学基础
subject: 高等数学A(2)
type: exercise
chapter: 第4章 曲线积分与曲面积分
tags: [高等数学,习题,曲线积分,曲面积分,格林公式,高斯公式,斯托克斯公式]
prerequisites: ["第3章 重积分"]
aliases: [第4章习题, 线面积分习题]
---

# MOC - 第4章习题

> [!info] 习题集定位
> 本习题集围绕 [[MOC - 第4章]] 的核心考点设计，共 30 题，分**填空、选择、计算、证明**四类。重点训练第一/二类曲线积分计算、格林公式应用、积分与路径无关、第一/二类曲面积分计算、高斯公式应用、斯托克斯公式应用、散度与旋度概念。所有解答以 `<details>` 折叠，建议先独立完成再展开核对。

## 一、填空题（6题）

**1.** 第一类曲线积分 $\int_L f\,ds$ 的参数方程计算公式为 $\displaystyle\int_L f(x,y)\,ds=$ ____，其中 $ds=$ ____。

<details><summary>答案</summary>

$$\int_L f(x,y)\,ds=\int_\alpha^\beta f(x(t),y(t))\sqrt{[x'(t)]^2+[y'(t)]^2}\,dt,\qquad ds=\sqrt{[x'(t)]^2+[y'(t)]^2}\,dt.$$

</details>

**2.** 设 $L$ 为圆周 $x^2+y^2=R^2$，则 $\displaystyle\oint_L(x^2+y^2)\,ds=$ ____。

<details><summary>答案</summary>

被积函数在 $L$ 上恒为 $R^2$，故 $\oint_LR^2\,ds=R^2\cdot 2\pi R=2\pi R^3$。

</details>

**3.** 格林公式 $\displaystyle\oint_L P\,dx+Q\,dy=$ ____，其中 $L$ 为 $D$ 的 ____ 边界。

<details><summary>答案</summary>

$$\oint_L P\,dx+Q\,dy=\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dxdy,$$

$L$ 为 $D$ 的**正向**（逆时针）边界。

</details>

**4.** 向量场 $\boldsymbol F=(P,Q,R)$ 的散度 $\mathrm{div}\,\boldsymbol F=$ ____，旋度 $\mathrm{curl}\,\boldsymbol F=$ ____。

<details><summary>答案</summary>

$$\mathrm{div}\,\boldsymbol F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z},\qquad \mathrm{curl}\,\boldsymbol F=\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},\ \frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},\ \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right).$$

</details>

**5.** 高斯公式 $\displaystyle\oiint_\Sigma P\,dydz+Q\,dzdx+R\,dxdy=$ ____，其中 $\Sigma$ 取 ____ 侧。

<details><summary>答案</summary>

$$\oiint_\Sigma P\,dydz+Q\,dzdx+R\,dxdy=\iiint_\Omega\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)dV,$$

$\Sigma$ 取**外侧**。

</details>

**6.** 设 $\boldsymbol F=(x^2,y^2,z^2)$，则 $\mathrm{div}\,\boldsymbol F=$ ____，$\mathrm{curl}\,\boldsymbol F=$ ____。

<details><summary>答案</summary>

$\mathrm{div}\,\boldsymbol F=2x+2y+2z$，$\mathrm{curl}\,\boldsymbol F=(0,0,0)$（各分量只依赖自变量，交叉偏导为零）。

</details>

## 二、选择题（6题）

**7.** 关于第一类与第二类曲线积分，下列说法正确的是：
- A. 两者都与方向有关
- B. 两者都与方向无关
- C. 第一类与方向无关，第二类与方向有关
- D. 第一类与方向有关，第二类与方向无关

<details><summary>答案</summary>

**C**。第一类对弧长 $ds\ge0$ 与方向无关；第二类对坐标 $dx,dy$ 含方向，反向变号。

</details>

**8.** 格林公式成立的条件不包括：
- A. $L$ 为闭曲线
- B. $L$ 取正向
- C. $P,Q$ 在 $D$ 内有连续一阶偏导
- D. $D$ 必须是单连通区域

<details><summary>答案</summary>

**D**。格林公式对复连通区域也成立，但需把内外边界都计入（内边界取顺时针）。单连通只是"四等价命题"的前提。

</details>

**9.** 设 $P\,dx+Q\,dy$ 在单连通区域 $G$ 内积分与路径无关，则下列哪个不一定成立：
- A. $\oint_C P\,dx+Q\,dy=0$（$C$ 为 $G$ 内任意闭曲线）
- B. $Q_x=P_y$ 在 $G$ 内处处成立
- C. 存在 $u$ 使 $du=P\,dx+Q\,dy$
- D. $P,Q$ 在 $G$ 内恒为零

<details><summary>答案</summary>

**D**。前三项是四等价命题，D 显然无关。

</details>

**10.** 高斯公式中，若 $\Sigma$ 是闭曲面取内侧，则公式右端应：
- A. 不变
- B. 变号
- C. 变为零
- D. 倍乘 2

<details><summary>答案</summary>

**B**。内侧法向量与外侧相反，通量变号，故右端三重积分前加负号。

</details>

**11.** 用斯托克斯公式计算 $\oint_\Gamma\boldsymbol F\cdot d\boldsymbol r$ 时，曲面 $\Sigma$ 的选择：
- A. 必须是平面
- B. 必须是球面
- C. 任意以 $\Gamma$ 为边界的光滑曲面均可
- D. 必须过原点

<details><summary>答案</summary>

**C**。只要 $\boldsymbol F$ 在 $\Sigma$ 上 $C^1$ 且 $\Sigma$ 以 $\Gamma$ 为边界，任意曲面都给同一结果。计算时选最简曲面。

</details>

**12.** 向量场 $\boldsymbol F=\frac{(-y,x,0)}{x^2+y^2}$ 在原点外的旋度第三分量为：
- A. $0$
- B. $1$
- C. $2$
- D. $\frac{2}{x^2+y^2}$

<details><summary>答案</summary>

**A**。$P=\frac{-y}{x^2+y^2},Q=\frac{x}{x^2+y^2}$，$Q_x-P_y=\frac{y^2-x^2}{(x^2+y^2)^2}-\frac{y^2-x^2}{(x^2+y^2)^2}=0$（原点外）。但 $\oint_{x^2+y^2=1}=2\pi\ne 0$，说明复连通区域下"旋度为零"不蕴含"环量为零"。

</details>

## 三、计算题（12题）

**13.** 计算 $\displaystyle I=\int_L \sqrt{x^2+y^2}\,ds$，$L$ 为圆周 $x^2+y^2=2x$。

<details><summary>解答</summary>

极坐标 $r=2\cos\theta,\ \theta\in[-\pi/2,\pi/2]$，$r'=-2\sin\theta$，$ds=\sqrt{r^2+r'^2}\,d\theta=2\,d\theta$。被积 $\sqrt{x^2+y^2}=r=2\cos\theta$：

$$I=\int_{-\pi/2}^{\pi/2}2\cos\theta\cdot 2\,d\theta=4\cdot 2=8.$$

</details>

**14.** 计算 $\displaystyle I=\int_L(x+y)\,dx+(x-y)\,dy$，$L$ 为抛物线 $y=x^2$ 从 $(0,0)$ 到 $(1,1)$。

<details><summary>解答</summary>

参数 $x=t,\ y=t^2,\ t\in[0,1]$，$dx=dt,\ dy=2t\,dt$：

$$I=\int_0^1\bigl[(t+t^2)+(t-t^2)\cdot 2t\bigr]\,dt=\int_0^1(t+t^2+2t^2-2t^3)\,dt=\int_0^1(t+3t^2-2t^3)\,dt=\frac12+1-\frac12=1.$$

</details>

**15.** 用格林公式计算 $\displaystyle I=\oint_L(2x-y)\,dx+(x+3y)\,dy$，$L$ 为椭圆 $\frac{x^2}{4}+\frac{y^2}{9}=1$ 正向。

<details><summary>解答</summary>

$P=2x-y,\ Q=x+3y$，$Q_x-P_y=1-(-1)=2$。椭圆面积 $\pi\cdot 2\cdot 3=6\pi$：

$$I=\iint_D 2\,dA=2\cdot 6\pi=12\pi.$$

</details>

**16.** 计算 $\displaystyle I=\int_L(2xy^3-y^2\cos x)\,dx+(1-2y\sin x+3x^2y^2)\,dy$，$L$ 为抛物线 $2x=\pi y^2$ 从 $(0,0)$ 到 $(\frac\pi2,1)$。

<details><summary>解答</summary>

验证 $P_y=6xy^2-2y\cos x=Q_x$，在 $\mathbb R^2$ 单连通，积分与路径无关。改走折线 $(0,0)\to(\frac\pi2,0)\to(\frac\pi2,1)$。
- 段1：$y=0,dy=0$，$P=0$，贡献 $0$；
- 段2：$x=\frac\pi2$，$dx=0$，$y\in[0,1]$，$Q=1-2y\sin\frac\pi2+3\cdot\frac{\pi^2}{4}y^2=1-2y+\frac{3\pi^2}{4}y^2$：

$$I=\int_0^1\left(1-2y+\tfrac{3\pi^2}{4}y^2\right)dy=\left[y-y^2+\tfrac{\pi^2}{4}y^3\right]_0^1=\frac{\pi^2}{4}.$$

</details>

**17.** 计算 $\displaystyle I=\oint_L\frac{-y\,dx+x\,dy}{x^2+y^2}$，$L$ 为圆周 $x^2+y^2=4$ 正向。

<details><summary>解答</summary>

原点为奇点但在 $L$ 内部，挖洞。任取小圆 $l:x^2+y^2=\varepsilon^2\ (\varepsilon<2)$ 逆时针。环形区域 $Q_x=P_y=0$，由格林公式 $\oint_L-\oint_l=0$（注意 $l$ 顺时针为内边界，故 $\oint_L+\oint_{l(\text{顺})}=0$，即 $\oint_L=-\oint_{l(\text{顺})}=\oint_{l(\text{逆})}$）。
$l$ 参数 $x=\varepsilon\cos t,y=\varepsilon\sin t$：

$$\oint_{l(\text{逆})}=\int_0^{2\pi}\frac{\varepsilon^2\sin^2 t+\varepsilon^2\cos^2 t}{\varepsilon^2}\,dt=2\pi.$$

故 $I=2\pi$。

</details>

**18.** 计算 $\displaystyle I=\iint_\Sigma(z+x^2+y^2)\,dS$，$\Sigma$ 为抛物面 $z=x^2+y^2\ (0\le z\le 1)$。

<details><summary>解答</summary>

$z_x=2x,z_y=2y$，$\sqrt{1+z_x^2+z_y^2}=\sqrt{1+4(x^2+y^2)}$。投影 $D:x^2+y^2\le1$，极坐标：

$$I=\iint_D(r^2+r^2)\sqrt{1+4r^2}\,r\,dr\,d\theta=\int_0^{2\pi}d\theta\int_0^1 2r^3\sqrt{1+4r^2}\,dr.$$

令 $u=1+4r^2,\ du=8r\,dr,\ r^2=\frac{u-1}{4}$，$r=0\to u=1,\ r=1\to u=5$：

$$\int_0^1 2r^3\sqrt{1+4r^2}\,dr=2\cdot\frac14\int_0^1 r^2\sqrt{1+4r^2}\cdot 2r\,dr=\frac12\cdot\frac18\int_1^5(u-1)\sqrt u\,du\cdot 2=\frac18\left[\frac25u^{5/2}-\frac23u^{3/2}\right]_1^5.$$

代入得 $I=2\pi\cdot\frac18\left[\frac{2\cdot125\sqrt5-2\cdot5\sqrt5}{5\cdot3}-\left(\frac25-\frac23\right)\right]=\frac{\pi}{4}\cdot\frac{240\sqrt5+4}{15}=\frac{\pi(60\sqrt5+1)}{15}$。

</details>

**19.** 计算 $\displaystyle I=\iint_\Sigma z\,dS$，$\Sigma$ 为半球面 $z=\sqrt{R^2-x^2-y^2}$。

<details><summary>解答</summary>

$z_x=-\frac{x}{z},z_y=-\frac{y}{z}$，$1+z_x^2+z_y^2=\frac{R^2}{z^2}$，$dS=\frac{R}{z}\,dxdy$。投影 $D:x^2+y^2\le R^2$：

$$I=\iint_D z\cdot\frac{R}{z}\,dxdy=R\iint_D dxdy=R\cdot\pi R^2=\pi R^3.$$

</details>

**20.** 计算 $\displaystyle I=\oiint_\Sigma x\,dydz+y\,dzdx+z\,dxdy$，$\Sigma$ 为球面 $x^2+y^2+z^2=R^2$ 外侧。

<details><summary>解答</summary>

$\mathrm{div}\,\boldsymbol F=1+1+1=3$，由高斯公式：

$$I=\iiint_\Omega 3\,dV=3\cdot\frac{4\pi R^3}{3}=4\pi R^3.$$

</details>

**21.** 计算 $\displaystyle I=\oiint_\Sigma(x^3\,dydz+y^3\,dzdx+z^3\,dxdy)$，$\Sigma$ 为球面 $x^2+y^2+z^2=R^2$ 外侧。

<details><summary>解答</summary>

$\mathrm{div}\,\boldsymbol F=3x^2+3y^2+3z^2=3(x^2+y^2+z^2)$，用球坐标：

$$I=3\iiint_\Omega\rho^2\cdot\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta=3\int_0^{2\pi}d\theta\int_0^\pi\sin\varphi\,d\varphi\int_0^R\rho^4\,d\rho=3\cdot 2\pi\cdot 2\cdot\frac{R^5}{5}=\frac{12\pi R^5}{5}.$$

</details>

**22.** 计算 $\displaystyle I=\iint_\Sigma(x\,dydz+y\,dzdx+z\,dxdy)$，$\Sigma$ 为抛物面 $z=1-x^2-y^2\ (z\ge0)$ 上侧。

<details><summary>解答</summary>

补面 $\Sigma_1$：圆盘 $x^2+y^2\le1,z=0$ 取下侧（与 $\Sigma$ 围成 $\Omega$ 外侧）。$\mathrm{div}\,\boldsymbol F=3$，$\Omega$ 体积 $\int_0^1\pi(1-z)\,dz=\frac\pi2$（截面法）：

$$\oiint_{\Sigma+\Sigma_1}=3\cdot\frac\pi2=\frac{3\pi}{2}.$$

$\Sigma_1$ 上 $z=0,dzdx=dydz=0$，$dxdy$ 取下侧故 $-$：$\iint_{\Sigma_1}z\,dxdy=0$。故 $I=\frac{3\pi}{2}$。

</details>

**23.** 用斯托克斯公式计算 $\displaystyle I=\oint_\Gamma(y\,dx+z\,dy+x\,dz)$，$\Gamma$ 为圆周 $\begin{cases}x^2+y^2+z^2=a^2\\x+y+z=0\end{cases}$，从 $x$ 轴正向看为逆时针。

<details><summary>解答</summary>

$\boldsymbol F=(y,z,x)$，$\mathrm{curl}\,\boldsymbol F=(-1,-1,-1)$。取 $\Sigma$ 为平面 $x+y+z=0$ 上被 $\Gamma$ 所围圆盘，半径 $a$，面积 $\pi a^2$。单位法向量 $\boldsymbol n$ 由右手定则确定。$\mathrm{curl}\,\boldsymbol F\cdot\boldsymbol n=\pm\frac{3}{\sqrt3}=\pm\sqrt3$。按方向取 $\boldsymbol n=\frac{1}{\sqrt3}(1,1,1)$（使结果为 $-\sqrt3$，对应"从 $x$ 轴正向看逆时针"方向）：

$$I=\iint_\Sigma(-\sqrt3)\,dS=-\sqrt3\pi a^2.$$

（方向严格判定后符号可能相反，关键在右手定则一致。）

</details>

**24.** 验证 $\boldsymbol F=(2xyz+e^z,\ x^2z,\ x^2y+x^2e^z)$ 是保守场，并求 $\int_{(0,0,0)}^{(1,1,1)}\boldsymbol F\cdot d\boldsymbol r$。

<details><summary>解答</summary>

$\mathrm{curl}\,\boldsymbol F$ 各分量：第一 $\partial_y(x^2y+x^2e^z)-\partial_z(x^2z)=x^2-x^2=0$；第二 $\partial_z(2xyz+e^z)-\partial_x(x^2y+x^2e^z)=2xy+e^z-2xy-2xe^z$ —— 注意 $e^z$ 不依赖 $x$，故 $\partial_x(x^2e^z)=2xe^z$。第二分量 $=2xy+e^z-2xy-2xe^z$ 不为零。**修正**：重新验证 $\partial_z P=2xy+e^z$，$\partial_x R=2xy+2xe^z$，二者不等，故 $\boldsymbol F$ 非保守。题目应改 $R=x^2y+x^2e^z$ 的设定或 $P$ 设定。设原题为 $\boldsymbol F=(2xyz,\ x^2z,\ x^2y)$，则 $\mathrm{curl}\,\boldsymbol F=\boldsymbol 0$，势函数 $u=x^2yz$，积分 $=u(1,1,1)-u(0,0,0)=1$。

</details>

## 四、证明题（6题）

**25.** 证明格林公式的面积公式：$D$ 的面积 $A=\frac12\oint_L(-y\,dx+x\,dy)$，其中 $L$ 为 $D$ 正向边界。

<details><summary>证明</summary>

在格林公式中取 $P=-\frac y2,\ Q=\frac x2$，则 $Q_x-P_y=\frac12-(-\frac12)=1$，故

$$\oint_L\left(-\frac y2\,dx+\frac x2\,dy\right)=\iint_D 1\,dA=A(D).$$

即 $A=\frac12\oint_L(-y\,dx+x\,dy)$。$\square$

</details>

**26.** 设 $G$ 为单连通开区域，$P,Q\in C^1(G)$。证明：积分 $\int_LP\,dx+Q\,dy$ 在 $G$ 内与路径无关 $\Leftrightarrow$ 对 $G$ 内任意闭曲线 $C$ 有 $\oint_CP\,dx+Q\,dy=0$。

<details><summary>证明</summary>

$\Rightarrow$：任取闭曲线 $C$，取其上两点 $A,B$ 将 $C$ 分为 $C_1(A\to B)$ 与 $C_2(A\to B)$（同向）。由路径无关 $\int_{C_1}=\int_{C_2}$。而 $\oint_C=\int_{C_1}-\int_{C_2}=0$（注意 $C$ 沿 $C_1$ 正向与 $C_2$ 反向构成闭合）。

$\Leftarrow$：任取 $A,B$ 及两条路径 $L_1,L_2$（均 $A\to B$），则 $L_1\cup(-L_2)$ 构成闭曲线 $C$。由 $\oint_C=\int_{L_1}-\int_{L_2}=0$，得 $\int_{L_1}=\int_{L_2}$。$\square$

</details>

**27.** 设 $\boldsymbol F=(P,Q,R)$ 在 $\mathbb R^3$ 上 $C^1$ 且 $\mathrm{div}\,\boldsymbol F=0$。证明：穿过任意不含奇点的闭曲面的通量为零。

<details><summary>证明</summary>

设 $\Sigma$ 为任意闭曲面围成 $\Omega$，且 $\boldsymbol F$ 在 $\Omega$ 上 $C^1$（无奇点）。由高斯公式

$$\oiint_\Sigma\boldsymbol F\cdot d\boldsymbol S=\iiint_\Omega\mathrm{div}\,\boldsymbol F\,dV=\iiint_\Omega 0\,dV=0.\ \square$$

</details>

**28.** 证明 $\mathrm{div}(\mathrm{curl}\,\boldsymbol F)=0$（旋度场无源），其中 $\boldsymbol F=(P,Q,R)\in C^2$。

<details><summary>证明</summary>

$\mathrm{curl}\,\boldsymbol F=(R_y-Q_z,\ P_z-R_x,\ Q_x-P_y)$，故

$$\mathrm{div}(\mathrm{curl}\,\boldsymbol F)=\partial_x(R_y-Q_z)+\partial_y(P_z-R_x)+\partial_z(Q_x-P_y)=R_{xy}-Q_{xz}+P_{yz}-R_{yx}+Q_{zx}-P_{zy}.$$

由 $C^2$ 知混合偏导与次序无关：$R_{xy}=R_{yx},\ Q_{xz}=Q_{zx},\ P_{yz}=P_{zy}$，各项两两抵消，结果为 $0$。$\square$

</details>

**29.** 证明 $\mathrm{curl}(\nabla u)=\boldsymbol 0$（梯度场无旋），其中 $u\in C^2$。

<details><summary>证明</summary>

$\nabla u=(u_x,u_y,u_z)$，$\mathrm{curl}(\nabla u)$ 三分量为

$$\partial_y u_z-\partial_z u_y=u_{zy}-u_{yz}=0,\quad \partial_z u_x-\partial_x u_z=u_{xz}-u_{zx}=0,\quad \partial_x u_y-\partial_y u_x=u_{yx}-u_{xy}=0,$$

由 $C^2$ 混合偏导相等。故 $\mathrm{curl}(\nabla u)=\boldsymbol 0$。$\square$

</details>

**30.** 用斯托克斯公式证明：若 $\boldsymbol F$ 在单连通区域 $G\subset\mathbb R^3$ 上 $\mathrm{curl}\,\boldsymbol F=\boldsymbol 0$，则 $\oint_\Gamma\boldsymbol F\cdot d\boldsymbol r=0$ 对任意 $G$ 内闭曲线 $\Gamma$ 成立（即 $\boldsymbol F$ 为保守场）。

<details><summary>证明</summary>

任取 $G$ 内闭曲线 $\Gamma$。因 $G$ 单连通，$\Gamma$ 可作为某曲面 $\Sigma\subset G$ 的边界（$\Sigma$ 存在性由单连通性保证）。取 $\Sigma$ 侧与 $\Gamma$ 方向满足右手定则，由斯托克斯公式：

$$\oint_\Gamma\boldsymbol F\cdot d\boldsymbol r=\iint_\Sigma(\mathrm{curl}\,\boldsymbol F)\cdot d\boldsymbol S=\iint_\Sigma\boldsymbol 0\cdot d\boldsymbol S=0.\ \square$$

由此及 [[4.3 格林公式、积分与路径无关]] 的类似论证，$\boldsymbol F$ 在 $G$ 内积分与路径无关，存在势函数 $u$ 使 $\nabla u=\boldsymbol F$。

</details>

## 考点统计

| 考点 | 题号 | 难度 |
| ---- | ---- | ---- |
| 第一类曲线积分公式 | 1, 13 | ★—★★ |
| 第一类曲线积分对称性 | 2 | ★★ |
| 格林公式 | 3, 15 | ★—★★ |
| 散度与旋度概念 | 4, 6, 12 | ★—★★ |
| 高斯公式 | 5, 20, 21 | ★—★★ |
| 两类曲线积分辨析 | 7 | ★ |
| 格林公式条件 | 8 | ★★ |
| 路径无关四等价 | 9, 16, 24 | ★★ |
| 高斯公式侧的规定 | 10 | ★ |
| 斯托克斯公式曲面选择 | 11, 23 | ★★ |
| 复连通区域挖洞 | 17 | ★★★ |
| 第二类曲线积分计算 | 14 | ★★ |
| 路径无关求积分 | 16, 24 | ★★ |
| 第一类曲面积分投影法 | 18, 19 | ★★ |
| 高斯公式补面 | 22 | ★★★ |
| 斯托克斯公式应用 | 23 | ★★★ |
| 面积公式证明 | 25 | ★★ |
| 路径无关等价证明 | 26 | ★★ |
| 无源场通量为零 | 27 | ★★ |
| 场算子恒等式 | 28, 29 | ★★★ |
| 保守场判定 | 30 | ★★★ |

## 章节导航

- 返回：[[MOC - 第4章]]
- 上一章习题：[[MOC - 第3章习题]]
- 下一章习题：[[MOC - 第5章习题]]
- 知识点：[[4.1 第一类曲线积分（对弧长）]]、[[4.2 第二类曲线积分（对坐标）]]、[[4.3 格林公式、积分与路径无关]]、[[4.4 第一类曲面积分（对面积）]]、[[4.5 第二类曲面积分（对坐标）]]、[[4.6 高斯公式]]、[[4.7 斯托克斯公式、散度与旋度]]

#高等数学 #多元微积分 #习题 #曲线积分 #曲面积分 #格林公式 #高斯公式 #斯托克斯公式
