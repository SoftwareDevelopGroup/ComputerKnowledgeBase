---
domain: 人工智能与前沿技术
type: 习题
status: 整理中
created: 2026-07-29
course: 云计算技术
chapter: 3
tags: ["云计算习题","容器技术","Docker","容器编排","期末复习"]
prerequisites: ["[[知识点/第3章 容器Docker技术/MOC - 第3章]]"]
source: 课后习题、本科期末试卷、云计算技能题库、前沿技术综合考题
---

# 第3章 容器Docker技术 — 综合练习题

> [!info] 题型说明
> 本习题集共 **32 题**,包含多种题型,建议用时 120 分钟完成。
> - 单选题(11 题)
> - 多选题(6 题)
> - 判断题(5 题)
> - 简答题(4 题)
> - 计算题(4 题)
> - 实操题(2 题)

---

## 一、单项选择题(每题 3 分,共 33 分)

### 第 1 题

容器与虚拟机的核心区别是?

A. 容器性能更低
B. 容器共享宿主机操作系统内核
C. 虚拟机无法实现资源隔离
D. 容器必须运行在虚拟机中

<details>
<summary>查看答案与解析</summary>

**答案：B**

**解析**：容器与虚拟机的本质区别在于隔离层级：容器通过 Linux 内核特性(namespaces、cgroups)实现进程级隔离,共享宿主机内核,启动速度快、资源开销小;虚拟机通过 Hypervisor 实现硬件级隔离,每个虚拟机有独立内核,资源开销大、启动慢。

</details>

---

### 第 2 题

Docker 的核心技术不包括以下哪一项?

A. Namespaces
B. Cgroups
C. Union File System
D. Hardware Virtualization

<details>
<summary>查看答案与解析</summary>

**答案：D**

**解析**：Docker 的核心技术包括：
- Namespaces：实现资源隔离(PID、NET、MNT 等)
- Cgroups：实现资源限制(CPU、内存、I/O)
- Union File System(UFS)：实现镜像分层存储

硬件虚拟化(Hardware Virtualization)是虚拟机技术,不是容器技术。

</details>

---

### 第 3 题

以下哪个 Namespace 用于实现容器间的网络隔离?

A. PID Namespace
B. NET Namespace
C. MNT Namespace
D. UTS Namespace

<details>
<summary>查看答案与解析</summary>

**答案：B**

**解析**：
- PID Namespace：进程 ID 隔离,容器内的进程有独立的 PID
- **NET Namespace**：网络隔离,容器有独立的网络栈(网卡、路由、iptables)
- MNT Namespace：文件系统挂载隔离
- UTS Namespace：主机名和域名隔离

</details>

---

### 第 4 题

Docker 镜像采用分层存储的主要优势是?

A. 提高安全性
B. 减少存储空间占用,加速镜像分发
C. 简化镜像构建流程
D. 支持跨平台运行

<details>
<summary>查看答案与解析</summary>

**答案：B**

**解析**：Docker 镜像采用分层存储(Union File System),多个镜像可共享相同的只读层,显著减少存储空间占用。镜像拉取时只需传输本地不存在的层,加速分发。镜像构建时也利用缓存层,加速构建过程。

</details>

---

### 第 5 题

Dockerfile 中 `CMD` 与 `ENTRYPOINT` 的区别是?

A. `CMD` 不可被覆盖,`ENTRYPOINT` 可被覆盖
B. `CMD` 可被覆盖,`ENTRYPOINT` 不易被覆盖
C. 两者功能完全相同
D. `CMD` 用于设置环境变量,`ENTRYPOINT` 用于启动命令

<details>
<summary>查看答案与解析</summary>

**答案：B**

**解析**：
- **CMD**：设置容器启动时执行的默认命令,可在 `docker run` 时被覆盖
- **ENTRYPOINT**：设置容器启动时的主命令,`docker run` 的参数会追加到 ENTRYPOINT 后,不易被覆盖

通常 ENTRYPOINT 用于设置主命令,CMD 用于设置默认参数。

</details>

---

### 第 6 题

Docker Compose 的主要作用是?

A. 构建 Docker 镜像
B. 管理单机多容器应用
C. 实现跨主机容器编排
D. 提供 Docker 镜像仓库

<details>
<summary>查看答案与解析</summary>

**答案：B**

**解析**：Docker Compose 用于定义和运行单机多容器应用,通过 `docker-compose.yml` 文件配置应用的服务、网络、卷等,一条命令启动所有服务。跨主机容器编排使用 Kubernetes 或 Docker Swarm。

</details>

---

### 第 7 题

以下哪种 Docker 网络模式允许容器使用宿主机的网络栈?

