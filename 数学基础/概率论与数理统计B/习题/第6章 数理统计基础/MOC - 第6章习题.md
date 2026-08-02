---
domain: 数学基础
subject: 概率论与数理统计B
type: exercise
chapter: 第6章 数理统计基础
tags: [概率论,数理统计,习题,统计量,抽样分布,卡方分布,t分布,F分布,正态总体]
prerequisites: ["高等数学","第4章 随机变量的数字特征","第5章 大数定律与中心极限定理","6.1 总体、样本、统计量","6.2 样本均值、样本方差、样本矩","6.3 三大抽样分布：χ²分布、t分布、F分布","6.4 正态总体统计量分布"]
aliases: [第6章习题, 数理统计基础习题]
---

# MOC - 第6章习题

> [!info] 习题说明
> 第6章习题覆盖统计量判别、$\bar X$ 与 $S^2$ 数字特征、三大抽样分布（$\chi^2$、$t$、$F$）定义与查表、正态总体抽样定理（单总体与两总体）。共 32 题，分为填空（10）、选择（10）、计算（8，含查表）、证明（4，含分布性质）。答案以 `<details>` 折叠。考点统计见末尾。

## 一、填空题（10 题）

> [!example] 填空 1
> 设 $X_1,\ldots,X_n$ 来自总体 $X$，$E(X)=\mu$，$D(X)=\sigma^2$。则 $E(\bar X)=$ ____，$D(\bar X)=$ ____。
> > [!success]- 答案
> > $\mu$；$\sigma^2/n$。

> [!example] 填空 2
> 设 $X_1,\ldots,X_n$ 来自 $N(\mu,\sigma^2)$。则 $\bar X\sim$ ____，$\dfrac{(n-1)S^2}{\sigma^2}\sim$ ____。
> > [!success]- 答案
> > $N(\mu,\sigma^2/n)$；$\chi^2(n-1)$。

> [!example] 填空 3
> 样本方差 $S^2=$ ____（用 $\sum(X_i-\bar X)^2$ 表示），其分母为 $n-1$ 的原因是 ____。
> > [!success]- 答案
> > $\dfrac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2$；保证 $E(S^2)=\sigma^2$（无偏性）。

> [!example] 填空 4
> 设 $Z\sim N(0,1)$，$Y\sim\chi^2(n)$，$Z,Y$ 独立。则 $\dfrac{Z}{\sqrt{Y/n}}\sim$ ____。
> > [!success]- 答案
> > $t(n)$。

> [!example] 填空 5
> 设 $X\sim\chi^2(n_1)$，$Y\sim\chi^2(n_2)$，$X,Y$ 独立。则 $\dfrac{X/n_1}{Y/n_2}\sim$ ____。
> > [!success]- 答案
> > $F(n_1,n_2)$。

> [!example] 填空 6
> $\chi^2(n)$ 分布的期望为 ____，方差为 ____。
> > [!success]- 答案
> > $n$；$2n$。

> [!example] 填空 7
> $t$ 分布分位点的对称性公式为 $t_{1-\alpha}(n)=$ ____。
> > [!success]- 答案
> > $-t_\alpha(n)$。

> [!example] 填空 8
> $F$ 分布分位点的倒数性质：$F_{1-\alpha}(n_1,n_2)=$ ____。
> > [!success]- 答案
> > $\dfrac{1}{F_\alpha(n_2,n_1)}$（注意自由度顺序交换）。

> [!example] 填空 9
> 设 $X_1,\ldots,X_n$ 来自 $N(\mu,\sigma^2)$，$\sigma$ 未知。则 $\dfrac{\bar X-\mu}{S/\sqrt n}\sim$ ____。
> > [!success]- 答案
> > $t(n-1)$。

> [!example] 填空 10
> 设 $X_1,\ldots,X_{10}$ 来自 $N(1,4)$。则 $E(S^2)=$ ____，$\dfrac{9S^2}{4}\sim$ ____。
> > [!success]- 答案
> > $4$；$\chi^2(9)$。

## 二、选择题（10 题）

> [!example] 选择 1
> 设 $X_1,\ldots,X_n$ 来自 $N(\mu,\sigma^2)$（$\mu,\sigma^2$ 未知）。下列不是统计量的是（ ）。
> A. $\bar X$  B. $S^2$  C. $\dfrac{\bar X-\mu}{\sigma}$  D. $\dfrac{1}{n}\sum(X_i-\bar X)^2$
> > [!success]- 答案
> > **C**。含未知参数 $\mu,\sigma$，不是统计量。

