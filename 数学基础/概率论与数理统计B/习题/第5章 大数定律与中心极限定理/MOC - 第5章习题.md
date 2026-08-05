---
domain: 数学基础
subject: 概率论与数理统计B
type: exercise
chapter: 第5章 大数定律与中心极限定理
tags: [概率论,数理统计,习题,大数定律,中心极限定理,切比雪夫不等式,连续性修正]
prerequisites: ["高等数学","第4章 随机变量的数字特征","5.1 切比雪夫不等式","5.2 大数定律","5.3 独立同分布中心极限定理","5.4 棣莫弗-拉普拉斯定理"]
aliases: [第5章习题, 大数定律与中心极限定理习题]
---

# MOC - 第5章习题

> [!info] 习题说明
> 第5章习题覆盖切比雪夫不等式估界、依概率收敛判别、大数定律条件区分、CLT 标准化与近似计算、棣莫弗-拉普拉斯定理（含连续性修正）。共 32 题，分为填空（10）、选择（10）、计算（8）、证明（4）。答案以 `<details>` 折叠。考点统计见末尾。

## 一、填空题（10 题）

> [!example] 填空 1
> 设 $X$ 的期望 $\mu=5$，方差 $\sigma^2=4$。由切比雪夫不等式，$P\{|X-5|\geq 6\}\leq$ ____。
> > [!success]- 答案
> > $\dfrac{4}{6^2}=\dfrac{1}{9}$。

> [!example] 填空 2
> 设 $E(X)=\mu$，$D(X)=\sigma^2$。取 $\epsilon=2\sigma$，则 $P\{|X-\mu|<2\sigma\}\geq$ ____。
> > [!success]- 答案
> > $1-\dfrac{\sigma^2}{(2\sigma)^2}=1-\dfrac{1}{4}=\dfrac{3}{4}$。

> [!example] 填空 3
> 设 $X_n\xrightarrow{P}a$，$Y_n\xrightarrow{P}b$，则 $X_n+Y_n\xrightarrow{P}$ ____。
> > [!success]- 答案
> > $a+b$（依概率收敛的可加性）。

> [!example] 填空 4
> 设 $X_1,\ldots,X_{50}$ 独立同分布，$E(X_i)=2$，$D(X_i)=4$。令 $Y=\sum_{i=1}^{50}X_i$，则 $Y\sim\approx N($ ____, ____ $)$。
> > [!success]- 答案
> > $N(100,200)$。$E(Y)=50\times 2=100$，$D(Y)=50\times 4=200$。

> [!example] 填空 5
> 设 $X_i$ 独立同分布，$E(X_i)=1$，$D(X_i)=1$。则 $\dfrac{\sum_{i=1}^{100}X_i-100}{10}\sim\approx$ ____。
> > [!success]- 答案
> > $N(0,1)$（标准正态）。

> [!example] 填空 6
> 设 $Y\sim B(100,0.3)$。用正态近似，$Y\sim\approx N($ ____, ____ $)$。
> > [!success]- 答案
> > $N(30,21)$。$np=30$，$np(1-p)=21$。

> [!example] 填空 7
> 设 $Y\sim B(100,0.5)$，则 $\sqrt{D(Y)}=$ ____。
> > [!success]- 答案
> > $\sqrt{100\times 0.5\times 0.5}=5$。

> [!example] 填空 8
> 辛钦大数定律要求 $X_1,X_2,\ldots$ 满足 ____ 和 ____ 两个条件。
> > [!success]- 答案
> > 独立同分布；期望存在。

> [!example] 填空 9
> 用正态近似计算 $P\{Y\leq k\}$（$Y\sim B(n,p)$）时，端点修正为 $k+$ ____。
> > [!success]- 答案
> > $0.5$（即用 $\Phi\!\left(\dfrac{k+0.5-np}{\sqrt{npq}}\right)$）。

> [!example] 填空 10
> 伯努利大数定律的结论是：频率 $\dfrac{n_A}{n}\xrightarrow{P}$ ____。
> > [!success]- 答案
> > $p$（事件 $A$ 的概率）。

## 二、选择题（10 题）

> [!example] 选择 1
> 切比雪夫不等式成立的必要条件是（ ）。
> A. $X$ 服从正态分布  B. $X$ 是连续型  C. $E(X),D(X)$ 存在  D. $X$ 非负
> > [!success]- 答案
> > **C**。切比雪夫不等式只要求期望方差存在，与分布形式无关。