A. Bridge 模式
B. Host 模式
C. None 模式
D. Overlay 模式

<details>
<summary>查看答案与解析</summary>

**答案：B**

**解析**：
- Bridge 模式：默认模式,容器有独立网络栈,通过 NAT 访问外部
- **Host 模式**：容器共享宿主机网络栈,直接使用宿主机端口,性能最高但无网络隔离
- None 模式：禁用网络栈
- Overlay 模式：跨主机网络,用于 Docker Swarm

</details>

---

### 第 8 题

Docker Volume 与 Bind Mount 的主要区别是?

A. Volume 存储在宿主机特定位置,由 Docker 管理;Bind Mount 可挂载任意宿主机路径
B. Volume 性能更高
C. Bind Mount 不支持跨容器共享
D. Volume 只能存储配置文件

<details>
<summary>查看答案与解析</summary>

**答案：A**

**解析**：
- **Volume**：存储在 `/var/lib/docker/volumes/`,由 Docker 管理,推荐用于持久化数据,易于备份和迁移
- **Bind Mount**：挂载宿主机任意路径,用于开发场景(如代码同步),依赖宿主机路径结构

Volume 和 Bind Mount 性能相近,都支持跨容器共享。

</details>

---

### 第 9 题

以下哪个命令用于查看 Docker 容器的资源使用情况?

A. `docker ps`
B. `docker stats`
C. `docker inspect`
D. `docker logs`

<details>
<summary>查看答案与解析</summary>

**答案：B**

**解析**：
- `docker ps`：列出运行中的容器
- **`docker stats`**：实时显示容器的 CPU、内存、网络、磁盘 I/O 使用情况
- `docker inspect`：查看容器详细配置信息
- `docker logs`：查看容器日志

</details>

---

### 第 10 题

镜像构建上下文(Context)的作用是?

A. 指定镜像构建的 Dockerfile 路径
B. 限制 Docker 客户端发送给 Docker 守护进程的文件范围
C. 设置构建时的环境变量
D. 指定构建缓存的位置

<details>
<summary>查看答案与解析</summary>

**答案：B**

**解析**：Docker 构建镜像时,Docker 客户端会将构建上下文(指定路径下的所有文件)打包发送给 Docker 守护进程。上下文限制了发送的文件范围,避免发送不必要的文件(如 `.git` 目录),加速构建过程。通常使用 `.dockerignore` 文件排除不需要的文件。

</details>

---

### 第 11 题

以下哪项不是 Docker 的优势?

A. 秒级启动速度
B. 跨平台兼容性
C. 强隔离性
D. 镜像分层复用

<details>
<summary>查看答案与解析</summary>

**答案：C**

**解析**：容器共享宿主机内核,隔离性弱于虚拟机,存在内核漏洞逃逸风险。Docker 的优势包括：秒级启动(A)、跨平台(B)、镜像分层复用(D)、轻量级、标准化打包。

</details>

---

## 二、多项选择题(每题 4 分,共 24 分)

### 第 12 题

Docker 的核心组件包括?(多选)

A. Docker Client
B. Docker Daemon
C. Docker Registry
D. Docker Compose
E. Docker Machine

<details>
<summary>查看答案与解析</summary>

**答案：A、B、C**

**解析**：
- A 正确：Docker Client(docker 命令)用于与 Docker Daemon 交互
- B 正确：Docker Daemon(dockerd)是 Docker 服务端进程,管理镜像、容器、网络等
- C 正确：Docker Registry 是镜像仓库(Docker Hub、私有仓库)
- D、E 是辅助工具,不是核心组件

</details>

---

### 第 13 题

以下哪些是 Docker 的使用场景?(多选)

A. 持续集成/持续部署(CI/CD)
B. 微服务架构
C. 开发环境标准化
D. 高性能计算(HPC)
E. 资源隔离要求极高的多租户场景

<details>
<summary>查看答案与解析</summary>

**答案：A、B、C**

**解析**：
- A 正确：容器化 CI/CD 流水线,环境一致性
- B 正确：微服务独立部署、弹性伸缩
- C 正确：开发、测试、生产环境一致性
- D 错误：高性能计算通常使用裸机或虚拟机,避免容器性能损耗
- E 错误：容器隔离性弱,不适合高隔离性多租户场景

</details>

---

### 第 14 题

Dockerfile 中用于构建镜像的指令包括?(多选)

A. FROM
B. RUN
C. COPY
D. EXPOSE
E. VOLUME

<details>
<summary>查看答案与解析</summary>

**答案：A、B、C、D、E**

**解析**：
- A 正确：指定基础镜像
- B 正确：执行命令并提交结果
- C 正确：复制文件到镜像
- D 正确：声明暴露的端口
- E 正确：创建挂载点

