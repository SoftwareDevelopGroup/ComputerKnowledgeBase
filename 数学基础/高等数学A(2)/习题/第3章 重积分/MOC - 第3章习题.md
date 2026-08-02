---
domain: 数学基础
subject: 高等数学A(2)
type: exercise
chapter: 第3章 重积分
tags: [高等数学,习题,二重积分,三重积分,极坐标,柱坐标,球坐标]
prerequisites: ["高等数学A(1)"]
aliases: [第3章习题, 重积分习题]
---

# MOC - 第3章习题

> [!info] 习题集定位
> 本习题集围绕 [[MOC - 第3章]] 的核心考点设计，共 30 题，分**填空、选择、计算、证明**四类。重点训练二重积分（直角/极坐标）、积分次序交换、三重积分（直角/柱/球）、几何与物理应用。所有解答以 `<details>` 折叠，建议先独立完成再展开核对。

## 一、填空题（6题）

**1.** 极坐标变换 $x=r\cos\theta,\ y=r\sin\theta$ 的雅可比行列式 $J=$ ____，面积元素 $dA=$ ____。

<details><summary>答案</summary>

$$J=r,\qquad dA=r\,dr\,d\theta.$$

</details>

**2.** 交换积分次序：$\displaystyle\int_0^1 dx\int_x^1 f(x,y)\,dy=$ ____。

<details><summary>答案</summary>

积分区域 $D=\{0\le x\le 1,\ x\le y\le 1\}$，等价于 $\{0\le y\le 1,\ 0\le x\le y\}$，故

$$\int_0^1 dx\int_x^1 f\,dy=\int_0^1 dy\int_0^y f\,dx.$$

</details>

**3.** 球坐标变换 $x=\rho\sin\varphi\cos\theta,\ y=\rho\sin\varphi\sin\theta,\ z=\rho\cos\varphi$ 的体积元素 $dV=$ ____。

<details><summary>答案</summary>

$$dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.$$

</details>

**4.** 心形线 $r=a(1+\cos\theta)$ 所围区域面积 $A=$ ____。

<details><summary>答案</summary>

$$A=\frac{1}{2}\int_0^{2\pi} r^2\,d\theta=\frac{a^2}{2}\int_0^{2\pi}(1+\cos\theta)^2 d\theta=\frac{a^2}{2}(2\pi+0+\pi)=\frac{3\pi a^2}{2}.$$

</details>

**5.** 球体 $x^2+y^2+z^2\le R^2$ 的体积 $V=$ ____。

<details><summary>答案</summary>

$$V=\frac{4\pi R^3}{3}.$$

</details>

**6.** $\displaystyle\iint_{x^2+y^2\le R^2}(x^2+y^2)\,dA=$ ____。

<details><summary>答案</summary>

用极坐标：$\displaystyle\int_0^{2\pi}d\theta\int_0^R r^2\cdot r\,dr=2\pi\cdot\frac{R^4}{4}=\frac{\pi R^4}{2}.$

</details>

## 二、选择题（6题）

**7.** 关于累次积分 $\displaystyle\int_a^b dx\int_{y_1(x)}^{y_2(x)} f\,dy$ 的下列说法正确的是：
- A. $y_1(x),y_2(x)$ 必须是常数
- B. $y_1(x),y_2(x)$ 是 $x$ 的函数且 $a,b$ 是常数
- C. $a$ 可以是 $y$ 的函数
- D. 内层积分限与外层变量无关

<details><summary>答案</summary>

**B**。外层积分限必须是常数，内层积分限是外层变量的函数。

</details>

**8.** 三重积分 $\iiint_\Omega f\,dV$，$\Omega$ 是球 $x^2+y^2+z^2\le R^2$，最合适的坐标系是：
- A. 直角坐标
- B. 球坐标
- C. 柱坐标
- D. 任意皆可

<details><summary>答案</summary>

**B**。球对称区域用球坐标，体积元素 $\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$ 最简。

</details>

**9.** 曲面 $z=z(x,y)$ 在 $D_{xy}$ 上的曲面面积公式为：
- A. $\iint_{D_{xy}}\sqrt{1+z_x^2+z_y^2}\,dxdy$
- B. $\iint_{D_{xy}}\sqrt{1+z_x^2}\,dxdy$
- C. $\iint_{D_{xy}}\sqrt{z_x^2+z_y^2}\,dxdy$
- D. $\iint_{D_{xy}}\frac{1}{\sqrt{1+z_x^2+z_y^2}}\,dxdy$