> [!example] 选择 2
> 下列哪个序列不满足辛钦大数定律的条件？（ ）
> A. $X_i$ 独立同分布，$X_i\sim N(0,1)$
> B. $X_i$ 独立同分布，$X_i\sim U(0,1)$
> C. $X_i$ 独立同分布，$X_i$ 服从柯西分布
> D. $X_i$ 独立同分布，$X_i\sim \mathrm{Exp}(1)$
> > [!success]- 答案
> > **C**。柯西分布期望不存在，辛钦大数定律不适用。

> [!example] 选择 3
> 切比雪夫大数定律要求随机变量序列（ ）。
> A. 独立同分布  B. 独立且方差一致有界  C. 独立同分布且期望存在  D. 仅独立
> > [!success]- 答案
> > **B**。切比雪夫大数定律不要求同分布，但要求方差一致有界。

> [!example] 选择 4
> 设 $X_i$ 独立同分布，$E(X_i)=\mu$，$D(X_i)=\sigma^2$，$n=100$。则 $\bar X$ 的近似分布为（ ）。
> A. $N(\mu,\sigma^2)$  B. $N(\mu,\sigma^2/100)$  C. $N(100\mu,100\sigma^2)$  D. $N(\mu/100,\sigma^2/100)$
> > [!success]- 答案
> > **B**。$\bar X\sim\approx N(\mu,\sigma^2/n)=N(\mu,\sigma^2/100)$。

> [!example] 选择 5
> 用正态近似计算 $P\{Y_n=k\}$（$Y_n\sim B(n,p)$，$n$ 大）时，正确的修正为（ ）。
> A. $P\{k-0.5<Y_n<k+0.5\}$  B. $P\{Y_n=k+0.5\}$  C. $P\{k<Y_n<k+1\}$  D. 不需修正
> > [!success]- 答案
> > **A**。点概率用 $P\{k-0.5<Y_n<k+0.5\}$ 近似。

> [!example] 选择 6
> 下列命题正确的是（ ）。
> A. 大数定律要求方差存在
> B. CLT 比大数定律弱
> C. 依概率收敛必依分布收敛
> D. 切比雪夫不等式可给精确概率
> > [!success]- 答案
> > **C**。依概率收敛 $\Rightarrow$ 依分布收敛；反之不真。A 错（辛钦不要求方差）；B 错（CLT 更强）；D 错（只给上界）。

> [!example] 选择 7
> 设 $Y\sim B(200,0.4)$。下列近似方法最合适的是（ ）。
> A. 直接精确计算  B. 泊松近似  C. 正态近似  D. 均匀近似
> > [!success]- 答案
> > **C**。$np=80\geq 5$，$n(1-p)=120\geq 5$，用正态近似。

> [!example] 选择 8
> 设 $Y\sim B(500,0.005)$。下列近似方法最合适的是（ ）。
> A. 正态近似  B. 泊松近似（$\lambda=2.5$）  C. 指数近似  D. 直接精确计算
> > [!success]- 答案
> > **B**。$n$ 大 $p$ 小，$np=2.5$ 适中，用泊松近似。

> [!example] 选择 9
> 关于依概率收敛，下列说法错误的是（ ）。
> A. $X_n\xrightarrow{P}a$ 则 $X_n\xrightarrow{d}a$
> B. 常数 $a$ 视作退化随机变量时 $X_n\xrightarrow{P}a$
> C. $X_n\xrightarrow{P}a$ 则 $X_n$ 必几乎处处收敛于 $a$
> D. $X_n\xrightarrow{P}a$，$g$ 连续则 $g(X_n)\xrightarrow{P}g(a)$
> > [!success]- 答案
> > **C**。依概率收敛不蕴含几乎处处收敛（后者更强）。

> [!example] 选择 10
> 设 $X_i$ 独立同分布，$E(X_i)=0$，$D(X_i)=1$。令 $Z_n=\dfrac{1}{\sqrt n}\sum_{i=1}^n X_i$。当 $n\to\infty$，$Z_n$ 的极限分布是（ ）。
> A. $N(0,1)$  B. $N(0,n)$  C. $0$  D. $N(0,1/n)$
> > [!success]- 答案
> > **A**。由 CLT，$Z_n=\dfrac{\sum X_i-0}{\sqrt n\cdot 1}\xrightarrow{d}N(0,1)$。

## 三、计算题（8 题）

> [!example] 计算 1（切比雪夫估界）
> 设 $X$ 的期望 $\mu=50$，方差 $\sigma^2=25$。用切比雪夫不等式估计 $P\{40<X<60\}$ 的下界。
> > [!success]- 答案
> > $\{40<X<60\}=\{|X-50|<10\}$，$\epsilon=10$。
> > $$P\{|X-50|<10\}\geq 1-\dfrac{25}{100}=1-0.25=0.75.$$

