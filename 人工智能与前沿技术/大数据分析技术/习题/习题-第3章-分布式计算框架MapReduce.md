---
domain: 人工智能与前沿技术
type: 习题
status: 整理中
created: 2026-07-27
course: 大数据分析技术
chapter: 3
tags: ["大数据", "习题", "期末复习", "大数据开发"]
prerequisites: ["[[知识点/第3章-分布式计算框架MapReduce/MOC - 第3章]]"]
source: 大数据课后习题、本科期末试卷、企业面试真题汇编
---

# 习题-第3章-分布式计算框架MapReduce

> [!abstract] 本章习题概述
> 本章习题涵盖MapReduce的编程模型、工作流程和Shuffle机制，帮助巩固分布式计算核心知识。

## 一、选择题

### 3.1 MapReduce编程模型

**题目1**：MapReduce的Map函数的输入是（ ）

A. <key, value>对
B. <value, key>对
C. 单独的value
D. 单独的key

**答案**：A

**解析**：Map函数的输入是<key, value>对，key是行偏移量，value是行内容。

---

**题目2**：MapReduce的Reduce函数的输入是（ ）

A. <key, value>对
B. <key, list(value)>对
C. <list(key), value>对
D. <list(key), list(value)>对

**答案**：B

**解析**：Reduce函数的输入是<key, list(value)>对，同一个key的所有value会被收集到一起。

---

### 3.2 MapReduce工作流程

**题目3**：MapReduce的工作流程中，Map任务的输出首先写入（ ）

A. HDFS
B. 本地磁盘
C. 内存
D. 网络

**答案**：B

**解析**：Map任务的输出首先写入本地磁盘，而不是HDFS。

---

**题目4**：MapReduce的工作流程中，负责分配任务的组件是（ ）

A. NameNode
B. DataNode
C. JobTracker
D. TaskTracker

**答案**：C

**解析**：JobTracker负责分配任务和监控任务执行。

---

### 3.3 Shuffle机制

**题目5**：MapReduce的Shuffle过程不包括（ ）

A. 排序
B. 分区
C. 合并
D. 计算

**答案**：D

**解析**：Shuffle过程包括分区、排序、合并等，但不包括计算。

---

**题目6**：MapReduce中，Partitioner的作用是（ ）

A. 对key进行排序
B. 将key分配到不同的Reduce任务
C. 合并多个文件
D. 压缩数据

**答案**：B

**解析**：Partitioner的作用是将Map输出的key分配到不同的Reduce任务。

---

## 二、填空题

### 3.1 MapReduce编程模型

**题目1**：MapReduce的编程模型包括______、______和______三个阶段。

**答案**：Map、Shuffle、Reduce

---

**题目2**：Map函数的输出是一系列______对。

**答案**：<key, value>

---

### 3.2 MapReduce工作流程

**题目3**：MapReduce的工作流程包括______、______、______和______四个阶段。

**答案**：Split、Map、Shuffle、Reduce

---

**题目4**：每个Split对应一个______任务。

**答案**：Map

---

### 3.3 Shuffle机制

**题目5**：Shuffle过程包括______、______、______和______四个步骤。

**答案**：分区、排序、合并、拷贝

---

**题目6**：默认的Partitioner是______，它根据key的______值进行分区。

**答案**：HashPartitioner、哈希

---

## 三、简答题

### 3.1 MapReduce编程模型

**题目1**：请简述MapReduce的编程模型。

**参考答案**：

MapReduce的编程模型包括三个阶段：

1. **Map阶段**：将输入数据切分为多个Split，每个Split由一个Map任务处理。Map函数接收<key, value>对，输出一系列<key, value>对。

2. **Shuffle阶段**：对Map输出进行分区、排序、合并，然后将数据拷贝到Reduce任务。

3. **Reduce阶段**：每个Reduce任务处理一个分区的数据，对同一个key的所有value进行聚合操作，输出最终结果。

---

**题目2**：请编写一个简单的WordCount程序。

**参考答案**：

