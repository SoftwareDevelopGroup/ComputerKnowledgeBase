---
domain: 数学基础
subject: 高等数学A(2)
type: exercise
chapter: 第5章 无穷级数
tags: [高等数学,习题,无穷级数,正项级数,幂级数,傅里叶级数]
prerequisites: ["高等数学A(1)"]
aliases: [第5章习题, 无穷级数习题]
---

# MOC - 第5章习题

> [!info] 习题集说明
> 本文件汇集第5章"无穷级数"30 道精选习题，覆盖填空、选择、计算、证明四种题型，对应 [[MOC - 第5章]] 七个小节的全部核心考点。答案与提示以 `<details>` 折叠呈现，计算题给出完整步骤。重点：正项级数审敛、交错级数、绝对收敛与条件收敛判别、幂级数收敛半径与收敛域、和函数求法、函数展开成幂级数、傅里叶级数展开。

## 一、填空题（6 题）

### T1
几何级数 $\displaystyle\sum_{n=0}^{\infty}\left(-\dfrac{1}{2}\right)^n=$ ________。

<details>
<summary>答案</summary>

$|q|=\dfrac{1}{2}<1$，由 [[5.1 常数项级数概念与性质|几何级数]] 公式 $\sum q^n=\dfrac{1}{1-q}$：
$$\sum_{n=0}^{\infty}\left(-\dfrac{1}{2}\right)^n=\dfrac{1}{1-(-1/2)}=\dfrac{2}{3}$$
</details>

### T2
若级数 $\sum u_n$ 的部分和 $S_n=\dfrac{2n}{n+1}$，则 $\sum u_n=$ ________，$u_n=$ ________。

<details>
<summary>答案</summary>

$S=\lim_{n\to\infty}S_n=\lim\dfrac{2n}{n+1}=2$；$u_n=S_n-S_{n-1}=\dfrac{2n}{n+1}-\dfrac{2(n-1)}{n}=\dfrac{2}{n(n+1)}$。
</details>

### T3
幂级数 $\displaystyle\sum_{n=1}^{\infty}\dfrac{x^n}{n!}$ 的收敛半径 $R=$ ________，收敛域为 ________。

<details>
<summary>答案</summary>

$R=\lim\left|\dfrac{a_n}{a_{n+1}}\right|=\lim\dfrac{(n+1)!}{n!}=\lim(n+1)=+\infty$，收敛域 $(-\infty,+\infty)$。和函数为 $e^x-1$（[[5.6 函数展开成幂级数|指数展开]] 减去首项）。
</details>

### T4
级数 $\displaystyle\sum_{n=1}^{\infty}\dfrac{1}{n(n+2)}$ 的和 $S=$ ________。

<details>
<summary>答案</summary>

裂项 $\dfrac{1}{n(n+2)}=\dfrac{1}{2}\left(\dfrac{1}{n}-\dfrac{1}{n+2}\right)$，
$$S_n=\dfrac{1}{2}\left[\left(1-\dfrac{1}{3}\right)+\left(\dfrac{1}{2}-\dfrac{1}{4}\right)+\cdots+\left(\dfrac{1}{n}-\dfrac{1}{n+2}\right)\right]$$
前两项保留 $1, \dfrac{1}{2}$，后两项保留 $-\dfrac{1}{n+1}, -\dfrac{1}{n+2}$，故
$$S=\dfrac{1}{2}\left(1+\dfrac{1}{2}\right)=\dfrac{3}{4}$$
</details>

### T5
函数 $f(x)=e^x$ 的麦克劳林级数为 ________，收敛域 ________。

<details>
<summary>答案</summary>

$$e^x=\sum_{n=0}^{\infty}\dfrac{x^n}{n!}=1+x+\dfrac{x^2}{2!}+\cdots,\quad x\in(-\infty,+\infty)$$
见 [[5.6 函数展开成幂级数|六大展开式]]。
</details>

### T6
设 $f(x)=\pi-x$（$0\leq x\leq \pi$）作正弦延拓，则其正弦级数在 $x=\dfrac{\pi}{2}$ 处收敛于 ________。

<details>
<summary>答案</summary>

