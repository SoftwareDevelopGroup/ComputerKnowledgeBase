---
domain: 人工智能与前沿技术
type: MOC
status: 整理中
created: 2026-07-29
course: 嵌入式系统
chapter: 8
tags: ["嵌入式","MCU","RTOS","边缘AI","底层开发","物联网"]
prerequisites: ["第7章-嵌入式人机交互与传感器采集"]
source: 《嵌入式系统原理及应用》本科通用教材、TensorFlow Lite Micro文档
---

# 第8章 嵌入式AI部署

> [!abstract] 本章定位
> 本章学习边缘计算、轻量化模型、嵌入式AI框架和实际部署方法。

## 学习主线

```mermaid
flowchart LR
    A[AI基础] --> B[边缘计算]
    B --> C[模型优化]
    C --> D[TFLite Micro]
    D --> E[MCU部署]
    E --> F[应用实例]
```

## 章节内容

- [[8.1-边缘计算与轻量化模型]]：边缘计算概念、模型压缩、量化
- [[8.2-TensorFlow Lite Micro]]：TFLM框架、解释器、算子
- [[8.3-MCU AI部署实践]]：数据采集、模型生成、部署流程

## 核心考点

> [!important] 必掌握
> 1. 边缘计算与云计算的区别
> 2. 模型量化的基本原理（INT8）
> 3. TensorFlow Lite Micro的架构
> 4. TFLM在STM32上的移植
> 5. AI模型的内存布局
> 6. 典型嵌入式AI应用（关键词检测、图像分类）

## 复习自测

> [!question] 自测题
> 1. 什么是边缘计算？为什么要在边缘设备上部署AI？
> 2. 模型量化（Float32→INT8）的基本步骤是什么？
> 3. TensorFlow Lite Micro的四大组件是什么？
> 4. 如何将训练好的模型转换为TFLite格式？
> 5. 在资源受限的MCU上运行AI需要考虑哪些因素？
> 6. 如何优化AI模型以适应嵌入式设备？