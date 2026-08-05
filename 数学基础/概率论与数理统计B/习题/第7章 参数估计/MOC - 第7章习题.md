---
domain: 数学基础
subject: 概率论与数理统计B
type: exercise
chapter: 第7章 参数估计
tags: [概率论, 数理统计, 习题, 参数估计, 矩估计, 极大似然估计, 区间估计]
prerequisites: ["高等数学", "第7章 参数估计"]
aliases: [第7章习题, 参数估计习题]
---

# MOC - 第7章习题

> [!info] 习题说明
> 本章习题覆盖 [[MOC - 第7章|参数估计]] 全部考点，分填空、选择、计算、证明四类，共 32 题。计算题含矩估计、MLE 求解与区间估计计算；证明题聚焦无偏性。答案置于 `<details>` 折叠区，计算题给出完整步骤。

## 一、填空题（10 题）

**1.** 设 $X_1,\ldots,X_n\sim N(\mu,\sigma^2)$，$\mu,\sigma^2$ 未知，则 $\mu,\sigma^2$ 的矩估计分别为 $\hat\mu=$ ＿＿＿，$\widehat{\sigma^2}=$ ＿＿＿。

**2.** 设 $X_1,\ldots,X_n\sim U(0,\theta)$，则 $\theta$ 的矩估计为 ＿＿＿，MLE 为 ＿＿＿。

**3.** 设 $X_1,\ldots,X_n\sim \Pi(\lambda)$，则 $\lambda$ 的 MLE 为 ＿＿＿。

**4.** 设 $X_1,\ldots,X_n\sim \mathrm{Exp}(\lambda)$，则 $\lambda$ 的 MLE 为 ＿＿＿。

**5.** 样本方差 $S^2=\dfrac{1}{n-1}\sum(X_i-\bar X)^2$ 是 $\sigma^2$ 的 ＿＿＿ 估计（无偏/有偏）。

**6.** $\sigma^2$ 已知时，$\mu$ 的 $1-\alpha$ 置信区间为 ＿＿＿，所用枢轴量服从 ＿＿＿ 分布。

**7.** $\sigma^2$ 未知时，$\mu$ 的 $1-\alpha$ 置信区间为 ＿＿＿，枢轴量自由度为 ＿＿＿。

**8.** $\mu$ 未知时，$\sigma^2$ 的 $1-\alpha$ 置信区间为 ＿＿＿，枢轴量服从 ＿＿＿ 分布。

**9.** 设 $X_1,\ldots,X_n\sim N(\mu,\sigma^2)$，$D(\bar X)=$ ＿＿＿。

**10.** 设 $\hat\theta$ 是 $\theta$ 的 MLE，$g$ 单值，则 $g(\theta)$ 的 MLE 为 ＿＿＿（不变性）。

<details><summary>填空题答案</summary>

1. $\hat\mu=\bar X$，$\widehat{\sigma^2}=\dfrac{1}{n}\sum(X_i-\bar X)^2$
2. 矩估计 $2\bar X$；MLE $X_{(n)}=\max\{X_i\}$
3. $\hat\lambda=\bar X$
4. $\hat\lambda=\dfrac{1}{\bar X}=\dfrac{n}{\sum X_i}$
5. 无偏
6. $\bar X\pm z_{\alpha/2}\dfrac{\sigma}{\sqrt n}$；$N(0,1)$
7. $\bar X\pm t_{\alpha/2}(n-1)\dfrac{S}{\sqrt n}$；自由度 $n-1$
8. $\left(\dfrac{(n-1)S^2}{\chi_{\alpha/2}^2(n-1)},\dfrac{(n-1)S^2}{\chi_{1-\alpha/2}^2(n-1)}\right)$；$\chi^2(n-1)$
9. $\dfrac{\sigma^2}{n}$
10. $g(\hat\theta)$

</details>

## 二、选择题（10 题）

**1.** 关于矩估计，下列说法错误的是（　）。
A. 矩估计的理论依据是辛钦大数定律
B. 矩估计一定唯一
C. 矩估计可能不最优
D. 总体矩不存在时矩估计失效