<details><summary>答案</summary>

**A**。法向量与 $z$ 轴夹角余弦 $\cos\gamma=\frac{1}{\sqrt{1+z_x^2+z_y^2}}$，$dS=\frac{dxdy}{\cos\gamma}$。

</details>

**10.** 交换积分次序时，下列哪一步是必须的：
- A. 仅交换 $dx,dy$ 顺序
- B. 仅调整上下限符号
- C. 还原积分区域并重新分型
- D. 利用对称性直接互换

<details><summary>答案</summary>

**C**。必须先由累次积分还原区域 $D$，再按新次序重新判断 X型/Y型并写出新的积分限。

</details>

**11.** 二重积分中值定理 $\iint_D f\,dA=f(\xi,\eta)\cdot m(D)$ 成立的充分条件是：
- A. $f$ 在 $D$ 上可积
- B. $f$ 在有界闭**连通**区域 $D$ 上连续
- C. $D$ 是矩形
- D. $f$ 非负

<details><summary>答案</summary>

**B**。需要 $f$ 连续（保证取得最值与介值）且 $D$ 连通（保证介值定理成立）。

</details>

**12.** 设 $\Omega$ 关于 $yOz$ 面对称，$f$ 关于 $x$ 是奇函数，则 $\iiint_\Omega f\,dV=$ ____。
- A. $0$
- B. $2\iiint_{\Omega/2} f\,dV$
- C. $\iiint_\Omega f\,dV$
- D. 不确定

<details><summary>答案</summary>

**A**。奇函数在对称区域上积分为零。

</details>

## 三、计算题（12题）

**13.** 计算 $\displaystyle I=\iint_D xy\,dA$，$D$ 由 $y=x,\ y=x^2$ 围成。

<details><summary>解答</summary>

交点：$x=x^2\Rightarrow x=0,1$。X型 $D=\{0\le x\le 1,\ x^2\le y\le x\}$：

$$I=\int_0^1 x\,dx\int_{x^2}^x y\,dy=\int_0^1 x\cdot\frac{x^2-x^4}{2}\,dx=\frac{1}{2}\int_0^1(x^3-x^5)\,dx=\frac{1}{2}\left(\frac{1}{4}-\frac{1}{6}\right)=\frac{1}{24}.$$

</details>

**14.** 计算 $\displaystyle I=\int_0^1 dy\int_y^1 \frac{\sin x}{x}\,dx$。

<details><summary>解答</summary>

$\int\frac{\sin x}{x}\,dx$ 无初等原函数，交换次序。$D=\{0\le y\le 1,\ y\le x\le 1\}$，即 $\{0\le x\le 1,\ 0\le y\le x\}$：

$$I=\int_0^1 dx\int_0^x\frac{\sin x}{x}\,dy=\int_0^1\sin x\,dx=1-\cos 1.$$

</details>

**15.** 计算 $\displaystyle I=\iint_D (x^2+y^2)\,dA$，$D=\{x^2+y^2\le 2x\}$。

<details><summary>解答</summary>

$D$ 即 $(x-1)^2+y^2\le 1$，圆心 $(1,0)$ 半径 1。极坐标下边界 $r=2\cos\theta,\ \theta\in[-\pi/2,\pi/2]$：

$$I=\int_{-\pi/2}^{\pi/2}d\theta\int_0^{2\cos\theta} r^2\cdot r\,dr=\int_{-\pi/2}^{\pi/2}\frac{(2\cos\theta)^4}{4}\,d\theta=4\int_{-\pi/2}^{\pi/2}\cos^4\theta\,d\theta.$$

由 $\int_{-\pi/2}^{\pi/2}\cos^4\theta\,d\theta=2\int_0^{\pi/2}\cos^4\theta\,d\theta=2\cdot\frac{3\pi}{16}=\frac{3\pi}{8}$，故 $I=4\cdot\frac{3\pi}{8}=\frac{3\pi}{2}$。

</details>

**16.** 计算 $\displaystyle I=\iint_{1\le x^2+y^2\le 4}\frac{1}{\sqrt{x^2+y^2}}\,dA$。

<details><summary>解答</summary>

圆环，用极坐标，$r\in[1,2],\theta\in[0,2\pi]$：

$$I=\int_0^{2\pi}d\theta\int_1^2\frac{1}{r}\cdot r\,dr=2\pi\cdot 1=2\pi.$$

</details>

**17.** 计算 $\displaystyle I=\iiint_{[0,1]^3} xyz\,dV$。

