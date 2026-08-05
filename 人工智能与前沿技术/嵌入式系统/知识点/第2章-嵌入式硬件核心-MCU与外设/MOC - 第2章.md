---
domain: 人工智能与前沿技术
type: MOC
status: 整理中
created: 2026-07-29
course: 嵌入式系统
chapter: 2
tags: ["嵌入式","MCU","RTOS","边缘AI","底层开发","物联网"]
prerequisites: ["第1章-嵌入式系统基础概念与软硬件架构"]
source: 《嵌入式系统原理及应用》本科通用教材、STM32开发实战手册
---

# 第2章 嵌入式硬件核心：MCU与外设

> [!abstract] 本章定位
> 本章深入MCU内部架构，学习各类外设的原理与配置方法，为后续驱动开发打下基础。

## 学习主线

```mermaid
flowchart LR
    A[MCU架构] --> B[时钟与启动]
    B --> C[GPIO]
    C --> D[定时器/PWM]
    D --> E[ADC/DAC]
```

## 章节内容

- [[2.1-MCU核心架构与启动流程]]：ARM架构、时钟树、Boot流程
- [[2.2-GPIO与中断控制器]]：GPIO配置、EXTI中断、NVIC
- [[2.3-定时器、ADC与DAC外设]]：定时器/PWM、ADC采样、DAC输出

## 核心考点

> [!important] 必掌握
> 1. Cortex-M内核架构、寄存器组、寻址模式
> 2. 时钟源选择与时钟树配置（HSI/HSE/LSI/LSE）
> 3. 启动流程：BootLoader → SystemInit → main
> 4. GPIO六种模式的区别与使用场景
> 5. EXTI外部中断配置与NVIC优先级分组
> 6. 定时器的计数模式、PWM输出、输入捕获
> 7. ADC的转换模式、DMA传输、校准

## 知识图谱

```mermaid
mindmap
  root((MCU与外设))
    MCU核心
      Cortex-M架构
      寄存器组
      流水线
      中断向量表
    时钟系统
      HSI内部
      HSE外部
      LSI内部低功耗
      LSE外部低功耗
      PLL锁相环
    GPIO
      输入模式
      输出模式
      复用功能
      模拟模式
    定时器
      基本定时器
      通用定时器
      高级定时器
      PWM
      输入捕获
    ADC
      单次转换
      连续转换
      扫描模式
      注入通道
    中断系统
      EXTI
      NVIC
      优先级分组
```

## 复习自测

> [!question] 自测题
> 1. Cortex-M3的三级流水线是什么？
> 2. STM32的时钟树是怎样的？PLL如何配置？
> 3. 描述MCU的启动流程。
> 4. GPIO的六种模式分别是什么？适用场景？
> 5. NVIC的优先级分组有哪几种？
> 6. 如何配置定时器输出PWM？
> 7. ADC的DMA模式如何配置？