$f$ 在 $x=\dfrac{\pi}{2}$ 处连续，正弦级数收敛于 $f\left(\dfrac{\pi}{2}\right)=\pi-\dfrac{\pi}{2}=\dfrac{\pi}{2}$。参见 [[5.7 傅里叶级数|狄利克雷收敛定理]]。
</details>

## 二、选择题（6 题）

### T7
下列级数中收敛的是（  ）。

A. $\displaystyle\sum_{n=1}^{\infty}\dfrac{n}{n+1}$
B. $\displaystyle\sum_{n=1}^{\infty}\dfrac{1}{\sqrt{n}}$
C. $\displaystyle\sum_{n=1}^{\infty}\dfrac{1}{n^2}$
D. $\displaystyle\sum_{n=1}^{\infty}\dfrac{\cos n}{n}$

<details>
<summary>答案</summary>

**C**。A 通项 $u_n\to 1\neq 0$ 发散；B 是 $p=\dfrac{1}{2}$ 的 p 级数发散；C 是 $p=2$ 的 p 级数收敛；D 一般项级数，绝对值 $\sum|\cos n|/n$ 发散但本身条件收敛（需要更多分析），但比 C 不优先选。
</details>

### T8
若级数 $\sum u_n$ 收敛，则下列级数中必收敛的是（  ）。

A. $\sum |u_n|$
B. $\sum u_n^2$
C. $\sum \dfrac{u_n}{1+u_n}$
D. $\sum \dfrac{u_n - u_{n+1}}{2}$

<details>
<summary>答案</summary>

**D**。由 [[5.1 常数项级数概念与性质|级数线性性质]]，$\sum\dfrac{u_n-u_{n+1}}{2}=\dfrac{1}{2}(u_1-\lim u_{n+1})=\dfrac{u_1}{2}$（telescope）。A、B 反例 $\sum(-1)^n/n$；C 当 $u_n\to -1$ 时分母为零。
</details>

### T9
下列命题正确的是（  ）。

A. 若 $\sum u_n$ 收敛，则 $\sum u_n^2$ 收敛
B. 若 $\sum|u_n|$ 收敛，则 $\sum u_n$ 收敛
C. 若 $\sum u_n$ 发散，则 $\sum|u_n|$ 发散
D. 若 $u_n\to 0$，则 $\sum u_n$ 收敛

<details>
<summary>答案</summary>

**B**。由 [[5.3 交错级数、绝对收敛与条件收敛|绝对收敛蕴涵收敛]]。A 反例 $u_n=\dfrac{(-1)^n}{\sqrt{n}}$（条件收敛）但 $u_n^2=\dfrac{1}{n}$ 发散；C 反例 $u_n=\dfrac{(-1)^n}{\sqrt{n}}$，原级数收敛（条件收敛）而非发散；D 是必要非充分条件。
</details>

### T10
幂级数 $\displaystyle\sum_{n=1}^{\infty}\dfrac{(-1)^n x^n}{n}$ 的收敛域为（  ）。

A. $(-1, 1)$
B. $[-1, 1]$
C. $[-1, 1)$
D. $(-1, 1]$

<details>
<summary>答案</summary>

**D**。$R=\lim\dfrac{n+1}{n}=1$；$x=1$：$\sum\dfrac{(-1)^n}{n}$ 由 [[5.3 交错级数、绝对收敛与条件收敛|莱布尼茨法]]收敛；$x=-1$：$\sum\dfrac{1}{n}$ 调和级数发散。故收敛域 $(-1,1]$。详见 [[5.4 幂级数收敛半径与收敛域|例题 1]]。
</details>

### T11
设 $f(x)$ 是以 $2\pi$ 为周期的函数，在 $(-\pi,\pi)$ 上 $f(x)=x$，则其傅里叶级数在 $x=\pi$ 处收敛于（  ）。

A. $\pi$
B. $0$
C. $\dfrac{\pi}{2}$
D. 不收敛

<details>
<summary>答案</summary>

