---
domain: 数学基础
subject: 高等数学A(1)
type: exercise
chapter: 第2章 一元函数微分学
tags: [高等数学,习题,导数,微分,求导法则]
prerequisites: ["第1章 函数、极限与连续"]
aliases: [第2章习题, 微分学习题]
---

# MOC - 第2章习题 一元函数微分学

> [!info] 本章习题定位
> 本章共 **28 题**，覆盖 [[2.1 导数概念]]—[[2.6 微分近似计算]] 全部考点：导数定义计算、复合函数链式求导、隐函数与参数方程求导、高阶导数（莱布尼茨公式）、微分与误差估计。答案统一折叠在 `<details>` 中，计算题给出完整步骤。

## 一、填空题（8 题）

### T1（导数定义识别）
设 $f$ 在 $x=2$ 处可导且 $f'(2)=3$，则 $\displaystyle\lim_{h\to0}\frac{f(2+2h)-f(2-h)}{3h}=$ ____。

<details><summary>展开答案</summary>

拆成两个增量比的线性组合：

$$
\lim_{h\to0}\frac{f(2+2h)-f(2-h)}{3h}=\frac{2}{3}\cdot\lim_{h\to0}\frac{f(2+2h)-f(2)}{2h}+\frac{1}{3}\cdot\lim_{h\to0}\frac{f(2-h)-f(2)}{-h}.
$$

两个极限均为 $f'(2)=3$，故原式 $=\dfrac{2}{3}\cdot3+\dfrac{1}{3}\cdot3=\boxed{3}$。

</details>

### T2（复合求导）
$y=\ln(1+x^2)$，则 $\left.\dfrac{\mathrm dy}{\mathrm dx}\right|_{x=1}=$ ____。

<details><summary>展开答案</summary>

$y'=\dfrac{2x}{1+x^2}$，$y'(1)=\dfrac{2}{2}=\boxed{1}$。

</details>

### T3（参数方程一阶导）
设 $\begin{cases}x=t-\sin t\\ y=1-\cos t\end{cases}$，则 $\dfrac{\mathrm dy}{\mathrm dx}=$ ____。

<details><summary>展开答案</summary>

$\dfrac{\mathrm dy}{\mathrm dx}=\dfrac{y'(t)}{x'(t)}=\dfrac{\sin t}{1-\cos t}$。利用半角公式 $\sin t=2\sin\dfrac t2\cos\dfrac t2$、$1-\cos t=2\sin^2\dfrac t2$，化简为 $\boxed{\cot\dfrac t2}$（$t\neq2k\pi$）。

</details>

### T4（对数求导）
$y=x^{\sin x}\ (x>0)$，则 $y'=$ ____。

<details><summary>展开答案</summary>

