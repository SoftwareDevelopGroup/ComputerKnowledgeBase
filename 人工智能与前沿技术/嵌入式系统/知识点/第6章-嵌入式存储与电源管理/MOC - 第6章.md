---
domain: 人工智能与前沿技术
type: MOC
status: 整理中
created: 2026-07-29
course: 嵌入式系统
chapter: 6
tags: ["嵌入式","MCU","RTOS","边缘AI","底层开发","物联网"]
prerequisites: ["第5章-实时操作系统RTOS内核原理"]
source: 《嵌入式系统原理及应用》本科通用教材、STM32开发实战手册
---

# 第6章 嵌入式存储与电源管理

> [!abstract] 本章定位
> 本章学习嵌入式系统的存储介质、存储管理和电源管理技术。

## 学习主线

```mermaid
flowchart LR
    A[存储介质] --> B[Flash存储器]
    B --> C[EEPROM]
    C --> D[SD卡与文件系统]
    D --> E[电源管理]
    E --> F[低功耗设计]
```

## 章节内容

- [[6.1-Flash与EEPROM存储]]：Flash工作原理、EEPROM特性、驱动实现
- [[6.2-SD卡与文件系统]]：SD卡协议、FatFs文件系统、读写操作
- [[6.3-电源管理与低功耗]]：电源模块、睡眠模式、功耗优化

## 核心考点

> [!important] 必掌握
> 1. Flash存储器的擦写机制与寿命
> 2. EEPROM与Flash的区别与应用场景
> 3. SPI Flash的读写时序
> 4. SD卡的SPI模式初始化与读写
> 5. FatFs文件系统的移植与使用
> 6. STM32的睡眠、停机、待机模式
> 7. 低功耗设计的基本原则

## 复习自测

> [!question] 自测题
> 1. Flash存储器有哪些类型？各有什么特点？
> 2. 为什么Flash的擦写次数有限？
> 3. EEPROM和Flash在使用上有什么区别？
> 4. 如何通过SPI接口读取SD卡？
> 5. FatFs文件系统如何初始化和使用？
> 6. STM32有哪几种低功耗模式？进入和退出条件是什么？