这些都是构建指令,会生成镜像层。

</details>

---

### 第 15 题

Docker 容器资源限制可通过哪些方式实现?(多选)

A. `docker run --cpus`
B. `docker run --memory`
C. `docker run --ulimit`
D. Docker Compose 的 `deploy.resources`
E. 使用特权模式

<details>
<summary>查看答案与解析</summary>

**答案：A、B、C、D**

**解析**：
- A 正确：限制 CPU 使用量
- B 正确：限制内存使用量
- C 正确：设置 ulimit 资源限制(如文件描述符数量)
- D 正确：Docker Compose 中配置资源限制
- E 错误：特权模式提升容器权限,不限制资源

</details>

---

### 第 16 题

以下哪些 Namespace 被 Docker 使用?(多选)

A. PID
B. NET
C. IPC
D. USER
E. TIME

<details>
<summary>查看答案与解析</summary>

**答案：A、B、C、D**

**解析**：
- A 正确：进程 ID 隔离
- B 正确：网络栈隔离
- C 正确：进程间通信隔离
- D 正确：用户和用户组隔离(需启用 user namespace)
- E 错误：TIME Namespace 是 Linux 5.6 新增特性,Docker 默认不使用

</details>

---

### 第 17 题

Docker 镜像仓库的类型包括?(多选)

A. 公共仓库(Docker Hub)
B. 私有仓库(Registry)
C. 企业级仓库(Harbor)
D. 云服务仓库(ECR、ACR)
E. 本地缓存

<details>
<summary>查看答案与解析</summary>

**答案：A、B、C、D**

**解析**：
- A 正确：Docker Hub 是官方公共仓库
- B 正确：私有仓库如 Docker Registry
- C 正确：Harbor 提供企业级特性(镜像扫描、RBAC)
- D 正确：云服务商提供的镜像仓库
- E 错误：本地缓存不是独立仓库类型,是 Docker 的缓存机制

</details>

---

## 三、判断题(每题 2 分,共 10 分)

### 第 18 题

Docker 容器内的进程运行在宿主机的 PID Namespace 中。

<details>
<summary>查看答案与解析</summary>

**答案：错误**

**解析**：Docker 容器内的进程运行在独立的 PID Namespace 中,容器内的 PID 从 1 开始。在宿主机上通过 `ps aux` 可以看到容器进程,但 PID 是宿主机的 PID,与容器内的 PID 不同。

</details>

---

### 第 19 题

Docker 镜像的每一层都是只读的,容器层是可写的。

<details>
<summary>查看答案与解析</summary>

**答案：正确**

**解析**：Docker 镜像采用分层存储,每一层都是只读的。容器启动时,在镜像顶层添加一个可写的容器层(Container Layer),所有对容器的修改都写入容器层,采用 Copy-on-Write(CoW)机制。

</details>

---

### 第 20 题

Docker 容器重启后,容器内的文件修改会丢失。

<details>
<summary>查看答案与解析</summary>

**答案：错误**

**解析**：容器重启后,容器层的数据仍然保留,文件修改不会丢失。只有容器删除后,容器层才会被清理。持久化数据应使用 Volume 或 Bind Mount,避免数据随容器删除而丢失。

</details>

---

### 第 21 题

一个 Docker 容器只能运行一个进程。

<details>
<summary>查看答案与解析</summary>

**答案：错误**

**解析**：Docker 容器可以运行多个进程,但推荐"单容器单进程"模式,便于监控、日志收集和故障排查。如需运行多个进程,可使用 supervisord 或 shell 脚本管理。

</details>

---

### 第 22 题

Docker Compose 可以替代 Kubernetes 用于生产环境的容器编排。

<details>
<summary>查看答案与解析</summary>

**答案：错误**

**解析**：Docker Compose 用于单机多容器应用管理,不支持跨主机编排、自动扩缩容、滚动升级等生产级特性。生产环境应使用 Kubernetes 或 Docker Swarm,提供高可用、负载均衡、自动恢复等能力。

</details>

---

## 四、简答题(每题 6 分,共 24 分)

### 第 23 题

对比容器与虚拟机的架构差异,并说明各自的优缺点和适用场景。

<details>
<summary>查看参考答案</summary>

**架构差异对比**：

| 对比维度 | 容器(Docker) | 虚拟机(VM) |
|---------|-------------|-----------|
| **隔离层级** | 进程级隔离(共享内核) | 硬件级隔离(独立内核) |
| **启动速度** | 秒级启动 | 分钟级启动 |
| **资源开销** | MB 级内存,几乎无性能损耗 | GB 级内存,5-15% 性能损耗 |
| **镜像大小** | MB~几百 MB | GB~几十 GB |
| **隔离性** | 弱(共享内核,存在逃逸风险) | 强(独立内核,硬件级隔离) |
| **移植性** | 高(标准化镜像格式) | 中(需硬件虚拟化支持) |
| **资源密度** | 高(单机可运行数百个容器) | 低(单机通常运行 10-20 个虚拟机) |

