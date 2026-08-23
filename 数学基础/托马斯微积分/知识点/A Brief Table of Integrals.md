---
domain: 数学基础
subject: 托马斯微积分
cssclasses:
  - thomas-calculus
type: knowledge
chapter: Back Matter
section: A Brief Table of Integrals（积分简表）
tags: [微积分, 积分表, 不定积分, 定积分, 基本积分, 三角积分, 双曲积分, 托马斯微积分]
prerequisites:
  - "[[5.5 Indefinite Integrals and the Substitution Method]]"
  - "[[8.1 Using Basic Integration Formulas]]"
aliases: [积分简表, A Brief Table of Integrals, 积分表]
---

# A Brief Table of Integrals（积分简表）

> [!info] 📘 本节引言
> 这是托马斯微积分所附的常用积分简表，按被积函数的形式分类，供积分计算时查阅。表中字母 $a, b, c, k$ 均为常数，$n, m$ 为正整数，$C$ 为积分常数。

## 基本形式（Basic Forms）

$$ \int k\,dx = kx + C, \quad k \text{ 为任意常数} \tag{1} $$

$$ \int x^n\,dx = \frac{x^{n+1}}{n+1} + C, \quad n \neq -1 \tag{2} $$

$$ \int \frac{dx}{x} = \ln\lvert x\rvert + C \tag{3} $$

$$ \int e^x\,dx = e^x + C \tag{4} $$

$$ \int a^x\,dx = \frac{a^x}{\ln a} + C \quad (a > 0,\ a \neq 1) \tag{5} $$

$$ \int \sin x\,dx = -\cos x + C \tag{6} $$

$$ \int \cos x\,dx = \sin x + C \tag{7} $$

$$ \int \sec^2 x\,dx = \tan x + C \tag{8} $$

$$ \int \csc^2 x\,dx = -\cot x + C \tag{9} $$

$$ \int \sec x \tan x\,dx = \sec x + C \tag{10} $$

$$ \int \csc x \cot x\,dx = -\csc x + C \tag{11} $$

$$ \int \tan x\,dx = \ln\lvert\sec x\rvert + C \tag{12} $$

$$ \int \cot x\,dx = \ln\lvert\sin x\rvert + C \tag{13} $$

$$ \int \sinh x\,dx = \cosh x + C \tag{14} $$

$$ \int \cosh x\,dx = \sinh x + C \tag{15} $$

$$ \int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin\frac{x}{a} + C \tag{16} $$

$$ \int \frac{dx}{a^2 + x^2} = \frac{1}{a}\arctan\frac{x}{a} + C \tag{17} $$

$$ \int \frac{dx}{x\sqrt{x^2 - a^2}} = \frac{1}{a}\operatorname{arcsec}\left\lvert\frac{x}{a}\right\rvert + C \tag{18} $$

$$ \int \frac{dx}{\sqrt{a^2 + x^2}} = \sinh^{-1}\frac{x}{a} + C \quad (a > 0) \tag{19} $$

$$ \int \frac{dx}{\sqrt{x^2 - a^2}} = \cosh^{-1}\frac{x}{a} + C \quad (x > a > 0) \tag{20} $$

## 含 $ax + b$ 的形式（Forms Involving $ax + b$）

$$ \int (ax + b)^n\,dx = \frac{(ax + b)^{n+1}}{a(n+1)} + C, \quad n \neq -1 \tag{21} $$

$$ \int x(ax + b)^n\,dx = \frac{(ax + b)^{n+1}}{a^2}\left[\frac{ax + b}{n+2} - \frac{b}{n+1}\right] + C, \quad n \neq -1, -2 \tag{22} $$

$$ \int (ax + b)^{-1}\,dx = \frac{1}{a}\ln\lvert ax + b\rvert + C \tag{23} $$

$$ \int x(ax + b)^{-1}\,dx = \frac{x}{a} - \frac{b}{a^2}\ln\lvert ax + b\rvert + C \tag{24} $$