> [!example] 选择 2
> 设 $X_1,\ldots,X_n$ 来自总体 $X$，$E(X)=\mu$，$D(X)=\sigma^2$。下列正确的是（ ）。
> A. $E(S^2)=\sigma^2/n$  B. $D(\bar X)=\sigma^2$  C. $E(\bar X)=\mu$  D. $E(S^2)=\dfrac{n-1}{n}\sigma^2$
> > [!success]- 答案
> > **C**。$E(\bar X)=\mu$；$D(\bar X)=\sigma^2/n$；$E(S^2)=\sigma^2$；$E(B_2)=\dfrac{n-1}{n}\sigma^2$。

> [!example] 选择 3
> 设 $X\sim N(0,1)$，$Y\sim\chi^2(5)$，$X,Y$ 独立。则 $\dfrac{X}{\sqrt{Y/5}}\sim$（ ）。
> A. $N(0,1)$  B. $t(5)$  C. $F(1,5)$  D. $\chi^2(5)$
> > [!success]- 答案
> > **B**。由 $t$ 分布定义。

> [!example] 选择 4
> 设 $X\sim\chi^2(10)$，$Y\sim\chi^2(15)$，$X,Y$ 独立。则 $X+Y\sim$（ ）。
> A. $\chi^2(25)$  B. $\chi^2(150)$  C. $F(10,15)$  D. $t(25)$
> > [!success]- 答案
> > **A**。$\chi^2$ 分布可加性。

> [!example] 选择 5
> 设 $X_1,\ldots,X_5$ 来自 $N(0,1)$。则 $\sum_{i=1}^5 X_i^2\sim$（ ）。
> A. $N(0,5)$  B. $\chi^2(5)$  C. $t(5)$  D. $F(5,1)$
> > [!success]- 答案
> > **B**。标准正态平方和服从 $\chi^2(n)$。

> [!example] 选择 6
> 关于 $t$ 分布，下列说法错误的是（ ）。
> A. 密度关于 $y$ 轴对称  B. $n>30$ 时近似正态  C. $t_{1-\alpha}(n)=-t_\alpha(n)$  D. $t$ 分布可加
> > [!success]- 答案
> > **D**。$t$ 分布一般**不可加**（$\chi^2$ 才可加）。

> [!example] 选择 7
> 设 $X_1,\ldots,X_{16}$ 来自 $N(\mu,\sigma^2)$。则 $\dfrac{\bar X-\mu}{\sigma/4}\sim$（ ）。
> A. $t(15)$  B. $N(0,1)$  C. $\chi^2(15)$  D. $F(1,15)$
> > [!success]- 答案
> > **B**。$\sigma$ 已知，标准化得 $N(0,1)$。

> [!example] 选择 8
> 设 $X_1,\ldots,X_{16}$ 来自 $N(\mu,\sigma^2)$。则 $\dfrac{\bar X-\mu}{S/4}\sim$（ ）。
> A. $t(15)$  B. $N(0,1)$  C. $\chi^2(15)$  D. $F(1,15)$
> > [!success]- 答案
> > **A**。$\sigma$ 未知用 $S$ 替代，得 $t(n-1)=t(15)$。

> [!example] 选择 9
> 关于 $\bar X$ 与 $S^2$ 的独立性，下列正确的是（ ）。
> A. 任何总体下都独立  B. 仅正态总体下独立  C. 大样本下独立  D. 与总体无关
> > [!success]- 答案
> > **B**。$\bar X\perp S^2$ 是正态总体的特殊性质。

> [!example] 选择 10
> 设两独立正态总体方差相等，$n_1=8,n_2=10$。则均值差统计量的自由度为（ ）。
> A. $16$  B. $17$  C. $18$  D. $9$
> > [!success]- 答案
> > **A**。$n_1+n_2-2=8+10-2=16$。

## 三、计算题（8 题）

> [!example] 计算 1（统计量数字特征）
> 设 $X_1,\ldots,X_{10}$ 来自 $N(2,9)$。求 $E(\bar X)$、$D(\bar X)$、$E(S^2)$。
> > [!success]- 答案
> > $\mu=2$，$\sigma^2=9$，$n=10$。
> > $E(\bar X)=2$；$D(\bar X)=9/10=0.9$；$E(S^2)=9$。

> [!example] 计算 2（样本方差计算）
> 抽得样本值 $3,5,7,9,11$。求 $\bar x$ 与 $s^2$。
> > [!success]- 答案
> > $\bar x=\dfrac{3+5+7+9+11}{5}=7$。
> > $\sum(X_i-\bar X)^2=(3-7)^2+(5-7)^2+(7-7)^2+(9-7)^2+(11-7)^2=16+4+0+4+16=40$。
> > $s^2=\dfrac{40}{5-1}=10$（分母 $n-1=4$）。