<details><summary>解答</summary>

变量已分离：

$$I=\int_0^1 x\,dx\cdot\int_0^1 y\,dy\cdot\int_0^1 z\,dz=\frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{8}.$$

</details>

**18.** 计算 $\displaystyle I=\iiint_\Omega (x^2+y^2)\,dV$，$\Omega$ 由 $z=\sqrt{x^2+y^2}$ 与 $z=1$ 围成。

<details><summary>解答</summary>

圆锥，用柱坐标。$\Omega$ 投影 $x^2+y^2\le 1$，$r\in[0,1],z\in[r,1],\theta\in[0,2\pi]$：

$$I=\int_0^{2\pi}d\theta\int_0^1 r\,dr\int_r^1 r^2\,dz=2\pi\int_0^1 r^3(1-r)\,dr=2\pi\left(\frac{1}{4}-\frac{1}{5}\right)=\frac{\pi}{10}.$$

</details>

**19.** 计算 $\displaystyle I=\iiint_\Omega (x^2+y^2+z^2)\,dV$，$\Omega=\{x^2+y^2+z^2\le R^2\}$。

<details><summary>解答</summary>

球对称用球坐标，$\rho\in[0,R],\varphi\in[0,\pi],\theta\in[0,2\pi]$：

$$I=\int_0^{2\pi}d\theta\int_0^\pi d\varphi\int_0^R\rho^2\cdot\rho^2\sin\varphi\,d\rho=2\pi\cdot 2\cdot\frac{R^5}{5}=\frac{4\pi R^5}{5}.$$

</details>

**20.** 计算 $\displaystyle I=\iiint_\Omega z^2\,dV$，$\Omega=\{x^2+y^2+z^2\le R^2\}$。

<details><summary>解答</summary>

被积函数仅含 $z$，用先二后一。截面 $D_z=\{x^2+y^2\le R^2-z^2\}$，面积 $\pi(R^2-z^2)$：

$$I=\int_{-R}^R z^2\pi(R^2-z^2)\,dz=2\pi\left[\frac{R^2 z^3}{3}-\frac{z^5}{5}\right]_0^R=2\pi R^5\left(\frac{1}{3}-\frac{1}{5}\right)=\frac{4\pi R^5}{15}.$$

</details>

**21.** 求旋转抛物面 $z=x^2+y^2$ 在 $x^2+y^2\le 1$ 上的曲面面积。

<details><summary>解答</summary>

$z_x=2x,\ z_y=2y$，$1+z_x^2+z_y^2=1+4(x^2+y^2)=1+4r^2$。极坐标：

$$A=\int_0^{2\pi}d\theta\int_0^1\sqrt{1+4r^2}\cdot r\,dr=2\pi\cdot\frac{1}{12}(1+4r^2)^{3/2}\Big|_0^1=\frac{\pi}{6}(5\sqrt{5}-1).$$

</details>

**22.** 求由 $z=x^2+y^2$ 与 $z=1$ 围成的立体体积。

<details><summary>解答</summary>

投影 $D=\{x^2+y^2\le 1\}$，体积 $V=\iint_D(1-x^2-y^2)\,dA$，极坐标：

$$V=\int_0^{2\pi}d\theta\int_0^1(1-r^2)r\,dr=2\pi\left(\frac{1}{2}-\frac{1}{4}\right)=\frac{\pi}{2}.$$

</details>

**23.** 求均匀圆锥体 $\Omega=\{z\ge\sqrt{x^2+y^2},\ z\le 1\}$ 的质心。

<details><summary>解答</summary>

由对称性 $\bar x=\bar y=0$。体积 $V=\frac{\pi}{3}$（圆锥体积）。计算 $\iiint_\Omega z\,dV$，用柱坐标 $r\in[0,1],z\in[r,1],\theta\in[0,2\pi]$：

$$\iiint_\Omega z\,dV=\int_0^{2\pi}d\theta\int_0^1 r\,dr\int_r^1 z\,dz=2\pi\int_0^1 r\cdot\frac{1-r^2}{2}\,dr=\pi\left(\frac{1}{2}-\frac{1}{4}\right)=\frac{\pi}{4}.$$

故 $\bar z=\frac{\pi/4}{\pi/3}=\frac{3}{4}$，质心 $(0,0,\frac{3}{4})$。

</details>

**24.** 求均匀圆柱体 $\Omega=\{x^2+y^2\le R^2,\ 0\le z\le h\}$（密度 $\rho$）对 $z$ 轴的转动惯量 $I_z$，并用质量 $m$ 表示。