**容器优缺点**：
- 优点：启动快、资源利用率高、移植性好、标准化打包
- 缺点：隔离性弱、安全风险较高、依赖宿主机内核

**虚拟机优缺点**：
- 优点：隔离性强、安全性高、支持异构操作系统
- 缺点：启动慢、资源开销大、镜像体积大

**适用场景**：
- **容器适用场景**：微服务架构、CI/CD 流水线、开发测试环境、无状态应用、云原生应用
- **虚拟机适用场景**：多租户环境、安全隔离要求高的场景、传统应用迁移、异构操作系统、高性能计算

</details>

---

### 第 24 题

解释 Docker 的镜像分层原理,并说明 Copy-on-Write(CoW)机制如何工作。

<details>
<summary>查看参考答案</summary>

**镜像分层原理**：

Docker 镜像由多个只读层组成,每层对应 Dockerfile 中的一条指令(FROM、RUN、COPY 等)。分层存储带来以下优势：

1. **存储空间节省**：多个镜像可共享相同的基础层
2. **镜像拉取加速**：只需下载本地不存在的层
3. **构建加速**：利用缓存层,避免重复构建

**镜像层结构**：

```
┌─────────────────────────────┐
│   容器层(Container Layer)    │ ← 可写层
├─────────────────────────────┤
│   镜像层 3 (RUN npm install) │ ← 只读
├─────────────────────────────┤
│   镜像层 2 (COPY . /app)     │ ← 只读
├─────────────────────────────┤
│   镜像层 1 (FROM node:14)    │ ← 只读(基础镜像)
└─────────────────────────────┘
```

**Copy-on-Write(CoW)机制**：

容器启动时,在镜像顶层添加可写的容器层。当容器需要修改文件时:

1. **读取文件**：从镜像层直接读取(无需复制)
2. **修改文件**：
   - 从镜像层复制文件到容器层(Copy)
   - 在容器层修改文件(Write)
   - 后续读取使用容器层的修改版本
3. **删除文件**：在容器层标记文件为删除(实际不删除镜像层文件)

CoW 机制确保镜像层保持只读,多个容器可安全共享相同镜像,节省存储空间。

</details>

---

### 第 25 题

简述 Docker 的四种网络模式(Bridge、Host、None、Overlay)的原理与适用场景。

<details>
<summary>查看参考答案</summary>

**四种网络模式对比**：

| 网络模式 | 原理 | 特点 | 适用场景 |
|---------|------|------|---------|
| **Bridge**(桥接) | 默认模式,容器有独立网络栈,通过虚拟网桥 docker0 连接,使用 NAT 访问外部 | 网络隔离性好,支持端口映射 | 大多数应用场景 |
| **Host**(主机) | 容器共享宿主机网络栈,直接使用宿主机端口和 IP | 性能最高,无网络隔离 | 高性能网络应用、网络监控工具 |
| **None**(无网络) | 禁用容器网络栈,无网卡、路由等 | 完全隔离,需手动配置网络 | 安全要求高、自定义网络配置 |
| **Overlay**(覆盖) | 跨主机网络,基于 VXLAN 技术 | 跨主机容器通信,支持加密 | Docker Swarm 集群 |

**Bridge 模式详解**：
- 容器有独立 IP(通常 172.17.0.0/16 网段)
- 通过 NAT 访问外部网络
- 宿主机端口映射:`-p 宿主机端口:容器端口`
- 容器间通过虚拟网桥通信

**Host 模式详解**：
- 容器直接使用宿主机 IP 和端口
- 无需端口映射,性能损耗最小
- 端口冲突风险高,隔离性弱

**Overlay 模式详解**：
- 用于跨主机容器通信
- 基于 VXLAN 封装,支持加密
- 需要服务发现(如 Consul)或 Docker Swarm

**自定义网络**：
- 创建用户定义网络:`docker network create mynet`
- 支持容器名解析(DNS)
- 推荐用于多容器应用

</details>

---

### 第 26 题

解释 Dockerfile 中 `COPY` 与 `ADD` 指令的区别,并说明 Docker 多阶段构建(Multi-stage Build)的作用。

<details>
<summary>查看参考答案</summary>

**COPY 与 ADD 对比**：

