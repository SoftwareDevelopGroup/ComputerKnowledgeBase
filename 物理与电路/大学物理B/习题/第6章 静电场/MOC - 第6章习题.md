---
domain: 物理与电路
subject: 大学物理B
type: exercise
chapter: 第6章 静电场
tags: [大学物理,习题,电场强度,高斯定理,电势,电容,电介质]
prerequisites: ["高等数学A(2)"]
aliases: [第6章习题, 静电场习题]
---

# MOC - 第6章习题

> [!info] 习题集定位
> 本习题集围绕 [[MOC - 第6章]] 的核心考点设计，共 30 题，分**填空、选择、计算、证明/讨论**四类。重点训练：库仑定律与点电荷电场、电场叠加与积分法（直线、圆环、圆盘）、高斯定理的三类对称性应用（球/轴/面）、电势叠加与电势差计算、$\vec E=-\nabla V$ 的运用、导体静电平衡与感应电荷、电介质极化与 $\vec D$ 高斯定理、电容器电容与串并联、电场能量与能量密度。所有解答以 `<details>` 折叠，建议先独立完成再展开核对。计算中取 $k=\dfrac{1}{4\pi\varepsilon_0}\approx 9.0\times10^9\,\mathrm{N\cdot m^2/C^2}$，$\varepsilon_0=8.85\times10^{-12}\,\mathrm{C^2/(N\cdot m^2)}$，$e=1.60\times10^{-19}\,\mathrm C$。

## 一、填空题（6题）

**1.** 真空中两静止点电荷 $q_1,q_2$ 间距离为 $r$，库仑定律表达式 $\vec F=$ ____；其中静电力常量 $k=$ ____，真空介电常数 $\varepsilon_0=$ ____；当 $r\to 0$ 时该定律 ____（成立/失效），原因是 ____。

<details><summary>答案</summary>

$$\vec F_{12}=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}\hat r_{12}=k\frac{q_1q_2}{r^2}\hat r_{12}.$$

$$k\approx 9.0\times10^{9}\,\mathrm{N\cdot m^2/C^2},\quad \varepsilon_0=8.85\times10^{-12}\,\mathrm{C^2/(N\cdot m^2)}.$$

$r\to 0$ 时**失效**，因点电荷模型不再适用（带电体几何尺寸不可忽略），需考虑电荷分布。

</details>

**2.** 电场强度 $\vec E$ 的定义式 $\vec E=$ ____，单位是 ____ 或 ____；点电荷 $q$ 在距 $r$ 处产生的电场 $\vec E=$ ____，方向规定为 ____。

<details><summary>答案</summary>

$$\vec E=\lim_{q_0\to 0}\frac{\vec F}{q_0},\quad \text{单位 } \mathrm{N/C}=\mathrm{V/m}.$$

$$\vec E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat r=k\frac{q}{r^2}\hat r.$$

方向：$q>0$ 沿径向向外；$q<0$ 沿径向指向电荷。

</details>

**3.** 静电场高斯定理的积分形式 $\oint_S\vec E\cdot d\vec S=$ ____，微分形式 $\nabla\cdot\vec E=$ ____；该定理表明静电场是 ____ 场；面外电荷对闭合面 $\vec E$ 的通量贡献为 ____，对面内 $\vec E$ 的贡献 ____（为零/不为零）。

<details><summary>答案</summary>

$$\oint_S\vec E\cdot d\vec S=\frac{Q_{内}}{\varepsilon_0},\quad \nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}.$$

静电场是**有源**场。面外电荷对通量贡献为**零**（进多少出多少），但对 $\vec E$ 的贡献**不为零**（$\vec E$ 是所有电荷共同产生）。

</details>

**4.** 静电场环路定理 $\oint_L\vec E\cdot d\vec l=$ ____，表明静电场是 ____ 场，静电力是 ____ 力；由此可引入电势 $V$，其定义 $V_A=$ ____（取无穷远为零势）；$\vec E$ 与 $V$ 的微分关系 $\vec E=$ ____。

<details><summary>答案</summary>

$$\oint_L\vec E\cdot d\vec l=0.$$

静电场是**无旋**场，静电力是**保守**力。

$$V_A=\int_A^{\infty}\vec E\cdot d\vec l,\quad \vec E=-\nabla V.$$

</details>

**5.** 静电平衡时，导体内部 $\vec E=$ ____，导体是 ____ 体，电荷只分布在 ____；导体表面电场大小 $E=$ ____，方向 ____ 表面；接地空腔导体能屏蔽 ____（外场对内 / 内场对外 / 双向）。

<details><summary>答案</summary>

导体内 $\vec E=0$；导体是**等势**体；电荷只分布在**外表面**（实心导体）或内、外表面（空腔导体有内部电荷时）。

$$E=\frac{\sigma}{\varepsilon_0},\quad \text{方向沿外法线}.$$

接地空腔导体**双向屏蔽**（既屏蔽外场对腔内，也屏蔽腔内对外）。

</details>

**6.** 平行板电容器（极板面积 $S$、间距 $d$、介质 $\varepsilon_r$）的电容 $C=$ ____；充电至电压 $U$ 时储能 $W=$ ____（三种形式）；电场能量密度 $w=$ ____，电容器中总能量 $W=\int_V w\,dV=$ ____。

<details><summary>答案</summary>

$$C=\frac{\varepsilon_0\varepsilon_r S}{d}.$$

$$W=\frac{1}{2}CU^2=\frac{Q^2}{2C}=\frac{1}{2}QU.$$

$$w=\frac{1}{2}\varepsilon_0\varepsilon_r E^2=\frac{1}{2}\vec D\cdot\vec E.$$