**B**。$x=\pi$ 是延拓后的间断点，$f(\pi^-)=\pi$，$f(\pi^+)=-\pi$（周期延拓后从 $-\pi$ 跳到 $\pi$），由 [[5.7 傅里叶级数|狄利克雷收敛定理]]收敛于 $\dfrac{\pi+(-\pi)}{2}=0$。
</details>

### T12
下列函数的麦克劳林展开式中收敛域为 $(-1,1]$ 的是（  ）。

A. $e^x$
B. $\sin x$
C. $\ln(1+x)$
D. $\dfrac{1}{1-x}$

<details>
<summary>答案</summary>

**C**。$e^x$、$\sin x$ 收敛域为 $(-\infty,+\infty)$；$\ln(1+x)$ 收敛域 $(-1,1]$；$\dfrac{1}{1-x}$ 收敛域 $(-1,1)$。见 [[5.6 函数展开成幂级数|六大展开式]]。
</details>

## 三、计算题（12 题）

### T13
判别级数 $\displaystyle\sum_{n=1}^{\infty}\dfrac{n^2+1}{n^4+2}$ 的敛散性。

<details>
<summary>解答</summary>

用 [[5.2 正项级数审敛法|比较审敛法极限形式]]，取 $v_n=\dfrac{1}{n^2}$：
$$\lim_{n\to\infty}\dfrac{u_n}{v_n}=\lim_{n\to\infty}\dfrac{n^2(n^2+1)}{n^4+2}=\lim_{n\to\infty}\dfrac{n^4+n^2}{n^4+2}=1$$
$\sum\dfrac{1}{n^2}$（$p=2>1$）收敛，故原级数收敛。
</details>

### T14
判别 $\displaystyle\sum_{n=1}^{\infty}\dfrac{2^n\cdot n!}{n^n}$ 的敛散性。

<details>
<summary>解答</summary>

用 [[5.2 正项级数审敛法|比值审敛法]]：
$$\dfrac{u_{n+1}}{u_n}=\dfrac{2^{n+1}(n+1)!\cdot n^n}{2^n n!\cdot (n+1)^{n+1}}=\dfrac{2(n+1)\cdot n^n}{(n+1)^{n+1}}=\dfrac{2}{\left(1+\dfrac{1}{n}\right)^n}\to \dfrac{2}{e}$$
因 $\left(1+\dfrac{1}{n}\right)^n\to e$，故 $\rho=\dfrac{2}{e}<1$，级数收敛。
</details>

### T15
判别 $\displaystyle\sum_{n=1}^{\infty}(-1)^n\dfrac{\ln n}{n}$ 的绝对/条件收敛性。

<details>
<summary>解答</summary>

**绝对收敛判别**：$\sum\dfrac{\ln n}{n}$，由 $\ln n>1$（$n\geq 3$），$\dfrac{\ln n}{n}>\dfrac{1}{n}$，与 $\sum\dfrac{1}{n}$ 比较发散，故不绝对收敛。

**原级数判别**：$u_n=\dfrac{\ln n}{n}$。$f(x)=\dfrac{\ln x}{x}$，$f'(x)=\dfrac{1-\ln x}{x^2}<0$（$x>e$），故 $n\geq 3$ 时 $u_n$ 单调减；又 $\lim_{n\to\infty}\dfrac{\ln n}{n}=0$（洛必达）。由 [[5.3 交错级数、绝对收敛与条件收敛|莱布尼茨法]]收敛。

故原级数**条件收敛**。
</details>

### T16
求幂级数 $\displaystyle\sum_{n=1}^{\infty}\dfrac{(x+1)^n}{n\cdot 3^n}$ 的收敛域。

<details>
<summary>解答</summary>

令 $t=x+1$，化为 $\sum\dfrac{t^n}{n\cdot 3^n}$。$R=\lim\dfrac{(n+1)\cdot 3^{n+1}}{n\cdot 3^n}=3$。
- $t=3$：$\sum\dfrac{1}{n}$ 调和级数发散；
- $t=-3$：$\sum\dfrac{(-1)^n}{n}$ 莱布尼茨法收敛。

故 $t\in[-3, 3)$，即 $-3\leq x+1<3$，$-4\leq x<2$。收敛域 $\boxed{[-4, 2)}$。
</details>