| 指令 | 功能 | 特点 | 推荐用法 |
|------|------|------|---------|
| **COPY** | 复制文件或目录到镜像 | 简单直接,只做复制 | 推荐用于复制应用文件 |
| **ADD** | 复制文件或目录到镜像 | 支持自动解压 tar 文件、支持 URL 下载 | 特殊场景(解压、下载) |

**COPY 示例**：
```dockerfile
COPY ./app /app
COPY config.json /etc/app/config.json
```

**ADD 示例**：
```dockerfile
ADD https://example.com/file.tar.gz /tmp/  # 下载文件
ADD app.tar.gz /app/  # 自动解压
```

**多阶段构建(Multi-stage Build)**：

多阶段构建允许在一个 Dockerfile 中定义多个构建阶段,最终镜像只包含运行所需文件,显著减小镜像体积。

**示例**：

```dockerfile
# 阶段1: 构建阶段
FROM golang:1.20 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o myapp .

# 阶段2: 运行阶段
FROM alpine:3.18
WORKDIR /app
COPY --from=builder /app/myapp .  # 从构建阶段复制二进制文件
CMD ["./myapp"]
```

**多阶段构建优势**：
1. **减小镜像体积**：最终镜像不包含构建工具(如编译器、依赖)
2. **简化构建流程**：无需多个 Dockerfile 或外部构建脚本
3. **安全性提升**：最终镜像不包含源代码和构建工具
4. **典型场景**：编译型语言(Go、Java、C++)应用构建

</details>

---

## 五、计算题(每题 8 分,共 32 分)

### 第 27 题：容器资源规划

某企业计划使用 Docker 容器化部署微服务应用,现有 5 台物理服务器,每台配置为:
- CPU: 32 核
- 内存: 128 GB
- 磁盘: 2 TB SSD

每个微服务容器配置为:
- CPU: 2 核(限制)
- 内存: 4 GB(限制)
- 存储: 10 GB(镜像 + 数据)

假设:
- 系统保留资源: CPU 10%、内存 20%
- 资源利用率目标: 80%
- 容器网络开销: 200 MB 内存

请计算:

1. 每台服务器最多可运行多少个容器?
2. 5 台服务器总共可部署多少个微服务实例?
3. 若需要部署 100 个微服务实例,是否满足需求?

<details>
<summary>查看参考答案</summary>

**1. 计算单台服务器最大容器数**

**CPU 限制**:
- 可用 CPU 核数: 32 × (1 - 10%) = 28.8 核
- 考虑利用率: 28.8 × 80% = 23.04 核
- 每容器 CPU: 2 核
- CPU 限制最大容器数: 23.04 ÷ 2 = **11.52** → 向下取整为 **11 个**

**内存限制**:
- 可用内存: 128 × (1 - 20%) = 102.4 GB
- 考虑利用率: 102.4 × 80% = 81.92 GB
- 每容器内存: 4 GB + 0.2 GB(网络开销) = 4.2 GB
- 内存限制最大容器数: 81.92 ÷ 4.2 = **19.5** → 向下取整为 **19 个**

**存储限制**:
- 总存储: 2 TB = 2048 GB
- 每容器存储: 10 GB
- 存储限制最大容器数: 2048 ÷ 10 = **204.8** → 向下取整为 **204 个**

**结论**: CPU 是瓶颈,每台服务器最多运行 **11 个容器**。

**2. 计算总部署实例数**

- 服务器数量: 5 台
- 每台最大容器数: 11 个
- 总部署实例数: 5 × 11 = **55 个微服务实例**

**3. 判断是否满足 100 个实例需求**

- 需求: 100 个实例
- 实际部署能力: 55 个实例
- 缺口: 100 - 55 = **45 个实例**

**结论**: 不满足需求,需增加服务器或调整容器资源限制。

**解决方案**:
1. 增加服务器数量: 需额外 5 台(100 ÷ 11 = 9.1 → 10 台)
2. 降低容器资源限制: 如每容器 1 核 CPU,可支持 23 个容器/台
3. 优化资源利用率目标

</details>

---

### 第 28 题：镜像分层存储计算

某应用使用三层 Docker 镜像:

**基础镜像层(Base Image)**:
- Ubuntu 基础镜像: 200 MB
- Python 运行时: 150 MB
- 依赖库: 80 MB

**应用层(Application Layer)**:
- 应用代码: 50 MB
- 配置文件: 1 MB

**运行时层(Runtime Layer)**:
- 日志文件(运行时生成): 不计入镜像大小

现有 3 个应用共享相同的 Python 基础镜像,请计算:

1. 若每个应用独立存储镜像,总存储空间需求是多少?
2. 使用 Docker 分层存储后,实际存储空间需求是多少?
3. 节省了多少存储空间?节省比例是多少?

