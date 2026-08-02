---
domain: 数学基础
subject: 高等数学A(1)
type: exercise
chapter: 第5章 定积分
tags: [高等数学,习题,定积分,牛顿莱布尼茨公式,反常积分,换元法,分部积分]
prerequisites: ["第4章 不定积分","第5章 定积分"]
aliases: [第5章习题, 定积分习题]
---

# MOC - 第5章习题

> [!info] 习题说明
> 第5章习题覆盖定积分定义与性质、变上限积分与牛顿—莱布尼茨公式、定积分换元与分部积分（含对称区间性质与 Wallis 公式）、反常积分敛散性判别与计算、Γ 函数。共 30 题，分为填空（6）、选择（6）、计算（12）、证明（6）。答案以 `<details>` 折叠。考点统计见末尾。

## 一、填空题（6 题）

> [!example] 填空 1
> $\displaystyle\int_0^1 (3x^2-2x+1)\,\mathrm dx=$ ____。
> > [!success]- 答案
> > $\Big[x^3-x^2+x\Big]_0^1=1-1+1=1$。

> [!example] 填空 2
> $\displaystyle\int_{-1}^1 \dfrac{x^3\sin^2 x}{1+x^4}\,\mathrm dx=$ ____。
> > [!success]- 答案
> > 奇函数在对称区间积分 $=0$。

> [!example] 填空 3
> $\displaystyle\int_0^{\pi/2}\cos^5 x\,\mathrm dx=$ ____。
> > [!success]- 答案
> > 由 Wallis 公式：$I_5=\dfrac{4}{5}\cdot\dfrac{2}{3}\cdot 1=\dfrac{8}{15}$。

> [!example] 填空 4
> $\displaystyle\int_1^{+\infty}\dfrac{\mathrm dx}{x^3}=$ ____。
> > [!success]- 答案
> > $p=3>1$ 收敛，$\displaystyle\int_1^{+\infty}\dfrac{\mathrm dx}{x^3}=\dfrac{1}{3-1}=\dfrac{1}{2}$。

> [!example] 填空 5
> 设 $F(x)=\displaystyle\int_0^x e^{-t^2}\,\mathrm dt$，则 $F'(x)=$ ____。
> > [!success]- 答案
> > 由变上限积分求导定理，$F'(x)=e^{-x^2}$。

> [!example] 填空 6
> $\Gamma(4)=$ ____。
> > [!success]- 答案
> > $\Gamma(4)=3!=6$。

## 二、选择题（6 题）

> [!example] 选择 1
> 下列积分中收敛的是（　）。
> A. $\int_1^{+\infty}\dfrac{\mathrm dx}{\sqrt{x}}$　B. $\int_0^1\dfrac{\mathrm dx}{x}$　C. $\int_1^{+\infty}\dfrac{\mathrm dx}{x^2}$　D. $\int_0^1\dfrac{\mathrm dx}{x^2}$
> > [!success]- 答案
> > C。A 的 $p=\frac{1}{2}<1$ 发散；B 的 $q=1$ 发散；D 的 $q=2>1$ 发散；C 的 $p=2>1$ 收敛。

> [!example] 选择 2
> $\displaystyle\int_0^{\pi} x\sin x\,\mathrm dx=$（　）。
> A. $\pi$　B. $-\pi$　C. $0$　D. $2\pi$
> > [!success]- 答案
> > A。分部积分：$\Big[-x\cos x\Big]_0^\pi+\int_0^\pi\cos x\,\mathrm dx=\pi+0=\pi$。

> [!example] 选择 3
> 设 $f(x)$ 连续，$\displaystyle\int_0^{x^2}f(t)\,\mathrm dt$ 对 $x$ 的导数为（　）。
> A. $f(x^2)$　B. $2x\,f(x^2)$　C. $f(x)$　D. $2x\,f(x)$
> > [!success]- 答案
> > B。复合函数求导：$\dfrac{\mathrm d}{\mathrm dx}\int_0^{x^2}f(t)\,\mathrm dt=f(x^2)\cdot 2x$。