**2.** 设 $X_1,\ldots,X_n\sim U(0,\theta)$，$\theta$ 的 MLE 是（　）。
A. $2\bar X$　B. $X_{(n)}$　C. $\bar X$　D. $\dfrac{n+1}{n}X_{(n)}$

**3.** 下列关于 $S^2=\dfrac{1}{n-1}\sum(X_i-\bar X)^2$ 的说法正确的是（　）。
A. 是 $\sigma^2$ 的 MLE　B. 分母为 $n$ 才无偏　C. 是 $\sigma^2$ 的无偏估计　D. 是 $\sigma$ 的无偏估计

**4.** 比较无偏估计 $\hat\theta_1,\hat\theta_2$ 的有效性，依据是（　）。
A. $E(\hat\theta_1)$ 与 $E(\hat\theta_2)$　B. $D(\hat\theta_1)$ 与 $D(\hat\theta_2)$　C. 偏度　D. 区间长度

**5.** 一致性是估计量的（　）。
A. 小样本性质　B. 大样本性质　C. 无偏性的特例　D. 与样本量无关

**6.** $\sigma^2$ 未知时构造 $\mu$ 的置信区间用 $t$ 而非 $Z$，原因是（　）。
A. $t$ 更精确　B. $Z$ 含未知 $\sigma$ 不能作枢轴量　C. $t$ 区间更短　D. 习惯

**7.** $\mu$ 未知时 $\sigma^2$ 的枢轴量 $\dfrac{(n-1)S^2}{\sigma^2}$ 服从（　）。
A. $\chi^2(n)$　B. $\chi^2(n-1)$　C. $t(n-1)$　D. $F(n-1,1)$

**8.** 置信水平 $1-\alpha$ 的含义是（　）。
A. $\theta$ 落入区间的概率
B. 区间覆盖 $\theta$ 的概率
C. $\theta$ 是随机变量
D. 区间端点不随机

**9.** 其他条件不变，提高置信水平 $1-\alpha$，则置信区间（　）。
A. 变窄　B. 变宽　C. 不变　D. 无法确定

**10.** 两正态总体方差比 $\sigma_1^2/\sigma_2^2$ 的区间估计用（　）枢轴量。
A. $Z$　B. $t$　C. $\chi^2$　D. $F$

<details><summary>选择题答案</summary>

1. **B**（矩估计可能不唯一，如泊松分布可用一阶或二阶矩）
2. **B**
3. **C**
4. **B**
5. **B**
6. **B**
7. **B**
8. **B**
9. **B**
10. **D**

</details>

## 三、计算题（8 题）

**1.（矩估计）** 设 $X_1,\ldots,X_n\sim U(a,b)$，$a,b$ 未知，求 $a,b$ 的矩估计。

<details><summary>解答</summary>

$E(X)=\dfrac{a+b}{2}$，$D(X)=\dfrac{(b-a)^2}{12}$，$E(X^2)=D(X)+[E(X)]^2$。令
$$\begin{cases}\bar X=\dfrac{a+b}{2}\\ A_2=\dfrac{(b-a)^2}{12}+\left(\dfrac{a+b}{2}\right)^2\end{cases}$$
由 $A_2-\bar X^2=\dfrac{(b-a)^2}{12}$，得 $b-a=2\sqrt{3(A_2-\bar X^2)}$，结合 $a+b=2\bar X$：
$$\boxed{\hat a=\bar X-\sqrt{3(A_2-\bar X^2)}=\bar X-\sqrt{3}\cdot S_n,\quad \hat b=\bar X+\sqrt{3}\cdot S_n}$$
其中 $S_n^2=A_2-\bar X^2=\dfrac1n\sum(X_i-\bar X)^2$。

</details>

**2.（MLE）** 设 $X_1,\ldots,X_n\sim N(\mu,\sigma^2)$，$\mu,\sigma^2$ 均未知，求 MLE。

<details><summary>解答</summary>