> [!example] 计算 3（分布判别）
> 设 $X_1,\ldots,X_{25}$ 来自 $N(0,1)$。指出 $\sum_{i=1}^{25}X_i^2$、$\dfrac{X_1}{\sqrt{\sum_{i=2}^{25}X_i^2/24}}$、$\dfrac{\sum_{i=1}^{10}X_i^2/10}{\sum_{i=11}^{25}X_i^2/15}$ 的分布。
> > [!success]- 答案
> > - $\sum_{i=1}^{25}X_i^2\sim\chi^2(25)$；
> > - $\dfrac{X_1}{\sqrt{\sum_{i=2}^{25}X_i^2/24}}\sim t(24)$；
> > - $\dfrac{\sum_{i=1}^{10}X_i^2/10}{\sum_{i=11}^{25}X_i^2/15}\sim F(10,15)$。

> [!example] 计算 4（$\bar X$ 概率）
> 设 $X_1,\ldots,X_9$ 来自 $N(0,4)$。求 $P\{\bar X>1\}$。
> > [!success]- 答案
> > $\bar X\sim N(0,4/9)$，$\sigma_{\bar X}=2/3$。
> > $$P\{\bar X>1\}=1-\Phi\!\left(\dfrac{1}{2/3}\right)=1-\Phi(1.5)\approx 1-0.9332=0.0668.$$

> [!example] 计算 5（$S^2$ 概率）
> 设 $X_1,\ldots,X_{10}$ 来自 $N(\mu,4)$。求 $P\{S^2>8\}$（用 $\chi^2$ 分位点表示）。
> > [!success]- 答案
> > $\dfrac{9S^2}{4}\sim\chi^2(9)$。$P\{S^2>8\}=P\!\left\{\dfrac{9S^2}{4}>\dfrac{9\times 8}{4}\right\}=P\{\chi^2(9)>18\}=1-\Phi_{\chi^2}(18)$。
> > 查表 $\chi^2_{0.975}(9)\approx 19.02$，$\chi^2_{0.95}(9)\approx 16.92$，故 $P\{\chi^2(9)>18\}\approx 0.027$（介于 $0.025$ 与 $0.05$ 之间，插值约 $0.027$）。

> [!example] 计算 6（查表）
> 查表给出：$\chi^2_{0.05}(10)$、$\chi^2_{0.95}(10)$、$t_{0.05}(10)$、$t_{0.025}(10)$、$F_{0.05}(5,10)$、$F_{0.95}(5,10)$。
> > [!success]- 答案（典型值，以教材附表为准）
> > - $\chi^2_{0.05}(10)\approx 3.940$，$\chi^2_{0.95}(10)\approx 18.307$；
> > - $t_{0.05}(10)\approx -1.812$，$t_{0.025}(10)\approx 2.228$；
> > - $F_{0.05}(5,10)\approx 3.326$，$F_{0.95}(5,10)=\dfrac{1}{F_{0.05}(10,5)}\approx \dfrac{1}{4.735}\approx 0.211$。

> [!example] 计算 7（两样本 $F$）
> 设 $X_1,\ldots,X_6$ 来自 $N(\mu_1,\sigma_1^2)$，$Y_1,\ldots,Y_{10}$ 来自 $N(\mu_2,\sigma_2^2)$，两样本独立。设 $\sigma_1^2=\sigma_2^2$，求 $P\{S_1^2/S_2^2>F_{0.05}(5,9)\}$。
> > [!success]- 答案
> > 由定理 6.4.6，$\dfrac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}=\dfrac{S_1^2}{S_2^2}\sim F(5,9)$（因 $\sigma_1^2=\sigma_2^2$）。
> > 故 $P\{S_1^2/S_2^2>F_{0.05}(5,9)\}=0.05$。

> [!example] 计算 8（综合）
> 设 $X_1,\ldots,X_5$ 来自 $N(0,1)$。令 $Y=X_1+\cdots+X_5$，$Z=X_1^2+\cdots+X_5^2$。求 $E(Y)$、$D(Y)$、$E(Z)$、$D(Z)$，并指出 $Z$ 的分布。
> > [!success]- 答案
> > - $Y\sim N(0,5)$（独立正态和），$E(Y)=0$，$D(Y)=5$；
> > - $Z\sim\chi^2(5)$，$E(Z)=5$，$D(Z)=10$。

## 四、证明题（4 题）

> [!example] 证明 1
> 设 $X_1,\ldots,X_n$ 来自总体 $X$（$E(X)=\mu$，$D(X)=\sigma^2$）。证明 $E(\bar X)=\mu$，$D(\bar X)=\sigma^2/n$。
> > [!success]- 答案
> > $E(\bar X)=\dfrac{1}{n}\sum E(X_i)=\dfrac{1}{n}\cdot n\mu=\mu$。
> > 由独立性 $D(\bar X)=\dfrac{1}{n^2}\sum D(X_i)=\dfrac{1}{n^2}\cdot n\sigma^2=\dfrac{\sigma^2}{n}$。