> [!example] 选择 4
> $\displaystyle\int_{-\pi}^{\pi}\sin^3 x\,\mathrm dx=$（　）。
> A. $0$　B. $\pi$　C. $2\pi$　D. $4$
> > [!success]- 答案
> > A。$\sin^3 x$ 为奇函数，对称区间积分 $=0$。

> [!example] 选择 5
> $\displaystyle\int_0^1\dfrac{\mathrm dx}{\sqrt{1-x^2}}=$（　）。
> A. $\dfrac{\pi}{2}$　B. $\pi$　C. $1$　D. 发散
> > [!success]- 答案
> > A。$x=1$ 为瑕点，$\displaystyle\int_0^1\dfrac{\mathrm dx}{\sqrt{1-x^2}}=\arcsin x\Big|_0^1=\dfrac{\pi}{2}$。

> [!example] 选择 6
> $\Gamma\!\left(\dfrac{1}{2}\right)=$（　）。
> A. $1$　B. $\dfrac{\pi}{2}$　C. $\sqrt{\pi}$　D. $\pi$
> > [!success]- 答案
> > C。$\Gamma\!\left(\dfrac{1}{2}\right)=\sqrt{\pi}$。

## 三、计算题（12 题）

> [!example] 计算 1
> $\displaystyle\int_0^4\dfrac{\mathrm dx}{1+\sqrt{x}}$。
> > [!success]- 答案
> > 令 $x=t^2$，$\mathrm dx=2t\,\mathrm dt$，换限 $0\to0,4\to2$。
> > $\displaystyle\int_0^2\dfrac{2t}{1+t}\,\mathrm dt=2\int_0^2\left(1-\dfrac{1}{1+t}\right)\mathrm dt=2\Big[t-\ln(1+t)\Big]_0^2=2(2-\ln 3)$。

> [!example] 计算 2
> $\displaystyle\int_0^{\pi/2} e^x\sin x\,\mathrm dx$。
> > [!success]- 答案
> > 两次分部积分得 $I=\dfrac{1}{2}(e^{\pi/2}+1)$（循环型分部积分）。

> [!example] 计算 3
> $\displaystyle\int_{-2}^2 (x^3\cos x+x^2-1)\,\mathrm dx$。
> > [!success]- 答案
> > $x^3\cos x$ 为奇函数，积分为 $0$；$\int_{-2}^2(x^2-1)\,\mathrm dx=2\int_0^2(x^2-1)\,\mathrm dx=2\Big[\dfrac{x^3}{3}-x\Big]_0^2=\dfrac{4}{3}$。

> [!example] 计算 4
> $\displaystyle\int_0^{+\infty}x e^{-x}\,\mathrm dx$。
> > [!success]- 答案
> > 分部积分：$\Big[-xe^{-x}\Big]_0^{+\infty}+\int_0^{+\infty}e^{-x}\,\mathrm dx=0+\Big[-e^{-x}\Big]_0^{+\infty}=1$。

> [!example] 计算 5
> $\displaystyle\int_0^{\ln 2}\sqrt{e^x-1}\,\mathrm dx$。
> > [!success]- 答案
> > 令 $u=\sqrt{e^x-1}$，$x=\ln(1+u^2)$，$\mathrm dx=\dfrac{2u}{1+u^2}\,\mathrm du$，$0\to0,\ln2\to1$。
> > $\int_0^1 \dfrac{2u^2}{1+u^2}\,\mathrm du=2\int_0^1\left(1-\dfrac{1}{1+u^2}\right)\mathrm du=2-\dfrac{\pi}{2}$。

> [!example] 计算 6
> $\displaystyle\int_0^{\pi/4}\dfrac{\sin x}{1+\cos x}\,\mathrm dx$。
> > [!success]- 答案
> > 凑微分：$-\ln(1+\cos x)\Big|_0^{\pi/4}=-\ln\left(1+\dfrac{\sqrt2}{2}\right)+\ln 2=\ln\dfrac{2}{1+\sqrt2/2}=\ln\dfrac{4}{2+\sqrt2}$。