$$W=w\cdot Sd=\frac12\varepsilon_0\varepsilon_r E^2 Sd=\frac{1}{2}CU^2\ \checkmark.$$

</details>

## 二、选择题（6题）

**7.** 关于电场强度 $\vec E$ 与电势 $V$，下列说法正确的是：
- A. $\vec E$ 为零处 $V$ 必为零
- B. $V$ 为零处 $\vec E$ 必为零
- C. $\vec E$ 大处 $V$ 必高
- D. $\vec E$ 与等势面处处正交，且指向 $V$ 减小方向

<details><summary>答案</summary>

**D**。$\vec E=-\nabla V$，电场与电势梯度反号，故 $\vec E$ 指向 $V$ 减小方向且垂直等势面。$\vec E=0$ 处 $V$ 可为任意常数（如均匀带电球壳内 $E=0$ 但 $V=kQ/R\ne 0$）；$V=0$ 处 $\vec E$ 可不为零（如偶极子中垂面 $V=0$ 但 $\vec E\ne\vec 0$）；$\vec E$ 大处 $V$ 梯度大但不一定 $V$ 高（如电势零点附近）。

</details>

**8.** 在点电荷 $+q$ 的电场中，作一球形高斯面包围 $q$。若把 $q$ 移开球心但仍保持在球内，则：
- A. 球面上 $\vec E$ 不变，通量不变
- B. 球面上 $\vec E$ 改变，通量不变
- C. 球面上 $\vec E$ 不变，通量改变
- D. 球面上 $\vec E$ 改变，通量改变

<details><summary>答案</summary>

**B**。高斯定理 $\oint\vec E\cdot d\vec S=Q_{内}/\varepsilon_0$，$Q_{内}=q$ 不变故通量不变；但球面上各点 $\vec E$ 由对称分布变为非对称（$q$ 偏离球心后 $\vec E$ 不再沿径向均匀），故 $\vec E$ 改变。这正说明高斯定理不能用来反解 $\vec E$（除非对称性足够强）。

</details>

**9.** 下列各情形中可用高斯定理直接求 $\vec E$ 的是：
- A. 电偶极子的电场
- B. 有限长均匀带电直线的电场
- C. 无限长均匀带电圆柱体的电场
- D. 均匀带电圆环轴线上的电场

<details><summary>答案</summary>

**C**。仅当电荷分布具有**球对称、轴对称、面对称**时才能由高斯定理反解 $\vec E$。无限长均匀带电圆柱体具有轴对称，可选同轴圆柱面为高斯面。电偶极子、有限长直线、圆环轴线均无足够对称性，必须用 [[6.2 电场强度叠加原理]] 的积分法（或先求 $V$ 再求 $\vec E$）。

</details>

**10.** 一不带电金属球壳，球心处放点电荷 $+q$，达到静电平衡后：
- A. 球壳内表面带 $+q$，外表面带 $-q$
- B. 球壳内表面带 $-q$，外表面带 $+q$
- C. 球壳内、外表面均带 $+q/2$
- D. 球壳内、外表面均不带电

<details><summary>答案</summary>

**B**。在导体壳内（$R_1<r<R_2$）取高斯面，$\vec E=0$ ⇒ $Q_{内}=0$ ⇒ $q+q_{内表}=0$ ⇒ $q_{内表}=-q$。球壳总电荷为零（不带电），故 $q_{外表}=+q$。详见 [[6.6 静电场中的导体与电介质]] 例1。

</details>

**11.** 平行板电容器充电后断开电源，将两极板间距 $d$ 增大为 $2d$，则：
- A. 电容增大，电压增大，储能增大
- B. 电容减小，电压增大，储能增大
- C. 电容减小，电压不变，储能减小
- D. 电容增大，电压减小，储能不变

<details><summary>答案</summary>

**B**。断开电源 ⇒ 电荷 $Q$ 不变。$C=\varepsilon_0 S/d$，$d\to 2d$ ⇒ $C'=C/2$（减小）；$U=Q/C$ ⇒ $U'=2U$（增大）；$W=Q^2/(2C)$ ⇒ $W'=2W$（增大）。外力克服两板静电引力做功转化为电场能。若不断开电源（恒压），$U$ 不变 $Q$ 减半 $W$ 减半，结论相反。

</details>

**12.** 关于电介质中的高斯定理 $\oint\vec D\cdot d\vec S=Q_{自由}$，下列说法正确的是：
- A. $\vec D$ 仅由自由电荷产生，与极化电荷无关
- B. $\vec D$ 由所有电荷（自由 + 极化）共同产生
- C. $\vec D$ 在介质分界面处必定连续
- D. 在线性各向同性介质中 $\vec D=\varepsilon_0\vec E$

<details><summary>答案</summary>

**B**。$\vec D=\varepsilon_0\vec E+\vec P$ 是 $\vec E$（所有电荷共同产生）与 $\vec P$（极化电荷贡献）的合成；其通量只与**自由电荷**有关，但 $\vec D$ 本身由所有电荷决定。$\vec D$ 在介质分界面处**法向分量**连续（无自由面电荷时），切向分量不一定连续。线性各向同性介质中 $\vec D=\varepsilon_0\varepsilon_r\vec E=\varepsilon\vec E$，非 $\varepsilon_0\vec E$。

</details>

## 三、计算题（14题）

**13.** 真空中三个等量正点电荷 $+q$ 分别置于边长 $a$ 的正三角形三个顶点。求三角形中心处的电场强度（大小与方向）。已知中心到顶点距离 $r=a/\sqrt 3$。

<details><summary>解答</summary>

**分析**：设三个电荷位于正三角形顶点 $A,B,C$，中心 $O$。每个电荷在 $O$ 处电场大小 $E_1=kq/r^2=3kq/a^2$，方向沿对应顶点到中心连线（指向外，因 $q>0$）。

