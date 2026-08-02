---
domain: 数学基础
subject: 高等数学A(2)
type: exercise
chapter: 第6章 常微分方程
tags: [高等数学,习题,一阶微分方程,二阶常系数线性微分方程]
prerequisites: ["高等数学A(1)"]
aliases: [第6章习题, 微分方程习题]
---

# MOC - 第6章习题

> [!info] 习题集定位
> 本习题集围绕 [[MOC - 第6章]] 的核心考点设计，共 28 题，分**填空、选择、计算、证明/应用**四类。重点训练可分离变量方程、一阶线性方程、齐次方程、可降阶方程、二阶常系数齐次/非齐次方程求解，以及微分方程建模应用。所有解答以 `<details>` 折叠，建议先独立完成再展开核对。

## 一、填空题（6题）

**1.** 微分方程 $(x^2+1)y'''+2y'-xy=0$ 的阶数是 ____，属于 ____（线性/非线性）、____（常系数/变系数）方程。

<details><summary>答案</summary>

阶数为 **3**（最高阶导数为 $y'''$）；**线性**（关于 $y,y',y'',y'''$ 一次）；**变系数**（系数 $x^2+1,0,-x,2$ 含 $x$）。

</details>

**2.** 一阶线性方程 $\dfrac{dy}{dx}+P(x)y=Q(x)$ 的通解公式为 $y=$ ____。

<details><summary>答案</summary>

$$y=e^{-\int P(x)\,dx}\left[\int Q(x)\,e^{\int P(x)\,dx}\,dx+C\right].$$

</details>

**3.** 微分方程 $y''-3y'+2y=0$ 的通解为 $y=$ ____。

<details><summary>答案</summary>

特征方程 $r^2-3r+2=0$，$r_1=1,r_2=2$，故 $y=C_1 e^x+C_2 e^{2x}$。

</details>

**4.** 微分方程 $y''+4y'+4y=0$ 的通解为 $y=$ ____。

<details><summary>答案</summary>

$r^2+4r+4=0$，$(r+2)^2=0$，$r=-2$（二重），$y=(C_1+C_2 x)e^{-2x}$。

</details>

**5.** 微分方程 $y''+2y'+5y=0$ 的通解为 $y=$ ____。

<details><summary>答案</summary>

$r^2+2r+5=0$，$\Delta=-16$，$r=-1\pm 2i$，$y=e^{-x}(C_1\cos 2x+C_2\sin 2x)$。

</details>

**6.** 设 $y_1=e^x,\ y_2=xe^x$ 都是某二阶齐次线性方程的解，则其特征根为 $r=$ ____（重数 ____）。

<details><summary>答案</summary>

由通解形式 $y=(C_1+C_2 x)e^x$ 知特征根 $r=1$ 是二重根。特征方程 $(r-1)^2=0$ 即 $r^2-2r+1=0$，对应方程 $y''-2y'+y=0$。

</details>

## 二、选择题（6题）

**7.** 下列方程中是一阶线性微分方程的是：
- A. $y'+y^2=e^x$
- B. $y'\sin x+y\cos x=\ln x$
- C. $yy'+x=0$
- D. $y'=e^{y/x}$

<details><summary>答案</summary>

**B**。$y'\sin x+y\cos x=\ln x$ 化为 $y'+(\cot x)y=\dfrac{\ln x}{\sin x}$，关于 $y,y'$ 一次且系数仅与 $x$ 有关，是一阶线性方程。A 含 $y^2$；C 含 $yy'$；D 含 $e^{y/x}$，都非线性。

</details>