> [!example] 计算 7
> 判别 $\displaystyle\int_0^{+\infty}\dfrac{\mathrm dx}{x(\ln x)^2}$ 的敛散性。
> > [!success]- 答案
> > 令 $u=\ln x$，$\mathrm du=\dfrac{\mathrm dx}{x}$，$\displaystyle\int_1^{+\infty}\dfrac{\mathrm du}{u^2}=1$，收敛。

> [!example] 计算 8
> $\displaystyle\int_0^1\dfrac{\mathrm dx}{(2-x)\sqrt{1-x}}$。
> > [!success]- 答案
> > 令 $x=1-t^2$，$\mathrm dx=-2t\,\mathrm dt$，$0\to1,1\to0$。
> > $\int_0^1\dfrac{2t\,\mathrm dt}{(1+t^2)t}=2\int_0^1\dfrac{\mathrm dt}{1+t^2}=\dfrac{\pi}{2}$。

> [!example] 计算 9
> 设 $f(x)=\displaystyle\int_1^x \dfrac{\sin t}{t}\,\mathrm dt$，求 $f'(x)$ 与 $f''(x)$。
> > [!success]- 答案
> > $f'(x)=\dfrac{\sin x}{x}$，$f''(x)=\dfrac{x\cos x-\sin x}{x^2}$。

> [!example] 计算 10
> $\displaystyle\int_0^{\pi}\sqrt{\sin x-\sin^3 x}\,\mathrm dx$。
> > [!success]- 答案
> > $\sqrt{\sin x(1-\sin^2 x)}=\sqrt{\sin x}\,|\cos x|$。
> > $\int_0^{\pi/2}\sqrt{\sin x}\cos x\,\mathrm dx+\int_{\pi/2}^\pi\sqrt{\sin x}(-\cos x)\,\mathrm dx=\dfrac{2}{3}+\dfrac{2}{3}=\dfrac{4}{3}$。

> [!example] 计算 11
> $\displaystyle\int_1^{+\infty}\dfrac{\mathrm dx}{x^2(x+1)}$。
> > [!success]- 答案
> > 部分分式：$\dfrac{1}{x^2(x+1)}=-\dfrac{1}{x}+\dfrac{1}{x^2}+\dfrac{1}{x+1}$。
> > $\Big[-\ln x-\dfrac{1}{x}+\ln(x+1)\Big]_1^{+\infty}=\ln 2+\dfrac{1}{1}-\ln 2=1$（收敛）。

> [!example] 计算 12
> 用梯形法（$n=4$）近似 $\displaystyle\int_0^1\dfrac{\mathrm dx}{1+x^2}$。
> > [!success]- 答案
> > $h=0.25$，$x_0=0,x_1=0.25,x_2=0.5,x_3=0.75,x_4=1$。
> > $f$ 值：$1,0.9412,0.8,0.64,0.5$。
> > $T_4=\dfrac{0.25}{2}[1+2(0.9412+0.8+0.64)+0.5]\approx 0.7828$（精确值 $\pi/4\approx0.7854$）。

## 四、证明题（6 题）

> [!example] 证明 1
> 证明：$\displaystyle\int_0^{\pi/2}\sin^n x\,\mathrm dx=\int_0^{\pi/2}\cos^n x\,\mathrm dx$。
> > [!success]- 答案
> > 令 $x=\dfrac{\pi}{2}-t$，$\mathrm dx=-\mathrm dt$，换限 $\dfrac{\pi}{2}\to0,0\to\dfrac{\pi}{2}$。
> > $\int_0^{\pi/2}\sin^n x\,\mathrm dx=\int_0^{\pi/2}\sin^n\!\left(\dfrac{\pi}{2}-t\right)\mathrm dt=\int_0^{\pi/2}\cos^n t\,\mathrm dt$。

> [!example] 证明 2
> 设 $f(x)$ 在 $[-a,a]$ 上连续且为奇函数，证明 $F(x)=\displaystyle\int_0^x f(t)\,\mathrm dt$ 为偶函数。
> > [!success]- 答案
> > $F(-x)=\int_0^{-x}f(t)\,\mathrm dt$，令 $u=-t$，$\mathrm du=-\mathrm dt$，$0\to0,-x\to x$。
> > $F(-x)=\int_0^{x}f(-u)(-\mathrm du)\cdot(-1)=\int_0^x[-f(u)](-\mathrm du)=\int_0^x f(u)\,\mathrm du=F(x)$。

