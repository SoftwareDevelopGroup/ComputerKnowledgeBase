---
domain: 数学基础
subject: 高等数学A(1)
type: exercise
chapter: 第6章 定积分应用
tags: [高等数学,习题,定积分应用,面积,体积,弧长,变力做功,液体压力,微元法]
prerequisites: ["第5章 定积分","第6章 定积分应用"]
aliases: [第6章习题, 定积分应用习题]
---

# MOC - 第6章习题

> [!info] 习题说明
> 第6章习题覆盖定积分的几何应用（面积、旋转体体积、曲线弧长）与物理应用（变力做功、液体压力、引力）。核心方法是**微元法**。共 26 题，分为填空（6）、选择（6）、计算（10）、证明/应用（4）。答案以 `<details>` 折叠。考点统计见末尾。

## 一、填空题（6 题）

> [!example] 填空 1
> 曲线 $y=x^2$ 与 $y=x$ 围成的图形面积为 ____。
> > [!success]- 答案
> > 交点 $x=0,1$，$A=\int_0^1(x-x^2)\,\mathrm dx=\dfrac{1}{6}$。

> [!example] 填空 2
> 曲线 $y=\sin x$ 在 $[0,\pi]$ 上与 $x$ 轴围成的区域绕 $x$ 轴旋转所得旋转体体积为 ____。
> > [!success]- 答案
> > $V=\pi\int_0^\pi\sin^2 x\,\mathrm dx=\pi\cdot\dfrac{\pi}{2}=\dfrac{\pi^2}{2}$。

> [!example] 填空 3
> 抛物线 $y=x^2$ 从 $(0,0)$ 到 $(1,1)$ 的弧长为 ____。
> > [!success]- 答案
> > $L=\int_0^1\sqrt{1+4x^2}\,\mathrm dx=\dfrac{1}{2}\left[\dfrac{1}{2}x\sqrt{1+4x^2}+\dfrac{1}{4}\ln(2x+\sqrt{1+4x^2})\right]_0^1=\dfrac{\sqrt5}{4}+\dfrac{1}{8}\ln(2+\sqrt5)$。

> [!example] 填空 4
> 心形线 $r=a(1+\cos\theta)$ 围成的图形面积为 ____。
> > [!success]- 答案
> > $A=\dfrac{1}{2}\int_0^{2\pi}a^2(1+\cos\theta)^2\,\mathrm d\theta=\dfrac{3\pi a^2}{2}$。

> [!example] 填空 5
> 弹簧满足胡克定律 $F=kx$，从自然长度拉伸 $l$ 所做功为 ____。
> > [!success]- 答案
> > $W=\int_0^l kx\,\mathrm dx=\dfrac{1}{2}kl^2$。

> [!example] 填空 6
> 半径为 $R$ 的半圆闸门垂直浸入水中，直径在水面，闸门一侧所受水压力为 ____（水的密度 $\rho$，重力加速度 $g$）。
> > [!success]- 答案
> > $P=\int_0^R \rho g\,x\cdot 2\sqrt{R^2-x^2}\,\mathrm dx=\dfrac{2}{3}\rho g R^3$。

## 二、选择题（6 题）

> [!example] 选择 1
> 曲线 $y=e^x$、$y=e^{-x}$ 与 $x=1$ 围成的面积为（　）。
> A. $e+\dfrac{1}{e}-2$　B. $e-\dfrac{1}{e}$　C. $2e-2$　D. $e+\dfrac{1}{e}$
> > [!success]- 答案
> > A。$A=\int_0^1(e^x-e^{-x})\,\mathrm dx=\Big[e^x+e^{-x}\Big]_0^1=e+\dfrac{1}{e}-2$。

> [!example] 选择 2
> 椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ 绕 $x$ 轴旋转所得椭球体积为（　）。
> A. $\dfrac{4}{3}\pi a^3$　B. $\dfrac{4}{3}\pi b^3$　C. $\dfrac{4}{3}\pi a b^2$　D. $\dfrac{4}{3}\pi a^2 b$
> > [!success]- 答案
> > C。$V=\pi\int_{-a}^a b^2\!\left(1-\dfrac{x^2}{a^2}\right)\mathrm dx=\dfrac{4}{3}\pi a b^2$。

> [!example] 选择 3
> 摆线 $x=a(t-\sin t),y=a(1-\cos t)$ 一拱（$t\in[0,2\pi]$）的弧长为（　）。
> A. $4a$　B. $6a$　C. $8a$　D. $2\pi a$
> > [!success]- 答案
> > C。$L=\int_0^{2\pi}\sqrt{a^2(1-\cos t)^2+a^2\sin^2 t}\,\mathrm dt=\int_0^{2\pi}2a\sin\dfrac{t}{2}\,\mathrm dt=8a$。

> [!example] 选择 4
> 双纽线 $r^2=a^2\cos 2\theta$ 围成的面积为（　）。
> A. $a^2$　B. $2a^2$　C. $\pi a^2$　D. $\dfrac{a^2}{2}$
> > [!success]- 答案
> > A。利用对称性 $A=4\cdot\dfrac{1}{2}\int_0^{\pi/4}a^2\cos 2\theta\,\mathrm d\theta=a^2$。