> [!example] 计算 2（确定 $n$）
> 设 $X_i$ 独立同分布，$E(X_i)=\mu$，$D(X_i)=4$。要使 $P\{|\bar X_n-\mu|<0.5\}\geq 0.95$，用切比雪夫不等式估计 $n$ 的最小值。
> > [!success]- 答案
> > $D(\bar X_n)=\dfrac{4}{n}$。
> > $$P\{|\bar X_n-\mu|<0.5\}\geq 1-\dfrac{4/n}{0.25}=1-\dfrac{16}{n}\geq 0.95.$$
> > $n\geq \dfrac{16}{0.05}=320$。

> [!example] 计算 3（CLT 求和概率）
> 设 $X_i$ 独立同分布，$E(X_i)=3$，$D(X_i)=4$。求 $P\{280<\sum_{i=1}^{100}X_i<320\}$ 的近似值（用 $\Phi$ 表示）。
> > [!success]- 答案
> > $Y=\sum X_i$，$E(Y)=300$，$D(Y)=400$，$\sqrt{D(Y)}=20$。
> > $$P\{280<Y<320\}=P\left\{\dfrac{280-300}{20}<\dfrac{Y-300}{20}<\dfrac{320-300}{20}\right\}=\Phi(1)-\Phi(-1)=2\Phi(1)-1.$$

> [!example] 计算 4（CLT 均值形式）
> 设 $X_i$ 独立同分布，$\mu=10$，$\sigma^2=9$，$n=36$。求 $P\{\bar X>10.5\}$。
> > [!success]- 答案
> > $\bar X\sim\approx N(10,9/36)=N(10,0.25)$，$\sqrt{D(\bar X)}=0.5$。
> > $$P\{\bar X>10.5\}=1-\Phi\!\left(\dfrac{10.5-10}{0.5}\right)=1-\Phi(1)\approx 1-0.8413=0.1587.$$

> [!example] 计算 5（棣莫弗-拉普拉斯区间）
> 掷均匀硬币 200 次，求正面次数在 90 到 110 之间（含端点）的概率。
> > [!success]- 答案
> > $Y\sim B(200,0.5)$，$np=100$，$npq=50$，$\sqrt{npq}\approx 7.071$。
> > 带连续性修正：$P\{90\leq Y\leq 110\}\approx \Phi\!\left(\dfrac{110.5-100}{7.071}\right)-\Phi\!\left(\dfrac{89.5-100}{7.071}\right)=\Phi(1.484)-\Phi(-1.484)=2\Phi(1.484)-1$。

> [!example] 计算 6（棣莫弗-拉普拉斯单边）
> 某批次产品次品率 $p=0.1$，抽检 100 件。求次品数不少于 15 的概率。
> > [!success]- 答案
> > $Y\sim B(100,0.1)$，$np=10$，$npq=9$，$\sqrt{npq}=3$。
> > $P\{Y\geq 15\}=P\{Y\geq 14.5\}\approx 1-\Phi\!\left(\dfrac{14.5-10}{3}\right)=1-\Phi(1.5)\approx 1-0.9332=0.0668$。

> [!example] 计算 7（CLT 综合）
> 某餐厅每日顾客数 $X_i$ 独立同分布，$E(X_i)=200$，$\sigma=20$。求 30 天总顾客数超过 6200 的概率。
> > [!success]- 答案
> > $Y=\sum_{i=1}^{30}X_i$，$E(Y)=6000$，$D(Y)=30\times 400=12000$，$\sqrt{D(Y)}\approx 109.54$。
> > $$P\{Y>6200\}=1-\Phi\!\left(\dfrac{6200-6000}{109.54}\right)\approx 1-\Phi(1.826)\approx 1-0.966=0.034.$$

> [!example] 计算 8（CLT 反求参数）
> 设 $X_i$ 独立同分布，$E(X_i)=\mu$，$D(X_i)=25$。要使 $P\{|\bar X_{100}-\mu|\leq 1\}\geq 0.95$，验证是否满足。
> > [!success]- 答案
> > $\bar X_{100}\sim\approx N(\mu,25/100)=N(\mu,0.25)$，$\sqrt{D}=0.5$。
> > $$P\{|\bar X_{100}-\mu|\leq 1\}=P\left\{\left|\dfrac{\bar X_{100}-\mu}{0.5}\right|\leq 2\right\}=2\Phi(2)-1\approx 2\times 0.9772-1=0.9544\geq 0.95.$$
> > 满足。

## 四、证明题（4 题）

