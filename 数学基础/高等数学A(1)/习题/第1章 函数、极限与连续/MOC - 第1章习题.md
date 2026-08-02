---
domain: 数学基础
subject: 高等数学A(1)
type: exercise
chapter: 第1章 函数、极限与连续
tags: [高等数学,习题,极限,连续,间断点,等价无穷小,重要极限,零点定理]
prerequisites: ["1.1 集合与函数", "1.2 数列极限", "1.3 函数极限", "1.4 无穷小量与无穷大量", "1.5 极限运算法则", "1.6 极限存在准则、两个重要极限", "1.7 无穷小的比较", "1.8 函数连续性与间断点"]
aliases: [第1章习题, 函数极限连续习题]
---

# MOC - 第1章习题 函数、极限与连续

> [!info] 习题说明
> 本章习题覆盖函数特性、$\varepsilon$-$N$ 与 $\varepsilon$-$\delta$ 论证、极限计算（代入/约分/有理化/等价无穷小替换/两个重要极限/洛必达法则预告）、无穷小比较、间断点分类与判别、闭区间连续函数性质证明。共 30 题：填空 8、选择 8、计算 8、证明 6。所有答案与解析折叠展示，计算题给出完整步骤，建议先独立完成再核对。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 对应笔记 |
| ---- | ---- | ------ | -------- |
| 填 1–2 | 填空 | 函数定义域、复合函数 | [[1.1 集合与函数]] |
| 填 3–4 | 填空 | 数列极限、$\varepsilon$-$N$ | [[1.2 数列极限]] |
| 填 5–6 | 填空 | 函数极限、左右极限 | [[1.3 函数极限]] |
| 填 7–8 | 填空 | 等价无穷小、两个重要极限 | [[1.6 极限存在准则、两个重要极限]]、[[1.7 无穷小的比较]] |
| 选 1–2 | 选择 | 函数特性、反函数 | [[1.1 集合与函数]] |
| 选 3–4 | 选择 | 极限存在性、左右极限 | [[1.3 函数极限]] |
| 选 5–6 | 选择 | 极限运算法则适用条件 | [[1.5 极限运算法则]] |
| 选 7–8 | 选择 | 间断点分类 | [[1.8 函数连续性与间断点]] |
| 计 1–3 | 计算 | 极限计算（约分/有理化/重要极限） | [[1.5 极限运算法则]]、[[1.6 极限存在准则、两个重要极限]] |
| 计 4–5 | 计算 | 等价无穷小替换 | [[1.7 无穷小的比较]] |
| 计 6 | 计算 | $1^\infty$ 型幂指极限 | [[1.6 极限存在准则、两个重要极限]] |
| 计 7 | 计算 | 分段函数极限与连续性 | [[1.3 函数极限]]、[[1.8 函数连续性与间断点]] |
| 计 8 | 计算 | 间断点分类 | [[1.8 函数连续性与间断点]] |
| 证 1–2 | 证明 | $\varepsilon$-$N$、$\varepsilon$-$\delta$ | [[1.2 数列极限]]、[[1.3 函数极限]] |
| 证 3–4 | 证明 | 夹逼准则、单调有界准则 | [[1.2 数列极限]]、[[1.6 极限存在准则、两个重要极限]] |
| 证 5–6 | 证明 | 零点定理、介值定理 | [[1.8 函数连续性与间断点]] |

## 一、填空题（共 8 题）

**填 1** 函数 $y=\dfrac{\sqrt{x-1}}{\ln(x-2)}+\arcsin\dfrac{x-1}{2}$ 的定义域是 ______。

**填 2** 设 $f(x)=x^2$，$g(x)=2^x$，则 $f(g(x))=$ ______，$g(f(x))=$ ______。

**填 3** 设 $a_n=\dfrac{3n^2-2n+1}{2n^2+5}$，则 $\displaystyle\lim_{n\to\infty}a_n=$ ______；用 $\varepsilon$-$N$ 语言证明时，对给定 $\varepsilon>0$，可取 $N=$ ______（写出一个表达式即可）。

**填 4** $\displaystyle\lim_{n\to\infty}\frac{1+\frac12+\frac1{2^2}+\cdots+\frac1{2^n}}{n}=$ ______。

**填 5** $\displaystyle\lim_{x\to2}\frac{x^2-4}{x-2}=$ ______。

**填 6** 设 $f(x)=\dfrac{|x|}{x}$，则 $\displaystyle\lim_{x\to0^-}f(x)=$ ______，$\displaystyle\lim_{x\to0^+}f(x)=$ ______，$\displaystyle\lim_{x\to0}f(x)$ ______（填"存在/不存在"）。

