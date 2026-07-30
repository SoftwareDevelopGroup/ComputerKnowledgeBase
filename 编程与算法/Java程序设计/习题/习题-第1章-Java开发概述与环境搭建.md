---
domain: 编程与算法
type: 习题
status: 整理中
created: 2026-07-26
course: Java程序设计
chapter: 1
tags: ["Java", "面向对象", "编程基础", "习题"]
source: 《Java程序设计》本科通用教材
---

# 习题-第1章-Java开发概述与环境搭建

> [!abstract] 本章习题说明
> 本章习题涵盖Java语言特点、JVM/JRE/JDK区别、编译运行流程等核心知识点。

## 一、选择题

1. Java语言的特点不包括（ ）
   A. 跨平台性
   B. 面向对象
   C. 指针操作
   D. 自动内存管理

2. JDK包含（ ）
   A. JRE和开发工具
   B. 仅JRE
   C. 仅JVM
   D. 仅开发工具

3. Java程序的编译结果是（ ）
   A. 机器码
   B. 字节码
   C. 汇编代码
   D. 源代码

4. Java程序运行时需要（ ）
   A. JDK
   B. JRE
   C. 编译器
   D. 编辑器

5. 以下哪个是Java的LTS版本（ ）
   A. JDK 10
   B. JDK 11
   C. JDK 12
   D. JDK 13

## 二、填空题

1. Java的核心特点包括：______、______、______、______。

2. JVM的中文全称是______。

3. JDK包含______和______。

4. Java程序的执行过程分为：______、______、______三个阶段。

5. Java源文件的扩展名是______，编译后的字节码文件扩展名是______。

## 三、简答题

1. 简述Java语言的主要特点。

2. 简述JVM、JRE、JDK的区别和关系。

3. 简述Java程序的编译运行流程。

4. 什么是跨平台性？Java如何实现跨平台？

5. 简述Java的应用领域。

## 四、编程题

1. 编写一个Java程序，输出"Hello, Java!"。

2. 编写一个Java程序，接收命令行参数并输出。

3. 编写一个Java程序，计算两个数的和。

## 参考答案

### 选择题答案

1. C
2. A
3. B
4. B
5. B

### 填空题答案

1. 跨平台性、面向对象、安全性、健壮性
2. Java虚拟机
3. JRE、开发工具
4. 编辑、编译、运行
5. .java、.class

### 编程题参考代码

**第1题**

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

**第2题**

```java
public class ArgsTest {
    public static void main(String[] args) {
        for (String arg : args) {
            System.out.println(arg);
        }
    }
}
```

**第3题**

```java
public class Sum {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        int sum = a + b;
        System.out.println("和为: " + sum);
    }
}
```