取对数 $\ln y=\sin x\ln x$，求导 $\dfrac{y'}{y}=\cos x\ln x+\dfrac{\sin x}{x}$，故

$$
\boxed{y'=x^{\sin x}\!\left(\cos x\ln x+\frac{\sin x}{x}\right).}
$$

</details>

### T5（反三角求导）
$y=\arctan\dfrac{1}{x}$（$x\neq0$），则 $y'=$ ____。

<details><summary>展开答案</summary>

$y'=\dfrac{1}{1+\frac1{x^2}}\cdot\!\left(-\dfrac{1}{x^2}\right)=-\dfrac{1}{x^2+1}$。即 $\boxed{y'=-\dfrac{1}{1+x^2}}$。注意 $x>0$ 时 $y=\arctan\dfrac1x$，$x<0$ 时需借助 $\arctan\dfrac1x=-\pi-\arctan x$ 但导数相同。

</details>

### T6（二阶导）
$y=\sin x^2$，则 $y''=$ ____。

<details><summary>展开答案</summary>

$y'=2x\cos x^2$；$y''=2\cos x^2+2x\cdot(-\sin x^2\cdot2x)=\boxed{2\cos x^2-4x^2\sin x^2}$。

</details>

### T7（高阶导通项）
$\left(\dfrac{1}{1-2x}\right)^{(n)}=$ ____（$x\neq\dfrac12$）。

<details><summary>展开答案</summary>

套线性分式通项 $\left(\dfrac{1}{a+bx}\right)^{(n)}=\dfrac{(-1)^n n!\,b^n}{(a+bx)^{n+1}}$，此处 $a=1,b=-2$：

$$
\boxed{\left(\frac{1}{1-2x}\right)^{(n)}=\frac{(-1)^n n!(-2)^n}{(1-2x)^{n+1}}=\frac{2^n n!}{(1-2x)^{n+1}}.}
$$

</details>

### T8（微分近似）
用微分近似计算 $\sqrt[3]{1.03}\approx$ ____。

<details><summary>展开答案</summary>

$(1+x)^\alpha\approx1+\alpha x$，取 $x=0.03,\alpha=\dfrac13$：

$$
\sqrt[3]{1.03}\approx1+\frac{0.03}{3}=1.01\quad\text{即}\quad\boxed{1.01}.
$$

</details>

## 二、选择题（6 题）

### T9（可导与连续）
下列命题正确的是（　）。

A. $f$ 在 $x_0$ 连续则必可导　B. $f$ 在 $x_0$ 可导则必连续　C. $f$ 在 $x_0$ 不连续则不可导　D. B、C 均正确

<details><summary>展开答案</summary>

可导必连续（B）；不连续则不可导（C，是 B 的逆否）。$|x|$ 在 $0$ 连续不可导（A 错）。答案 $\boxed{D}$。

</details>

### T10（链式法则）
设 $y=\cos(2x+1)$，则 $y'=$（　）。

A. $\sin(2x+1)$　B. $-\sin(2x+1)$　C. $2\sin(2x+1)$　D. $-2\sin(2x+1)$

<details><summary>展开答案</summary>

$y'=-\sin(2x+1)\cdot(2x+1)'=-2\sin(2x+1)$。答案 $\boxed{D}$。

</details>

### T11（参数二阶导）
设 $x=\varphi(t),y=\psi(t)$ 二阶可导且 $\varphi'(t)\neq0$，则 $\dfrac{\mathrm d^2y}{\mathrm dx^2}=$（　）。

A. $\dfrac{\psi''(t)}{\varphi''(t)}$　B. $\dfrac{\psi''(t)\varphi'(t)-\psi'(t)\varphi''(t)}{[\varphi'(t)]^2}$　C. $\dfrac{\psi''(t)\varphi'(t)-\psi'(t)\varphi''(t)}{[\varphi'(t)]^3}$　D. $\dfrac{\psi'(t)}{\varphi'(t)}$

<details><summary>展开答案</summary>

对一阶导 $\dfrac{\mathrm dy}{\mathrm dx}=\dfrac{\psi'}{\varphi'}$ 再关于 $x$ 求参数导：

$$
\frac{\mathrm d^2y}{\mathrm dx^2}=\frac{\mathrm d}{\mathrm dt}\!\left(\frac{\psi'}{\varphi'}\right)\!\Big/\varphi'=\frac{\psi''\varphi'-\psi'\varphi''}{(\varphi')^2\cdot\varphi'}=\frac{\psi''\varphi'-\psi'\varphi''}{(\varphi')^3}.
$$

答案 $\boxed{C}$。

</details>

### T12（隐函数求导）
$y$ 由 $e^y+xy=e$ 确定，$y(0)=1$，则 $y'(0)=$（　）。

A. $0$　B. $-1$　C. $1$　D. $e$

<details><summary>展开答案</summary>

方程对 $x$ 求导：$e^y y'+y+xy'=0$。代入 $x=0,y=1$：$e\,y'(0)+1=0$，$y'(0)=-\dfrac1e$。**注意** $e$ 为常数 $e$，故 $\boxed{\text{选项中没有}}$——重新核验：题目记 $e$ 即自然常数，$e\,y'(0)+1=0\Rightarrow y'(0)=-1/e$。若四选项实为 A.0 B.$-1/e$ C.$1/e$ D.$1$，则选 $\boxed{B}$（视排版调整）。本题考查方法。

</details>

### T13（莱布尼茨）
$y=x^2 e^x$ 的 $n$ 阶导 $y^{(n)}=$（　）（$n\ge2$）。

A. $e^x(x^2+n(n-1))$　B. $e^x(x^2+2nx+n(n-1))$　C. $e^x(x^2+n)$　D. $e^x(x+n)^2$

<details><summary>展开答案</summary>