$L=(2\pi\sigma^2)^{-n/2}\exp\!\left[-\dfrac{1}{2\sigma^2}\sum(X_i-\mu)^2\right]$。
$\ln L=-\dfrac n2\ln(2\pi)-\dfrac n2\ln\sigma^2-\dfrac{1}{2\sigma^2}\sum(X_i-\mu)^2$。
对 $\mu$：$\dfrac{\partial}{\partial\mu}=\dfrac{1}{\sigma^2}\sum(X_i-\mu)=0\Rightarrow\hat\mu=\bar X$。
对 $\sigma^2$：$-\dfrac n{2\sigma^2}+\dfrac{1}{2\sigma^4}\sum(X_i-\hat\mu)^2=0\Rightarrow\widehat{\sigma^2}=\dfrac1n\sum(X_i-\bar X)^2$。
$$\boxed{\hat\mu=\bar X,\quad \widehat{\sigma^2}=\frac1n\sum(X_i-\bar X)^2}$$

</details>

**3.（MLE）** 设 $X_1,\ldots,X_n\sim U(0,\theta)$，求 $\theta$ 的 MLE。

<details><summary>解答</summary>

$L(\theta)=1/\theta^n$（要求 $0<X_i<\theta$ 即 $\theta\geq X_{(n)}$）。$L$ 关于 $\theta$ 递减，故在 $\theta=X_{(n)}$ 处取最大。
$$\boxed{\hat\theta=X_{(n)}=\max\{X_i\}}$$

</details>

**4.（MLE 不变性）** 上题中求 $E(X)=\theta/2$ 的 MLE。

<details><summary>解答</summary>

由 MLE 不变性，$g(\theta)=\theta/2$ 的 MLE 为 $g(\hat\theta)=\hat\theta/2=X_{(n)}/2$。
$$\boxed{\widehat{E(X)}=\frac{X_{(n)}}{2}}$$

</details>

**5.（区间估计）** 某正态总体 $\sigma^2=9$ 已知，抽 $n=25$，$\bar x=20$，求 $\mu$ 的 $95\%$ 置信区间。

<details><summary>解答</summary>

$\sigma^2$ 已知用 $Z$：$\bar x\pm z_{0.025}\dfrac{\sigma}{\sqrt n}$。$z_{0.025}=1.96$，$\sigma=3$，$\sqrt n=5$。
$$20\pm 1.96\times\frac{3}{5}=20\pm 1.176$$
$$\boxed{(18.824,\ 21.176)}$$

</details>

**6.（区间估计）** 正态总体 $\sigma^2$ 未知，$n=16$，$\bar x=10$，$s^2=4$，求 $\mu$ 的 $95\%$ 置信区间。

<details><summary>解答</summary>

用 $t(n-1)=t(15)$，$t_{0.025}(15)=2.131$，$s=2$。
$$10\pm 2.131\times\frac{2}{4}=10\pm 1.0655$$
$$\boxed{(8.93,\ 11.07)}$$

</details>

**7.（有效性）** 设 $X_1,\ldots,X_n\sim N(\mu,\sigma^2)$，比较 $\hat\mu_1=\bar X$ 与 $\hat\mu_2=\dfrac{1}{2}X_1+\dfrac{1}{2}X_2$ 的有效性。

<details><summary>解答</summary>

均无偏：$E(\hat\mu_1)=E(\hat\mu_2)=\mu$。
$D(\hat\mu_1)=\sigma^2/n$；$D(\hat\mu_2)=\dfrac14\sigma^2+\dfrac14\sigma^2=\dfrac{\sigma^2}{2}$。
当 $n>2$ 时 $\sigma^2/n<\sigma^2/2$，故 $\bar X$ 更有效。

</details>

**8.（两总体）** 两正态总体方差相等未知，$n_1=n_2=10$，$\bar x=20$，$\bar y=18$，$s_1^2=4$，$s_2^2=6$，求 $\mu_1-\mu_2$ 的 $95\%$ 置信区间。

<details><summary>解答</summary>

