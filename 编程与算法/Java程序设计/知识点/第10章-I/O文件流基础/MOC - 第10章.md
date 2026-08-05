---
domain: 编程与算法
type: MOC
status: 整理中
created: 2026-07-26
course: Java程序设计
chapter: 10
tags: ["Java", "面向对象", "编程基础", "期末复习"]
prerequisites: ["第9章-常用工具类与集合基础"]
source: 《Java程序设计》本科通用教材
---

# 第10章-I/O文件流基础

> [!abstract] 本章定位
> 本章介绍Java的I/O文件流基础，包括字节流、字符流、文件操作等内容。

## 学习主线

```mermaid
flowchart LR
  A[I/O流概述] --> B[文件读写]
  B --> C[缓冲流与字符流]
```

## 章节内容

- [[10.1-I/O流概述.md]]：字节流、字符流、流的分类
- [[10.2-文件读写.md]]：File类、FileInputStream、FileOutputStream
- [[10.3-缓冲流与字符流.md]]：BufferedReader、BufferedWriter、PrintWriter

## 考点汇总

> [!important] 核心考点
> 1. 字节流和字符流的区别
> 2. File类的常用方法
> 3. FileInputStream和FileOutputStream的使用
> 4. BufferedReader和BufferedWriter的使用
> 5. try-with-resources的使用
> 6. 文件操作的异常处理

## 前后章节依赖

| 方向 | 章节 | 依赖关系 |
|-----|------|---------|
| 先修 | 第9章 | 集合可以与I/O配合使用 |
| 后续 | - | 本课程最后一章 |

## 复习自测

> [!question] 自测题
> 1. 字节流和字符流的区别是什么？
> 2. File类的常用方法有哪些？
> 3. 如何使用FileInputStream读取文件？
> 4. 如何使用BufferedReader读取文本文件？
> 5. try-with-resources的作用是什么？