$$ \int x(ax + b)^{-2}\,dx = \frac{1}{a^2}\left[\ln\lvert ax + b\rvert + \frac{b}{ax + b}\right] + C \tag{25} $$

$$ \int \frac{dx}{x(ax + b)} = \frac{1}{b}\ln\left\lvert\frac{x}{ax + b}\right\rvert + C \tag{26} $$

$$ \int (\sqrt{ax + b})^n\,dx = \frac{2}{a}\frac{(\sqrt{ax + b})^{n+2}}{n+2} + C, \quad n \neq -2 \tag{27} $$

$$ \int \frac{\sqrt{ax + b}}{x}\,dx = 2\sqrt{ax + b} + b\int\frac{dx}{x\sqrt{ax + b}} + C \tag{28} $$

$$ \text{(a)} \quad \int \frac{dx}{x\sqrt{ax + b}} = \frac{1}{\sqrt{b}}\ln\left\lvert\frac{\sqrt{ax + b} - \sqrt{b}}{\sqrt{ax + b} + \sqrt{b}}\right\rvert + C \tag{29a} $$

$$ \text{(b)} \quad \int \frac{dx}{x\sqrt{ax - b}} = \frac{2}{\sqrt{b}}\arctan\sqrt{\frac{ax - b}{b}} + C \tag{29b} $$

$$ \int \frac{\sqrt{ax + b}}{x^2}\,dx = -\frac{\sqrt{ax + b}}{x} + \frac{a}{2}\int\frac{dx}{x\sqrt{ax + b}} + C \tag{30} $$

$$ \int \frac{dx}{x^2\sqrt{ax + b}} = -\frac{\sqrt{ax + b}}{bx} - \frac{a}{2b}\int\frac{dx}{x\sqrt{ax + b}} + C \tag{31} $$

## 含 $a^2 + x^2$ 的形式（Forms Involving $a^2 + x^2$）

$$ \int \frac{dx}{a^2 + x^2} = \frac{1}{a}\arctan\frac{x}{a} + C \tag{32} $$

$$ \int \frac{dx}{(a^2 + x^2)^2} = \frac{x}{2a^2(a^2 + x^2)} + \frac{1}{2a^3}\arctan\frac{x}{a} + C \tag{33} $$

$$ \int \frac{dx}{\sqrt{a^2 + x^2}} = \sinh^{-1}\frac{x}{a} + C = \ln\left(x + \sqrt{a^2 + x^2}\right) + C \tag{34} $$

$$ \int \sqrt{a^2 + x^2}\,dx = \frac{x}{2}\sqrt{a^2 + x^2} + \frac{a^2}{2}\ln\left(x + \sqrt{a^2 + x^2}\right) + C \tag{35} $$

$$ \int x^2\sqrt{a^2 + x^2}\,dx = \frac{x}{8}(a^2 + 2x^2)\sqrt{a^2 + x^2} - \frac{a^4}{8}\ln\left(x + \sqrt{a^2 + x^2}\right) + C \tag{36} $$

$$ \int \frac{\sqrt{a^2 + x^2}}{x}\,dx = \sqrt{a^2 + x^2} - a\ln\left\lvert\frac{a + \sqrt{a^2 + x^2}}{x}\right\rvert + C \tag{37} $$

$$ \int \frac{\sqrt{a^2 + x^2}}{x^2}\,dx = \ln\left(x + \sqrt{a^2 + x^2}\right) - \frac{\sqrt{a^2 + x^2}}{x} + C \tag{38} $$

$$ \int \frac{x^2}{\sqrt{a^2 + x^2}}\,dx = -\frac{a^2}{2}\ln\left(x + \sqrt{a^2 + x^2}\right) + \frac{x\sqrt{a^2 + x^2}}{2} + C \tag{39} $$

$$ \int \frac{dx}{x\sqrt{a^2 + x^2}} = -\frac{1}{a}\ln\left\lvert\frac{a + \sqrt{a^2 + x^2}}{x}\right\rvert + C \tag{40} $$

$$ \int \frac{dx}{x^2\sqrt{a^2 + x^2}} = -\frac{\sqrt{a^2 + x^2}}{a^2 x} + C \tag{41} $$