### T17
求幂级数 $\displaystyle\sum_{n=0}^{\infty}\dfrac{x^{2n}}{(2n)!}$ 的收敛域，并指出其和函数。

<details>
<summary>解答</summary>

这是缺项幂级数（仅偶次幂），用比值法直接对 $u_n(x)$：
$$\left|\dfrac{u_{n+1}(x)}{u_n(x)}\right|=\dfrac{|x|^{2n+2}}{(2n+2)!}\cdot\dfrac{(2n)!}{|x|^{2n}}=\dfrac{|x|^2}{(2n+1)(2n+2)}\to 0<1$$
对任意 $x$ 成立，故 $R=+\infty$，收敛域 $(-\infty,+\infty)$。

和函数：$\dfrac{e^x+e^{-x}}{2}=\cosh x$（双曲余弦）。由 $e^x=\sum\dfrac{x^n}{n!}$ 与 $e^{-x}=\sum\dfrac{(-1)^n x^n}{n!}$，相加后奇次项抵消，偶次项加倍，得 $\cosh x=\sum\dfrac{x^{2n}}{(2n)!}$。
</details>

### T18
求幂级数 $\displaystyle\sum_{n=1}^{\infty}\dfrac{x^{n+1}}{n(n+1)}$ 的和函数。

<details>
<summary>解答</summary>

收敛半径 $R=1$。端点 $x=\pm 1$：$\sum\dfrac{1}{n(n+1)}$ 收敛（裂项），$\sum\dfrac{(-1)^{n+1}}{n(n+1)}$ 绝对收敛。收敛域 $[-1,1]$。

设 $S(x)=\sum\dfrac{x^{n+1}}{n(n+1)}$，求导消去 $n(n+1)$：
$$S'(x)=\sum_{n=1}^{\infty}\dfrac{x^n}{n}$$
再求导：$S''(x)=\sum x^{n-1}=\dfrac{1}{1-x}$（$|x|<1$）。
积分还原 $S'(x)=-\ln(1-x)$（用 [[5.5 幂级数运算与和函数|例题 1]] 结果），再积分（$S(0)=0$）：
$$S(x)=-\int_0^x\ln(1-t)\,\mathrm{d}t=x+(1-x)\ln(1-x)$$
故 $S(x)=x+(1-x)\ln(1-x)$，$x\in[-1,1]$。端点 $x=1$ 取极限 $S(1)=1$。
</details>

### T19
将 $f(x)=\dfrac{x}{1+x^2}$ 展开为 $x$ 的幂级数，并指出收敛域。

<details>
<summary>解答</summary>

由几何级数 $\dfrac{1}{1-t}=\sum t^n$（$|t|<1$），令 $t=-x^2$：
$$\dfrac{1}{1+x^2}=\sum_{n=0}^{\infty}(-1)^n x^{2n},\quad |x|<1$$
两边乘 $x$：
$$\dfrac{x}{1+x^2}=\sum_{n=0}^{\infty}(-1)^n x^{2n+1}=x-x^3+x^5-\cdots,\quad x\in(-1,1)$$
端点 $x=\pm 1$ 通项不趋于零，发散。
</details>

### T20
将 $f(x)=\arctan x$ 展开为 $x$ 的幂级数，并求 $\sum_{n=0}^{\infty}\dfrac{(-1)^n}{2n+1}$。

<details>
<summary>解答</summary>

$f'(x)=\dfrac{1}{1+x^2}=\sum_{n=0}^{\infty}(-1)^n x^{2n}$（$|x|<1$）。逐项积分（$f(0)=0$）：
$$\arctan x=\int_0^x\dfrac{1}{1+t^2}\,\mathrm{d}t=\sum_{n=0}^{\infty}\dfrac{(-1)^n}{2n+1}x^{2n+1}$$
端点 $x=1$：$\sum\dfrac{(-1)^n}{2n+1}$ 由莱布尼茨法收敛；$x=-1$ 类似收敛。收敛域 $[-1,1]$。

令 $x=1$：
$$\sum_{n=0}^{\infty}\dfrac{(-1)^n}{2n+1}=\arctan 1=\dfrac{\pi}{4}$$
</details>