> [!example] 证明 2
> 设 $X_1,\ldots,X_n$ 来自 $N(\mu,\sigma^2)$。证明 $\dfrac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$（提示：用恒等式分解与 $\bar X\perp S^2$）。
> > [!success]- 答案
> > 令 $Z_i=\dfrac{X_i-\mu}{\sigma}\sim N(0,1)$。$\sum Z_i^2=\sum\!\left(\dfrac{X_i-\bar X}{\sigma}\right)^2+\dfrac{n(\bar X-\mu)^2}{\sigma^2}=\dfrac{(n-1)S^2}{\sigma^2}+\left(\dfrac{\bar X-\mu}{\sigma/\sqrt n}\right)^2$。
> > 左边 $\sim\chi^2(n)$；第二项 $\sim\chi^2(1)$；由 [[6.4 正态总体统计量分布]]定理 6.4.3 知两项独立。
> > 由 $\chi^2$ 可加性：$\chi^2(n)-\chi^2(1)\sim\chi^2(n-1)$，即 $\dfrac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$。

> [!example] 证明 3
> 证明 $t$ 分布的对称性：若 $T\sim t(n)$，则 $t_{1-\alpha}(n)=-t_\alpha(n)$。
> > [!success]- 答案
> > $t$ 分布密度 $f(x)$ 为偶函数，故 $T$ 与 $-T$ 同分布。
> > $1-\alpha=P\{T\leq t_{1-\alpha}\}=P\{-T\geq -t_{1-\alpha}\}=P\{T\geq -t_{1-\alpha}\}=1-P\{T\leq -t_{1-\alpha}\}$。
> > 故 $P\{T\leq -t_{1-\alpha}\}=\alpha$，即 $-t_{1-\alpha}=t_\alpha$，亦即 $t_{1-\alpha}=-t_\alpha$。

> [!example] 证明 4
> 证明 $F$ 分布的倒数性质：若 $F\sim F(n_1,n_2)$，则 $\dfrac{1}{F}\sim F(n_2,n_1)$，且 $F_{1-\alpha}(n_1,n_2)=\dfrac{1}{F_\alpha(n_2,n_1)}$。
> > [!success]- 答案
> > 由定义 $F=\dfrac{X/n_1}{Y/n_2}$（$X\sim\chi^2(n_1)$，$Y\sim\chi^2(n_2)$ 独立），则 $\dfrac{1}{F}=\dfrac{Y/n_2}{X/n_1}\sim F(n_2,n_1)$（分子分母都是独立 $\chi^2$ 标准化量）。
> > 由 $P\{F\leq F_{1-\alpha}(n_1,n_2)\}=1-\alpha$ 得 $P\!\left\{\dfrac{1}{F}\geq \dfrac{1}{F_{1-\alpha}(n_1,n_2)}\right\}=1-\alpha$。
> > 故 $P\!\left\{\dfrac{1}{F}\leq \dfrac{1}{F_{1-\alpha}(n_1,n_2)}\right\}=\alpha$。又 $\dfrac{1}{F}\sim F(n_2,n_1)$，故 $\dfrac{1}{F_{1-\alpha}(n_1,n_2)}=F_\alpha(n_2,n_1)$。

## 考点统计

| 题型 | 题数 | 主要考点 |
| ---- | ---- | ---- |
| 填空 | 10 | $\bar X,S^2$ 数字特征、三大分布定义、$t$/$F$ 分位点对称与倒数性质、$\chi^2$ 期望方差 |
| 选择 | 10 | 统计量判别、$E(S^2)$ 无偏、三大分布构造、$\bar X\perp S^2$ 条件、$t$ 不可加、$\sigma$ 已知/未知选 $Z$/$t$ |
| 计算 | 8 | 数字特征、样本方差计算、分布判别、$\bar X$/$S^2$ 概率、查表、两样本 $F$/$t$ |
| 证明 | 4 | $\bar X$ 数字特征、$\dfrac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$、$t$ 对称性、$F$ 倒数性质 |

## 章节导航

- 上一级：[[MOC - 第6章]]
- 本章知识点：[[6.1 总体、样本、统计量]]、[[6.2 样本均值、样本方差、样本矩]]、[[6.3 三大抽样分布：χ²分布、t分布、F分布]]、[[6.4 正态总体统计量分布]]
- 上一章习题：[[MOC - 第5章习题]]
- 下一章习题：[[MOC - 第7章习题]]