**填 7** 当 $x\to0$ 时，$\sin 3x\sim$ ______，$1-\cos 2x\sim$ ______，$\mathrm e^{2x}-1\sim$ ______。

**填 8** $\displaystyle\lim_{x\to0}\frac{\sin 2x}{\tan 3x}=$ ______；$\displaystyle\lim_{x\to\infty}\left(1+\frac{2}{x}\right)^{3x}=$ ______。

## 二、选择题（共 8 题）

**选 1** 下列函数中与 $y=\ln x^2$（$D=\mathbb{R}\setminus\{0\}$）相同的是（ ）
A. $y=2\ln x$  B. $y=2\ln|x|$  C. $y=(\ln x)^2$  D. $y=\ln(x+x)$

**选 2** 函数 $y=x^2\ (x\ge0)$ 的反函数是（ ）
A. $y=\pm\sqrt{x}$  B. $y=-\sqrt{x}$  C. $y=\sqrt{x}$  D. $y=\sqrt{-x}$

**选 3** 下列极限存在的是（ ）
A. $\displaystyle\lim_{x\to0}\sin\frac1x$  B. $\displaystyle\lim_{x\to\infty}\sin x$  C. $\displaystyle\lim_{x\to0}\frac{\sin x}{x^2}$  D. $\displaystyle\lim_{x\to0}x\sin\frac1x$

**选 4** $\displaystyle\lim_{x\to0}\frac{\mathrm e^{\frac1x}}{1+\mathrm e^{\frac1x}}$（ ）
A. $=0$  B. $=1$  C. $=\frac12$  D. 不存在

**选 5** 下列运算中正确的是（ ）
A. $\displaystyle\lim_{x\to0}\frac{x+\sin\frac1x}{x}=\lim_{x\to0}\frac{x}{x}+\lim_{x\to0}\frac{\sin\frac1x}{x}=1+0$
B. $\displaystyle\lim_{x\to0}\frac{\tan x-\sin x}{x^3}=\lim_{x\to0}\frac{x-x}{x^3}=0$
C. $\displaystyle\lim_{x\to0}\frac{\sin x}{x}=1$（用第一个重要极限）
D. $\displaystyle\lim_{x\to0}\frac{\ln(1+x)-x}{x^2}=\lim_{x\to0}\frac{x-x}{x^2}=0$（用 $\ln(1+x)\sim x$ 替换）

**选 6** 设 $\displaystyle\lim_{x\to x_0}f(x)=A$，$\displaystyle\lim_{x\to x_0}g(x)$ 不存在，则下列一定成立的是（ ）
A. $\lim[f+g]$ 不存在  B. $\lim[f\cdot g]$ 不存在  C. $\lim[f+g]$ 存在  D. 以上都不对

**选 7** 函数 $f(x)=\dfrac{x^2-x}{|x|(x-1)}$ 的间断点个数与可去间断点个数分别为（ ）
A. 2 个，1 个  B. 2 个，0 个  C. 1 个，1 个  D. 3 个，1 个

**选 8** 设 $f$ 在 $[a,b]$ 上连续，$f(a)f(b)<0$，则下列正确的是（ ）
A. $f$ 在 $(a,b)$ 内恰有一个零点
B. $f$ 在 $(a,b)$ 内至少有一个零点
C. $f$ 在 $[a,b]$ 上有最大值但未必有最小值
D. $f$ 在 $(a,b)$ 内取到最大值

## 三、计算题（共 8 题）

**计 1** 求极限 $\displaystyle\lim_{x\to1}\frac{x^3-1}{x^2-1}$。

**计 2** 求极限 $\displaystyle\lim_{x\to0}\frac{\sqrt{1+x}-\sqrt{1-x}}{x}$。

**计 3** 求极限 $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x\sin x}$。

**计 4** 求极限 $\displaystyle\lim_{x\to0}\frac{\mathrm e^{x^2}-1}{\cos x-1}$。

**计 5** 求极限 $\displaystyle\lim_{x\to0}\frac{\ln(1+x^2)}{\sqrt{1+x^2}-1}$。

**计 6** 求极限 $\displaystyle\lim_{x\to\infty}\left(\frac{x+1}{x-2}\right)^x$。

**计 7** 设 $f(x)=\begin{cases}x\sin\frac1x+1,&x<0\\a,&x=0\\\dfrac{\sin x}{x},&x>0\end{cases}$，求 $a$ 使 $f$ 在 $x=0$ 处连续，并求 $\displaystyle\lim_{x\to0}f(x)$。

