---
domain: 数据库技术
subject: Oracle数据库管理
type: knowledge
chapter: 第2章 Oracle安装与环境配置
tags: [Oracle,DBA,安装,监听,环境变量,ORACLE_HOME,静默安装]
prerequisites: ["数据库原理", "MOC - 第1章 Oracle数据库概述"]
---

# MOC - 第2章 Oracle安装与环境配置

> [!info] 本章定位
> 本章从生产部署视角完整覆盖Oracle 19c从环境准备→软件安装→网络配置→验证连通性的全流程。核心建立三个认知：**生产环境的软硬件基线要求**、**图形化/静默两种安装方式**、**监听+TNS+环境变量三件套的配置与排错**，是DBA最基础的实战技能。

## 学习路线图

```mermaid
flowchart LR
    A["2.1 软硬件环境要求"] --> B["2.2 数据库软件安装步骤"]
    B --> C["2.3 监听与环境变量配置"]
    style A fill:#4F86F7,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#6FB98F,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#FF8C42,stroke:#333,stroke-width:2px,color:#fff
```

## 知识点导航

| 节 | 主题 | 核心要点 | 入口 | 重要度 |
|---|---|---|---|---|
| 2.1 | Oracle软硬件环境要求 | 硬件基线（内存/磁盘/Swap/tmpfs）、内核参数、用户组、目录结构ORACLE_BASE/HOME | [[2.1 Oracle软硬件环境要求]] | ⭐⭐⭐⭐ |
| 2.2 | 数据库软件安装步骤 | GUI图形化安装流程、先决条件检查、静默安装response file、DBCA建库、NETCA监听配置 | [[2.2 数据库软件安装步骤]] | ⭐⭐⭐⭐⭐ |
| 2.3 | 监听与环境变量配置 | listener.ora/tnsnames.ora、ORACLE_HOME/SID/PATH/LD_LIBRARY_PATH/NLS_LANG、lsnrctl/tnsping/sqlplus验证 | [[2.3 监听程序、环境变量配置]] | ⭐⭐⭐⭐⭐ |

## 核心考点

> [!warning] 重点掌握
> 1. **ORACLE_BASE vs ORACLE_HOME**：BASE是Oracle产品根目录，HOME是特定版本软件目录（多版本并存时BASE下有多个HOME）
> 2. **用户与组**：oracle用户（软件所有者）、oinstall组（主组，安装组）、dba组（OS认证组，对应SYSDBA权限）
> 3. **内核参数/etc/sysctl.conf**：semmsl/semmns/semopm/semmni信号量、shmmax共享内存、shmmni、file-max文件句柄
> 4. **两种安装方式**：GUI（runInstaller）适合学习；静默安装（-silent -responseFile）适合脚本化批量部署
> 5. **建库三工具**：DBCA图形化建库 → NETCA配置监听 → 手动创建数据库（CREATE DATABASE，高级DBA掌握）
> 6. **监听配置三大件**：listener.ora（服务端）、tnsnames.ora（客户端别名）、sqlnet.ora（全局网络参数）
> 7. **环境变量六件套**：ORACLE_BASE、ORACLE_HOME、ORACLE_SID、PATH、LD_LIBRARY_PATH、NLS_LANG
> 8. **连接诊断三步走**：lsnrctl status看监听 → tnsping别名看网络 → sqlplus用户名/密码@别名验证登录

## 自测题

> [!question] 自测题1
> 为什么Oracle要求Swap分区至少等于物理内存大小（当内存≤16GB时）？如果Swap设置过小会导致什么问题？
> 
> > [!check]- 参考答案
> > - Oracle SGA+PGA会占用大量内存，Swap作为物理内存不足时的兜底缓冲，防止内核OOM Killer杀掉Oracle进程
> > - Swap设置过小的后果：① 内存压力大时直接触发OOM Killer杀进程（数据库异常挂掉）；② 安装时先决条件检查失败，无法启动安装程序；③ 大事务/大排序场景下PGA不足报错ORA-04030（进程内存不足）
> > - 推荐规则：RAM≤8GB → Swap=RAM；8GB<RAM≤16GB → Swap=8GB；RAM>16GB → Swap≥16GB

> [!question] 自测题2
> Oracle安装后执行$ORACLE_HOME/root.sh脚本的作用是什么？用哪个用户执行？
> 
> > [!check]- 参考答案
> > - **执行用户**：必须用root用户执行（oracle用户无权限修改系统级文件）
> > - **主要作用**：
> >   1. 将oracle可执行文件权限设置为SETUID（允许普通用户启动Oracle进程）
> >   2. 在/etc/oratab注册数据库实例（供dbstart/dbshut脚本使用，自动启停）
> >   3. 配置/usr/local/bin下的dbhome、oraenv、coraenv环境变量脚本
> >   4. 配置系统服务（如系统服务systemd/init.d脚本
> > - 安装流程中，GUI安装完成后会弹窗提示手动执行root.sh

> [!question] 自测题3
> 说明listener.ora和tnsnames.ora各自的作用，位于客户端还是服务端？
> 
> > [!check]- 参考答案
> > - **listener.ora（服务端配置）**：
> >   - 位置：Oracle服务器端$ORACLE_HOME/network/admin/
> >   - 作用：配置监听器监听哪些地址/端口，静态注册哪些SID（也可以省略，监听器动态注册实例到监听）
> >   - 典型配置：LISTENER=(ADDRESS=(PROTOCOL=TCP)(HOST=xxx)(PORT=1521))
> > - **tnsnames.ora（客户端配置）**：
> >   - 位置：客户端$ORACLE_HOME/network/admin/（客户端端均可存在，服务端也可有用于连接其他数据库）
> >   - 作用：定义网络服务名别名（如ORCL = 描述连接串映射，将别名转换为主机:端口:服务名
> >   - 典型用途：sqlplus scott/tiger@ORCL 中的ORCL就是tnsnames.ora中定义的别名

> [!question] 自测题4
> Oracle用户的.bash_profile中设置了export ORACLE_SID=prod，但是执行sqlplus / as sysdba报错ORA-01034: ORACLE not available，可能的原因有哪些？
> 
> > [!check]- 参考答案
> > 按排查优先级排序：
> > 1. **实例根本没启动**：`ps -ef | grep pmon`查看PMON进程是否存在，不存在需执行STARTUP
> > 2. **ORACLE_SID与实际实例名不符**：ps -ef | grep ora_pmon_ 后面的后缀就是实际SID，如果显示ora_pmon_test而ORACLE_SID=prod就不匹配
> > 3. **ORACLE_HOME设置错误**：$ORACLE_HOME/bin/oracle可执行文件路径不对，导致无法找到实例
> > 4. **操作系统用户不属于dba组**：id命令查看当前用户组，不属于dba组会导致"/"OS认证失败
> > 5. **共享内存段残留**：上次异常关闭后共享内存没释放，ipcs -m查看残留段后ipcrm -m shmid清理

## 章节导航

- 上一级：[[MOC - Oracle数据库管理]]
- 上一章：[[MOC - 第1章 Oracle数据库概述]]
- 下一章：[[MOC - 第3章]]
- 本章习题：[[MOC - 第2章习题]]
- 上一章习题：[[MOC - 第1章习题]]
- 下一章习题：[[MOC - 第3章习题]]
