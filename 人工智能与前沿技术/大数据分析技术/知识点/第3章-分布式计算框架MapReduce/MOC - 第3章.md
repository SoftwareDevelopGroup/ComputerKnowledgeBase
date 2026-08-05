---
domain: 人工智能与前沿技术
type: MOC
status: 整理中
created: 2026-07-27
course: 大数据分析技术
chapter: 3
tags: ["大数据", "分布式计算", "Hadoop", "Spark", "数据分析", "人工智能"]
prerequisites: ["第2章-分布式文件存储HDFS"]
source: 《大数据技术原理与应用》林子雨 本科通用教材
---

# 第3章-分布式计算框架MapReduce

> [!abstract] 本章定位
> 本章介绍MapReduce的编程模型、工作流程和Shuffle机制，是分布式计算的基础。

## 学习主线

```mermaid
flowchart LR
  A[MapReduce模型] --> B[Map阶段]
  A --> C[Shuffle阶段]
  A --> D[Reduce阶段]
```

## 章节内容

- [[3.1-MapReduce编程模型.md]]：Map函数、Reduce函数、键值对处理
- [[3.2-MapReduce工作流程.md]]：任务划分、执行流程、数据流动
- [[3.3-Shuffle机制.md]]：分区、排序、合并、归约

## 考点汇总

> [!important] 核心考点
> 1. MapReduce的编程模型：Map函数和Reduce函数的作用
> 2. MapReduce的工作流程：任务划分、执行流程
> 3. Shuffle机制：分区、排序、合并、归约
> 4. MapReduce的优缺点：优点和局限性
> 5. MapReduce与Spark的对比

## 前后章节依赖

| 方向 | 章节 | 依赖关系 |
|-----|------|---------|
| 先修 | 第2章 | HDFS是MapReduce的存储基础 |
| 后续 | 第4章 | Spark是MapReduce的改进 |

## 复习自测

> [!question] 自测题
> 1. MapReduce的编程模型是什么？Map函数和Reduce函数分别做什么？
> 2. MapReduce的工作流程是怎样的？
> 3. Shuffle阶段包含哪些步骤？
> 4. MapReduce有什么优缺点？
> 5. MapReduce与Spark有什么区别？