**计 8** 求函数 $f(x)=\dfrac{x}{\tan x}$ 在 $x=0$、$x=\frac\pi2$、$x=\pi$ 处的间断点类型；若为可去间断点，补充定义使其连续。

## 四、证明题（共 6 题）

**证 1** 用 $\varepsilon$-$N$ 语言证明 $\displaystyle\lim_{n\to\infty}\frac{n+1}{2n-1}=\frac12$。

**证 2** 用 $\varepsilon$-$\delta$ 语言证明 $\displaystyle\lim_{x\to3}(2x-1)=5$。

**证 3** 用夹逼准则证明 $\displaystyle\lim_{n\to\infty}\frac{\sin n}{n}=0$。

**证 4** 设 $a_1=\sqrt2$，$a_{n+1}=\sqrt{2+a_n}$。证明 $\{a_n\}$ 收敛，并求 $\displaystyle\lim_{n\to\infty}a_n$。

**证 5** 证明方程 $x^5-3x+1=0$ 在 $(0,1)$ 内至少有一个实根。

**证 6** 设 $f$ 在 $[0,2a]$ 上连续，$f(0)=f(2a)$。证明存在 $\xi\in[0,a]$ 使 $f(\xi)=f(\xi+a)$。

## 答案与解析

<details>
<summary>点击展开答案与解析</summary>

### 一、填空题答案

**填 1** 定义域 $(2,3)$。条件：$x-1\ge0$（即 $x\ge1$）；$\ln(x-2)\ne0$ 且 $x-2>0$（即 $x>2$ 且 $x\ne3$）；$\left|\frac{x-1}{2}\right|\le1$（即 $-1\le x\le3$）。取交集：$x>2$、$x\ne3$、$x\le3$，得 $(2,3)$。

**填 2** $f(g(x))=(2^x)^2=2^{2x}=4^x$；$g(f(x))=2^{x^2}$。

**填 3** $\lim a_n=\frac32$。化简 $\left|\frac{3n^2-2n+1}{2n^2+5}-\frac32\right|=\left|\frac{2(3n^2-2n+1)-3(2n^2+5)}{2(2n^2+5)}\right|=\frac{|-4n-13|}{2(2n^2+5)}=\frac{4n+13}{2(2n^2+5)}$。当 $n\ge1$ 时 $\le\frac{17n}{2n^2}=\frac{17}{2n}$，故可取 $N=\left\lceil\frac{17}{2\varepsilon}\right\rceil$。

**填 4** $0$。分子 $S_n=\frac{1-(1/2)^{n+1}}{1-1/2}=2(1-2^{-(n+1)})\to2$，故 $\frac{S_n}{n}\to\frac{2}{\infty}=0$。

**填 5** $4$。$\frac{x^2-4}{x-2}=\frac{(x-2)(x+2)}{x-2}=x+2\to4$（$x\to2$）。

**填 6** $f(0^-)=-1$，$f(0^+)=1$，$\lim_{x\to0}f(x)$ 不存在。

**填 7** $\sin 3x\sim3x$；$1-\cos 2x\sim\frac12(2x)^2=2x^2$；$\mathrm e^{2x}-1\sim2x$。

**填 8** $\frac{\sin 2x}{\tan 3x}\sim\frac{2x}{3x}=\frac23$；$\left(1+\frac2x\right)^{3x}=\left[\left(1+\frac2x\right)^{x/2}\right]^6\to\mathrm e^6$。

### 二、选择题答案

**选 1** B。$\ln x^2=\ln|x|^2=2\ln|x|$，定义域 $\mathbb{R}\setminus\{0\}$ 与原函数一致；A 项 $2\ln x$ 定义域仅 $(0,+\infty)$，不同。

**选 2** C。$y=x^2\ (x\ge0)$ 严格单调增，反函数 $y=\sqrt{x}\ (x\ge0)$。

**选 3** D。$\lim_{x\to0}x\sin\frac1x=0$（有界 $\sin\frac1x$ 与无穷小 $x$ 之积）；A、B 振荡不存在；C $\frac{\sin x}{x^2}=\frac{\sin x}{x}\cdot\frac1x\to1\cdot\infty=\infty$ 不存在（极限为无穷属不存在）。

**选 4** D。$x\to0^+$ 时 $\frac1x\to+\infty$，$\mathrm e^{1/x}\to+\infty$，分式 $\to1$；$x\to0^-$ 时 $\frac1x\to-\infty$，$\mathrm e^{1/x}\to0$，分式 $\to0$。左右极限不等，极限不存在。