**对称性**：三电场方向彼此成 $120^\circ$ 角，大小相等。矢量和：

$$\vec E=\vec E_A+\vec E_B+\vec E_C.$$

取 $x$ 轴沿 $OA$ 方向（$\vec E_A$ 方向）。$\vec E_B$ 与 $\vec E_A$ 夹角 $120^\circ$，$\vec E_C$ 与 $\vec E_A$ 夹角 $-120^\circ$（即 $240^\circ$）。

分量：
$$E_x=E_1+E_1\cos 120^\circ+E_1\cos(-120^\circ)=E_1\left(1-\frac12-\frac12\right)=0.$$
$$E_y=0+E_1\sin 120^\circ+E_1\sin(-120^\circ)=E_1\left(\frac{\sqrt 3}{2}-\frac{\sqrt 3}{2}\right)=0.$$

故 $\vec E=0$。

**结论**：正三角形中心处 $\vec E=\vec 0$。这与电势叠加（[[MOC - 第6章]] 自测3）相比，电势不为零（$V=\sqrt 3\,kq/a$），但电场为零——电势是标量不能因对称抵消。

</details>

**14.** 半径 $R=0.10\,\mathrm m$ 的均匀带电圆环，总电荷 $Q=+5.0\times10^{-9}\,\mathrm C$。求轴线上距环心 $x=0.12\,\mathrm m$ 处的电场强度大小与方向。

<details><summary>解答</summary>

**公式**（[[6.2 电场强度叠加原理]]）：
$$E=\frac{1}{4\pi\varepsilon_0}\frac{Qx}{(R^2+x^2)^{3/2}}.$$

**代入**：
$$R^2+x^2=0.01+0.0144=0.0244\,\mathrm{m^2},$$
$$(R^2+x^2)^{3/2}=0.0244^{3/2}=0.0244\times\sqrt{0.0244}\approx 0.0244\times 0.1562=0.003812\,\mathrm{m^3}.$$
$$E=9.0\times10^9\times\frac{5.0\times10^{-9}\times 0.12}{0.003812}=\frac{5.4}{0.003812}\approx 1416\,\mathrm{N/C}.$$

方向：沿轴线远离环心（$Q>0$）。

**检验**：单位 $\mathrm{N\cdot m^2/C^2\times C\times m/m^3=N/C}$ ✓；远场极限 $x\gg R$ 时 $E\approx kQ/x^2=9\times10^9\times 5\times10^{-9}/0.0144=3125\,\mathrm{N/C}$，本例 $x$ 仅 $1.2R$ 故小于此值 ✓。

</details>

**15.** 半径 $R$ 的无限长均匀带电圆柱体，体密度 $\rho=+2.0\times10^{-6}\,\mathrm{C/m^3}$，$R=0.050\,\mathrm m$。求柱内 ($r=0.030\,\mathrm m$) 与柱外 ($r=0.10\,\mathrm m$) 的电场。

<details><summary>解答</summary>

**柱内** ($r<R$)：取半径 $r$、长 $l$ 的同轴圆柱面为高斯面。$Q_{内}=\rho\cdot\pi r^2 l$，$\vec E$ 沿径向，侧面通量 $E\cdot 2\pi r l$，两底面通量为零。由高斯定理：
$$E\cdot 2\pi r l=\frac{\rho\pi r^2 l}{\varepsilon_0}\Rightarrow E=\frac{\rho r}{2\varepsilon_0}.$$
$$E_{内}=\frac{2.0\times10^{-6}\times 0.030}{2\times 8.85\times10^{-12}}=\frac{6.0\times10^{-8}}{1.77\times10^{-11}}\approx 3390\,\mathrm{N/C}.$$

**柱外** ($r>R$)：$Q_{内}=\rho\cdot\pi R^2 l$（柱体全部电荷），
$$E=\frac{\rho R^2}{2\varepsilon_0 r}.$$
$$E_{外}=\frac{2.0\times10^{-6}\times 0.0025}{2\times 8.85\times10^{-12}\times 0.10}=\frac{5.0\times10^{-9}}{1.77\times10^{-12}}\approx 2825\,\mathrm{N/C}.$$

**检验**：单位 $\rho r/\varepsilon_0=\mathrm{C/m^3\times m\div C^2/(N\cdot m^2)=N/C}$ ✓；$r=R$ 处两式一致：$E_{内}(R)=\rho R/(2\varepsilon_0)=E_{外}(R)$ ✓。

</details>

**16.** 一无限大均匀带电平面，面密度 $\sigma=+4.0\times10^{-6}\,\mathrm{C/m^2}$。求其两侧电场。若在此平面右侧距 $d=0.05\,\mathrm m$ 处平行放置另一面密度 $\sigma'=-4.0\times10^{-6}\,\mathrm{C/m^2}$ 的平面，求两平面之间与两平面外侧的电场。

<details><summary>解答</summary>

**单平面**（[[6.3 高斯定理]]）：
$$E=\frac{\sigma}{2\varepsilon_0}=\frac{4.0\times10^{-6}}{2\times 8.85\times10^{-12}}\approx 2.26\times10^5\,\mathrm{N/C}.$$
方向：右侧沿 $+x$，左侧沿 $-x$（$\sigma>0$ 时背离平面）。