## 含 $a^2 - x^2$ 的形式（Forms Involving $a^2 - x^2$）

$$ \int \frac{dx}{a^2 - x^2} = \frac{1}{2a}\ln\left\lvert\frac{x + a}{x - a}\right\rvert + C \tag{42} $$

$$ \int \frac{dx}{(a^2 - x^2)^2} = \frac{x}{2a^2(a^2 - x^2)} + \frac{1}{4a^3}\ln\left\lvert\frac{x + a}{x - a}\right\rvert + C \tag{43} $$

$$ \int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin\frac{x}{a} + C \tag{44} $$

$$ \int \sqrt{a^2 - x^2}\,dx = \frac{x}{2}\sqrt{a^2 - x^2} + \frac{a^2}{2}\arcsin\frac{x}{a} + C \tag{45} $$

$$ \int x^2\sqrt{a^2 - x^2}\,dx = \frac{a^4}{8}\arcsin\frac{x}{a} - \frac{1}{8}x\sqrt{a^2 - x^2}(a^2 - 2x^2) + C \tag{46} $$

$$ \int \frac{\sqrt{a^2 - x^2}}{x}\,dx = \sqrt{a^2 - x^2} - a\ln\left\lvert\frac{a + \sqrt{a^2 - x^2}}{x}\right\rvert + C \tag{47} $$

$$ \int \frac{\sqrt{a^2 - x^2}}{x^2}\,dx = -\arcsin\frac{x}{a} - \frac{\sqrt{a^2 - x^2}}{x} + C \tag{48} $$

$$ \int \frac{x^2}{\sqrt{a^2 - x^2}}\,dx = \frac{a^2}{2}\arcsin\frac{x}{a} - \frac{1}{2}x\sqrt{a^2 - x^2} + C \tag{49} $$

$$ \int \frac{dx}{x\sqrt{a^2 - x^2}} = -\frac{1}{a}\ln\left\lvert\frac{a + \sqrt{a^2 - x^2}}{x}\right\rvert + C \tag{50} $$

$$ \int \frac{dx}{x^2\sqrt{a^2 - x^2}} = -\frac{\sqrt{a^2 - x^2}}{a^2 x} + C \tag{51} $$

## 含 $x^2 - a^2$ 的形式（Forms Involving $x^2 - a^2$）

$$ \int \frac{dx}{\sqrt{x^2 - a^2}} = \ln\lvert x + \sqrt{x^2 - a^2}\rvert + C \tag{52} $$

$$ \int \sqrt{x^2 - a^2}\,dx = \frac{x}{2}\sqrt{x^2 - a^2} - \frac{a^2}{2}\ln\lvert x + \sqrt{x^2 - a^2}\rvert + C \tag{53} $$

$$ \int (\sqrt{x^2 - a^2})^n\,dx = \frac{x(\sqrt{x^2 - a^2})^n}{n+1} - \frac{na^2}{n+1}\int(\sqrt{x^2 - a^2})^{n-2}\,dx, \quad n \neq -1 \tag{54} $$

$$ \int \frac{dx}{(\sqrt{x^2 - a^2})^n} = \frac{x(\sqrt{x^2 - a^2})^{2-n}}{(2-n)a^2} - \frac{n-3}{(n-2)a^2}\int\frac{dx}{(\sqrt{x^2 - a^2})^{n-2}}, \quad n \neq 2 \tag{55} $$

$$ \int x(\sqrt{x^2 - a^2})^n\,dx = \frac{(\sqrt{x^2 - a^2})^{n+2}}{n+2} + C, \quad n \neq -2 \tag{56} $$

$$ \int x^2\sqrt{x^2 - a^2}\,dx = \frac{x}{8}(2x^2 - a^2)\sqrt{x^2 - a^2} - \frac{a^4}{8}\ln\lvert x + \sqrt{x^2 - a^2}\rvert + C \tag{57} $$

$$ \int \frac{\sqrt{x^2 - a^2}}{x}\,dx = \sqrt{x^2 - a^2} - a\operatorname{arcsec}\left\lvert\frac{x}{a}\right\rvert + C \tag{58} $$