### T21
将 $f(x)=\sin^2 x$ 展开为 $x$ 的幂级数。

<details>
<summary>解答</summary>

用三角恒等式 $\sin^2 x=\dfrac{1-\cos 2x}{2}$，由 [[5.6 函数展开成幂级数|余弦展开]] $\cos t=\sum\dfrac{(-1)^n t^{2n}}{(2n)!}$：
$$\cos 2x=\sum_{n=0}^{\infty}\dfrac{(-1)^n (2x)^{2n}}{(2n)!}=\sum_{n=0}^{\infty}\dfrac{(-1)^n 4^n x^{2n}}{(2n)!}$$
故
$$\sin^2 x=\dfrac{1}{2}-\dfrac{1}{2}\sum_{n=0}^{\infty}\dfrac{(-1)^n 4^n x^{2n}}{(2n)!}=\sum_{n=1}^{\infty}\dfrac{(-1)^{n+1} 4^n x^{2n}}{2\cdot(2n)!}$$
收敛域 $(-\infty,+\infty)$。
</details>

### T22
设 $f(x)=\begin{cases}x, & 0\leq x\leq \pi\\ 0, & -\pi\leq x<0\end{cases}$ 以 $2\pi$ 为周期延拓，求其傅里叶级数。

<details>
<summary>解答</summary>

由 [[5.7 傅里叶级数|傅里叶系数公式]]：
$$a_0=\dfrac{1}{\pi}\int_{-\pi}^{\pi}f(x)\,\mathrm{d}x=\dfrac{1}{\pi}\int_0^\pi x\,\mathrm{d}x=\dfrac{\pi}{2}$$
$$a_n=\dfrac{1}{\pi}\int_0^\pi x\cos nx\,\mathrm{d}x=\dfrac{1}{\pi}\cdot\dfrac{(-1)^n-1}{n^2}\cdot\pi\cdot\dfrac{1}{?}$$
直接分部积分：$\int_0^\pi x\cos nx\,\mathrm{d}x=\left.\dfrac{x\sin nx}{n}\right|_0^\pi-\dfrac{1}{n}\int_0^\pi\sin nx\,\mathrm{d}x=0-\dfrac{1}{n}\cdot\dfrac{1-\cos n\pi}{n}=\dfrac{(-1)^n-1}{n^2}$
故 $a_n=\dfrac{(-1)^n-1}{\pi n^2}$。当 $n$ 偶时 $a_n=0$；$n$ 奇时 $a_n=-\dfrac{2}{\pi n^2}$。
$$b_n=\dfrac{1}{\pi}\int_0^\pi x\sin nx\,\mathrm{d}x=\dfrac{1}{\pi}\cdot\dfrac{-\pi\cos n\pi}{n}=\dfrac{(-1)^{n+1}}{n}$$
傅里叶级数：
$$f(x)\sim\dfrac{\pi}{4}+\sum_{n=1}^{\infty}\left[\dfrac{(-1)^n-1}{\pi n^2}\cos nx+\dfrac{(-1)^{n+1}}{n}\sin nx\right]$$
在 $x=0$ 处 $f(0^+)=0$，$f(0^-)=0$，级数收敛于 $0=f(0)$。在 $x=\pi$ 处 $f(\pi^-)=\pi$，$f(\pi^+)=0$（周期延拓），收敛于 $\dfrac{\pi}{2}$。
</details>

### T23
将 $f(x)=x+1$（$0\leq x\leq \pi$）展开为余弦级数。

<details>
<summary>解答</summary>

作偶延拓 $F(x)=|x|+1$（$x\in[-\pi,\pi]$），$b_n=0$。
$$a_0=\dfrac{2}{\pi}\int_0^\pi(x+1)\,\mathrm{d}x=\dfrac{2}{\pi}\cdot\dfrac{\pi^2}{2}+\dfrac{2}{\pi}\cdot\pi=\pi+2$$
$$a_n=\dfrac{2}{\pi}\int_0^\pi(x+1)\cos nx\,\mathrm{d}x$$
分部积分：$\int_0^\pi x\cos nx\,\mathrm{d}x=\dfrac{(-1)^n-1}{n^2}$（见 T22），$\int_0^\pi\cos nx\,\mathrm{d}x=0$（$n\geq 1$）。故 $a_n=\dfrac{2[(-1)^n-1]}{\pi n^2}$。