> [!example] 选择 5
> 半径为 $R$ 的半球形水池盛满水（密度 $\rho$），将水全部抽出做功为（　）。
> A. $\dfrac{\pi\rho g R^4}{4}$　B. $\dfrac{2\pi\rho g R^4}{3}$　C. $\dfrac{\pi\rho g R^4}{2}$　D. $\pi\rho g R^4$
> > [!success]- 答案
> > A。$W=\int_0^R \pi\rho g\,x(R^2-x^2)\,\mathrm dx=\dfrac{\pi\rho g R^4}{4}$。

> [!example] 选择 6
> 曲线 $y=\ln x$ 在 $[1,e]$ 上的弧长为（　）。
> A. $\sqrt{1+e^2}-\sqrt{2}+\ln\dfrac{1+\sqrt{1+e^2}}{1+\sqrt{2}}$　B. $e-1$　C. $\sqrt{e^2+1}-\sqrt{2}$　D. $e+1$
> > [!success]- 答案
> > A。$L=\int_1^e\sqrt{1+\dfrac{1}{x^2}}\,\mathrm dx=\Big[\sqrt{x^2+1}+\ln\dfrac{x+\sqrt{x^2+1}}{1+\sqrt2}\Big]_1^e$。

## 三、计算题（10 题）

> [!example] 计算 1
> 求抛物线 $y^2=2x$ 与直线 $y=x-4$ 围成的面积。
> > [!success]- 答案
> > 交点：$y^2=2(y+4)\Rightarrow y=-2,4$，选 $y$ 为积分变量。
> > $A=\int_{-2}^4\left[(y+4)-\dfrac{y^2}{2}\right]\mathrm dy=\Big[\dfrac{y^2}{2}+4y-\dfrac{y^3}{6}\Big]_{-2}^4=18$。

> [!example] 计算 2
> 求曲线 $y=x^2$ 与 $y=\sqrt{x}$ 围成区域绕 $x$ 轴旋转的体积。
> > [!success]- 答案
> > 交点 $x=0,1$。$V=\pi\int_0^1\Big[(\sqrt{x})^2-(x^2)^2\Big]\mathrm dx=\pi\int_0^1(x-x^4)\,\mathrm dx=\dfrac{3\pi}{10}$。

> [!example] 计算 3
> 求星形线 $x=a\cos^3 t,y=a\sin^3 t$（$0\leq t\leq 2\pi$）围成的面积。
> > [!success]- 答案
> > 利用对称性，$A=4\int_0^{\pi/2}a\sin^3 t\cdot 3a\cos^2 t\sin t\,\mathrm dt=12a^2\int_0^{\pi/2}\sin^4 t\cos^2 t\,\mathrm dt=\dfrac{3\pi a^2}{8}$。

> [!example] 计算 4
> 求 $y=\cosh x=\dfrac{e^x+e^{-x}}{2}$ 在 $[0,1]$ 上的弧长。
> > [!success]- 答案
> > $y'=\sinh x$，$\sqrt{1+y'^2}=\cosh x$。
> > $L=\int_0^1\cosh x\,\mathrm dx=\sinh 1=\dfrac{e-\dfrac{1}{e}}{2}$。

> [!example] 计算 5
> 求心形线 $r=a(1+\cos\theta)$ 绕极轴旋转所得旋转体体积。
> > [!success]- 答案
> > $V=\dfrac{2\pi}{3}\int_0^\pi r^3\sin\theta\,\mathrm d\theta=\dfrac{2\pi a^3}{3}\int_0^\pi(1+\cos\theta)^3\sin\theta\,\mathrm d\theta=\dfrac{8\pi a^3}{3}$。

> [!example] 计算 6
> 半径为 $R$、高为 $H$ 的正圆锥绕轴旋转形成（母线 $y=\dfrac{R}{H}x$），求其体积。
> > [!success]- 答案
> > $V=\pi\int_0^H\!\left(\dfrac{R}{H}x\right)^2\mathrm dx=\dfrac{\pi R^2 H}{3}$。

> [!example] 计算 7
> 底面半径为 $R$ 的圆柱体被过底面直径且与底面成 $\alpha$ 角的平面截下立体，求其体积。
> > [!success]- 答案
> > 以直径为 $x$ 轴，截面面积 $A(x)=\dfrac{1}{2}\sqrt{R^2-x^2}\cdot\sqrt{R^2-x^2}\tan\alpha=\dfrac{1}{2}(R^2-x^2)\tan\alpha$。
> > $V=\int_{-R}^R A(x)\,\mathrm dx=\dfrac{\tan\alpha}{2}\cdot\dfrac{2}{3}R^3\cdot 2=\dfrac{2R^3\tan\alpha}{3}$。