<details>
<summary>查看参考答案</summary>

**1. 独立存储总空间**

每个应用镜像大小:
- 基础镜像层: 200 + 150 + 80 = 430 MB
- 应用层: 50 + 1 = 51 MB
- 单应用镜像: 430 + 51 = 481 MB

3 个应用总空间:
- 总空间: 481 × 3 = **1,443 MB ≈ 1.44 GB**

**2. 分层存储实际空间**

分层存储策略:
- 基础镜像层(Ubuntu + Python + 依赖): 所有应用共享,只存储一次
- 应用层: 每个应用独立存储

计算:
- 基础镜像层(共享): 430 MB × 1 = 430 MB
- 应用层(3 个): 51 MB × 3 = 153 MB
- 总空间: 430 + 153 = **583 MB ≈ 0.58 GB**

**3. 节省空间与比例**

- 节省空间: 1,443 - 583 = **860 MB ≈ 0.86 GB**
- 节省比例: 860 ÷ 1,443 × 100% = **59.6%**

**结论**: 分层存储节省了约 60% 的存储空间,显著减少存储成本和镜像分发时间。

</details>

---

### 第 29 题：容器网络性能分析

某容器化应用使用 Bridge 网络模式,测试数据如下:

**容器间通信(同一主机)**:
- 平均延迟: 0.5 ms
- 吞吐量: 5 Gbps

**容器到宿主机通信**:
- 平均延迟: 0.3 ms
- 吞吐量: 8 Gbps

**容器到外部网络(通过 NAT)**:
- 平均延迟: 1.2 ms
- 吞吐量: 4 Gbps

若改为 Host 网络模式,预计性能提升:
- 延迟降低: 30%
- 吞吐量提升: 20%

请计算:

1. Host 模式下容器到外部网络的延迟和吞吐量
2. 若应用要求延迟 < 1 ms,哪种模式满足要求?
3. 从性能和隔离性角度分析两种模式的适用场景

<details>
<summary>查看参考答案</summary>

**1. 计算 Host 模式性能**

**容器到外部网络性能**:

- Bridge 模式延迟: 1.2 ms
- Host 模式延迟: 1.2 × (1 - 30%) = 1.2 × 0.7 = **0.84 ms**

- Bridge 模式吞吐量: 4 Gbps
- Host 模式吞吐量: 4 × (1 + 20%) = 4 × 1.2 = **4.8 Gbps**

**2. 判断延迟是否满足要求**

应用要求: 延迟 < 1 ms

- Bridge 模式: 1.2 ms > 1 ms,**不满足**
- Host 模式: 0.84 ms < 1 ms,**满足**

**结论**: Host 模式满足延迟要求。

**3. 模式对比与适用场景**

| 对比维度 | Bridge 模式 | Host 模式 |
|---------|------------|-----------|
| **性能** | 较低(NAT 开销) | 最高(共享网络栈) |
| **隔离性** | 好(独立网络栈) | 差(共享网络栈) |
| **端口冲突** | 无(独立端口空间) | 有(共享宿主机端口) |
| **适用场景** | 大多数应用、多租户环境 | 高性能网络应用、监控工具 |

**适用场景分析**:

- **Bridge 模式适用场景**:
  - 标准应用部署
  - 多容器端口隔离
  - 安全性要求高的场景
  - 多租户环境

- **Host 模式适用场景**:
  - 高性能网络应用(如 API 网关、负载均衡器)
  - 网络监控工具(如 Prometheus Node Exporter)
  - 对网络性能要求极高的场景
  - 单一应用部署(无端口冲突风险)

**推荐**: 对于延迟敏感型应用(如实时交易系统),推荐 Host 模式;对于一般应用,Bridge 模式在隔离性和性能间取得平衡。

</details>

---

### 第 30 题：镜像构建优化

某应用镜像构建时间为 8 分钟,Dockerfile 如下:

```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
CMD ["python3", "app.py"]
```

假设各步骤耗时:
- 基础镜像拉取: 30 秒(本地已缓存)
- apt-get update & install: 2 分钟
- COPY: 10 秒
- pip install: 5 分钟(下载 100 个依赖包)

请计算:

1. 若修改应用代码,重新构建需要多长时间?
2. 若优化 Dockerfile,将依赖安装前置,修改应用代码后构建时间是多少?
3. 优化后的构建时间节省了百分之多少?

<details>
<summary>查看参考答案</summary>

**1. 原始 Dockerfile 重新构建时间**

Docker 构建缓存机制: 若某层指令或上下文文件未变化,使用缓存。