$$ \int \frac{\sqrt{x^2 - a^2}}{x^2}\,dx = \ln\lvert x + \sqrt{x^2 - a^2}\rvert - \frac{\sqrt{x^2 - a^2}}{x} + C \tag{59} $$

$$ \int \frac{x^2}{\sqrt{x^2 - a^2}}\,dx = \frac{a^2}{2}\ln\lvert x + \sqrt{x^2 - a^2}\rvert + \frac{x}{2}\sqrt{x^2 - a^2} + C \tag{60} $$

$$ \int \frac{dx}{x\sqrt{x^2 - a^2}} = \frac{1}{a}\operatorname{arcsec}\left\lvert\frac{x}{a}\right\rvert + C = \frac{1}{a}\operatorname{arccos}\left\lvert\frac{a}{x}\right\rvert + C \tag{61} $$

$$ \int \frac{dx}{x^2\sqrt{x^2 - a^2}} = \frac{\sqrt{x^2 - a^2}}{a^2 x} + C \tag{62} $$

## 三角函数形式（Trigonometric Forms）

$$ \int \sin ax\,dx = -\frac{1}{a}\cos ax + C \tag{63} $$

$$ \int \cos ax\,dx = \frac{1}{a}\sin ax + C \tag{64} $$

$$ \int \sin^2 ax\,dx = \frac{x}{2} - \frac{\sin 2ax}{4a} + C \tag{65} $$

$$ \int \cos^2 ax\,dx = \frac{x}{2} + \frac{\sin 2ax}{4a} + C \tag{66} $$

$$ \int \sin^n ax\,dx = -\frac{\sin^{n-1} ax \cos ax}{na} + \frac{n-1}{n}\int\sin^{n-2} ax\,dx \tag{67} $$

$$ \int \cos^n ax\,dx = \frac{\cos^{n-1} ax \sin ax}{na} + \frac{n-1}{n}\int\cos^{n-2} ax\,dx \tag{68} $$

$$ \text{(a)} \quad \int \sin ax \cos bx\,dx = -\frac{\cos(a+b)x}{2(a+b)} - \frac{\cos(a-b)x}{2(a-b)} + C, \quad a^2 \neq b^2 \tag{69a} $$

$$ \text{(b)} \quad \int \sin ax \sin bx\,dx = \frac{\sin(a-b)x}{2(a-b)} - \frac{\sin(a+b)x}{2(a+b)} + C, \quad a^2 \neq b^2 \tag{69b} $$

$$ \text{(c)} \quad \int \cos ax \cos bx\,dx = \frac{\sin(a-b)x}{2(a-b)} + \frac{\sin(a+b)x}{2(a+b)} + C, \quad a^2 \neq b^2 \tag{69c} $$

$$ \int \sin ax \cos ax\,dx = -\frac{\cos 2ax}{4a} + C \tag{70} $$

$$ \int \sin^n ax \cos ax\,dx = \frac{\sin^{n+1} ax}{(n+1)a} + C, \quad n \neq -1 \tag{71} $$

$$ \int \frac{\cos ax}{\sin ax}\,dx = \frac{1}{a}\ln\lvert\sin ax\rvert + C \tag{72} $$

$$ \int \cos^n ax \sin ax\,dx = -\frac{\cos^{n+1} ax}{(n+1)a} + C, \quad n \neq -1 \tag{73} $$

$$ \int \frac{\sin ax}{\cos ax}\,dx = -\frac{1}{a}\ln\lvert\cos ax\rvert + C \tag{74} $$

$$ \int \sin^n ax \cos^m ax\,dx = -\frac{\sin^{n-1} ax \cos^{m+1} ax}{a(m+n)} + \frac{n-1}{m+n}\int\sin^{n-2} ax \cos^m ax\,dx, \quad n \neq -m \quad (\text{降 } \sin^n ax) \tag{75} $$