> [!example] 证明 1
> 设 $X_1,X_2,\ldots$ 独立同分布，$E(X_i)=\mu$，$D(X_i)=\sigma^2<\infty$。证明 $\bar X_n\xrightarrow{P}\mu$（切比雪夫大数定律在同分布情形的特例）。
> > [!success]- 答案
> > $E(\bar X_n)=\mu$，$D(\bar X_n)=\sigma^2/n$。对任意 $\epsilon>0$，由 [[5.1 切比雪夫不等式]]：
> > $$P\{|\bar X_n-\mu|\geq \epsilon\}\leq \dfrac{D(\bar X_n)}{\epsilon^2}=\dfrac{\sigma^2}{n\epsilon^2}\to 0.$$
> > 故 $\bar X_n\xrightarrow{P}\mu$。

> [!example] 证明 2
> 设 $X_n\xrightarrow{P}a$，$g$ 是连续函数。证明 $g(X_n)\xrightarrow{P}g(a)$（连续映射定理）。
> > [!success]- 答案
> > 对任意 $\epsilon>0$，由 $g$ 在 $a$ 处连续，$\exists\delta>0$，使 $|x-a|<\delta\Rightarrow |g(x)-g(a)|<\epsilon$。
> > 故 $\{|g(X_n)-g(a)|\geq\epsilon\}\subseteq \{|X_n-a|\geq\delta\}$，从而
> > $$P\{|g(X_n)-g(a)|\geq\epsilon\}\leq P\{|X_n-a|\geq\delta\}\to 0.$$
> > 即 $g(X_n)\xrightarrow{P}g(a)$。

> [!example] 证明 3
> 设 $X_n\xrightarrow{P}a$，$Y_n\xrightarrow{P}b$（$a,b$ 为常数）。证明 $X_n+Y_n\xrightarrow{P}a+b$。
> > [!success]- 答案
> > 由 $\{|X_n+Y_n-(a+b)|\geq\epsilon\}\subseteq \{|X_n-a|\geq\epsilon/2\}\cup\{|Y_n-b|\geq\epsilon/2\}$：
> > $$P\{|X_n+Y_n-(a+b)|\geq\epsilon\}\leq P\{|X_n-a|\geq\epsilon/2\}+P\{|Y_n-b|\geq\epsilon/2\}\to 0.$$

> [!example] 证明 4
> 设 $X_1,\ldots,X_n$ 独立同分布，$E(X_i)=\mu$，$D(X_i)=\sigma^2$。证明 $\dfrac{1}{n}\sum_{i=1}^n (X_i-\bar X)^2\xrightarrow{P}\sigma^2$（即样本二阶中心矩依概率收敛于方差）。
> > [!success]- 答案
> > 记 $M_2=\dfrac{1}{n}\sum(X_i-\bar X)^2=\dfrac{1}{n}\sum X_i^2-\bar X^2$。
> > 由辛钦大数定律：$\dfrac{1}{n}\sum X_i\xrightarrow{P}\mu$；$\dfrac{1}{n}\sum X_i^2\xrightarrow{P}E(X^2)=\mu^2+\sigma^2$（独立同分布 + 期望存在）。
> > 由连续映射定理（[[证明 2]]）：$\bar X^2\xrightarrow{P}\mu^2$。
> > 再由可加性（[[证明 3]]）：$M_2=\dfrac{1}{n}\sum X_i^2-\bar X^2\xrightarrow{P}(\mu^2+\sigma^2)-\mu^2=\sigma^2$。

## 考点统计

| 题型 | 题数 | 主要考点 |
| ---- | ---- | ---- |
| 填空 | 10 | 切比雪夫上界、$k\sigma$ 形式、依概率收敛性质、CLT 标准化、二项正态近似参数、连续性修正 |
| 选择 | 10 | 不等式条件、大数定律条件区分、柯西分布反例、依概率收敛与依分布收敛关系、近似方法选择 |
| 计算 | 8 | 切比雪夫估界、确定 $n$、CLT 求和/均值概率、棣莫弗-拉普拉斯区间/单边、CLT 反求参数 |
| 证明 | 4 | 切比雪夫大数定律、连续映射定理、依概率收敛可加性、样本二阶中心矩收敛 |

## 章节导航

- 上一级：[[MOC - 第5章]]
- 本章知识点：[[5.1 切比雪夫不等式]]、[[5.2 大数定律]]、[[5.3 独立同分布中心极限定理]]、[[5.4 棣莫弗-拉普拉斯定理]]
- 上一章习题：[[MOC - 第4章习题]]
- 下一章习题：[[MOC - 第6章习题]]