<details><summary>解答</summary>

$I_z=\iiint_\Omega(x^2+y^2)\rho\,dV$，柱坐标：

$$I_z=\rho\int_0^{2\pi}d\theta\int_0^R r\,dr\int_0^h r^2\,dz=\rho\cdot 2\pi\cdot\frac{R^4}{4}\cdot h=\frac{\rho\pi R^4 h}{2}.$$

由 $m=\rho\pi R^2 h$，故 $I_z=\frac{1}{2}mR^2$。

</details>

## 四、证明题（6题）

**25.** 设 $f$ 在 $D$ 上连续，$D$ 关于 $y$ 轴对称。证明：若 $f$ 关于 $x$ 是奇函数，则 $\iint_D f\,dA=0$；若关于 $x$ 是偶函数，则 $\iint_D f\,dA=2\iint_{D/2} f\,dA$。

<details><summary>证明</summary>

设 $D^+=D\cap\{x\ge 0\}$，$D^-=D\cap\{x\le 0\}$。由 $D$ 关于 $y$ 轴对称，$(x,y)\in D^+\Leftrightarrow(-x,y)\in D^-$。作变量代换 $x\to -x$：

$$\iint_{D^-} f(x,y)\,dA=\iint_{D^+} f(-u,y)\,dud y.$$

若 $f$ 关于 $x$ 奇：$f(-u,y)=-f(u,y)$，故 $\iint_{D^-} f=-\iint_{D^+} f$，从而 $\iint_D f=\iint_{D^+}f+\iint_{D^-}f=0$。

若 $f$ 关于 $x$ 偶：$f(-u,y)=f(u,y)$，故 $\iint_{D^-}f=\iint_{D^+}f$，从而 $\iint_D f=2\iint_{D^+}f$。$\square$

</details>

**26.** 设 $f$ 在 $D=[0,1]^2$ 上连续，$0\le f\le 1$。证明：$0\le\iint_D f\,dA\le 1$。

<details><summary>证明</summary>