$$ \int \sin^n ax \cos^m ax\,dx = \frac{\sin^{n+1} ax \cos^{m-1} ax}{a(m+n)} + \frac{m-1}{m+n}\int\sin^n ax \cos^{m-2} ax\,dx, \quad m \neq -n \quad (\text{降 } \cos^m ax) \tag{76} $$

$$ \int \frac{dx}{b + c\sin ax} = \frac{-2}{a\sqrt{b^2 - c^2}}\arctan\left[\sqrt{\frac{b-c}{b+c}}\tan\left(\frac{\pi}{4} - \frac{ax}{2}\right)\right] + C, \quad b^2 > c^2 \tag{77} $$

$$ \int \frac{dx}{b + c\sin ax} = \frac{-1}{a\sqrt{c^2 - b^2}}\ln\left\lvert\frac{c + b\sin ax + \sqrt{c^2 - b^2}\cos ax}{b + c\sin ax}\right\rvert + C, \quad b^2 < c^2 \tag{78} $$

$$ \int \frac{dx}{1 + \sin ax} = -\frac{1}{a}\tan\left(\frac{\pi}{4} - \frac{ax}{2}\right) + C \tag{79} $$

$$ \int \frac{dx}{1 - \sin ax} = \frac{1}{a}\tan\left(\frac{\pi}{4} + \frac{ax}{2}\right) + C \tag{80} $$

$$ \int \frac{dx}{b + c\cos ax} = \frac{2}{a\sqrt{b^2 - c^2}}\arctan\left[\sqrt{\frac{b-c}{b+c}}\tan\frac{ax}{2}\right] + C, \quad b^2 > c^2 \tag{81} $$

$$ \int \frac{dx}{b + c\cos ax} = \frac{1}{a\sqrt{c^2 - b^2}}\ln\left\lvert\frac{c + b\cos ax + \sqrt{c^2 - b^2}\sin ax}{b + c\cos ax}\right\rvert + C, \quad b^2 < c^2 \tag{82} $$

$$ \int \frac{dx}{1 + \cos ax} = \frac{1}{a}\tan\frac{ax}{2} + C \tag{83} $$

$$ \int \frac{dx}{1 - \cos ax} = -\frac{1}{a}\cot\frac{ax}{2} + C \tag{84} $$

$$ \int x\sin ax\,dx = \frac{1}{a^2}\sin ax - \frac{x}{a}\cos ax + C \tag{85} $$

$$ \int x\cos ax\,dx = \frac{1}{a^2}\cos ax + \frac{x}{a}\sin ax + C \tag{86} $$

$$ \int x^n\sin ax\,dx = -\frac{x^n}{a}\cos ax + \frac{n}{a}\int x^{n-1}\cos ax\,dx \tag{87} $$

$$ \int x^n\cos ax\,dx = \frac{x^n}{a}\sin ax - \frac{n}{a}\int x^{n-1}\sin ax\,dx \tag{88} $$

$$ \int \tan ax\,dx = \frac{1}{a}\ln\lvert\sec ax\rvert + C \tag{89} $$

$$ \int \cot ax\,dx = \frac{1}{a}\ln\lvert\sin ax\rvert + C \tag{90} $$

$$ \int \tan^2 ax\,dx = \frac{1}{a}\tan ax - x + C \tag{91} $$

$$ \int \cot^2 ax\,dx = -\frac{1}{a}\cot ax - x + C \tag{92} $$

$$ \int \tan^n ax\,dx = \frac{\tan^{n-1} ax}{a(n-1)} - \int\tan^{n-2} ax\,dx, \quad n \neq 1 \tag{93} $$

$$ \int \cot^n ax\,dx = -\frac{\cot^{n-1} ax}{a(n-1)} - \int\cot^{n-2} ax\,dx, \quad n \neq 1 \tag{94} $$

$$ \int \sec ax\,dx = \frac{1}{a}\ln\lvert\sec ax + \tan ax\rvert + C \tag{95} $$

$$ \int \csc ax\,dx = -\frac{1}{a}\ln\lvert\csc ax + \cot ax\rvert + C \tag{96} $$