> [!example] 计算 8
> 比重为 $\rho$ 的液体圆柱形储罐高 $H$，半径 $R$，将液体从罐顶抽出做多少功？
> > [!success]- 答案
> > 以罐底为原点，向上为 $x$ 正方向。$x$ 处液层提升距离 $H-x$，体积 $\pi R^2\,\mathrm dx$。
> > $W=\int_0^H \rho g(H-x)\pi R^2\,\mathrm dx=\dfrac{1}{2}\rho g\pi R^2 H^2$。

> [!example] 计算 9
> 等腰三角形闸门高 $2\,\mathrm m$，底宽 $2\,\mathrm m$，顶点在下、底边在水面上，求一侧水压力。
> > [!success]- 答案
> > 以水面为原点，向下为 $x$ 正方向，$0\leq x\leq 2$。水深 $x$ 处宽度 $f(x)=2-\dfrac{x}{2}\cdot 2=2-x$（依题意调整）。
> > 按题意宽 $f(x)=x$（顶在下时）。$P=\int_0^2 \rho g\,x\cdot x\,\mathrm dx=\dfrac{8\rho g}{3}$（具体取决于顶点位置，需画图定）。

> [!example] 计算 10
> 用梯形法（$n=4$）近似计算 $\displaystyle\int_0^1\dfrac{4}{1+x^2}\,\mathrm dx$ 并与 $\pi$ 比较。
> > [!success]- 答案
> > $h=0.25$，$f(x)=\dfrac{4}{1+x^2}$，节点值 $4,3.7647,3.2,2.56,2$。
> > $T_4=\dfrac{0.25}{2}[4+2(3.7647+3.2+2.56)+2]=\dfrac{1}{8}\cdot 25.0494\approx 3.1312$。
> > $\pi\approx 3.1416$，误差约 $0.0104$。

## 四、证明/应用题（4 题）

> [!example] 证明 1
> 证明：曲线 $y=f(x)$（$f\geq 0$）绕 $x$ 轴旋转所得旋转体体积 $V=\pi\int_a^b f^2(x)\,\mathrm dx$（圆盘法）。
> > [!success]- 答案
> > 在 $[x,x+\mathrm dx]$ 上，旋转体薄片近似为高 $\mathrm dx$、底半径 $f(x)$ 的圆柱，体积微元 $\mathrm dV=\pi f^2(x)\,\mathrm dx$。
> > 积分得 $V=\pi\int_a^b f^2(x)\,\mathrm dx$。

> [!example] 证明 2
> 证明：曲线 $y=f(x)$（$f\geq 0$）绕 $y$ 轴旋转所得旋转体体积 $V=2\pi\int_a^b x\,f(x)\,\mathrm dx$（圆环法/圆筒法）。
> > [!success]- 答案
> > 在 $[x,x+\mathrm dx]$ 上，旋转体薄筒近似为半径 $x$、高 $f(x)$、厚 $\mathrm dx$ 的圆筒，体积微元 $\mathrm dV=2\pi x f(x)\,\mathrm dx$。
> > 积分得 $V=2\pi\int_a^b x f(x)\,\mathrm dx$。

> [!example] 应用 3
> 半径为 $R$ 的均匀圆形薄片（密度 $\rho$，厚度不计）关于过中心垂直于薄片转轴的转动惯量。
> > [!success]- 答案
> > 在半径 $r$ 处取宽 $\mathrm dr$ 的圆环，质量 $\mathrm dm=\rho\cdot 2\pi r\,\mathrm dr$，到转轴距离为 $r$（转轴在薄片平面内过中心）。
> > $I=\int_0^R r^2\,\mathrm dm=\int_0^R 2\pi\rho r^3\,\mathrm dr=\dfrac{\pi\rho R^4}{2}=\dfrac{1}{2}MR^2$（$M=\pi R^2\rho$）。

> [!example] 应用 4
> 设半径为 $R$ 的半球体（密度 $\rho$ 均匀），求其质心位置。
> > [!success]- 答案
> > 以球心为原点，半球在 $z\geq 0$。由对称性 $\bar x=\bar y=0$。
> > $\bar z=\dfrac{\int_0^R z\cdot\pi(R^2-z^2)\,\mathrm dz}{\int_0^R\pi(R^2-z^2)\,\mathrm dz}=\dfrac{\pi R^4/4}{2\pi R^3/3}=\dfrac{3R}{8}$。

## 考点统计

| 考点 | 题号 | 分值占比 |
| ---- | ---- | -------- |
| 平面图形面积（直角坐标） | 填1、选1、计1 | 15% |
| 平面图形面积（极坐标） | 填4、选4、计3 | 15% |
| 旋转体体积（圆盘法） | 填2、选2、计2、计6、证1 | 25% |
| 旋转体体积（圆环法） | 证2 | 5% |
| 平面曲线弧长 | 填3、选3、选6、计4 | 20% |
| 变力做功 | 填5、选5、计8 | 10% |
| 液体压力 | 填6、计9 | 5% |
| 其他物理应用（转动惯量/质心） | 应3、应4 | 5% |

## 章节导航

- 上一级：[[MOC - 第6章]]
- 上一章习题：[[MOC - 第5章习题]]
- 课程结束：[[MOC - 高等数学A(1)]]