余弦级数：
$$x+1=\dfrac{\pi+2}{2}+\sum_{n=1}^{\infty}\dfrac{2[(-1)^n-1]}{\pi n^2}\cos nx,\quad x\in[0,\pi]$$
</details>

### T24
求 $\displaystyle\sum_{n=1}^{\infty}\dfrac{n}{2^n}$ 的和。

<details>
<summary>解答</summary>

考虑幂级数 $S(x)=\sum nx^n$，由 [[5.5 幂级数运算与和函数|先积后导法]]：
$$S(x)=x\sum nx^{n-1}=x\left(\sum x^n\right)'=x\cdot\dfrac{1}{(1-x)^2}=\dfrac{x}{(1-x)^2},\quad |x|<1$$
令 $x=\dfrac{1}{2}$：
$$\sum_{n=1}^{\infty}\dfrac{n}{2^n}=S\left(\dfrac{1}{2}\right)=\dfrac{1/2}{(1/2)^2}=2$$
</details>

## 四、证明题（6 题）

### T25
证明：若 $\sum u_n$ 收敛，$\sum v_n$ 收敛，且 $u_n\leq w_n\leq v_n$，则 $\sum w_n$ 收敛。

<details>
<summary>证明</summary>

由 $u_n\leq w_n\leq v_n$，$0\leq w_n-u_n\leq v_n-u_n$。$\sum(v_n-u_n)$ 收敛（[[5.1 常数项级数概念与性质|线性性质]]），由 [[5.2 正项级数审敛法|比较审敛法]] $\sum(w_n-u_n)$ 收敛。又 $\sum u_n$ 收敛，故
$$\sum w_n=\sum(w_n-u_n)+\sum u_n$$
收敛。$\square$
</details>

### T26
证明 $\displaystyle\lim_{n\to\infty}\dfrac{n^n}{n!}=+\infty$（提示：构造级数 $\sum\dfrac{n!}{n^n}$）。

<details>
<summary>证明</summary>

考虑级数 $\sum\dfrac{n!}{n^n}$，用比值法：
$$\dfrac{u_{n+1}}{u_n}=\dfrac{(n+1)!\cdot n^n}{n!\cdot (n+1)^{n+1}}=\dfrac{1}{\left(1+\dfrac{1}{n}\right)^n}\to\dfrac{1}{e}<1$$
故级数收敛。由 [[5.1 常数项级数概念与性质|收敛必要条件]] $\dfrac{n!}{n^n}\to 0$，即 $\dfrac{n^n}{n!}\to +\infty$。$\square$
</details>

### T27
设 $\sum u_n$、$\sum v_n$ 都收敛，且 $v_n>0$，$\lim\dfrac{u_n}{v_n}=1$。证明：$\sum u_n$ 绝对收敛 $\Leftrightarrow$ $\sum v_n$ 绝对收敛。

<details>
<summary>证明</summary>

由 $\lim\dfrac{|u_n|}{|v_n|}=1$（极限为正），由 [[5.2 正项级数审敛法|比较审敛法极限形式]]，$\sum|u_n|$ 与 $\sum|v_n|$ 同敛散。故 $\sum u_n$ 绝对收敛 $\Leftrightarrow$ $\sum|u_n|$ 收敛 $\Leftrightarrow$ $\sum|v_n|$ 收敛 $\Leftrightarrow$ $\sum v_n$ 绝对收敛。$\square$
</details>

### T28
设 $\sum u_n^2$ 与 $\sum v_n^2$ 都收敛，证明 $\sum u_n v_n$ 绝对收敛。

<details>
<summary>证明</summary>