$$ \int \sec^2 ax\,dx = \frac{1}{a}\tan ax + C \tag{97} $$

$$ \int \csc^2 ax\,dx = -\frac{1}{a}\cot ax + C \tag{98} $$

$$ \int \sec^n ax\,dx = \frac{\sec^{n-2} ax \tan ax}{a(n-1)} + \frac{n-2}{n-1}\int\sec^{n-2} ax\,dx, \quad n \neq 1 \tag{99} $$

$$ \int \csc^n ax\,dx = -\frac{\csc^{n-2} ax \cot ax}{a(n-1)} + \frac{n-2}{n-1}\int\csc^{n-2} ax\,dx, \quad n \neq 1 \tag{100} $$

$$ \int \sec^n ax \tan ax\,dx = \frac{\sec^n ax}{na} + C, \quad n \neq 0 \tag{101} $$

$$ \int \csc^n ax \cot ax\,dx = -\frac{\csc^n ax}{na} + C, \quad n \neq 0 \tag{102} $$

## 反三角函数形式（Inverse Trigonometric Forms）

$$ \int \arcsin ax\,dx = x\arcsin ax + \frac{1}{a}\sqrt{1 - a^2x^2} + C \tag{103} $$

$$ \int \arccos ax\,dx = x\arccos ax - \frac{1}{a}\sqrt{1 - a^2x^2} + C \tag{104} $$

$$ \int \arctan ax\,dx = x\arctan ax - \frac{1}{2a}\ln(1 + a^2x^2) + C \tag{105} $$

$$ \int x^n\arcsin ax\,dx = \frac{x^{n+1}}{n+1}\arcsin ax - \frac{a}{n+1}\int\frac{x^{n+1}\,dx}{\sqrt{1 - a^2x^2}}, \quad n \neq -1 \tag{106} $$

$$ \int x^n\arccos ax\,dx = \frac{x^{n+1}}{n+1}\arccos ax + \frac{a}{n+1}\int\frac{x^{n+1}\,dx}{\sqrt{1 - a^2x^2}}, \quad n \neq -1 \tag{107} $$

$$ \int x^n\arctan ax\,dx = \frac{x^{n+1}}{n+1}\arctan ax - \frac{a}{n+1}\int\frac{x^{n+1}\,dx}{1 + a^2x^2}, \quad n \neq -1 \tag{108} $$

## 指数与对数形式（Exponential and Logarithmic Forms）

$$ \int e^{ax}\,dx = \frac{1}{a}e^{ax} + C \tag{109} $$

$$ \int b^{ax}\,dx = \frac{1}{a}\frac{b^{ax}}{\ln b} + C, \quad b > 0,\ b \neq 1 \tag{110} $$

$$ \int xe^{ax}\,dx = \frac{e^{ax}}{a^2}(ax - 1) + C \tag{111} $$

$$ \int x^n e^{ax}\,dx = \frac{1}{a}x^n e^{ax} - \frac{n}{a}\int x^{n-1} e^{ax}\,dx \tag{112} $$

$$ \int x^n b^{ax}\,dx = \frac{x^n b^{ax}}{a\ln b} - \frac{n}{a\ln b}\int x^{n-1} b^{ax}\,dx, \quad b > 0,\ b \neq 1 \tag{113} $$

$$ \int e^{ax}\sin bx\,dx = \frac{e^{ax}}{a^2 + b^2}(a\sin bx - b\cos bx) + C \tag{114} $$

$$ \int e^{ax}\cos bx\,dx = \frac{e^{ax}}{a^2 + b^2}(a\cos bx + b\sin bx) + C \tag{115} $$

$$ \int \ln ax\,dx = x\ln ax - x + C \tag{116} $$

$$ \int x^n(\ln ax)^m\,dx = \frac{x^{n+1}(\ln ax)^m}{n+1} - \frac{m}{n+1}\int x^n(\ln ax)^{m-1}\,dx, \quad n \neq -1 \tag{117} $$

$$ \int x^{-1}(\ln ax)^m\,dx = \frac{(\ln ax)^{m+1}}{m+1} + C, \quad m \neq -1 \tag{118} $$