$S_w^2=\dfrac{9\times4+9\times6}{18}=5$，$S_w=\sqrt5$。自由度 $18$，$t_{0.025}(18)=2.101$。
$$\bar x-\bar y\pm t_{0.025}(18)S_w\sqrt{\frac1{10}+\frac1{10}}=2\pm 2.101\times\sqrt5\times\sqrt{0.2}$$
$$=2\pm 2.101\times\sqrt{1}=2\pm 2.101$$
$$\boxed{(-0.101,\ 4.101)}$$

</details>

## 四、证明题（4 题）

**1.** 证明 $E(\bar X)=\mu$（样本均值是总体均值的无偏估计）。

<details><summary>证明</summary>

$E(\bar X)=E\!\left(\dfrac1n\sum X_i\right)=\dfrac1n\sum E(X_i)=\dfrac1n\cdot n\mu=\mu$。$\square$

</details>

**2.** 证明 $E(S^2)=\sigma^2$（$S^2=\dfrac{1}{n-1}\sum(X_i-\bar X)^2$）。

<details><summary>证明</summary>

$\sum(X_i-\bar X)^2=\sum X_i^2-n\bar X^2$。
$E(\sum X_i^2)=n(\sigma^2+\mu^2)$；$E(\bar X^2)=D(\bar X)+[E(\bar X)]^2=\dfrac{\sigma^2}{n}+\mu^2$，故 $E(n\bar X^2)=\sigma^2+n\mu^2$。
$E[\sum(X_i-\bar X)^2]=(n-1)\sigma^2$，故 $E(S^2)=\dfrac{1}{n-1}\cdot(n-1)\sigma^2=\sigma^2$。$\square$

</details>

**3.** 证明 $\bar X$ 是 $\mu$ 的一致估计。

<details><summary>证明</summary>

$E(\bar X)=\mu$，$D(\bar X)=\sigma^2/n\to 0$。由切比雪夫不等式 $P\{|\bar X-\mu|\geq\varepsilon\}\leq\dfrac{D(\bar X)}{\varepsilon^2}=\dfrac{\sigma^2}{n\varepsilon^2}\to0$，故 $\bar X\xrightarrow{P}\mu$。$\square$

</details>

**4.** 设 $X_1,\ldots,X_n\sim U(0,\theta)$，证明 MLE $\hat\theta=X_{(n)}$ 是 $\theta$ 的相合估计但非无偏。

<details><summary>证明</summary>

**非无偏**：$X_{(n)}$ 的密度 $f_{X_{(n)}}(y)=n\left(\dfrac{y}{\theta}\right)^{n-1}\dfrac1\theta$（$0<y<\theta$）。
$$E(X_{(n)})=\int_0^\theta y\cdot n\frac{y^{n-1}}{\theta^n}dy=\frac{n}{n+1}\theta\neq\theta.$$
故有偏，无偏修正为 $\dfrac{n+1}{n}X_{(n)}$。

**相合**：对任意 $\varepsilon>0$，$P\{X_{(n)}-\theta<-\varepsilon\}=P\{X_{(n)}<\theta-\varepsilon\}=\left(\dfrac{\theta-\varepsilon}{\theta}\right)^n\to0$；又 $X_{(n)}\leq\theta$ 恒成立，故 $P\{|X_{(n)}-\theta|\geq\varepsilon\}\to0$，即 $X_{(n)}\xrightarrow{P}\theta$。$\square$

</details>

## 考点统计

| 考点 | 题号 | 题量 |
| ---- | ---- | ---- |
| 矩估计求解 | 填1、选1、计1 | 3 |
| MLE 求解 | 填2-4、选2、计2-4 | 7 |
| 无偏性与 $S^2$ | 填5、选3、证1-2 | 4 |
| 有效性 | 选4、计7 | 2 |
| 一致性 | 选5、证3-4 | 3 |
| 区间估计（单总体） | 填6-8、选6-9、计5-6 | 7 |
| 区间估计（两总体） | 选10、计8 | 2 |
| MLE 不变性 | 填10、计4 | 2 |

## 章节导航

- 上一级：[[MOC - 概率论与数理统计B]]
- 本章：[[MOC - 第7章]]
- 上一章习题：[[MOC - 第6章习题]]
- 下一章习题：[[MOC - 第8章习题]]