**双平面**（叠加原理）：设 $\sigma$ 平面在左、$\sigma'=-\sigma$ 平面在右。
- **板间**：两电场同向叠加，$E_{间}=\dfrac{\sigma}{2\varepsilon_0}+\dfrac{|\sigma'|}{2\varepsilon_0}=\dfrac{\sigma}{\varepsilon_0}\approx 4.52\times10^5\,\mathrm{N/C}$，方向由正板指向负板（$+x$）；
- **板外**（左侧或右侧）：两电场反向抵消，$E_{外}=0$。

这正是平行板电容器的理想模型，板间均匀电场 $E=\sigma/\varepsilon_0$。

**检验**：板间 $E=\sigma/\varepsilon_0$ 是单板 $E=\sigma/(2\varepsilon_0)$ 的两倍 ✓；板外为零是双板电荷相反的结果 ✓。

</details>

**17.** 半径 $R=0.20\,\mathrm m$ 的均匀带电球壳，总电荷 $Q=+6.0\times10^{-9}\,\mathrm C$。求：(1) 球壳内 ($r=0.10\,\mathrm m$) 与球壳外 ($r=0.30\,\mathrm m$) 的电场；(2) 球壳内与球壳上的电势。

<details><summary>解答</summary>

**(1) 电场**：
- 球内 $r<R$：球壳定理，$E=0$；
- 球外 $r>R$：$E=\dfrac{kQ}{r^2}=\dfrac{9.0\times10^9\times 6.0\times10^{-9}}{0.30^2}=\dfrac{54}{0.09}=600\,\mathrm{N/C}$。

**(2) 电势**（取无穷远为零势）：
- 球外 $V(r)=kQ/r$，球面上 $V(R)=\dfrac{kQ}{R}=\dfrac{9.0\times10^9\times 6.0\times10^{-9}}{0.20}=270\,\mathrm V$；
- 球内电势等于球面电势（球内 $E=0$，电势无变化）：$V_{内}=V(R)=270\,\mathrm V$。

**检验**：球壳内 $E=0$ 但 $V\ne 0$，是常见考点；球面上 $E$ 由外极限 $kQ/R^2=1350\,\mathrm{N/C}$ 给出（内极限为 0，故 $E$ 在球面处有突变，对应面电荷 $\sigma=Q/(4\pi R^2)$）✓。

</details>

**18.** 边长 $a=0.10\,\mathrm m$ 的正方形四顶点各放点电荷：$A(+q),B(+q),C(-q),D(-q)$，$q=2.0\times10^{-9}\,\mathrm C$（按 $A,B,C,D$ 顺序为相邻顶点）。求正方形中心 $O$ 处的电势（取无穷远为零势）。

<details><summary>解答</summary>

中心到任一顶点距离 $r=a/\sqrt 2=0.10/\sqrt 2=0.0707\,\mathrm m$。

**电势标量叠加**：
$$V=\sum_i\frac{kq_i}{r}=\frac{k}{r}(q+q-q-q)=0.$$

**结论**：$V_O=0$。

**注意**：若求电场则需矢量叠加，结果不为零。两 $+q$ 在 $O$ 处合电场沿 $AC$ 对角线（由 $B,D$ 中点指向 $A,C$ 中点），两 $-q$ 合电场同方向，故 $\vec E\ne\vec 0$。这是电势叠加（标量）与电场叠加（矢量）差异的典型例子。

</details>

**19.** 已知电势函数 $V(x,y,z)=3x^2-2y^2+z^2-6xz+5$（单位 $\mathrm V$，$x,y,z$ 单位 $\mathrm m$）。求点 $P(1,2,-1)$ 处的电场强度 $\vec E$。

<details><summary>解答</summary>

**用 $\vec E=-\nabla V$**：
$$E_x=-\frac{\partial V}{\partial x}=-(6x-6z),\quad E_y=-\frac{\partial V}{\partial y}=4y,\quad E_z=-\frac{\partial V}{\partial z}=-(2z-6x).$$

在 $P(1,2,-1)$：
$$E_x=-(6\cdot 1-6\cdot(-1))=-(6+6)=-12\,\mathrm{V/m},$$
$$E_y=4\cdot 2=8\,\mathrm{V/m},$$
$$E_z=-(2\cdot(-1)-6\cdot 1)=-(-2-6)=8\,\mathrm{V/m}.$$

$$\vec E(P)=(-12\hat i+8\hat j+8\hat k)\,\mathrm{V/m},$$
$$|\vec E|=\sqrt{144+64+64}=\sqrt{272}\approx 16.5\,\mathrm{V/m}.$$

**检验**：单位 $\partial V/\partial x$ 单位 $\mathrm{V/m}$，与 $\vec E$ 一致 ✓。

</details>

**20.** 半径 $R_1=0.050\,\mathrm m$ 的金属球带电 $Q=+3.0\times10^{-9}\,\mathrm C$，球外包有一层外半径 $R_2=0.10\,\mathrm m$ 的同心均匀电介质球壳（相对介电常数 $\varepsilon_r=2.5$）。求：(1) 介质内 ($R_1<r<R_2$) 与介质外 ($r>R_2$) 的电场；(2) 介质内、外表面的极化电荷。

<details><summary>解答</summary>

**(1) 电场**：球对称，用 $\vec D$ 高斯定理。面内自由电荷恒为 $Q$：
$$D\cdot 4\pi r^2=Q\Rightarrow D=\frac{Q}{4\pi r^2}=\frac{k\varepsilon_0 Q}{r^2}.$$

由 $\vec D=\varepsilon_0\varepsilon_r\vec E$ 分段：
- 介质内 $R_1<r<R_2$：$\varepsilon=\varepsilon_0\varepsilon_r$，$E=\dfrac{D}{\varepsilon}=\dfrac{kQ}{\varepsilon_r r^2}=\dfrac{9\times10^9\times 3\times10^{-9}}{2.5\,r^2}=\dfrac{10.8}{r^2}\,\mathrm{N/C}$；
- 介质外 $r>R_2$：$\varepsilon=\varepsilon_0$，$E=\dfrac{kQ}{r^2}=\dfrac{27}{r^2}\,\mathrm{N/C}$。

介质内电场为真空值的 $1/\varepsilon_r=1/2.5$ 倍。

**(2) 极化电荷**：极化强度 $\vec P=\varepsilon_0\chi_e\vec E=\varepsilon_0(\varepsilon_r-1)\vec E=\dfrac{\varepsilon_r-1}{\varepsilon_r}\vec D$。
- 介质内表面（$r=R_1^+$，外法线指向球心 $-\hat r$）：$\sigma_p=\vec P\cdot\hat n=-P(R_1)=-\dfrac{\varepsilon_r-1}{\varepsilon_r}\cdot\dfrac{Q}{4\pi R_1^2}$，
  $$Q_{p,内}=\sigma_p\cdot 4\pi R_1^2=-\frac{\varepsilon_r-1}{\varepsilon_r}Q=-\frac{1.5}{2.5}\times 3.0\times10^{-9}=-1.8\times10^{-9}\,\mathrm C.$$
- 介质外表面（$r=R_2^-$，外法线沿 $+\hat r$）：$Q_{p,外}=+\dfrac{\varepsilon_r-1}{\varepsilon_r}Q=+1.8\times10^{-9}\,\mathrm C$。

极化电荷代数和为零（电介质整体中性）✓。

**检验**：介质内 $E$ 与无介质情形 $kQ/r^2$ 相比缩小为 $1/\varepsilon_r$ ✓；极化电荷内负外正，符合"介质在电场中两端出现相反束缚电荷"的图像 ✓。

</details>

**21.** 平行板电容器极板面积 $S=200\,\mathrm{cm^2}=2.0\times10^{-2}\,\mathrm{m^2}$，间距 $d=2.0\,\mathrm{mm}=2.0\times10^{-3}\,\mathrm m$，板间为真空。求：(1) 电容；(2) 充电至 $U=100\,\mathrm V$ 时的电荷与储能；(3) 板间电场与能量密度。

<details><summary>解答</summary>

**(1) 电容**：
$$C=\frac{\varepsilon_0 S}{d}=\frac{8.85\times10^{-12}\times 2.0\times10^{-2}}{2.0\times10^{-3}}=8.85\times10^{-11}\,\mathrm F=88.5\,\mathrm{pF}.$$

**(2) 电荷与储能**：
$$Q=CU=8.85\times10^{-11}\times 100=8.85\times10^{-9}\,\mathrm C=8.85\,\mathrm{nC}.$$
$$W=\frac12 CU^2=\frac12\times 8.85\times10^{-11}\times 10^4=4.43\times10^{-7}\,\mathrm J=0.443\,\mu\mathrm J.$$

**(3) 电场与能量密度**：
$$E=\frac{U}{d}=\frac{100}{2.0\times10^{-3}}=5.0\times10^4\,\mathrm{V/m}.$$
$$w=\frac12\varepsilon_0 E^2=\frac12\times 8.85\times10^{-12}\times (5\times10^4)^2=\frac12\times 8.85\times10^{-12}\times 2.5\times10^9=1.11\times10^{-2}\,\mathrm{J/m^3}.$$

**总能量验证**：$W=w\cdot Sd=1.11\times10^{-2}\times 2\times10^{-2}\times 2\times10^{-3}=4.44\times10^{-7}\,\mathrm J$ ✓。

</details>

**22.** 同心球形电容器，内半径 $R_1=0.030\,\mathrm m$，外半径 $R_2=0.060\,\mathrm m$，两球间充满 $\varepsilon_r=3.0$ 的电介质。求电容，并计算充电至 $U=500\,\mathrm V$ 时的储能。

<details><summary>解答</summary>

**电容公式**（[[6.6 静电场中的导体与电介质]]）：
$$C=\frac{4\pi\varepsilon_0\varepsilon_r R_1R_2}{R_2-R_1}=\frac{4\pi\times 8.85\times10^{-12}\times 3.0\times 0.030\times 0.060}{0.030}.$$
$$C=4\pi\times 8.85\times10^{-12}\times 3.0\times 0.060=4\pi\times 1.593\times10^{-12}=2.00\times10^{-11}\,\mathrm F=20.0\,\mathrm{pF}.$$

**储能**：
$$W=\frac12 CU^2=\frac12\times 2.0\times10^{-11}\times (500)^2=\frac12\times 2.0\times10^{-11}\times 2.5\times10^5=2.5\times10^{-6}\,\mathrm J=2.5\,\mu\mathrm J.$$

**检验**：若 $\varepsilon_r=1$（真空），$C_{真空}\approx 6.67\,\mathrm{pF}$；介质使电容增大 $\varepsilon_r=3$ 倍 ✓。

</details>

**23.** $C_1=6\,\mu\mathrm F$、$C_2=3\,\mu\mathrm F$ 两电容器：(1) 串联后接 $U=90\,\mathrm V$，求总电容、各电容器电压与电荷；(2) 并联后接 $U=90\,\mathrm V$，求总电容、各电容器电荷。

<details><summary>解答</summary>

**(1) 串联**：
$$\frac{1}{C}=\frac{1}{6}+\frac{1}{3}=\frac{1}{6}+\frac{2}{6}=\frac{3}{6}=\frac12\Rightarrow C=2\,\mu\mathrm F.$$
电荷相同 $Q=CU=2\times 90=180\,\mu\mathrm C$。
$$U_1=\frac{Q}{C_1}=\frac{180}{6}=30\,\mathrm V,\quad U_2=\frac{Q}{C_2}=\frac{180}{3}=60\,\mathrm V.$$
$U_1+U_2=90\,\mathrm V$ ✓。注意 $C$ 小者 $U$ 大（$C_2$ 较小故电压较大）。

**(2) 并联**：
$$C=C_1+C_2=9\,\mu\mathrm F.$$
电压相同 $U=90\,\mathrm V$。
$$Q_1=C_1 U=6\times 90=540\,\mu\mathrm C,\quad Q_2=C_2 U=3\times 90=270\,\mu\mathrm C.$$
总电荷 $Q=Q_1+Q_2=810\,\mu\mathrm C=CU=9\times 90$ ✓。

</details>

**24.** 半径 $R$ 的金属球带电 $Q$，球外紧贴一层同心的电介质球壳（外半径 $2R$，相对介电常数 $\varepsilon_r$）。求：(1) 各区域 $\vec D$ 与 $\vec E$；(2) 介质内极化电荷体密度 $\rho_p$；(3) 球的电势（取无穷远为零势）。

<details><summary>解答</summary>

**(1) 各区域**（球对称，$\vec D,\vec E$ 沿径向）：
- 球内 $r<R$（导体内）：$\vec D=0,\vec E=0$；
- 介质内 $R<r<2R$：$D=\dfrac{Q}{4\pi r^2}$，$E=\dfrac{D}{\varepsilon_0\varepsilon_r}=\dfrac{Q}{4\pi\varepsilon_0\varepsilon_r r^2}=\dfrac{kQ}{\varepsilon_r r^2}$；
- 介质外 $r>2R$：$D=\dfrac{Q}{4\pi r^2}$，$E=\dfrac{D}{\varepsilon_0}=\dfrac{kQ}{r^2}$。

**(2) 极化电荷体密度**：$\vec P=\dfrac{\varepsilon_r-1}{\varepsilon_r}\vec D=\dfrac{(\varepsilon_r-1)Q}{4\pi\varepsilon_r r^2}\hat r$，
$$\rho_p=-\nabla\cdot\vec P=-\frac{1}{r^2}\frac{\partial}{\partial r}(r^2 P_r)=-\frac{1}{r^2}\frac{\partial}{\partial r}\left[\frac{(\varepsilon_r-1)Q}{4\pi\varepsilon_r}\right]=0.$$

介质内 $\rho_p=0$（极化电荷只分布在介质内、外表面）。

**(3) 球的电势**：球是等势体，取 $r=R$：
$$V(R)=\int_R^{\infty}E\,dr=\int_R^{2R}\frac{kQ}{\varepsilon_r r^2}\,dr+\int_{2R}^{\infty}\frac{kQ}{r^2}\,dr.$$
$$=\frac{kQ}{\varepsilon_r}\left(\frac{1}{R}-\frac{1}{2R}\right)+kQ\cdot\frac{1}{2R}=\frac{kQ}{2R\varepsilon_r}+\frac{kQ}{2R}=\frac{kQ}{2R}\left(1+\frac{1}{\varepsilon_r}\right).$$

**检验**：$\varepsilon_r=1$（无介质）时 $V=kQ/R$ ✓；$\varepsilon_r\to\infty$（理想导体外壳）时 $V\to kQ/(2R)$（介质内电场为零，球外电场对应球面 $2R$ 处点电荷）。

</details>

**25.** 平行板电容器（极板面积 $S$、间距 $d$、电压 $U$ 保持恒定），板间原为真空。今将一块厚度 $t<d$、相对介电常数 $\varepsilon_r$ 的电介质板完全填满板间宽度方向（紧贴一极板）插入。求：(1) 电容变化比 $C'/C_0$；(2) 储能变化比 $W'/W_0$；(3) 电源做的功。

<details><summary>解答</summary>

**(1) 电容**（[[6.6 静电场中的导体与电介质]] 例5）：
$$C'=\frac{\varepsilon_0\varepsilon_r S}{\varepsilon_r d-(\varepsilon_r-1)t},\quad C_0=\frac{\varepsilon_0 S}{d}.$$
$$\frac{C'}{C_0}=\frac{\varepsilon_r d}{\varepsilon_r d-(\varepsilon_r-1)t}.$$
当 $t=d$（介质填满）：$C'/C_0=\varepsilon_r$ ✓。

**(2) 储能**（恒压）：$W=\dfrac12 CU^2$，
$$\frac{W'}{W_0}=\frac{C'}{C_0}=\frac{\varepsilon_r d}{\varepsilon_r d-(\varepsilon_r-1)t}>1.$$

**(3) 电源做功**：电荷变化 $\Delta Q=(C'-C_0)U$，电源做功
$$W_{电源}=U\Delta Q=(C'-C_0)U^2.$$
能量守恒：$W_{电源}=\Delta W+W_{极化}$，其中 $\Delta W=W'-W_0=\dfrac12(C'-C_0)U^2$，故
$$W_{极化}=\frac12(C'-C_0)U^2=\Delta W.$$
即电源做功一半用于增加电容器储能，一半用于介质极化（电场力吸引介质进入做正功）。

</details>

**26.** 半径 $R_1$ 的金属球带电 $+Q$，其外有一半径 $R_2$ 的同心接地金属球壳（$R_2>R_1$）。求：(1) 球壳内、外表面感应电荷；(2) 各区域电场；(3) 内球与球壳间电压 $U_{12}$；(4) 系统电容。

<details><summary>解答</summary>

**(1) 感应电荷**：内球电荷 $+Q$ 在球壳内表面感应 $-Q$（由导体内 $\vec E=0$ + 高斯定理）。球壳接地 ⇒ 外表面电势为零 ⇒ 外表面电荷为零（无电场从外壳延伸到无穷远，否则 $V(\infty)-V(R_2)=\int E\,dr\ne 0$ 与接地矛盾）。故 $q_{内表}=-Q$，$q_{外表}=0$。

**(2) 电场**：
- $r<R_1$（导体内）：$E=0$；
- $R_1<r<R_2$：$E=\dfrac{kQ}{r^2}$（仅由内球 $+Q$ 与内表面 $-Q$ 之差，球壳定理使内表面 $-Q$ 在腔内不产生电场）；
- $r>R_2$：外壳外表电荷为零，$E=0$。

**球壳外无电场**——这是接地屏蔽的体现。

**(3) 内球与球壳间电压**：
$$U_{12}=V(R_1)-V(R_2)=\int_{R_1}^{R_2}E\,dr=\int_{R_1}^{R_2}\frac{kQ}{r^2}\,dr=kQ\left(\frac{1}{R_1}-\frac{1}{R_2}\right).$$

**(4) 系统电容**：球壳接地，与内球构成球形电容器，
$$C=\frac{Q}{U_{12}}=\frac{1}{k\left(\dfrac{1}{R_1}-\dfrac{1}{R_2}\right)}=\frac{4\pi\varepsilon_0 R_1R_2}{R_2-R_1}.$$

与未接地球形电容器电容相同（电容只依赖几何，与是否接地无关）✓。

</details>

## 四、证明与讨论题（4题）

**27.** 用高斯定理证明：均匀带电球壳内部电场处处为零（球壳定理），并讨论此结论与万有引力球壳定理的对应关系。

<details><summary>证明</summary>

设球壳半径 $R$，总电荷 $Q$。在球壳内任取一点 $P$（不一定在球心），过 $P$ 作以球心为心的同心球面 $S$（半径 $r<R$）。

由球对称性（电荷分布在球壳上各向同性），$\vec E$ 必沿径向（$\hat r$ 方向）且大小仅依赖 $r$。在 $S$ 上 $\vec E$ 大小恒定。

由高斯定理：
$$\oint_S\vec E\cdot d\vec S=E\cdot 4\pi r^2=\frac{Q_{内}}{\varepsilon_0}.$$

而 $S$ 在球壳内，$Q_{内}=0$（球壳电荷全在 $S$ 外），故 $E=0$。$\square$

**与万有引力球壳定理对应**：牛顿引力 $\vec F=-\dfrac{Gm_1m_2}{r^2}\hat r$ 与库仑力 $\vec F=\dfrac{kq_1q_2}{r^2}\hat r$ 形式完全类似（都是 $1/r^2$ 律，沿径向），故引力场 $\vec g$ 与电场 $\vec E$ 满足相同的高斯定理：
$$\oint\vec g\cdot d\vec S=-4\pi G M_{内}.$$

均匀球壳内部 $\vec g=0$，即球壳对内部物体无引力作用。这是 [[MOC - 第3章]] 中物体在地球内部所受引力的理论基础。

</details>

**28.** 证明：在均匀各向同性介质中，极化电荷体密度 $\rho_p$ 与自由电荷体密度 $\rho_{自由}$ 满足 $\rho_p=-\dfrac{\varepsilon_r-1}{\varepsilon_r}\rho_{自由}$，并讨论其物理意义。

<details><summary>证明</summary>

在线性各向同性介质中 $\vec P=\varepsilon_0\chi_e\vec E=\varepsilon_0(\varepsilon_r-1)\vec E$。又 $\vec D=\varepsilon_0\vec E+\vec P=\varepsilon_0\varepsilon_r\vec E$，故 $\vec P=\dfrac{\varepsilon_r-1}{\varepsilon_r}\vec D$。

取散度：
$$\rho_p=-\nabla\cdot\vec P=-\frac{\varepsilon_r-1}{\varepsilon_r}\nabla\cdot\vec D.$$

由 $\vec D$ 的高斯定理微分形式 $\nabla\cdot\vec D=\rho_{自由}$：
$$\rho_p=-\frac{\varepsilon_r-1}{\varepsilon_r}\rho_{自由}.\ \square$$

**物理意义**：
1. 极化电荷与自由电荷**反号**（介质极化产生的束缚电荷总是抵消外加自由电荷的电场）；
2. $|\rho_p/\rho_{自由}|=(\varepsilon_r-1)/\varepsilon_r<1$，极化电荷绝对值小于自由电荷；
3. $\varepsilon_r=1$（真空）时 $\rho_p=0$（无介质无极化）；
4. $\varepsilon_r\to\infty$（理想导体极限）时 $\rho_p\to -\rho_{自由}$，极化电荷完全抵消自由电荷——这正是导体静电平衡时 $\vec E_{内}=0$ 的微观机制；
5. 在均匀介质内部若无自由电荷（$\rho_{自由}=0$），则 $\rho_p=0$——极化电荷只出现在介质表面或不均匀处。详见 [[6.6 静电场中的导体与电介质]]。

</details>

**29.** 讨论下列情形中电场能量如何变化，并说明能量守恒关系：(a) 平行板电容器充电后**断开电源**，将两板间距增大；(b) 充电后**保持与电源连接**，将两板间距增大。

<details><summary>解答</summary>

设初始电容 $C_0=\varepsilon_0 S/d$，电荷 $Q_0$，电压 $U_0=Q_0/C_0$，储能 $W_0=Q_0^2/(2C_0)=\tfrac12 C_0 U_0^2$。增大间距 $d\to d'=2d$ ⇒ $C'=C_0/2$。

**(a) 断开电源（恒电荷 $Q=Q_0$）**：
- $Q'=Q_0$；
- $U'=Q/C'=2U_0$；
- $W'=Q^2/(2C')=2W_0$（储能**增加**）。

**能量来源**：外力克服两板静电引力（异性电荷相吸）做正功 $W_{外}=W'-W_0=W_0$。能量守恒：外力做功 = 储能增加 ✓。

**(b) 接电源（恒电压 $U=U_0$）**：
- $U'=U_0$；
- $Q'=C'U'=C_0 U_0/2=Q_0/2$；
- $W'=\tfrac12 C'U'^2=\tfrac12(C_0/2)U_0^2=W_0/2$（储能**减少**）。

**能量关系**：电源做功 $W_{电源}=U\Delta Q=U_0(Q_0/2-Q_0)=-\tfrac12 Q_0 U_0=-W_0$（电源吸收能量，即电荷回流到电源）；外力做功 $W_{外}$（同 (a)，克服静电引力）。

能量守恒：$W_{外}+W_{电源}=\Delta W=W'/W_0-1=-1/2$，即 $W_{外}-W_0=-W_0/2$，故 $W_{外}=W_0/2$。

**对比**：恒电荷时储能增加（外力做功全转化为电场能）；恒电压时储能减少（电源吸收部分能量，外力做功较少）。这是因恒电压下板间电场 $E=U/d$ 随 $d$ 增大而减小，静电引力也减小，故外力做功更少。

</details>

**30.** 综合讨论：静电场的两大基本定理（高斯定理与环路定理）分别刻画静电场的什么性质？为何二者结合才能完整描述静电场？分别举例说明仅凭其中一个定理不足以确定电场。

<details><summary>解答</summary>

**两大定理的性质**：
1. **高斯定理** $\oint\vec E\cdot d\vec S=Q_{内}/\varepsilon_0$（微分形式 $\nabla\cdot\vec E=\rho/\varepsilon_0$）：刻画静电场的**有源性**——电场线发自正电荷、终于负电荷，不会在无电荷处中断。
2. **环路定理** $\oint\vec E\cdot d\vec l=0$（微分形式 $\nabla\times\vec E=\vec 0$）：刻画静电场的**无旋性**——电场线不闭合，静电力做功与路径无关。

**为何需要两者结合**：从数学角度看，矢量场 $\vec E$ 由其**散度**（源）和**旋度**（涡）共同唯一确定（亥姆霍兹定理，需配合边界条件）。仅知散度不能确定旋度，反之亦然。物理上，散度给出"哪里有源"，旋度给出"是否有涡旋"，两者结合才完整描述场结构。

**仅凭一个定理不足以确定电场**：
- **仅高斯定理**不足以确定 $\vec E$：例如点电荷 $+q$ 与电偶极子的电场，若只取一个包围它们的高斯面，二者产生的通量相同（均等于 $q/\varepsilon_0$），但电场分布截然不同。又如[[#8.|题8]]中点电荷偏离球心后球面 $\vec E$ 改变但通量不变。一般情形下，高斯定理只给出积分量（总通量），不给出每点 $\vec E$ 的具体值与方向。
- **仅环路定理**不足以确定 $\vec E$：例如均匀电场 $\vec E_0$ 与点电荷电场 $\vec E_q$ 都满足环路积分为零，但分布完全不同。环路定理只要求场无旋，不能给出"哪里有源"。均匀电场 $\vec E_0$（无源无旋）和零场都满足环路定理，但显然不同——必须靠高斯定理区分（前者无源，后者也无源；但加上边界条件后可区分）。

**结论**：高斯定理 + 环路定理 + 边界条件（如无穷远 $\vec E\to 0$）三者结合，才能由电荷分布唯一确定静电场。这正是 [[MOC - 第8章]] 麦克斯韦方程组（4 个方程）的思想雏形——静电情形的麦克斯韦方程组即由这两个定理构成。

</details>

## 考点统计

| 考点 | 题号 | 难度 |
| ---- | ---- | ---- |
| 库仑定律、点电荷电场 | 1, 2, 13 | ★—★★ |
| 电场叠加（矢量 vs 标量） | 13, 18 | ★★ |
| 积分法（圆环、圆盘、直线） | 14 | ★★ |
| 高斯定理（球对称） | 3, 15, 17, 20, 24, 27 | ★★—★★★ |
| 高斯定理（轴对称） | 15 | ★★ |
| 高斯定理（面对称） | 16 | ★★ |
| 高斯定理适用条件 | 8, 9 | ★★ |
| 环路定理、电势定义 | 4, 27 | ★★ |
| 电势叠加与计算 | 17, 18 | ★★ |
| $\vec E=-\nabla V$ | 7, 19 | ★★ |
| 导体静电平衡 | 5, 10, 26 | ★★—★★★ |
| 静电屏蔽 | 26 | ★★★ |
| 电介质极化、$\vec D$ 高斯定理 | 12, 20, 24, 28 | ★★★ |
| 电容器电容 | 6, 21, 22, 23 | ★★ |
| 电容器串并联 | 23 | ★★ |
| 电场能量与能量密度 | 6, 21, 22, 25, 29 | ★★—★★★ |
| 介质对储能的影响（恒电荷/恒电压） | 11, 25, 29 | ★★★ |
| 综合定理讨论 | 30 | ★★★ |
| 证明题 | 27, 28 | ★★★ |

## 章节导航

- 返回：[[MOC - 第6章]]
- 上一章习题：[[MOC - 第5章习题]]
- 下一章习题：[[MOC - 第7章习题]]
- 知识点：[[6.1 库仑定律、电场强度]]、[[6.2 电场强度叠加原理]]、[[6.3 高斯定理]]、[[6.4 静电场环路定理、电势]]、[[6.5 电场强度与电势梯度]]、[[6.6 静电场中的导体与电介质]]

#大学物理 #电磁学 #习题 #静电场 #高斯定理 #电势 #电容 #电介质