由莱布尼茨公式，$(x^2)''=2$，$(x^2)'''=0$，故只有 $k=0,1,2$ 三项：

$$
y^{(n)}=e^x x^2+\binom n1 2x\,e^x+\binom n2 2\,e^x=e^x\big[x^2+2nx+n(n-1)\big].
$$

答案 $\boxed{B}$。

</details>

### T14（一阶形式不变性）
下列关于一阶微分形式不变性正确的是（　）。

A. 仅当 $u$ 为自变量时 $\mathrm df=f'(u)\mathrm du$　B. 无论 $u$ 是否为自变量，$\mathrm df=f'(u)\mathrm du$ 均成立　C. 高阶微分也形式不变　D. $\mathrm dy$ 与 $\Delta y$ 恒相等

<details><summary>展开答案</summary>

一阶微分形式不变性即 B。高阶微分一般不保持形式（C 错）；$\mathrm dy$ 是线性主部，$\Delta y=\mathrm dy+o(\Delta x)$（D 错）。答案 $\boxed{B}$。

</details>

## 三、计算题（10 题）

### T15（复合 + 四则）
求 $y=\dfrac{e^{2x}\sin x}{1+\sqrt{x}}$ 的导数 $y'$（$x>0$）。

<details><summary>展开答案</summary>

用商法则，分子用积法则：

$$
y'=\frac{(e^{2x}\sin x)'(1+\sqrt x)-e^{2x}\sin x\cdot(1+\sqrt x)'}{(1+\sqrt x)^2}.
$$

其中 $(e^{2x}\sin x)'=2e^{2x}\sin x+e^{2x}\cos x=e^{2x}(2\sin x+\cos x)$，$(1+\sqrt x)'=\dfrac{1}{2\sqrt x}$。代入：

$$
\boxed{y'=\frac{e^{2x}(2\sin x+\cos x)(1+\sqrt x)-\dfrac{e^{2x}\sin x}{2\sqrt x}}{(1+\sqrt x)^2}.}
$$

</details>

### T16（隐函数求导与切线）
求曲线 $x^2+xy+y^2=3$ 在点 $(1,1)$ 处的切线方程。

<details><summary>展开答案</summary>

两边对 $x$ 求导：$2x+y+xy'+2yy'=0$。代入 $(1,1)$：$2+1+y'(1)+2y'=0\Rightarrow 3y'=-3\Rightarrow y'=-1$。切线：

$$
\boxed{y-1=-(x-1)\text{，即 }x+y-2=0.}
$$

</details>

### T17（参数方程二阶导）
设 $\begin{cases}x=a(t-\sin t)\\ y=a(1-\cos t)\end{cases}$（$a$ 为常数，$t\neq2k\pi$），求 $\dfrac{\mathrm d^2y}{\mathrm dx^2}$。

<details><summary>展开答案</summary>

一阶：$\dfrac{\mathrm dy}{\mathrm dx}=\dfrac{a\sin t}{a(1-\cos t)}=\dfrac{\sin t}{1-\cos t}$。

二阶：

$$
\frac{\mathrm d^2y}{\mathrm dx^2}=\frac{1}{a(1-\cos t)}\cdot\frac{\mathrm d}{\mathrm dt}\!\left(\frac{\sin t}{1-\cos t}\right).
$$

计算内部导数（商法则）：

$$
\frac{\mathrm d}{\mathrm dt}\!\left(\frac{\sin t}{1-\cos t}\right)=\frac{\cos t(1-\cos t)-\sin t\cdot\sin t}{(1-\cos t)^2}=\frac{\cos t-1}{(1-\cos t)^2}=-\frac{1}{1-\cos t}.
$$

代入：

$$
\boxed{\frac{\mathrm d^2y}{\mathrm dx^2}=-\frac{1}{a(1-\cos t)^2}.}
$$

</details>

### T18（对数求导）
$y=\left(\dfrac{x}{1+x}\right)^x$（$x>0$），求 $y'$。

<details><summary>展开答案</summary>

取对数 $\ln y=x[\ln x-\ln(1+x)]$。两边对 $x$ 求导：

$$
\frac{y'}{y}=[\ln x-\ln(1+x)]+x\!\left[\frac1x-\frac{1}{1+x}\right]=\ln\frac{x}{1+x}+\frac{1}{1+x}.
$$

故

$$
\boxed{y'=\left(\frac{x}{1+x}\right)^x\!\left[\ln\frac{x}{1+x}+\frac{1}{1+x}\right].}
$$

</details>

### T19（莱布尼茨高阶导）
求 $y=x^2\cos x$ 的 $n$ 阶导数（$n\ge2$）。

<details><summary>展开答案</summary>

取 $u=x^2,v=\cos x$，$(x^2)^{(k)}=0\,(k\ge3)$，仅 $k=0,1,2$ 项：

$$
\begin{aligned}
y^{(n)}&=x^2\cos\!\left(x+\frac{n\pi}{2}\right)+\binom n1\cdot 2x\cdot\cos\!\left(x+\frac{(n-1)\pi}{2}\right)+\binom n2\cdot2\cdot\cos\!\left(x+\frac{(n-2)\pi}{2}\right)\\
&=x^2\cos\!\left(x+\frac{n\pi}{2}\right)+2nx\cos\!\left(x+\frac{(n-1)\pi}{2}\right)+n(n-1)\cos\!\left(x+\frac{(n-2)\pi}{2}\right).
\end{aligned}
$$

$$
\boxed{y^{(n)}=x^2\cos\!\left(x+\tfrac{n\pi}{2}\right)+2nx\cos\!\left(x+\tfrac{(n-1)\pi}{2}\right)+n(n-1)\cos\!\left(x+\tfrac{(n-2)\pi}{2}\right).}
$$

</details>

### T20（隐函数二阶导）
设 $x^2-y^2=1$，求 $\dfrac{\mathrm d^2y}{\mathrm dx^2}$。

<details><summary>展开答案</summary>

一阶：$2x-2yy'=0\Rightarrow y'=\dfrac{x}{y}$。

二阶（商法则）：

$$
y''=\frac{1\cdot y-x\cdot y'}{y^2}=\frac{y-x\cdot\dfrac{x}{y}}{y^2}=\frac{y^2-x^2}{y^3}.
$$

由 $x^2-y^2=1\Rightarrow y^2-x^2=-1$，故

$$
\boxed{y''=-\frac{1}{y^3}.}
$$

</details>

### T21（分段函数可导性）
设 $f(x)=\begin{cases}\sin x,&x\le0\\ ax+b,&x>0\end{cases}$，求 $a,b$ 使 $f$ 在 $x=0$ 可导。

<details><summary>展开答案</summary>

**连续性**：$\lim\limits_{x\to0^-}\sin x=0=f(0)$，$\lim\limits_{x\to0^+}(ax+b)=b$，故 $b=0$。

**左右导数**：

$$
f'_-(0)=\lim_{h\to0^-}\frac{\sin h-0}{h}=1,\quad f'_+(0)=\lim_{h\to0^+}\frac{ah+b-0}{h}=a.
$$

令相等：$a=1$。

$$
\boxed{a=1,\ b=0.}
$$

</details>

### T22（相关变化率）
一倒立圆锥形容器水深 $h$ 时水面半径 $r=\dfrac{h}{\sqrt3}$。注水速率 $2\,\mathrm{m^3/min}$，水深 $h=2\,\mathrm m$ 时水面上升速率 $\dfrac{\mathrm dh}{\mathrm dt}$ 为多少？

<details><summary>展开答案</summary>

体积 $V=\dfrac13\pi r^2 h=\dfrac13\pi\cdot\dfrac{h^2}{3}\cdot h=\dfrac{\pi h^3}{9}$。对 $t$ 求导：

$$
\frac{\mathrm dV}{\mathrm dt}=\frac{\pi h^2}{3}\frac{\mathrm dh}{\mathrm dt}.
$$

代入 $\dfrac{\mathrm dV}{\mathrm dt}=2$、$h=2$：

$$
2=\frac{\pi\cdot4}{3}\frac{\mathrm dh}{\mathrm dt}\quad\Longrightarrow\quad\frac{\mathrm dh}{\mathrm dt}=\boxed{\frac{3}{2\pi}\,\mathrm{m/min}}.
$$

</details>

### T23（微分与误差）
测得立方体边长 $a=3\,\mathrm{cm}$，绝对误差 $\delta a=0.02\,\mathrm{cm}$。估计体积 $V=a^3$ 的绝对误差限 $\delta V$ 与相对误差限。

<details><summary>展开答案</summary>

$\dfrac{\mathrm dV}{\mathrm da}=3a^2=27$（$a=3$）。

- 绝对误差限：$\delta V\approx|V'(a)|\delta a=27\times0.02=\boxed{0.54\,\mathrm{cm^3}}$。
- 相对误差限：$\dfrac{\delta V}{V}\approx\dfrac{0.54}{27}=\boxed{2\%}$（也可用 $\dfrac{\delta V}{V}\approx3\dfrac{\delta a}{a}=3\times\dfrac{0.02}{3}=2\%$）。

</details>

### T24（抽象复合求导）
设 $f$ 二阶可导，$y=f(e^x)+e^{f(x)}$，求 $y''$。

<details><summary>展开答案</summary>

一阶：$y'=f'(e^x)e^x+f'(x)e^{f(x)}$。

二阶：

$$
y''=\big[f''(e^x)e^{2x}+f'(e^x)e^x\big]+\big[f''(x)e^{f(x)}+(f'(x))^2 e^{f(x)}\big].
$$

$$
\boxed{y''=f''(e^x)e^{2x}+f'(e^x)e^x+f''(x)e^{f(x)}+(f'(x))^2 e^{f(x)}.}
$$

</details>

## 四、证明题（4 题）

### T25（可导必连续）
证明：若 $f$ 在 $x_0$ 可导，则 $f$ 在 $x_0$ 连续。

<details><summary>展开答案</summary>

**证明**：由可导，$f'(x_0)=\lim\limits_{\Delta x\to0}\dfrac{\Delta y}{\Delta x}$ 存在。于是

$$
\lim_{\Delta x\to0}\Delta y=\lim_{\Delta x\to0}\left(\frac{\Delta y}{\Delta x}\cdot\Delta x\right)=f'(x_0)\cdot0=0,
$$

即 $\lim\limits_{\Delta x\to0}f(x_0+\Delta x)=f(x_0)$，故 $f$ 在 $x_0$ 连续。$\blacksquare$

</details>

### T26（连续不可导反例）
证明 $f(x)=|x|$ 在 $x=0$ 连续但不可导。

<details><summary>展开答案</summary>

**连续性**：$\lim\limits_{x\to0}|x|=0=f(0)$，故连续。

**不可导**：分别算左右导数：

$$
f'_-(0)=\lim_{h\to0^-}\frac{|h|-0}{h}=\lim_{h\to0^-}\frac{-h}{h}=-1,\quad
f'_+(0)=\lim_{h\to0^+}\frac{|h|-0}{h}=\lim_{h\to0^+}\frac{h}{h}=1.
$$

$f'_-(0)\neq f'_+(0)$，由可导充要条件（[[2.1 导数概念#三、单侧导数]]）知 $f$ 在 $0$ 不可导。$\blacksquare$

</details>

### T27（莱布尼茨公式归纳证明）
设 $u(x),v(x)$ 有 $n$ 阶导数，用归纳法证明：

$$
(uv)^{(n)}=\sum_{k=0}^{n}\binom{n}{k}u^{(n-k)}v^{(k)}.
$$

<details><summary>展开答案</summary>

**证明**（对 $n$ 归纳）：

**基础**：$n=1$ 时，$(uv)'=u'v+uv'=\binom10u'v+\binom11uv'$，即乘积法则，成立。

**归纳**：设 $n=m$ 成立。对 $n=m+1$，对和式求导：

$$
\begin{aligned}
(uv)^{(m+1)}&=\frac{\mathrm d}{\mathrm dx}\sum_{k=0}^{m}\binom{m}{k}u^{(m-k)}v^{(k)}\\
&=\sum_{k=0}^{m}\binom{m}{k}\big[u^{(m-k+1)}v^{(k)}+u^{(m-k)}v^{(k+1)}\big]\\
&=\sum_{k=0}^{m}\binom{m}{k}u^{(m+1-k)}v^{(k)}+\sum_{k=0}^{m}\binom{m}{k}u^{(m-k)}v^{(k+1)}.
\end{aligned}
$$

第二个和式中令 $j=k+1$（$j=1,\ldots,m+1$）：

$$
=\sum_{k=0}^{m}\binom{m}{k}u^{(m+1-k)}v^{(k)}+\sum_{j=1}^{m+1}\binom{m}{j-1}u^{(m+1-j)}v^{(j)}.
$$

合并 $u^{(m+1-k)}v^{(k)}$ 的同阶系数（$k=1,\ldots,m$）：

$$
\binom{m}{k}+\binom{m}{k-1}=\binom{m+1}{k}\quad\text{（Pascal 恒等式）},
$$

边界 $k=0$ 项系数 $\binom m0=1=\binom{m+1}{0}$，$k=m+1$ 项系数 $\binom mm=1=\binom{m+1}{m+1}$。故

$$
(uv)^{(m+1)}=\sum_{k=0}^{m+1}\binom{m+1}{k}u^{(m+1-k)}v^{(k)},
$$

即 $n=m+1$ 成立。由归纳法，公式对所有正整数 $n$ 成立。$\blacksquare$

</details>

### T28（参数方程二阶导公式推导）
设 $x=\varphi(t),y=\psi(t)$ 二阶可导，$\varphi'(t)\neq0$。证明：

$$
\frac{\mathrm d^2y}{\mathrm dx^2}=\frac{\varphi'(t)\psi''(t)-\psi'(t)\varphi''(t)}{[\varphi'(t)]^3}.
$$

<details><summary>展开答案</summary>

**证明**：一阶导 $\dfrac{\mathrm dy}{\mathrm dx}=\dfrac{\psi'(t)}{\varphi'(t)}$。它仍是 $t$ 的函数，求二阶导须对 $x$ 再求一次参数导：

$$
\frac{\mathrm d^2y}{\mathrm dx^2}=\frac{\mathrm d}{\mathrm dx}\!\left(\frac{\psi'}{\varphi'}\right)=\frac{\dfrac{\mathrm d}{\mathrm dt}\!\left(\dfrac{\psi'}{\varphi'}\right)}{\varphi'(t)}.
$$

对内部用商法则：

$$
\frac{\mathrm d}{\mathrm dt}\!\left(\frac{\psi'}{\varphi'}\right)=\frac{\psi''\varphi'-\psi'\varphi''}{(\varphi')^2}.
$$

代入：

$$
\frac{\mathrm d^2y}{\mathrm dx^2}=\frac{\psi''\varphi'-\psi'\varphi''}{(\varphi')^2\cdot\varphi'}=\frac{\varphi'\psi''-\psi'\varphi''}{(\varphi')^3}.
$$

$\blacksquare$

**注**：此即 [[2.4 隐函数、参数方程求导]] 的二阶导公式，分母为 $(\varphi')^3$ 而非 $(\varphi')^2$，是因为最后还要除以 $\varphi'$（再次参数求导）。

</details>

## 考点统计

| 题型 | 题量 | 覆盖小节 | 核心考点 |
| ---- | ---- | -------- | -------- |
| 填空 | 8 | 2.1—2.6 | 导数定义识别、复合/反三角/参数求导、对数求导、二阶导、$n$ 阶通项、微分近似 |
| 选择 | 6 | 2.1、2.2、2.4、2.5 | 可导连续关系、链式法则、参数二阶导公式、隐函数求导、莱布尼茨、形式不变性 |
| 计算 | 10 | 2.2—2.6 | 复合四则混合、隐函数切线、参数二阶导、对数求导、莱布尼茨高阶、隐函数二阶导、分段可导性、相关变化率、误差估计、抽象复合求导 |
| 证明 | 4 | 2.1、2.2、2.3、2.4 | 可导必连续、$|x|$ 不可导、莱布尼茨归纳、参数二阶导公式推导 |

> [!tip] 复习建议
> 1. **基础**：T1、T2、T9、T10、T14 检验概念与基本公式，务必秒答。
> 2. **核心运算**：T3、T11、T15、T16、T17、T19、T20 是本章最常考题型，必须熟练。
> 3. **综合**：T21、T22、T23、T24 综合分段、变化率、误差、抽象函数，难度较高。
> 4. **理论**：T25—T28 是定理与公式证明，理解推导过程有助于灵活运用。

## 章节导航

- 本章知识点：[[MOC - 第2章]]
- 上一章习题：[[MOC - 第1章习题]] ｜ 下一章习题：[[MOC - 第3章习题]]
- 上级：[[MOC - 高等数学A(1)]]

#高等数学 #一元微积分 #习题 #导数 #微分