假设修改应用代码(COPY 步骤变化):
- FROM: 缓存命中,0 秒
- RUN apt-get: 缓存命中,0 秒
- COPY: 缓存失效(代码变化),10 秒
- RUN pip install: 缓存失效(后续层需重新构建),5 分钟
- 总时间: 0 + 0 + 10 + 300 = **310 秒 = 5 分 10 秒**

**2. 优化后的 Dockerfile**

将依赖安装前置,利用缓存:

```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt /app/requirements.txt  # 仅复制依赖文件
RUN pip install -r /app/requirements.txt     # 依赖安装
COPY . /app                                   # 最后复制代码
WORKDIR /app
CMD ["python3", "app.py"]
```

修改应用代码后构建时间:
- FROM: 缓存命中,0 秒
- RUN apt-get: 缓存命中,0 秒
- COPY requirements.txt: 缓存命中(依赖未变),0 秒
- RUN pip install: 缓存命中,0 秒
- COPY .: 缓存失效(代码变化),10 秒
- 总时间: **10 秒**

**3. 构建时间节省**

- 原始构建时间: 310 秒(5 分 10 秒)
- 优化后构建时间: 10 秒
- 节省时间: 310 - 10 = **300 秒**
- 节省比例: 300 ÷ 310 × 100% = **96.8%**

**结论**: 通过优化 Dockerfile 指令顺序,将不常变化的层前置,利用缓存机制,可将构建时间从 5 分钟以上降低到 10 秒,节省 96.8% 的时间。

**优化建议**:
1. 将依赖安装前置,利用缓存
2. 使用 `.dockerignore` 排除不必要文件
3. 合并多个 RUN 指令,减少层数
4. 使用多阶段构建,减小镜像体积

</details>

---

## 六、实操题(每题 8 分,共 16 分)

### 第 31 题：Dockerfile 编写与镜像构建

编写一个 Dockerfile,用于构建一个 Node.js Web 应用镜像,要求:

1. 基础镜像: node:18-alpine
2. 工作目录: /app
3. 复制 package.json 和 package-lock.json,安装依赖
4. 复制应用代码
5. 暴露端口 3000
6. 启动命令: npm start
7. 设置环境变量 NODE_ENV=production
8. 使用非 root 用户(node)运行容器

然后编写构建和运行命令。

<details>
<summary>查看参考答案</summary>

**Dockerfile**:

```dockerfile
# 基础镜像
FROM node:18-alpine

# 设置环境变量
ENV NODE_ENV=production

# 创建应用目录并设置为工作目录
WORKDIR /app

# 复制依赖描述文件
COPY package*.json ./

# 安装依赖(仅生产环境依赖)
RUN npm ci --only=production

# 复制应用代码
COPY . .

# 创建非 root 用户(Alpine 使用 adduser)
RUN addgroup -g 1000 -S nodejs && \
    adduser -S nodejs -u 1000 -G nodejs

# 更改文件所有者
RUN chown -R nodejs:nodejs /app

# 切换到非 root 用户
USER nodejs

# 暴露端口
EXPOSE 3000

# 启动命令
CMD ["npm", "start"]
```

**构建镜像命令**:

```bash
# 构建镜像(当前目录包含 Dockerfile)
docker build -t my-nodejs-app:v1.0 .

# 或指定 Dockerfile 路径
docker build -t my-nodejs-app:v1.0 -f Dockerfile .

# 查看构建的镜像
docker images | grep my-nodejs-app
```

**运行容器命令**:

```bash
# 运行容器(映射端口)
docker run -d \
  --name my-nodejs-container \
  -p 3000:3000 \
  my-nodejs-app:v1.0

# 运行容器(带环境变量和卷挂载)
docker run -d \
  --name my-nodejs-container \
  -p 3000:3000 \
  -e DATABASE_URL=postgres://user:pass@db:5432/mydb \
  -v /host/logs:/app/logs \
  --restart unless-stopped \
  my-nodejs-app:v1.0

# 查看容器状态
docker ps -a | grep my-nodejs-container

# 查看容器日志
docker logs -f my-nodejs-container

# 进入容器(以 root 用户)
docker exec -it -u root my-nodejs-container sh
```

**优化建议**:

1. **使用多阶段构建**(减小镜像体积):

```dockerfile
# 构建阶段
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# 运行阶段
FROM node:18-alpine
ENV NODE_ENV=production
WORKDIR /app
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
RUN addgroup -g 1000 -S nodejs && \
    adduser -S nodejs -u 1000 -G nodejs && \
    chown -R nodejs:nodejs /app
USER nodejs
EXPOSE 3000
CMD ["npm", "start"]
```

2. **使用 .dockerignore**(减少构建上下文):

```
node_modules
npm-debug.log
Dockerfile
.dockerignore
.git
.gitignore
README.md
.env
*.log
```