由估值不等式（[[3.1 二重积分定义与性质#四、二重积分的性质|保号性]]）：$0\le f\le 1\Rightarrow\iint_D 0\,dA\le\iint_D f\,dA\le\iint_D 1\,dA=1\cdot m(D)=1$。$\square$

</details>

**27.** 设 $f$ 在有界闭区域 $D$ 上连续，求 $\displaystyle\lim_{r\to 0}\frac{1}{\pi r^2}\iint_{D\cap B_r(x_0,y_0)} f\,dA$，其中 $(x_0,y_0)\in D$。并证明结论。

<details><summary>证明</summary>

由积分中值定理（[[3.1 二重积分定义与性质#四、二重积分的性质]]），存在 $(\xi,\eta)\in D\cap B_r(x_0,y_0)$ 使

$$\frac{1}{\pi r^2}\iint_{D\cap B_r}f\,dA=f(\xi,\eta)\cdot\frac{m(D\cap B_r)}{\pi r^2}.$$

当 $(x_0,y_0)$ 是 $D$ 内点时，$r$ 充分小后 $B_r\subset D$，$m(D\cap B_r)=\pi r^2$，故上式 $=f(\xi,\eta)$。又 $(\xi,\eta)\to(x_0,y_0)$（$r\to 0$），由 $f$ 连续得极限 $=f(x_0,y_0)$。$\square$

</details>

**28.** 设 $\Omega$ 关于原点中心对称（即 $(x,y,z)\in\Omega\Leftrightarrow(-x,-y,-z)\in\Omega$），$f$ 关于 $(x,y,z)$ 是奇函数（$f(-x,-y,-z)=-f(x,y,z)$）。证明 $\iiint_\Omega f\,dV=0$。

<details><summary>证明</summary>

将 $\Omega$ 分成两半 $\Omega^+,\Omega^-$，由中心对称存在一一对应 $(x,y,z)\leftrightarrow(-x,-y,-z)$。作变换 $u=-x,v=-y,w=-z$，雅可比 $|J|=1$：

$$\iiint_{\Omega^-}f(x,y,z)\,dV=\iiint_{\Omega^+}f(-u,-v,-w)\,dudvdw=-\iiint_{\Omega^+}f\,dV.$$

故 $\iiint_\Omega f=\iiint_{\Omega^+}f+\iiint_{\Omega^-}f=0$。$\square$

</details>

**29.** 用先二后一（切片法）证明球体 $x^2+y^2+z^2\le R^2$ 的体积公式 $V=\frac{4\pi R^3}{3}$。

<details><summary>证明</summary>

$V=\iiint_\Omega dV$。对每个 $z\in[-R,R]$，水平截面 $D_z=\{x^2+y^2\le R^2-z^2\}$，面积 $\pi(R^2-z^2)$：

$$V=\int_{-R}^R\pi(R^2-z^2)\,dz=\pi\left[R^2 z-\frac{z^3}{3}\right]_{-R}^R=\pi\left(2R^3-\frac{2R^3}{3}\right)=\frac{4\pi R^3}{3}.\ \square$$

</details>

**30.** 证明 Poisson 积分 $\displaystyle\iiint_{\mathbb{R}^3}e^{-(x^2+y^2+z^2)}\,dV=\pi^{3/2}$，并由此推导 $\int_{-\infty}^{+\infty}e^{-x^2}dx=\sqrt{\pi}$。

<details><summary>证明</summary>

用球坐标，$\rho\in[0,+\infty),\varphi\in[0,\pi],\theta\in[0,2\pi]$：

$$\iiint_{\mathbb{R}^3}e^{-\rho^2}\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta=\left(\int_0^{2\pi}d\theta\right)\left(\int_0^\pi\sin\varphi\,d\varphi\right)\left(\int_0^{+\infty}\rho^2 e^{-\rho^2}\,d\rho\right).$$

前两个因子 $=2\pi\cdot 2=4\pi$。第三个用分部积分 $\int_0^{+\infty}\rho^2 e^{-\rho^2}d\rho=\frac{\sqrt{\pi}}{4}$（由 $\int_{-\infty}^{+\infty}e^{-t^2}dt=\sqrt{\pi}$ 与 $\int_0^{+\infty}\rho^2 e^{-\rho^2}d\rho=\frac{1}{2}\Gamma(3/2)=\frac{\sqrt{\pi}}{4}$）。但更直接：由 Fubini 与独立性

$$\iiint_{\mathbb{R}^3}e^{-(x^2+y^2+z^2)}\,dV=\left(\int_{-\infty}^{+\infty}e^{-x^2}dx\right)^3.$$

由 3.3 节例1 $\iint_{\mathbb{R}^2}e^{-(x^2+y^2)}dA=\pi$，故 $\left(\int_{-\infty}^{+\infty}e^{-x^2}dx\right)^2=\pi$，从而 $\int_{-\infty}^{+\infty}e^{-x^2}dx=\sqrt{\pi}$。同理三维 $\iiint=\pi^{3/2}$。$\square$

</details>

## 考点统计

| 考点 | 题号 | 难度 |
| ---- | ---- | ---- |
| 极坐标变换与雅可比 | 1, 6, 15, 16 | ★—★★ |
| 积分次序交换 | 2, 14 | ★★ |
| 球坐标体积元素 | 3, 19 | ★—★★ |
| 极坐标几何应用 | 4 | ★★ |
| 球体积公式 | 5, 29 | ★—★★ |
| 累次积分基本概念 | 7, 11 | ★ |
| 坐标系选择 | 8 | ★ |
| 曲面面积公式 | 9, 21 | ★★ |
| 交换次序的方法 | 10 | ★ |
| 奇偶对称性 | 12, 25, 28 | ★★—★★★ |
| 直角坐标计算 | 13, 17 | ★ |
| 估值与中值定理 | 26, 27 | ★★★ |
| 柱坐标三重积分 | 18, 23, 24 | ★★ |
| 球坐标三重积分 | 19 | ★★ |
| 先二后一 | 20, 29 | ★★ |
| 曲面面积综合 | 21 | ★★★ |
| 立体体积 | 22 | ★★ |
| 质心 | 23 | ★★ |
| 转动惯量 | 24 | ★★ |
| 证明题 | 25-30 | ★★—★★★ |

## 章节导航

- 返回：[[MOC - 第3章]]
- 上一章习题：[[MOC - 第2章习题]]
- 下一章习题：[[MOC - 第4章习题]]
- 知识点：[[3.1 二重积分定义与性质]]、[[3.2 直角坐标下二重积分计算]]、[[3.3 极坐标下二重积分计算]]、[[3.4 三重积分定义与性质]]、[[3.5 三重积分：直角坐标、柱坐标、球坐标]]、[[3.6 重积分几何应用与物理应用]]

#高等数学 #多元微积分 #习题 #重积分
