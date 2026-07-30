---
domain: 人工智能与前沿技术
type: 习题
status: 整理中
created: 2026-07-27
course: 大数据分析技术
chapter: 4
tags: ["大数据", "习题", "期末复习", "大数据开发"]
prerequisites: ["[[知识点/第4章-Spark分布式计算引擎/MOC - 第4章]]"]
source: 大数据课后习题、本科期末试卷、企业面试真题汇编
---

# 习题-第4章-Spark分布式计算引擎

> [!abstract] 本章习题概述
> 本章习题涵盖Spark的架构、RDD编程模型和Spark SQL，帮助巩固Spark核心知识。

## 一、选择题

### 4.1 Spark架构与核心概念

**题目1**：Spark的核心抽象是（ ）

A. DataFrame
B. Dataset
C. RDD
D. SparkContext

**答案**：C

**解析**：RDD（Resilient Distributed Dataset）是Spark的核心抽象。

---

**题目2**：Spark的Driver负责（ ）

A. 执行具体的计算任务
B. 管理集群资源
C. 调度任务
D. 存储数据

**答案**：C

**解析**：Driver负责调度任务和管理作业执行。

---

### 4.2 RDD编程模型

**题目3**：以下哪个操作是RDD的Transformation操作？（ ）

A. count()
B. collect()
C. map()
D. saveAsTextFile()

**答案**：C

**解析**：map()是Transformation操作，其他都是Action操作。

---

**题目4**：以下哪个操作是RDD的Action操作？（ ）

A. filter()
B. reduceByKey()
C. take()
D. join()

**答案**：C

**解析**：take()是Action操作，其他都是Transformation操作。

---

### 4.3 Spark SQL与DataFrame

**题目5**：Spark SQL支持的数据源不包括（ ）

A. CSV
B. JSON
C. HDFS
D. XML

**答案**：D

**解析**：Spark SQL支持CSV、JSON、Parquet等数据源，但不直接支持XML。

---

**题目6**：DataFrame和RDD的区别是（ ）

A. DataFrame是弱类型的，RDD是强类型的
B. DataFrame是强类型的，RDD是弱类型的
C. DataFrame有Schema信息，RDD没有
D. DataFrame没有Schema信息，RDD有

**答案**：C

**解析**：DataFrame有Schema信息，RDD没有Schema信息。

---

## 二、填空题

### 4.1 Spark架构与核心概念

**题目1**：Spark的运行模式包括______、______、______和______。

**答案**：Local模式、Standalone模式、YARN模式、Mesos模式

---

**题目2**：Spark的执行模型中，Driver负责______，Executor负责______。

**答案**：调度任务、执行具体的计算任务

---

### 4.2 RDD编程模型

**题目3**：RDD的特性包括______、______和______。

**答案**：分区、只读、容错

---

**题目4**：RDD的操作分为______和______两类。

**答案**：Transformation、Action

---

### 4.3 Spark SQL与DataFrame

**题目5**：Spark SQL支持______、______和______三种查询方式。

**答案**：SQL查询、DataFrame API、Dataset API

---

**题目6**：DataFrame的创建方式包括______、______和______。

**答案**：从RDD创建、从数据源创建、从Hive表创建

---

## 三、简答题

### 4.1 Spark架构与核心概念

**题目1**：请简述Spark的架构设计。

**参考答案**：

Spark采用主从架构，主要由Driver和Executor组成：

1. **Driver**：主节点，负责调度任务和管理作业执行。
2. **Executor**：从节点，负责执行具体的计算任务和存储数据。
3. **Cluster Manager**：负责管理集群资源，包括Standalone、YARN、Mesos等。

Driver将作业分解为多个Stage，每个Stage由多个Task组成。Executor接收Task并执行，将结果返回给Driver。

---

### 4.2 RDD编程模型

**题目2**：请简述RDD的特性。

**参考答案**：

RDD的特性包括：

1. **分区**：RDD由多个分区组成，分区分布在不同的节点上。
2. **只读**：RDD是只读的，不能直接修改，只能通过Transformation操作创建新的RDD。
3. **容错**：RDD通过Lineage（血缘）实现容错，如果某个分区数据丢失，可以通过Lineage重新计算。
4. **缓存**：RDD可以缓存到内存或磁盘，提高重复计算的效率。
5. **分区器**：RDD可以指定分区器，控制数据的分布。

---

**题目3**：请编写一个Spark WordCount程序。

**参考答案**：

```scala
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

object WordCount {
    def main(args: Array[String]) {
        val conf = new SparkConf().setAppName("WordCount").setMaster("local")
        val sc = new SparkContext(conf)
        
        val textFile = sc.textFile("input.txt")
        val counts = textFile.flatMap(line => line.split(" "))
                             .map(word => (word, 1))
                             .reduceByKey(_ + _)
        
        counts.saveAsTextFile("output")
        sc.stop()
    }
}
```

---

**题目4**：请说明Transformation和Action操作的区别。

**参考答案**：

Transformation和Action操作的区别：

1. **Transformation**：
   - 延迟执行（Lazy Evaluation）
   - 返回新的RDD
   - 不触发实际计算
   - 例子：map()、filter()、reduceByKey()

2. **Action**：
   - 立即执行（Eager Evaluation）
   - 返回非RDD类型的结果
   - 触发实际计算
   - 例子：count()、collect()、saveAsTextFile()

