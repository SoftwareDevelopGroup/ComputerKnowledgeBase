---
domain: 编程与算法
type: 习题
status: 整理中
created: 2026-07-26
course: Java程序设计
chapter: 10
tags: ["Java", "面向对象", "编程基础", "习题"]
source: 《Java程序设计》本科通用教材
---

# 习题-第10章-I/O文件流基础

> [!abstract] 本章习题说明
> 本章习题涵盖I/O流概述、文件读写、缓冲流与字符流等核心知识点。

## 一、选择题

1. 字节流处理的是（ ）
   A. 文本数据
   B. 二进制数据
   C. 字符数据
   D. 字符串数据

2. 字符流处理的是（ ）
   A. 文本数据
   B. 二进制数据
   C. 字节数据
   D. 数字数据

3. File类用于（ ）
   A. 读取文件内容
   B. 写入文件内容
   C. 表示文件或目录路径
   D. 关闭文件

4. BufferedReader的优点是（ ）
   A. 支持按行读取
   B. 支持写入
   C. 支持随机访问
   D. 支持二进制数据

5. try-with-resources用于（ ）
   A. 自动关闭资源
   B. 抛出异常
   C. 捕获异常
   D. 声明异常

## 二、填空题

1. I/O流分为______流和______流。

2. 字节流的父类是______和______。

3. 字符流的父类是______和______。

4. FileInputStream用于______文件。

5. BufferedReader的______方法用于按行读取。

## 三、简答题

1. 简述字节流和字符流的区别。

2. 简述File类的常用方法。

3. 简述缓冲流的优点。

4. 简述try-with-resources的作用。

5. 简述文件操作的注意事项。

## 四、编程题

1. 编写一个Java程序，读取文本文件内容。

2. 编写一个Java程序，复制文件。

3. 编写一个Java程序，统计文件行数。

## 参考答案

### 选择题答案

1. B
2. A
3. C
4. A
5. A

### 填空题答案

1. 字节、字符
2. InputStream、OutputStream
3. Reader、Writer
4. 读取
5. readLine()

### 编程题参考代码

**第1题**

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadTextFile {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**第2题**

```java
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyFile {
    public static void main(String[] args) {
        try (BufferedInputStream bis = new BufferedInputStream(new FileInputStream("input.txt"));
             BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("output.txt"))) {
            
            byte[] buffer = new byte[1024];
            int length;
            while ((length = bis.read(buffer)) != -1) {
                bos.write(buffer, 0, length);
            }
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**第3题**

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class CountLines {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
            int count = 0;
            while (br.readLine() != null) {
                count++;
            }
            System.out.println("文件行数: " + count);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```