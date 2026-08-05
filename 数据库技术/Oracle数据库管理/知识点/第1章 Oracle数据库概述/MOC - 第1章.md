---
domain: 数据库技术
subject: Oracle数据库管理
type: knowledge
chapter: 第1章 Oracle数据库概述
tags: [Oracle,DBA,体系结构,RAC,实例,数据库]
prerequisites: ["数据库原理"]
---

# MOC - 第1章 Oracle数据库概述

> [!info] 本章定位
> 本章建立Oracle数据库的核心认知框架，从发展历史切入，明确Oracle产品定位与版本体系，全景展示Oracle体系结构，最后重点辨析**实例（Instance）**与**数据库（Database）**这两个Oracle独有的核心概念——这是理解后续所有DBA操作的前提。

## 学习路线图

```mermaid
flowchart LR
    A["1.1 Oracle发展与版本体系"] --> B["1.2 Oracle体系结构总览"]
    B --> C["1.3 数据库与实例概念区分"]
    style A fill:#4F86F7,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#6FB98F,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#FF8C42,stroke:#333,stroke-width:2px,color:#fff
```

## 知识点导航

| 节 | 主题 | 核心要点 | 入口 | 重要度 |
|---|---|---|---|---|
| 1.1 | Oracle发展与版本体系 | 发展历程、版本体系、竞品对比、云产品矩阵 | [[1.1 Oracle发展与版本体系]] | ⭐⭐⭐ |
| 1.2 | Oracle体系结构总览 | 实例vs数据库、客户端连接流程、网络结构 | [[1.2 Oracle体系结构总览]] | ⭐⭐⭐⭐ |
| 1.3 | 数据库与实例概念区分 | 物理文件构成、内存+进程、启动三阶段、RAC、ORACLE_SID | [[1.3 数据库与实例概念区分]] | ⭐⭐⭐⭐⭐ |

## 核心考点

> [!warning] 重点掌握
> 1. **实例与数据库的本质区别**：实例是内存+进程（临时），数据库是物理文件（永久）
> 2. **启动三阶段**：NOMOUNT→MOUNT→OPEN，每个阶段能做什么操作
> 3. **Oracle 19c**是当前长期支持版本（LTS），12c引入多租户CDB/PDB架构
> 4. **版本号格式**：major.minor.release.update.patch（如19.3.0.0.0）
> 5. **RAC集群**：多实例对应一个数据库，区别于单实例的一一对应
> 6. **客户端连接方式**：本地BEQueath vs 远程监听连接（1521端口）
> 7. **企业版核心特性**：RAC、Data Guard、分区、高级安全、RMAN等

## 自测题

> [!question] 自测题1
> Oracle 19c的版本号中，第三位数字"3"代表什么含义？
> 
> > [!check]- 参考答案
> > 第三位代表**release（发布版本）**。完整格式为 `major.minor.release.update.patch`，如19.3.0.0.0中：19=主版本号，3=发布版本，0=更新版本，0=补丁集版本。19.3.0是Oracle 19c的首个公开发布版本。

> [!question] 自测题2
> 为什么说Oracle实例是"临时的"而数据库是"永久的"？请举例说明。
> 
> > [!check]- 参考答案
> > - **实例（Instance）**由SGA内存和后台进程组成，数据库关闭后内存释放、进程终止，实例消失——是临时的运行态实体。
> > - **数据库（Database）**是磁盘上的物理文件（.dbf、.ctl、.log等），即使数据库关闭、服务器断电，文件仍存在——是永久的存储实体。
> > - 举例：服务器重启后，原来的实例已不存在，但可以重新启动实例加载原有数据库文件，数据不会丢失。

> [!question] 自测题3
> 在Oracle启动过程中，哪个阶段需要读取控制文件（Control File）？该阶段可以执行什么操作？
> 
> > [!check]- 参考答案
> > - **MOUNT（加载）阶段**需要读取控制文件。
> > - NOMOUNT阶段只启动实例（读参数文件、分配SGA、启动后台进程），不涉及数据库文件。
> > - MOUNT阶段根据控制文件中的记录找到数据文件和重做日志文件的位置，但不打开它们。
> > - MOUNT阶段可执行的操作：重命名数据文件、启用/禁用归档日志模式、执行恢复操作、查看V$DATABASE视图。

> [!question] 自测题4
> SID和Service Name有什么区别？各自在什么场景下使用？
> 
> > [!check]- 参考答案
> > - **SID（System Identifier）**：实例的唯一标识符，用于操作系统层面区分同一台机器上的不同实例。客户端通过环境变量ORACLE_SID指定本地连接的实例，对应BEQueath连接方式。
> > - **Service Name（服务名）**：数据库对外提供的逻辑服务名，一个数据库可注册多个服务名。远程客户端通过监听连接时使用服务名（1521端口），支持负载均衡和故障转移。
> > - 简单理解：SID是给操作系统和本地连接用的"实例名字"，Service Name是给远程客户端连接用的"数据库服务名字"。

## 章节导航

- 上一级：[[MOC - Oracle数据库管理]]
- 下一章：[[MOC - 第2章]]
- 本章习题：[[MOC - 第1章习题]]