</details>

---

### 第 32 题：Docker Compose 多服务编排

使用 Docker Compose 编排一个 Web 应用栈,包含:

1. **Web 服务**(Nginx):
   - 镜像: nginx:alpine
   - 端口映射: 80:80
   - 挂载卷: ./nginx.conf:/etc/nginx/nginx.conf
   - 依赖: app

2. **应用服务**(Node.js):
   - 构建: 当前目录的 Dockerfile
   - 端口: 3000(仅内部访问)
   - 环境变量: DATABASE_URL, NODE_ENV
   - 挂载卷: ./app:/app
   - 依赖: db, redis

3. **数据库服务**(PostgreSQL):
   - 镜像: postgres:15-alpine
   - 环境变量: POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
   - 挂载卷: postgres-data:/var/lib/postgresql/data
   - 端口: 5432(仅内部访问)

4. **缓存服务**(Redis):
   - 镜像: redis:7-alpine
   - 端口: 6379(仅内部访问)

编写 docker-compose.yml 文件,并写出启动、停止、查看日志的命令。

<details>
<summary>查看参考答案</summary>

**docker-compose.yml**:

```yaml
version: '3.8'

services:
  # Web 服务(Nginx 反向代理)
  web:
    image: nginx:alpine
    container_name: myapp-web
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app
    networks:
      - frontend
    restart: unless-stopped

  # 应用服务(Node.js)
  app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: myapp-app
    environment:
      - DATABASE_URL=postgres://myuser:mypass@db:5432/mydb
      - NODE_ENV=production
      - REDIS_URL=redis://redis:6379
    volumes:
      - ./app:/app
      - /app/node_modules  # 避免本地 node_modules 覆盖容器内
    depends_on:
      - db
      - redis
    networks:
      - frontend
      - backend
    restart: unless-stopped

  # 数据库服务(PostgreSQL)
  db:
    image: postgres:15-alpine
    container_name: myapp-db
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=mypass
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - backend
    restart: unless-stopped

  # 缓存服务(Redis)
  redis:
    image: redis:7-alpine
    container_name: myapp-redis
    networks:
      - backend
    restart: unless-stopped

# 定义网络
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge

# 定义卷
volumes:
  postgres-data:
    driver: local
```

**nginx.conf 配置示例**:

```nginx
events {
    worker_connections 1024;
}

http {
    upstream app_server {
        server app:3000;
    }

    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://app_server;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```

**常用命令**:

```bash
# 启动所有服务(后台运行)
docker-compose up -d

# 启动并查看日志(前台运行)
docker-compose up

# 仅构建镜像(不启动)
docker-compose build

# 查看服务状态
docker-compose ps

# 查看所有服务日志
docker-compose logs

# 实时查看特定服务日志
docker-compose logs -f app

# 停止所有服务
docker-compose stop

# 停止并删除容器、网络、卷
docker-compose down

# 停止并删除容器、网络、卷、镜像
docker-compose down --rmi all -v

# 重启特定服务
docker-compose restart app

# 扩展服务实例(运行 3 个 app 容器)
docker-compose up -d --scale app=3

# 进入容器
docker-compose exec app sh

# 查看服务资源使用情况
docker-compose top
```

**环境变量管理(推荐)**:

创建 `.env` 文件:

```env
# 数据库配置
POSTGRES_DB=mydb
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypass

# 应用配置
NODE_ENV=production
```

修改 docker-compose.yml:

```yaml
db:
  environment:
    - POSTGRES_DB=${POSTGRES_DB}
    - POSTGRES_USER=${POSTGRES_USER}
    - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
```

</details>

---

## 附录：章节知识点速查表

| 考点 | 重要程度 | 关联题目 |
|-----|---------|---------|
| 容器 vs 虚拟机 | ⭐⭐⭐⭐⭐ | 1, 23 |
| Docker 核心技术 | ⭐⭐⭐⭐⭐ | 2, 3, 16 |
| Docker 镜像分层 | ⭐⭐⭐⭐⭐ | 4, 19, 24, 28 |
| Dockerfile 指令 | ⭐⭐⭐⭐⭐ | 5, 14, 26, 31 |
| Docker 网络 | ⭐⭐⭐⭐ | 7, 25, 29 |
| Docker 存储 | ⭐⭐⭐⭐ | 8, 20 |
| Docker Compose | ⭐⭐⭐⭐⭐ | 6, 22, 32 |
| 容器资源管理 | ⭐⭐⭐⭐ | 9, 15, 27 |
| 镜像构建优化 | ⭐⭐⭐⭐ | 10, 30, 31 |
| Docker 应用场景 | ⭐⭐⭐ | 13, 23 |