由基本不等式 $|u_n v_n|\leq\dfrac{u_n^2+v_n^2}{2}$，因 $\sum\dfrac{u_n^2+v_n^2}{2}=\dfrac{1}{2}(\sum u_n^2+\sum v_n^2)$ 收敛，由 [[5.2 正项级数审敛法|比较审敛法]] $\sum|u_n v_n|$ 收敛，即 $\sum u_n v_n$ 绝对收敛。$\square$
</details>

### T29
证明：若正项级数 $\sum u_n$ 收敛，则 $\sum u_n^2$ 也收敛。

<details>
<summary>证明</summary>

因 $\sum u_n$ 收敛，由 [[5.1 常数项级数概念与性质|收敛必要条件]] $u_n\to 0$，故存在 $N$ 使 $n>N$ 时 $0<u_n<1$，从而 $u_n^2<u_n$。由 [[5.2 正项级数审敛法|比较审敛法]] $\sum u_n^2$ 收敛。$\square$

**反例说明逆不成立**：$u_n=\dfrac{1}{n}$，$\sum u_n^2=\sum\dfrac{1}{n^2}$ 收敛，但 $\sum u_n$ 调和级数发散。
</details>

### T30
证明：若 $f(x)$ 在 $[0, 2\pi]$ 上可积，且 $\int_0^{2\pi} f(x)\cos nx\,\mathrm{d}x=\int_0^{2\pi} f(x)\sin nx\,\mathrm{d}x=0$（$\forall n\geq 0$），则 $f(x)\equiv 0$。

<details>
<summary>证明</summary>

将 $f(x)$ 以 $2\pi$ 为周期延拓。条件表明 $f$ 的所有傅里叶系数 $a_n=b_n=0$，即傅里叶级数恒为零。

由 [[5.7 傅里叶级数|狄利克雷收敛定理]]（设 $f$ 满足狄利克雷条件），傅里叶级数处处收敛于 $\dfrac{f(x^+)+f(x^-)}{2}$。该值恒为零意味着 $f(x^+)+f(x^-)=0$ 对所有 $x$ 成立。

若 $f$ 连续，则 $f(x^+)=f(x^-)=f(x)$，故 $2f(x)=0$，$f\equiv 0$。

对一般可积函数，由 Parseval 等式（傅里叶分析定理）
$$\dfrac{1}{\pi}\int_0^{2\pi}f^2(x)\,\mathrm{d}x=\dfrac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2)=0$$
故 $\int f^2=0$，由 $f$ 连续或非负性质得 $f\equiv 0$。$\square$
</details>

## 五、考点统计

| 考点 | 题号 | 难度 | 备注 |
| ---- | ---- | ---- | ---- |
| 几何级数与调和级数 | T1, T2, T4, T7, T8 | 易 | 公式与定义 |
| 收敛必要条件 | T7, T26 | 易-中 | 通项趋于零判定 |
| 正项级数审敛法 | T13, T14, T27 | 中 | 比较法、比值法 |
| 交错级数与莱布尼茨法 | T15, T6 | 中 | 单调递减条件 |
| 绝对收敛与条件收敛 | T9, T15, T28, T29 | 中-难 | 反例对比 |
| 幂级数收敛半径与收敛域 | T3, T10, T16, T17 | 中 | 端点单独判别 |
| 缺项幂级数 | T17 | 中 | 直接比值法 |
| 和函数求法 | T18, T24, T17 | 中-难 | 先导后积/先积后导 |
| 函数间接展开 | T5, T12, T19, T20, T21 | 中 | 六大展开式应用 |
| 傅里叶系数计算 | T22, T23 | 中 | 分部积分 |
| 傅里叶级数收敛值 | T6, T11 | 中 | 间断点取平均 |
| 级数性质与不等式证明 | T25, T27, T28, T29 | 难 | 比较法+不等式 |
| Parseval 等式应用 | T30 | 难 | 拓展结论 |

## 章节导航

- 上一级：[[MOC - 第5章]]
- 上一章习题：[[MOC - 第4章习题]]（占位）
- 下一章习题：[[MOC - 第6章习题]]（占位）
- 返回：[[MOC - 高等数学A(2)]]

## 相关标签

#高等数学 #习题 #无穷级数 #正项级数 #幂级数 #傅里叶级数 #泰勒展开