**选 5** C。A 错：$\lim\sin\frac1x$ 不存在，不能拆项（正确做法是把 $\frac{x+\sin\frac1x}{x}=1+\frac{\sin\frac1x}{x}$，第二项 $=x\cdot\frac{\sin\frac1x}{x}$ 不对，应为 $\frac{\sin\frac1x}{x}=\frac1x\sin\frac1x$ 无极限——本题极限实际不存在）；B 错（加减分别替换，正确值 $\frac12$，见 [[1.7 无穷小的比较#例 4]]）；D 错（加减替换失效，正确值 $\frac12$，由 $\ln(1+x)=x-\frac{x^2}{2}+o(x^2)$ 知 $\frac{\ln(1+x)-x}{x^2}\to-\frac12$）。

**选 6** A。若 $\lim[f+g]$ 存在，则 $\lim g=\lim[(f+g)-f]=\lim(f+g)-\lim f$ 存在，与条件矛盾。故 $\lim[f+g]$ 必不存在。B 不一定：$f=0$、$g=\sin\frac1x$ 时 $\lim f\cdot g=0$ 存在。

**选 7** A。$f(x)=\frac{x(x-1)}{|x|(x-1)}$。$x=0$：$\lim_{x\to0^-}\frac{x}{-x}=-1$，$\lim_{x\to0^+}\frac{x}{x}=1$，左右不等，为跳跃（第一类，不可去）。$x=1$：$\lim_{x\to1}\frac{x}{|x|}=1$ 极限存在但函数无定义，为可去。共 2 个间断点，1 个可去。

**选 8** B。零点定理保证至少一个零点（A "恰有一个"过强）；最值定理保证既有最大值又有最小值（C 错）；最大值可能在端点取得（D 错）。

### 三、计算题解析

**计 1** 约分：$\frac{x^3-1}{x^2-1}=\frac{(x-1)(x^2+x+1)}{(x-1)(x+1)}=\frac{x^2+x+1}{x+1}\to\frac{3}{2}$（$x\to1$）。

**计 2** 分子有理化：
$$\frac{\sqrt{1+x}-\sqrt{1-x}}{x}=\frac{(1+x)-(1-x)}{x(\sqrt{1+x}+\sqrt{1-x})}=\frac{2x}{x(\sqrt{1+x}+\sqrt{1-x})}=\frac{2}{\sqrt{1+x}+\sqrt{1-x}}\to\frac{2}{2}=1.$$

**计 3** 用等价无穷小：$1-\cos x\sim\frac12x^2$，$x\sin x\sim x\cdot x=x^2$，故
$$\frac{1-\cos x}{x\sin x}\sim\frac{\frac12 x^2}{x^2}=\frac12.$$

**计 4** $\mathrm e^{x^2}-1\sim x^2$，$\cos x-1\sim-\frac12 x^2$，故 $\frac{x^2}{-\frac12 x^2}=-2$。

**计 5** $\ln(1+x^2)\sim x^2$；分母有理化 $\sqrt{1+x^2}-1=\frac{x^2}{\sqrt{1+x^2}+1}\sim\frac{x^2}{2}$。故 $\frac{x^2}{x^2/2}=2$。

**计 6** 改写 $\left(\frac{x+1}{x-2}\right)^x=\left(1+\frac{3}{x-2}\right)^x$。令 $t=\frac{3}{x-2}$，$x=2+\frac3t$，$x\to\infty$ 时 $t\to0$：
$$\left(1+t\right)^{2+3/t}=(1+t)^2\cdot\left[(1+t)^{1/t}\right]^3\to1\cdot\mathrm e^3=\mathrm e^3.$$

**计 7**
- $\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\left(x\sin\frac1x+1\right)=0+1=1$（$x\sin\frac1x\to0$）；
- $\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\frac{\sin x}{x}=1$。

左右极限相等，$\lim_{x\to0}f(x)=1$。连续要求 $f(0)=a=1$。

**计 8**
- $x=0$：$\lim_{x\to0}\frac{x}{\tan x}=\lim_{x\to0}\frac{x}{x}=1$（$\tan x\sim x$），极限存在但函数无定义，为**第一类（可去）**，补充 $f(0)=1$ 即连续。
- $x=\frac\pi2$：$\tan\frac\pi2$ 无定义且 $\tan x\to\infty$，$\frac{x}{\tan x}\to0$，为**第一类（可去）**，补充 $f(\frac\pi2)=0$ 即连续。
- $x=\pi$：$\lim_{x\to\pi}\frac{x}{\tan x}$，令 $t=x-\pi\to0$，$\frac{\pi+t}{\tan(\pi+t)}=\frac{\pi+t}{\tan t}\sim\frac{\pi+t}{t}\to\infty$，为**第二类（无穷）**间断点。

### 四、证明题解析

**证 1** 对任给 $\varepsilon>0$，
$$\left|\frac{n+1}{2n-1}-\frac12\right|=\left|\frac{2(n+1)-(2n-1)}{2(2n-1)}\right|=\frac{3}{2(2n-1)}.$$
要使 $\frac{3}{2(2n-1)}<\varepsilon$，只需 $n>\frac{1}{2}\left(\frac{3}{2\varepsilon}+1\right)$。取 $N=\left\lceil\frac{1}{2}\left(\frac{3}{2\varepsilon}+1\right)\right\rceil$，则 $n>N$ 时上式成立。故极限为 $\frac12$。

**证 2** $|(2x-1)-5|=2|x-3|$。对任给 $\varepsilon>0$，取 $\delta=\frac\varepsilon2$，则当 $0<|x-3|<\delta$ 时 $|2x-1-5|=2|x-3|<2\delta=\varepsilon$。故 $\lim_{x\to3}(2x-1)=5$。

**证 3** 因 $|\sin n|\le1$，故 $0\le\left|\frac{\sin n}{n}\right|\le\frac1n$。又 $\lim_{n\to\infty}\frac1n=0$，由夹逼准则（取 $a_n=0$、$c_n=\frac1n$、$b_n=\left|\frac{\sin n}{n}\right|$），$\lim_{n\to\infty}\left|\frac{\sin n}{n}\right|=0$，从而 $\lim_{n\to\infty}\frac{\sin n}{n}=0$。

**证 4**
- **有界**：归纳证 $a_n<2$。$a_1=\sqrt2<2$；设 $a_n<2$，则 $a_{n+1}=\sqrt{2+a_n}<\sqrt4=2$。
- **单调增**：$a_{n+1}^2-a_n^2=2+a_n-a_n^2=-(a_n-2)(a_n+1)$。因 $a_n<2$ 故 $a_n-2<0$，又 $a_n+1>0$，乘积 $-(a_n-2)(a_n+1)>0$，即 $a_{n+1}^2>a_n^2$，$a_{n+1}>a_n$。
- 由单调有界准则 $\{a_n\}$ 收敛。设 $\lim a_n=a$，对 $a_{n+1}=\sqrt{2+a_n}$ 取极限得 $a=\sqrt{2+a}$，即 $a^2-a-2=0$，解得 $a=2$（舍去 $a=-1$，因 $a_n>0$）。故 $\lim a_n=2$。

**证 5** 令 $f(x)=x^5-3x+1$，$f$ 在 $[0,1]$ 上连续。$f(0)=1>0$，$f(1)=1-3+1=-1<0$，$f(0)f(1)<0$。由零点定理，存在 $\xi\in(0,1)$ 使 $f(\xi)=0$，即方程在 $(0,1)$ 内有实根。

**证 6** 令 $F(x)=f(x)-f(x+a)$，$F$ 在 $[0,a]$ 上连续。$F(0)=f(0)-f(a)$，$F(a)=f(a)-f(2a)=f(a)-f(0)=-F(0)$。
- 若 $F(0)=0$，则 $f(0)=f(a)$，取 $\xi=0$ 即可；
- 若 $F(0)\ne0$，则 $F(0)$ 与 $F(a)=-F(0)$ 异号，由零点定理存在 $\xi\in(0,a)$ 使 $F(\xi)=0$，即 $f(\xi)=f(\xi+a)$。

综上，存在 $\xi\in[0,a]$ 使 $f(\xi)=f(\xi+a)$。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 | 合计 |
| ---- | ---- | ---- | -------- | ---- |
| 填空 | 8 | 4 分/题 | 函数定义域、复合函数、$\varepsilon$-$N$、左右极限、等价无穷小、两个重要极限 | 32 分 |
| 选择 | 8 | 4 分/题 | 函数相同判定、反函数、极限存在性、运算法则适用条件、间断点分类、零点定理 | 32 分 |
| 计算 | 8 | 8 分/题 | 约分、有理化、等价无穷小替换、$1^\infty$ 幂指极限、分段函数连续性、间断点补充定义 | 64 分 |
| 证明 | 6 | 7 分/题 | $\varepsilon$-$N$、$\varepsilon$-$\delta$、夹逼准则、单调有界准则、零点定理、介值定理构造 | 42 分 |
| **合计** | **30** | — | — | **170 分** |

## 章节导航

- 上一级：[[MOC - 高等数学A(1)]]
- 本章知识点：[[MOC - 第1章]]
- 下一章习题：[[MOC - 第2章习题]]

## 相关标签

#高等数学 #习题 #极限 #连续 #间断点 #等价无穷小 #重要极限 #零点定理