$$ \int \frac{dx}{x\ln ax} = \ln\lvert\ln ax\rvert + C \tag{119} $$

## 含 $\sqrt{2ax - x^2},\ a > 0$ 的形式（Forms Involving $\sqrt{2ax - x^2},\ a > 0$）

$$ \int \frac{dx}{\sqrt{2ax - x^2}} = \arcsin\left(\frac{x - a}{a}\right) + C \tag{120} $$

$$ \int \sqrt{2ax - x^2}\,dx = \frac{x - a}{2}\sqrt{2ax - x^2} + \frac{a^2}{2}\arcsin\left(\frac{x - a}{a}\right) + C \tag{121} $$

$$ \int (\sqrt{2ax - x^2})^n\,dx = \frac{(x - a)(\sqrt{2ax - x^2})^n}{n+1} + \frac{na^2}{n+1}\int(\sqrt{2ax - x^2})^{n-2}\,dx \tag{122} $$

$$ \int \frac{dx}{(\sqrt{2ax - x^2})^n} = \frac{(x - a)(\sqrt{2ax - x^2})^{2-n}}{(n-2)a^2} + \frac{n-3}{(n-2)a^2}\int\frac{dx}{(\sqrt{2ax - x^2})^{n-2}} \tag{123} $$

$$ \int x\sqrt{2ax - x^2}\,dx = \frac{(x + a)(2x - 3a)\sqrt{2ax - x^2}}{6} + \frac{a^3}{2}\arcsin\left(\frac{x - a}{a}\right) + C \tag{124} $$

$$ \int \frac{\sqrt{2ax - x^2}}{x}\,dx = \sqrt{2ax - x^2} + a\arcsin\left(\frac{x - a}{a}\right) + C \tag{125} $$

$$ \int \frac{\sqrt{2ax - x^2}}{x^2}\,dx = -2\sqrt{\frac{2a - x}{x}} - \arcsin\left(\frac{x - a}{a}\right) + C \tag{126} $$

$$ \int \frac{x\,dx}{\sqrt{2ax - x^2}} = a\arcsin\left(\frac{x - a}{a}\right) - \sqrt{2ax - x^2} + C \tag{127} $$

$$ \int \frac{dx}{x\sqrt{2ax - x^2}} = -\frac{1}{a}\sqrt{\frac{2a - x}{x}} + C \tag{128} $$

## 双曲函数形式（Hyperbolic Forms）

$$ \int \sinh ax\,dx = \frac{1}{a}\cosh ax + C \tag{129} $$

$$ \int \cosh ax\,dx = \frac{1}{a}\sinh ax + C \tag{130} $$

$$ \int \sinh^2 ax\,dx = \frac{\sinh 2ax}{4a} - \frac{x}{2} + C \tag{131} $$

$$ \int \cosh^2 ax\,dx = \frac{\sinh 2ax}{4a} + \frac{x}{2} + C \tag{132} $$

$$ \int \sinh^n ax\,dx = \frac{\sinh^{n-1} ax \cosh ax}{na} - \frac{n-1}{n}\int\sinh^{n-2} ax\,dx, \quad n \neq 0 \tag{133} $$

$$ \int \cosh^n ax\,dx = \frac{\cosh^{n-1} ax \sinh ax}{na} + \frac{n-1}{n}\int\cosh^{n-2} ax\,dx, \quad n \neq 0 \tag{134} $$

$$ \int x\sinh ax\,dx = \frac{x}{a}\cosh ax - \frac{1}{a^2}\sinh ax + C \tag{135} $$

$$ \int x\cosh ax\,dx = \frac{x}{a}\sinh ax - \frac{1}{a^2}\cosh ax + C \tag{136} $$

$$ \int x^n\sinh ax\,dx = \frac{x^n}{a}\cosh ax - \frac{n}{a}\int x^{n-1}\cosh ax\,dx \tag{137} $$

$$ \int x^n\cosh ax\,dx = \frac{x^n}{a}\sinh ax - \frac{n}{a}\int x^{n-1}\sinh ax\,dx \tag{138} $$