**8.** 方程 $y''=f(x,y')$（缺 $y$）的换元是：
- A. 令 $p=y'$，$y''=p\,\dfrac{dp}{dy}$
- B. 令 $p=y'$，$y''=\dfrac{dp}{dx}$
- C. 令 $u=y/x$
- D. 直接积分两次

<details><summary>答案</summary>

**B**。缺 $y$ 时把 $p=y'$ 视为 $x$ 的函数，$y''=p'=\dfrac{dp}{dx}$，化为关于 $p(x)$ 的一阶方程。A 是缺 $x$ 情形；C 是齐次方程换元；D 是 $y''=f(x)$ 情形。

</details>

**9.** 设 $y_1,y_2$ 是齐次方程 $y''+p(x)y'+q(x)y=0$ 的解，则下列说法正确的是：
- A. $y_1+y_2$ 一定是通解
- B. $C_1 y_1+C_2 y_2$ 一定是通解
- C. 当 $W(y_1,y_2)\ne 0$ 时 $C_1 y_1+C_2 y_2$ 是通解
- D. 当 $y_1,y_2$ 线性相关时 $C_1 y_1+C_2 y_2$ 是通解

<details><summary>答案</summary>

**C**。由 [[6.4 二阶线性微分方程解的结构]] 的通解结构定理，$y_1,y_2$ 线性无关（$W\ne 0$）时 $C_1 y_1+C_2 y_2$ 才是通解。

</details>

**10.** 微分方程 $y''-2y'+5y=0$ 的通解是：
- A. $y=C_1 e^x+C_2 e^{5x}$
- B. $y=(C_1+C_2 x)e^x$
- C. $y=e^x(C_1\cos 2x+C_2\sin 2x)$
- D. $y=e^{2x}(C_1\cos x+C_2\sin x)$

<details><summary>答案</summary>

**C**。特征方程 $r^2-2r+5=0$，$\Delta=4-20=-16$，$r=1\pm 2i$，$\alpha=1,\beta=2$。

</details>

**11.** 求 $y''+y=\cos x$ 的特解时，应设 $y^*=$ ____（已知齐次特征根为 $\pm i$）：
- A. $a\cos x+b\sin x$
- B. $x(a\cos x+b\sin x)$
- C. $x^2(a\cos x+b\sin x)$
- D. $a\cos x$

<details><summary>答案</summary>

**B**。$f(x)=\cos x$ 即 $\lambda=0,\omega=1$，$\lambda\pm i\omega=\pm i$ 是单特征根，故 $k=1$，应设 $y^*=x(a\cos x+b\sin x)$。

</details>

**12.** 关于伯努利方程 $y'+P(x)y=Q(x)y^\alpha$（$\alpha\ne 0,1$）的换元，下列正确的是：
- A. 令 $z=y^{\alpha}$
- B. 令 $z=y^{1-\alpha}$
- C. 令 $z=y'$
- D. 令 $z=y/x$

<details><summary>答案</summary>

**B**。两边除 $y^\alpha$ 后令 $z=y^{1-\alpha}$，$z'=(1-\alpha)y^{-\alpha}y'$，原方程化为关于 $z$ 的一阶线性方程。

</details>

## 三、计算题（12题）

**13.** 求可分离变量方程 $\dfrac{dy}{dx}=\dfrac{1+y^2}{1+x^2}$ 的通解。

<details><summary>解答</summary>

分离变量 $\dfrac{dy}{1+y^2}=\dfrac{dx}{1+x^2}$，两边积分：

$$\arctan y=\arctan x+C\ \Rightarrow\ y=\tan(\arctan x+C).$$

亦可由 $\tan(A-B)=\dfrac{\tan A-\tan B}{1+\tan A\tan B}$ 改写为 $y=\dfrac{x+\tan C}{1-x\tan C}=\dfrac{x+C_1}{1-C_1 x}$（$C_1=\tan C$）。

</details>

**14.** 求齐次方程 $(x-y)dy-(x+y)dx=0$ 的通解。

<details><summary>解答</summary>

化为 $\dfrac{dy}{dx}=\dfrac{x+y}{x-y}=\dfrac{1+(y/x)}{1-(y/x)}=\varphi(y/x)$，是齐次方程。令 $u=y/x$，$y=ux$，$y'=u+xu'$：

$$u+xu'=\frac{1+u}{1-u}\ \Rightarrow\ x\frac{du}{dx}=\frac{1+u}{1-u}-u=\frac{1+u-u+u^2}{1-u}=\frac{1+u^2}{1-u}.$$

分离 $\dfrac{1-u}{1+u^2}du=\dfrac{dx}{x}$，积分：

$$\int\frac{du}{1+u^2}-\int\frac{u\,du}{1+u^2}=\ln|x|+C_1\ \Rightarrow\ \arctan u-\frac{1}{2}\ln(1+u^2)=\ln|x|+C_1.$$

回代 $u=y/x$：

$$\arctan\frac{y}{x}-\frac{1}{2}\ln\!\left(1+\frac{y^2}{x^2}\right)=\ln|x|+C_1.$$

</details>

**15.** 求一阶线性方程 $xy'-2y=x^3 e^x$ 的通解（$x\ne 0$）。

<details><summary>解答</summary>

化为标准形 $y'-\dfrac{2}{x}y=x^2 e^x$，$P=-\dfrac{2}{x},\ Q=x^2 e^x$。积分因子 $\mu=e^{\int-2/x\,dx}=x^{-2}$。两边乘 $\mu$：

$$(x^{-2}y)'=e^x\ \Rightarrow\ x^{-2}y=e^x+C\ \Rightarrow\ y=x^2(e^x+C)=x^2 e^x+Cx^2.$$

</details>

**16.** 求伯努利方程 $y'-\dfrac{2}{x}y=x^2 y^2$ 的通解。

<details><summary>解答</summary>

$\alpha=2$，两边除 $y^2$：$y^{-2}y'-\dfrac{2}{x}y^{-1}=x^2$。令 $z=y^{-1}$，$z'=-y^{-2}y'$，故 $-z'-\dfrac{2z}{x}=x^2$，即 $z'+\dfrac{2}{x}z=-x^2$。

套公式 $P=\dfrac{2}{x},\ Q=-x^2$，$\mu=e^{\int 2/x\,dx}=x^2$：

$$(x^2 z)'=-x^4\ \Rightarrow\ x^2 z=-\frac{x^5}{5}+C\ \Rightarrow\ z=-\frac{x^3}{5}+\frac{C}{x^2}.$$

回代 $z=1/y$：$y=\dfrac{1}{-x^3/5+C/x^2}=\dfrac{5x^2}{C\cdot 5-x^5}=\dfrac{5x^2}{5C-x^5}$。又 $y\equiv 0$ 也是解。

</details>

**17.** 求可降阶方程 $y''=\dfrac{1}{x}y'$ 的通解。

<details><summary>解答</summary>

缺 $y$，令 $p=y'$，$y''=p'$：$p'=\dfrac{p}{x}$，分离 $\dfrac{dp}{p}=\dfrac{dx}{x}$，$\ln|p|=\ln|x|+C_1$，$p=C_1 x$。再积分 $y=\dfrac{C_1}{2}x^2+C_2$，改写常数：$y=C_1 x^2+C_2$。

</details>

**18.** 求 $y''=2yy'$ 满足 $y(0)=1,\ y'(0)=2$ 的特解。

<details><summary>解答</summary>

缺 $x$，令 $p=y'$，$y''=p\,dp/dy$：$p\,dp/dy=2yp$，即 $p(dp/dy-2y)=0$。

由 $y'(0)=2\ne 0$ 知 $p\ne 0$（局部），故 $dp/dy=2y$，$p=y^2+C_1$。由 $y(0)=1,y'(0)=2$：$2=1+C_1$，$C_1=1$，$p=y^2+1$。

再解 $y'/(y^2+1)=1$，$\arctan y=x+C_2$。由 $y(0)=1$：$C_2=\arctan 1=\dfrac{\pi}{4}$。故 $y=\tan\!\left(x+\dfrac{\pi}{4}\right)$。

</details>

**19.** 求 $y''-4y'+3y=0$ 满足 $y(0)=6,\ y'(0)=10$ 的特解。

<details><summary>解答</summary>

特征方程 $r^2-4r+3=0$，$r_1=1,r_2=3$。通解 $y=C_1 e^x+C_2 e^{3x}$，$y'=C_1 e^x+3C_2 e^{3x}$。

由 $y(0)=C_1+C_2=6$；$y'(0)=C_1+3C_2=10$。解得 $C_2=2,\ C_1=4$。故 $y=4e^x+2e^{3x}$。

</details>

**20.** 求 $y''+4y'+4y=e^{-2x}$ 的通解。

<details><summary>解答</summary>

**(1)** 齐次特征方程 $r^2+4r+4=0$，$(r+2)^2=0$，$r=-2$（二重）。$Y=(C_1+C_2 x)e^{-2x}$。

**(2)** $f(x)=e^{-2x}$，$\lambda=-2$ 是二重特征根，$k=2$。设 $y^*=x^2 A e^{-2x}=A x^2 e^{-2x}$。

求导：$y^{*\prime}=A(2x-2x^2)e^{-2x}$，$y^{*\prime\prime}=A(2-8x+4x^2)e^{-2x}$。代入 $y''+4y'+4y=e^{-2x}$：

$$A[(2-8x+4x^2)+4(2x-2x^2)+4x^2]e^{-2x}=e^{-2x},$$

化简得 $A\cdot 2=1$，$A=\dfrac{1}{2}$。故 $y^*=\dfrac{1}{2}x^2 e^{-2x}$。

**(3)** 通解 $y=(C_1+C_2 x)e^{-2x}+\dfrac{1}{2}x^2 e^{-2x}=\left(C_1+C_2 x+\dfrac{x^2}{2}\right)e^{-2x}$。

</details>

**21.** 求 $y''+y=\sin 2x$ 的通解。

<details><summary>解答</summary>

**(1)** 齐次特征方程 $r^2+1=0$，$r=\pm i$。$Y=C_1\cos x+C_2\sin x$。

**(2)** $f(x)=\sin 2x$，$\lambda=0,\omega=2$，$\lambda\pm i\omega=\pm 2i$ 不是特征根 $\pm i$，$k=0$。设 $y^*=a\cos 2x+b\sin 2x$。

$y^{*\prime}=-2a\sin 2x+2b\cos 2x$，$y^{*\prime\prime}=-4a\cos 2x-4b\sin 2x$。代入 $y''+y=\sin 2x$：

$$(-4a+a)\cos 2x+(-4b+b)\sin 2x=\sin 2x\ \Rightarrow\ -3a=0,\ -3b=1.$$

$a=0,\ b=-\dfrac{1}{3}$，$y^*=-\dfrac{1}{3}\sin 2x$。

**(3)** 通解 $y=C_1\cos x+C_2\sin x-\dfrac{1}{3}\sin 2x$。

</details>

**22.** 求 $y''-2y'-3y=3x+1$ 的通解。

<details><summary>解答</summary>

**(1)** 齐次特征方程 $r^2-2r-3=0$，$(r-3)(r+1)=0$，$r_1=3,r_2=-1$。$Y=C_1 e^{3x}+C_2 e^{-x}$。

**(2)** $f(x)=3x+1=e^{0\cdot x}(3x+1)$，$\lambda=0$ 不是特征根，$k=0$，$m=1$。设 $y^*=Ax+B$。

$y^{*\prime}=A$，$y^{*\prime\prime}=0$。代入 $y''-2y'-3y=3x+1$：$-2A-3(Ax+B)=3x+1$，即 $-3Ax+(-2A-3B)=3x+1$。

比较系数：$-3A=3\Rightarrow A=-1$；$-2A-3B=1\Rightarrow 2-3B=1\Rightarrow B=\dfrac{1}{3}$。$y^*=-x+\dfrac{1}{3}$。

**(3)** 通解 $y=C_1 e^{3x}+C_2 e^{-x}-x+\dfrac{1}{3}$。

</details>

**23.** 求 $y''+y=e^x+\cos x$ 的通解。

<details><summary>解答</summary>

由 [[6.4 二阶线性微分方程解的结构#四、解的叠加原理|叠加原理]]，分别求 $f_1=e^x$ 与 $f_2=\cos x$ 的特解。

**(1)** 齐次通解 $Y=C_1\cos x+C_2\sin x$。

**(2)** $f_1=e^x$：$\lambda=1$ 不是特征根 $\pm i$，$k=0$。设 $y_1^*=Ae^x$，$y_1^{*\prime\prime}=Ae^x$，代入 $y''+y=e^x$ 得 $2Ae^x=e^x$，$A=\dfrac{1}{2}$。$y_1^*=\dfrac{1}{2}e^x$。

**(3)** $f_2=\cos x$：$\lambda=0,\omega=1$，$\lambda\pm i\omega=\pm i$ 是单特征根，$k=1$。设 $y_2^*=x(a\cos x+b\sin x)$。由 [[6.6 二阶常系数非齐次线性微分方程#五、典型例题|例3]] 类似计算：$y_2^{*\prime\prime}+y_2^*=2b\cos x-2a\sin x=\cos x$，故 $a=0,b=\dfrac{1}{2}$。$y_2^*=\dfrac{1}{2}x\sin x$。

**(4)** 通解 $y=C_1\cos x+C_2\sin x+\dfrac{1}{2}e^x+\dfrac{1}{2}x\sin x$。

</details>

**24.** 求初值问题 $y''+y=x,\ y(0)=1,\ y'(0)=0$ 的特解。

<details><summary>解答</summary>

**(1)** 齐次通解 $Y=C_1\cos x+C_2\sin x$。

**(2)** $f(x)=x$，$\lambda=0$ 不是特征根 $\pm i$，$k=0$，$m=1$。设 $y^*=Ax+B$，$y^{*\prime\prime}=0$，代入 $y''+y=x$：$Ax+B=x$，$A=1,B=0$。$y^*=x$。

**(3)** 通解 $y=C_1\cos x+C_2\sin x+x$，$y'=-C_1\sin x+C_2\cos x+1$。

由 $y(0)=C_1=1$；$y'(0)=C_2+1=0\Rightarrow C_2=-1$。故 $y=\cos x-\sin x+x$。

</details>

## 四、证明题与应用题（4题）

**25.** 设 $y_1=e^{r_1 x},\ y_2=e^{r_2 x}$ 是 $y''+py'+qy=0$ 的两个解，$r_1\ne r_2$。证明 $y_1,y_2$ 线性无关，并由此写出通解。

<details><summary>证明</summary>

由 $r_i$ 是特征方程 $r^2+pr+q=0$ 的根直接验证 $y_i''+py_i'+qy_i=e^{r_i x}(r_i^2+pr_i+q)=0$，$i=1,2$。

计算朗斯基行列式（[[6.4 二阶线性微分方程解的结构]]）：

$$W(y_1,y_2)=\begin{vmatrix}e^{r_1 x}&e^{r_2 x}\\ r_1 e^{r_1 x}&r_2 e^{r_2 x}\end{vmatrix}=e^{r_1 x}\cdot r_2 e^{r_2 x}-r_1 e^{r_1 x}\cdot e^{r_2 x}=(r_2-r_1)e^{(r_1+r_2)x}.$$

由 $r_1\ne r_2$ 知 $r_2-r_1\ne 0$，又 $e^{(r_1+r_2)x}\ne 0$，故 $W\ne 0$，$y_1,y_2$ 线性无关。由 [[6.4 二阶线性微分方程解的结构#三、齐次方程通解结构|通解结构定理]]，通解为 $y=C_1 e^{r_1 x}+C_2 e^{r_2 x}$。$\square$

</details>

**26.**（解的结构）设 $y^*$ 是 $y''+p(x)y'+q(x)y=f(x)$ 的特解，$Y$ 是对应齐次方程的通解。证明：$y=Y+y^*$ 是非齐次方程的通解。

<details><summary>证明</summary>

设 $L[y]=y''+p(x)y'+q(x)y$。由 $L$ 的线性性（[[6.4 二阶线性微分方程解的结构#四、解的叠加原理|叠加原理]]）：

$$L[Y+y^*]=L[Y]+L[y^*]=0+f(x)=f(x),$$

故 $Y+y^*$ 是非齐次方程的解。

下证"通"：设 $\tilde y$ 是非齐次方程任一解，则

$$L[\tilde y-y^*]=L[\tilde y]-L[y^*]=f-f=0,$$

故 $\tilde y-y^*$ 是齐次方程的解。由 $Y$ 是齐次通解知存在常数 $C_1,C_2$ 使 $\tilde y-y^*=C_1 y_1+C_2 y_2$，即 $\tilde y=Y+y^*$。因此任一非齐次解都形如 $Y+y^*$，通解得证。$\square$

</details>

**27.**（应用题：放射性衰变）放射性物质的质量 $M(t)$ 的衰变速度与现存量成正比，比例系数 $k>0$。已知初始质量 $M(0)=M_0$，半衰期为 $T$（即 $M(T)=M_0/2$）。求 $M(t)$ 与 $T$ 的关系。

<details><summary>解答</summary>

由题意 $\dfrac{dM}{dt}=-kM$（负号表示减少）。分离变量 $\dfrac{dM}{M}=-k\,dt$，积分 $\ln|M|=-kt+C_1$，$M=Ce^{-kt}$。

由 $M(0)=M_0$：$C=M_0$，$M(t)=M_0 e^{-kt}$。

由半衰期 $M(T)=\dfrac{M_0}{2}$：$M_0 e^{-kT}=\dfrac{M_0}{2}$，$e^{-kT}=\dfrac{1}{2}$，$kT=\ln 2$，故

$$\boxed{T=\frac{\ln 2}{k},\qquad M(t)=M_0 e^{-kt}=M_0\cdot 2^{-t/T}.}$$

即半衰期 $T$ 与衰变常数 $k$ 成反比，且与初始质量无关。

</details>

**28.**（应用题：受迫振动）设弹簧—质点系统的运动方程为
$$y''+4y=\sin 2t,$$
初始条件 $y(0)=0,\ y'(0)=0$。求解并说明其物理意义。

<details><summary>解答</summary>

**(1)** 齐次特征方程 $r^2+4=0$，$r=\pm 2i$，$\alpha=0,\beta=2$。齐次通解 $Y=C_1\cos 2t+C_2\sin 2t$。

**(2)** $f(t)=\sin 2t$，$\lambda=0,\omega=2$，$\lambda\pm i\omega=\pm 2i$ 是单特征根，$k=1$。设 $y^*=t(a\cos 2t+b\sin 2t)$。

求导：$y^{*\prime}=a\cos 2t+b\sin 2t+t(-2a\sin 2t+2b\cos 2t)$，
$$y^{*\prime\prime}=-4a\sin 2t+4b\cos 2t+t(-4a\cos 2t-4b\sin 2t).$$

代入 $y''+4y=\sin 2t$：$y^{*\prime\prime}+4y^*=-4a\sin 2t+4b\cos 2t=\sin 2t$。

故 $-4a=1,\ 4b=0$，$a=-\dfrac{1}{4},\ b=0$。$y^*=-\dfrac{1}{4}t\cos 2t$。

**(3)** 通解 $y=C_1\cos 2t+C_2\sin 2t-\dfrac{1}{4}t\cos 2t$。

由 $y(0)=C_1=0$；$y'=2C_2\cos 2t-\dfrac{1}{4}\cos 2t+\dfrac{1}{2}t\sin 2t$，$y'(0)=2C_2-\dfrac{1}{4}=0$，$C_2=\dfrac{1}{8}$。故

$$\boxed{y=\frac{1}{8}\sin 2t-\frac{1}{4}t\cos 2t.}$$

**物理意义**：外力频率 $\omega=2$ 等于系统固有频率 $\beta=2$，发生**共振**。特解中 $t\cos 2t$ 项振幅随时间线性增长，理论上无限增大；实际系统中阻尼会限制振幅。这正是 $\lambda\pm i\omega$ 等于特征根导致 $k=1$ 的物理表现（[[6.6 二阶常系数非齐次线性微分方程]]）。

</details>

## 考点统计

| 考点 | 题号 | 难度 |
| ---- | ---- | ---- |
| 微分方程基本概念 | 1, 7 | ★ |
| 一阶线性通解公式 | 2, 15 | ★—★★ |
| 二阶常系数齐次三种情形 | 3, 4, 5, 6, 10, 19 | ★—★★ |
| 齐次通解结构 / 线性无关 | 9, 25 | ★★ |
| 可分离变量方程 | 13 | ★★ |
| 齐次方程换元 | 14 | ★★ |
| 一阶线性方程求解 | 15 | ★★ |
| 伯努利方程 | 12, 16 | ★★—★★★ |
| 可降阶方程（缺 $y$） | 8, 17 | ★★ |
| 可降阶方程（缺 $x$） | 18 | ★★★ |
| 待定系数法类型一 | 20, 22 | ★★—★★★ |
| 待定系数法类型二 | 11, 21 | ★★—★★★ |
| 叠加原理 | 23 | ★★★ |
| 解的结构证明 | 25, 26 | ★★—★★★ |
| 应用题（衰变） | 27 | ★★ |
| 应用题（共振） | 28 | ★★★ |
| 初值问题 | 18, 19, 24, 28 | ★★—★★★ |

## 章节导航

- 返回：[[MOC - 第6章]]
- 上一章习题：[[MOC - 第5章习题]]
- 知识点：[[6.1 微分方程基本概念]]、[[6.2 一阶微分方程]]、[[6.3 可降阶的高阶微分方程]]、[[6.4 二阶线性微分方程解的结构]]、[[6.5 二阶常系数齐次线性微分方程]]、[[6.6 二阶常系数非齐次线性微分方程]]

#高等数学 #习题 #微分方程 #一阶微分方程 #二阶常系数线性微分方程