> [!example] 证明 3
> 证明 Wallis 递推公式 $I_n=\dfrac{n-1}{n}I_{n-2}$（$n\geq 2$）。
> > [!success]- 答案
> > $I_n=\int_0^{\pi/2}\sin^n x\,\mathrm dx=-\int_0^{\pi/2}\sin^{n-1}x\,\mathrm d\cos x$，分部积分：
> > $=\Big[-\sin^{n-1}x\cos x\Big]_0^{\pi/2}+(n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2 x\,\mathrm dx$
> > $=(n-1)\int_0^{\pi/2}\sin^{n-2}x(1-\sin^2 x)\,\mathrm dx=(n-1)I_{n-2}-(n-1)I_n$。
> > 故 $nI_n=(n-1)I_{n-2}$，即 $I_n=\dfrac{n-1}{n}I_{n-2}$。

> [!example] 证明 4
> 证明：若 $f(x)$ 在 $[a,b]$ 上连续且 $f(x)\geq 0$，$f(x)\not\equiv 0$，则 $\displaystyle\int_a^b f(x)\,\mathrm dx>0$。
> > [!success]- 答案
> > 存在 $x_0\in[a,b]$ 使 $f(x_0)>0$。由连续性，存在 $x_0$ 的某邻域 $U\subset[a,b]$，在其中 $f(x)>\dfrac{f(x_0)}{2}>0$。
> > 设 $U$ 长度为 $\delta>0$，则 $\int_a^b f(x)\,\mathrm dx\geq\int_U \dfrac{f(x_0)}{2}\,\mathrm dx=\dfrac{\delta f(x_0)}{2}>0$。

> [!example] 证明 5
> 证明 $\Gamma(s+1)=s\,\Gamma(s)$（$s>0$）。
> > [!success]- 答案
> > $\Gamma(s+1)=\int_0^{+\infty}x^s e^{-x}\,\mathrm dx$，分部积分取 $u=x^s,\mathrm dv=e^{-x}\mathrm dx$：
> > $=\Big[-x^s e^{-x}\Big]_0^{+\infty}+s\int_0^{+\infty}x^{s-1}e^{-x}\,\mathrm dx=s\,\Gamma(s)$（边界项为 $0$）。

> [!example] 证明 6
> 设 $f(x)$ 在 $[0,1]$ 上连续，证明 $\displaystyle\int_0^{\pi}x\,f(\sin x)\,\mathrm dx=\dfrac{\pi}{2}\int_0^{\pi}f(\sin x)\,\mathrm dx$。
> > [!success]- 答案
> > 令 $x=\pi-t$：$\displaystyle\int_0^\pi x f(\sin x)\,\mathrm dx=\int_0^\pi (\pi-t)f(\sin t)\,\mathrm dt=\pi\int_0^\pi f(\sin t)\,\mathrm dt-\int_0^\pi t f(\sin t)\,\mathrm dt$。
> > 移项得 $2I=\pi J$，故 $I=\dfrac{\pi}{2}J$。

## 考点统计

| 考点 | 题号 | 分值占比 |
| ---- | ---- | -------- |
| 定积分基本计算 | 填1、选2、计1、计2、计3、计6 | 25% |
| 换元法与分部积分 | 计1、计2、计5、计10 | 20% |
| 对称区间与奇偶性 | 填2、填3、选4、计3 | 15% |
| 变上限积分求导 | 填5、选3、计9 | 15% |
| 反常积分敛散性与计算 | 填4、选1、选5、计4、计7、计11 | 15% |
| Γ 函数 | 填6、选6、证5 | 5% |
| 近似计算 | 计12 | 5% |

## 章节导航

- 上一级：[[MOC - 第5章]]
- 上一章习题：[[MOC - 第4章习题]]
- 下一章习题：[[MOC - 第6章习题]]