Spark采用延迟执行策略，只有遇到Action操作时才会触发实际计算。

---

### 4.3 Spark SQL与DataFrame

**题目5**：请简述Spark SQL的特点。

**参考答案**：

Spark SQL的特点包括：

1. **统一数据访问**：可以使用SQL查询各种数据源（HDFS、Hive、JSON、CSV等）。
2. **优化执行**：内置Catalyst优化器，自动优化SQL查询。
3. **与Spark集成**：可以与Spark的其他组件（Spark Streaming、MLlib）无缝集成。
4. **支持多种语言**：支持Scala、Java、Python、R等多种语言。
5. **DataFrame和Dataset**：提供DataFrame（弱类型）和Dataset（强类型）两种API。

---

**题目6**：请编写一个Spark SQL程序，读取CSV文件并进行查询。

**参考答案**：

```python
from pyspark.sql import SparkSession

# 创建SparkSession
spark = SparkSession.builder \
    .appName("Spark SQL Demo") \
    .getOrCreate()

# 读取CSV文件
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# 注册为临时表
df.createOrReplaceTempView("users")

# 执行SQL查询
result = spark.sql("SELECT name, age FROM users WHERE age > 18")

# 显示结果
result.show()

# 关闭SparkSession
spark.stop()
```

---

## 四、综合题

**题目1**：假设有以下输入数据（存储在input.txt中）：

```
Alice 25
Bob 30
Charlie 35
Alice 28
Bob 32
```

请编写一个Spark程序，统计每个人的平均年龄。

**参考答案**：

```scala
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

object AverageAge {
    def main(args: Array[String]) {
        val conf = new SparkConf().setAppName("AverageAge").setMaster("local")
        val sc = new SparkContext(conf)
        
        val input = sc.textFile("input.txt")
        
        // 解析数据：(name, age)
        val pairs = input.map(line => {
            val parts = line.split(" ")
            (parts(0), parts(1).toInt)
        })
        
        // 计算总和和计数：(name, (sum, count))
        val sumCount = pairs.mapValues(age => (age, 1))
                           .reduceByKey((a, b) => (a._1 + b._1, a._2 + b._2))
        
        // 计算平均年龄
        val average = sumCount.mapValues { case (sum, count) => sum.toDouble / count }
        
        average.saveAsTextFile("output")
        sc.stop()
    }
}
```

**输出结果**：

```
(Alice,26.5)
(Bob,31.0)
(Charlie,35.0)
```

---

**题目2**：请说明RDD的缓存机制及其作用。

**参考答案**：

RDD的缓存机制允许将RDD的数据存储在内存或磁盘中，以便后续操作可以直接使用，而不需要重新计算。

**缓存级别**：

| 级别 | 说明 |
|-----|------|
| **MEMORY_ONLY** | 仅存储在内存中 |
| **MEMORY_AND_DISK** | 优先存储在内存，内存不足时存储在磁盘 |
| **DISK_ONLY** | 仅存储在磁盘中 |
| **MEMORY_ONLY_SER** | 仅存储在内存中（序列化） |
| **MEMORY_AND_DISK_SER** | 优先存储在内存（序列化），内存不足时存储在磁盘 |

**作用**：

1. **提高性能**：避免重复计算，提高作业执行速度。
2. **减少I/O**：减少磁盘I/O和网络传输。
3. **支持交互式查询**：可以快速响应交互式查询。

**使用方法**：

```scala
rdd.cache()  // 默认使用MEMORY_ONLY级别
rdd.persist(StorageLevel.MEMORY_AND_DISK)  // 指定缓存级别
```

---

## 五、面试真题

**题目1**：Spark为什么比MapReduce快？

**参考答案**：

Spark比MapReduce快的原因包括：

1. **基于内存计算**：Spark的中间结果保存在内存中，而MapReduce写入磁盘。
2. **DAG调度**：Spark使用DAG（有向无环图）调度，可以优化任务执行顺序。
3. **减少数据传输**：Spark的Shuffle过程比MapReduce更高效。
4. **更好的内存管理**：Spark使用Tungsten引擎优化内存使用。
5. **丰富的API**：Spark提供了更丰富的API，可以减少代码量。

---

**题目2**：RDD、DataFrame和Dataset有什么区别？

**参考答案**：

1. **RDD**：
   - 无Schema信息
   - 强类型（Scala/Java）
   - 适合底层操作
   - 性能较低

2. **DataFrame**：
   - 有Schema信息
   - 弱类型
   - 适合结构化数据处理
   - 性能较高（有优化器）

3. **Dataset**：
   - 有Schema信息
   - 强类型
   - 结合了RDD和DataFrame的优点
   - 性能最高

---

**题目3**：Spark的宽依赖和窄依赖有什么区别？

**参考答案**：

1. **窄依赖**：
   - 每个父RDD的分区最多被一个子RDD的分区使用
   - 可以流水线执行
   - 例子：map()、filter()

2. **宽依赖**：
   - 父RDD的分区被多个子RDD的分区使用
   - 需要Shuffle操作
   - 例子：reduceByKey()、join()

Spark根据依赖关系将作业划分为多个Stage，窄依赖的操作可以在同一个Stage中执行，宽依赖会触发Stage边界。

---

> [!tip] 复习提示
> 本章重点掌握Spark的架构、RDD编程模型和Spark SQL。Spark是大数据处理的核心引擎，掌握这些知识对于大数据开发非常重要。