```java
public class WordCount {
    
    public static class Map extends Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();
        
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            StringTokenizer itr = new StringTokenizer(value.toString());
            while (itr.hasMoreTokens()) {
                word.set(itr.nextToken());
                context.write(word, one);
            }
        }
    }
    
    public static class Reduce extends Reducer<Text, IntWritable, Text, IntWritable> {
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            context.write(key, new IntWritable(sum));
        }
    }
    
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");
        job.setJarByClass(WordCount.class);
        job.setMapperClass(Map.class);
        job.setCombinerClass(Reduce.class);
        job.setReducerClass(Reduce.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

---

### 3.2 MapReduce工作流程

**题目3**：请简述MapReduce的工作流程。

**参考答案**：

MapReduce的工作流程包括：

1. **Split阶段**：将输入文件切分为固定大小的Split（默认与HDFS数据块大小相同）。

2. **Map阶段**：每个Split由一个Map任务处理。Map任务读取Split中的数据，调用用户定义的Map函数，输出<key, value>对，并写入本地磁盘。

3. **Shuffle阶段**：
   - **分区**：根据Partitioner将Map输出分配到不同的Reduce任务。
   - **排序**：对每个分区内的数据按key排序。
   - **合并**：将多个小文件合并为大文件。
   - **拷贝**：将数据拷贝到Reduce任务所在的节点。

4. **Reduce阶段**：每个Reduce任务处理一个分区的数据，调用用户定义的Reduce函数，对同一个key的所有value进行聚合操作，输出最终结果到HDFS。

---

### 3.3 Shuffle机制

**题目4**：请简述Shuffle机制的详细过程。

**参考答案**：

Shuffle机制包括以下步骤：

1. **Map端**：
   - **分区**：Map输出的每个<key, value>对根据Partitioner分配到不同的分区。
   - **排序**：对每个分区内的数据按key排序。
   - **Spill**：将排序后的数据写入内存缓冲区，当缓冲区满时，溢出到本地磁盘。
   - **Merge**：将多个溢出文件合并为一个大文件。

2. **Reduce端**：
   - **Copy**：从各个Map任务所在的节点拷贝属于自己分区的数据。
   - **Merge**：将拷贝的数据合并为一个有序的文件。
   - **Reduce**：调用用户定义的Reduce函数处理数据。

---

**题目5**：Combiner的作用是什么？在什么情况下可以使用Combiner？

**参考答案**：

Combiner的作用是在Map端对Map输出进行局部聚合，减少Shuffle过程中需要传输的数据量。

可以使用Combiner的条件：
1. 聚合操作是可交换的（顺序不影响结果）。
2. 聚合操作是可结合的（分组方式不影响结果）。

例如，求和、求最大值、求最小值等操作可以使用Combiner，但求平均值不能使用Combiner，因为平均值不满足可结合性。

---

## 四、综合题

**题目1**：假设有以下输入数据：

```
hello world
hello hadoop
hello mapreduce
world mapreduce
```

请画出WordCount程序的执行过程，包括Map阶段、Shuffle阶段和Reduce阶段的输入输出。

**参考答案**：

**Map阶段输入**：
```
<0, "hello world">
<12, "hello hadoop">
<26, "hello mapreduce">
<44, "world mapreduce">
```

**Map阶段输出**：
```
<hello, 1>, <world, 1>
<hello, 1>, <hadoop, 1>
<hello, 1>, <mapreduce, 1>
<world, 1>, <mapreduce, 1>
```

**Shuffle阶段**（排序和分组）：
```
<hadoop, [1]>
<hello, [1, 1, 1]>
<mapreduce, [1, 1]>
<world, [1, 1]>
```

**Reduce阶段输出**：
```
<hadoop, 1>
<hello, 3>
<mapreduce, 2>
<world, 2>
```

---

**题目2**：如何优化MapReduce作业的性能？

**参考答案**：

优化MapReduce作业性能的方法包括：

1. **数据本地性**：尽量将Map任务分配到数据所在的节点，减少网络传输。
2. **Combiner**：使用Combiner减少Shuffle数据量。
3. **分区优化**：合理设置分区数，使每个Reduce任务处理的数据量均衡。
4. **压缩**：对Map输出和Reduce输出进行压缩，减少磁盘I/O和网络传输。
5. **内存设置**：合理设置Map和Reduce任务的内存大小。
6. **数据预处理**：对数据进行预处理，减少不必要的数据处理。

---

## 五、面试真题

**题目1**：MapReduce的Shuffle过程是怎样的？

**参考答案**：

Shuffle是MapReduce的核心过程，包括：

1. **Map端**：
   - Map任务将输出写入内存缓冲区。
   - 当缓冲区满时，进行分区、排序，然后溢出到本地磁盘。
   - 多个溢出文件合并为一个有序的大文件。

2. **Reduce端**：
   - Reduce任务从各个Map任务所在节点拷贝属于自己分区的数据。
   - 将拷贝的数据合并为一个有序的文件。
   - 调用Reduce函数处理数据。

Shuffle过程的关键是排序和合并，保证Reduce任务接收到的数据是有序的。

---

**题目2**：MapReduce和Spark有什么区别？

**参考答案**：

1. **计算模型**：MapReduce是基于磁盘的批处理模型，Spark是基于内存的计算模型。
2. **速度**：Spark比MapReduce快10-100倍。
3. **易用性**：Spark提供了更丰富的API，更容易使用。
4. **中间结果**：MapReduce的中间结果写入磁盘，Spark的中间结果保存在内存中。
5. **适用场景**：MapReduce适合大规模批处理，Spark适合实时处理、交互式查询和机器学习。

---

**题目3**：什么是数据倾斜？如何解决数据倾斜问题？

**参考答案**：

数据倾斜是指某个Reduce任务处理的数据量远大于其他Reduce任务，导致作业执行时间过长。

解决数据倾斜的方法包括：

1. **预处理**：对数据进行预处理，过滤或拆分倾斜的key。
2. **加盐**：对倾斜的key添加随机前缀，分散到多个Reduce任务。
3. **自定义Partitioner**：使用自定义Partitioner均匀分配数据。
4. **Combiner**：使用Combiner减少Shuffle数据量。
5. **增加Reduce任务数**：增加Reduce任务数，使数据更均匀。

---

> [!tip] 复习提示
> 本章重点掌握MapReduce的编程模型、工作流程和Shuffle机制。这些是理解分布式计算的基础，也是后续学习Spark的基础。