$$ \int \tanh ax\,dx = \frac{1}{a}\ln(\cosh ax) + C \tag{139} $$

$$ \int \coth ax\,dx = \frac{1}{a}\ln\lvert\sinh ax\rvert + C \tag{140} $$

$$ \int \tanh^2 ax\,dx = x - \frac{1}{a}\tanh ax + C \tag{141} $$

$$ \int \coth^2 ax\,dx = x - \frac{1}{a}\coth ax + C \tag{142} $$

$$ \int \tanh^n ax\,dx = -\frac{\tanh^{n-1} ax}{(n-1)a} + \int\tanh^{n-2} ax\,dx, \quad n \neq 1 \tag{143} $$

$$ \int \coth^n ax\,dx = -\frac{\coth^{n-1} ax}{(n-1)a} + \int\coth^{n-2} ax\,dx, \quad n \neq 1 \tag{144} $$

$$ \int \operatorname{sech} ax\,dx = \frac{1}{a}\arcsin(\tanh ax) + C \tag{145} $$

$$ \int \operatorname{csch} ax\,dx = \frac{1}{a}\ln\left\lvert\tanh\frac{ax}{2}\right\rvert + C \tag{146} $$

$$ \int \operatorname{sech}^2 ax\,dx = \frac{1}{a}\tanh ax + C \tag{147} $$

$$ \int \operatorname{csch}^2 ax\,dx = -\frac{1}{a}\coth ax + C \tag{148} $$

$$ \int \operatorname{sech}^n ax\,dx = \frac{\operatorname{sech}^{n-2} ax \tanh ax}{(n-1)a} + \frac{n-2}{n-1}\int\operatorname{sech}^{n-2} ax\,dx, \quad n \neq 1 \tag{149} $$

$$ \int \operatorname{csch}^n ax\,dx = -\frac{\operatorname{csch}^{n-2} ax \coth ax}{(n-1)a} - \frac{n-2}{n-1}\int\operatorname{csch}^{n-2} ax\,dx, \quad n \neq 1 \tag{150} $$

$$ \int \operatorname{sech}^n ax \tanh ax\,dx = -\frac{\operatorname{sech}^n ax}{na} + C, \quad n \neq 0 \tag{151} $$

$$ \int \operatorname{csch}^n ax \coth ax\,dx = -\frac{\operatorname{csch}^n ax}{na} + C, \quad n \neq 0 \tag{152} $$

$$ \int e^{ax}\sinh bx\,dx = \frac{e^{ax}}{2}\left[\frac{e^{bx}}{a+b} - \frac{e^{-bx}}{a-b}\right] + C, \quad a^2 \neq b^2 \tag{153} $$

$$ \int e^{ax}\cosh bx\,dx = \frac{e^{ax}}{2}\left[\frac{e^{bx}}{a+b} + \frac{e^{-bx}}{a-b}\right] + C, \quad a^2 \neq b^2 \tag{154} $$

## 若干定积分（Some Definite Integrals）

$$ \int_0^{\infty} x^{n-1} e^{-x}\,dx = \Gamma(n) = (n-1)!, \quad n > 0 \tag{155} $$

$$ \int_0^{\infty} e^{-ax^2}\,dx = \frac{1}{2}\sqrt{\frac{\pi}{a}}, \quad a > 0 \tag{156} $$

$$ \int_0^{\pi/2} \sin^n x\,dx = \int_0^{\pi/2} \cos^n x\,dx = \begin{cases} \dfrac{1 \cdot 3 \cdot 5 \cdots (n-1)}{2 \cdot 4 \cdot 6 \cdots n} \cdot \dfrac{\pi}{2}, & \text{若 } n \text{ 为偶整数且 } n \ge 2 \\[6pt] \dfrac{2 \cdot 4 \cdot 6 \cdots (n-1)}{3 \cdot 5 \cdot 7 \cdots n}, & \text{若 } n \text{ 为奇整数且 } n \ge 3 \end{cases} \tag{157} $$
