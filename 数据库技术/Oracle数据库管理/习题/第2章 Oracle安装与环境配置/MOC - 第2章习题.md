---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第2章 Oracle安装与环境配置
section: 2.1 Oracle软硬件环境要求
tags: [Oracle,习题,DBA,安装,监听,环境变量,lsnrctl]
prerequisites: ["数据库原理", "MOC - 第2章 Oracle安装与环境配置"]
---

# MOC - 第2章 Oracle安装与环境配置 习题

> [!tip] 做题建议
> 本章习题覆盖安装准备、安装步骤、监听与环境变量。建议搭配虚拟机动手实战安装一遍，实操胜过死记硬背。

---

## 一、单选题（10题×2分=20分）

### 1.
Oracle 19c数据库软件解压包LINUX.X64_193000_db_home.zip应该解压到哪个目录？（  ）
A. /tmp/oracle_install临时目录，然后安装时指定HOME
B. 目标ORACLE_HOME目录本身
C. ORACLE_BASE根目录
D. oraInventory目录

<details>
<summary>查看答案</summary>
**B**。Oracle 19c重大变化：安装包必须直接解压到ORACLE_HOME（如/product/19.3.0/dbhome_1），解压后目录内容就是ORACLE_HOME内容，直接./runInstaller。这和11g/12cR1解压到临时目录再指定HOME不同。
</details>

### 2.
Oracle数据库软件的安装用户应该是？（  ）
A. root用户
B. oracle用户
C. grid用户
D. 任意用户均可

<details>
<summary>查看答案</summary>
**B**。Oracle软件必须由oracle用户（主组oinstall、附加组dba）安装。严禁root用户安装会导致权限问题不可修复。grid是安装ASM/Grid Infrastructure集群用户。
</details>

### 3.
以下哪个环境变量指向的是Oracle产品根目录，包含多版本数据库软件？（  ）
A. ORACLE_HOME
B. ORACLE_BASE
C. ORACLE_SID
D. TNS_ADMIN

<details>
<summary>查看答案</summary>
**B**。ORACLE_BASE是Oracle根目录（如/u01/app/oracle），其下product/子目录存放多个ORACLE_HOME版本（如11g/19c并存）。
</details>

### 4.
Oracle监听器默认监听的TCP端口号是？（  ）
A. 1521
B. 1522
C. 3306
D. 1526

<details>
<summary>查看答案</summary>
**A**。默认1521。1522/1526是常见的修改后的非默认端口。生产建议修改默认端口1522/1526等。
</details>

### 5.
修改listener.ora后，想让监听重新加载配置而不中断已连接会话，应该执行哪个命令？（  ）
A. lsnrctl restart
B. lsnrctl stop; lsnrctl start
C. lsnrctl reload
D. lsnrctl refresh

<details>
<summary>查看答案</summary>
**C**。reload重载监听配置，已建立的客户端连接不受影响。stop/start或restart会中断现有连接。
</details>

### 6.
安装Oracle时先决条件检查不通过（如内核参数/sem参数设置不够），生产环境正确做法是？（  ）
A. 点Ignore All忽略，强制安装
B. 运行Fixup Script修复脚本（CVU生成runfixup.sh）或手动改sysctl.conf后sysctl -p生效
C. 直接重启服务器
D. 升级硬件

<details>
<summary>查看答案</summary>
**B**。生产必须解决，首选Fixup Script（自动修复大部分参数），然后sysctl -p；A不推荐，除非测试环境临时装。
</details>

### 7.
下列哪个Oracle用户组对应SYSDBA权限的操作系统认证，即组成员可以sqlplus / as sysdba登录？（  ）
A. oinstall
B. dba
C. oper
D. asmadmin

<details>
<summary>查看答案</summary>
**B**。dba组=OS认证SYSDBA组。oinstall是Oracle Inventory安装组（软件文件属主组，主组）。oper是SYSOPER权限组。
</details>

### 8.
tnsnames.ora中推荐使用以下哪种方式指定连接的数据库，以支持RAC和ADG的灵活切换？（  ）
A. SID = orcl
B. SERVICE_NAME = orcl.example.com
C. INSTANCE_NAME = orcl
D. DB_NAME = orcl

<details>
<summary>查看答案</summary>
**B**。推荐使用SERVICE_NAME。SID只单实例支持，不支持RAC负载均衡/故障转移和ADG切换。
</details>

### 9.
以下哪个命令是只检查别名解析、IP端口、监听服务名注册情况，**不验证用户名密码**？（  ）
A. sqlplus scott/tiger@ORCL
B. lsnrctl status
C. tnsping ORCL
D. ping 192.168.1.100

<details>
<summary>查看答案</summary>
**C**。tnsping只测试网络+服务名注册。sqlplus验证密码。ping只测试IP通。lsnrctl是监听管理不是测试连接。
</details>

### 10.
安装完成后root.sh脚本的作用不包括？（  ）
A. 设置oracle二进制SETUID权限
B. 注册/etc/oratab数据库实例信息
C. 创建oracle用户和dba组
D. 设置/usr/local/bin/dbhome等脚本

<details>
<summary>查看答案</summary>
**C**。用户/组在**安装前**手动创建或预安装RPM包创建。root.sh不创建用户。
</details>

---

## 二、多选题（5题×3分=15分）

### 11.
Oracle 19c Linux安装前需要配置的内核参数包括？（  ）
A. kernel.shmmax / kernel.shmmni / kernel.shmall（共享内存）
B. kernel.sem信号量
C. fs.file-max打开文件数
D. net.ipv4.ip_local_port_range端口范围
E. net.core.rmem_max/wmem_max Socket缓冲区

<details>
<summary>查看答案</summary>
**ABCDE**。五个都是必须配置的核心内核参数。
</details>

### 12.
静默安装Oracle的特点和使用场景是？（  ）
A. 适合批量部署、无人值守、脚本自动化
B. 需要response file响应文件
C. 运行时不需要DISPLAY环境变量
D. 安装过程没有GUI界面
E. 安装成功率比GUI高

<details>
<summary>查看答案</summary>
**ABCD**。E错误，两者成功率相同，只是方式不同。
</details>

### 13.
以下哪些是Oracle 19c安装后必须配置的环境变量？（  ）
A. ORACLE_BASE
B. ORACLE_HOME
C. ORACLE_SID
D. PATH加入$ORACLE_HOME/bin
E. LD_LIBRARY_PATH
F. NLS_LANG

<details>
<summary>查看答案</summary>
**ABCDEF**全选。六个都是必须的，生产建议全部配置到.bash_profile。
</details>

### 14.
客户端执行`sqlplus scott/tiger@ORCL`时，报错TNS-12514: TNS:listener does not currently know of service requested in connect descriptor。可能的原因？（  ）
A. 监听器没启动
B. tnsnames.ora中SERVICE_NAME写错了
C. 实例没启动，PMON还没动态注册服务
D. 没配置listener.ora的静态注册SID_LIST_LISTENER，又没等PMON动态注册
E. HOST写错IP地址

<details>
<summary>查看答案</summary>
**BCD**。TNS-12514含义是"监听不知道这个服务名"。A错：监听没启动会报TNS-12541: TNS:no listener。E错：IP不通会报TNS-12543 host unreachable。
</details>

### 15.
DBCA创建数据库时，正确的生产建库原则是？（  ）
A. 字符集选择AL32UTF8（Unicode，避免乱码，全球语言）
B. 启用ARCHIVELOG归档模式
C. 创建为容器数据库CDB + 创建至少1个PDB（Oracle 19c推荐多租户）
D. 配置闪回恢复区FRA（fast_recovery_area
E. SYS/SYSTEM设强密码
F. 用模板Data_Warehouse.dbc创建OLTP交易库

<details>
<summary>查看答案</summary>
**ABCDE**。F错误：OLTP交易库用General_Purpose.dbc（一般用途）或Transaction_Processing.dbc。Data_Warehouse.dbc参数优化面向数据仓库分析场景。
</details>

---

## 三、判断题（5题×2分=10分）

### 16.
Oracle安装程序./runInstaller可以使用root用户执行，因为root拥有最高权限。（  ）

<details>
<summary>查看答案</summary>
**×**。严禁root执行安装程序，必须oracle用户。root安装的后果：属主root:root，oracle用户无法写ORACLE_HOME，后续无法启动/打补丁，且难以修复。
</details>

### 17.
tnsping ORCL执行成功OK（10ms），说明可以正常用sqlplus scott/tiger@ORCL登录数据库。（  ）

<details>
<summary>查看答案</summary>
**×**。tnsping只验证网络层：别名解析+IP通+监听端口+监听服务名注册。不验证用户名密码、实例是否OPEN、用户是否锁。tnsping成功不代表能登录，但是连接诊断第2步。
</details>

### 18.
ORACLE_HOME=/u01/app/oracle/product/19.3.0/dbhome_1，同一台服务器只能有一个ORACLE_HOME（一个Oracle版本）。（  ）

<details>
<summary>查看答案</summary>
**×**。一个ORACLE_BASE下可以存在多个ORACLE_HOME，如同时安装11g（dbhome_2）和19c（dbhome_1），通过切换.bash_profile的ORACLE_HOME/PATH来使用。多版本并存很常见（迁移/升级场景）。
</details>

### 19.
Oracle监听是实例的一部分，实例关闭监听也会停止。（  ）

<details>
<summary>查看答案</summary>
**×**。监听是**独立**于实例的进程，实例关闭监听仍运行。监听关闭不影响已经建立的连接（客户端和服务器进程直连，不需要监听中转）。
</details>

### 20.
shmmax内核参数推荐设置为物理内存的一半，单位是字节。（  ）

<details>
<summary>查看答案</summary>
**√**。kernel.shmmax=单个共享内存段的最大大小，单位字节。生产推荐：RAM≥8GB时shmmax=物理内存的50%（如16GB RAM → 8GB=8589934592字节）。
</details>

---

## 四、简答题（4题×5分=20分）

### 21.
请说明oinstall组和dba组的区别，哪个是oracle用户的主组？

<details>
<summary>查看答案</summary>

**oinstall组（安装组）**：
- 作用：Oracle Inventory安装清单组，ORACLE_HOME和Inventory下所有软件文件的**所属组**都是oinstall
- 必须作为oracle用户的**主组（gid）**

**dba组（管理组）**：
- 作用：OS认证SYSDBA组。属于dba组的操作系统用户可以执行`sqlplus / as sysdba`免密登录数据库，拥有SYSDBA超级权限
- 作为oracle用户的**附加组（groups）**

**推荐用户创建命令**：`useradd -g oinstall -G dba oracle`（主组oinstall，附加组dba）。
权限分离（安装和运维权限分离）是生产安全最佳实践。
</details>

### 22.
请说明Oracle启动的三阶段，以及安装完成后`sqlplus / as sysdba`报错"ORA-01034: ORACLE not available"的可能原因和排查步骤。

<details>
<summary>查看答案</summary>

**启动三阶段**：NOMOUNT→MOUNT→OPEN（参见1.3节）

**ORA-01034报错原因+排查**：
1. **实例没启动**（最常见）：`ps -ef | grep ora_pmon`没有PMON进程，需要执行`STARTUP`
2. **ORACLE_SID设置错误**：echo $ORACLE_SID 和 ps ora_pmon_xxx 后缀不一致
3. **ORACLE_HOME错误**：$ORACLE_HOME/bin/oracle可执行路径错误，需要核对PATH
4. **不属于dba组**：`id`查看当前用户是否在dba组
5. **残留共享内存**：异常关闭后`ipcs -m`看残留Oracle共享内存段，`ipcrm -m shmid`清理

排查顺序：`echo $ORACLE_SID` → `ps -ef | grep pmon` → `echo $ORACLE_HOME` → `id`
</details>

### 23.
图形化安装Oracle时DISPLAY变量的作用是什么？远程SSH安装时如何配置X11转发？

<details>
<summary>查看答案</summary>
**DISPLAY变量作用**：告知GUI程序将图形界面输出到哪个X Server显示。Oracle Universal Installer是Java图形程序，必须通过DISPLAY找到显示设备。

**远程SSH X11转发配置**：
1. SSH客户端（Xshell/SecureCRT/MobaXterm）：会话属性→连接→SSH→隧道→**勾选转发X11**（Forward X11）
2. 或用命令行`ssh -X oracle@服务器IP`（-X=启用X11转发）
3. 连接后验证：`echo $DISPLAY` 会自动设置成`localhost:10.0`左右
4. 测试图形：`xclock` / `xeyes`弹出小钟表窗口即可
5. 运行`cd $ORACLE_HOME && ./runInstaller`启动GUI

如果没配置X转发就运行./runInstaller，会报错：`Exception in thread "main" java.lang.NoClassDefFoundError`或DISPLAY not set。
</details>

### 24.
请写Oracle 19c生产建库DBCA时，需要特别注意的字符集、归档、FRA、CDB/PDB四个关键配置项的选择及理由。

<details>
<summary>查看答案</summary>

| 配置项 | 正确选择 | 理由 |
|---|---|---|
| **字符集 Character Set** | **AL32UTF8** | ① 原生Unicode，支持全球语言，② 防止ZHS16GBK遇到生僻字/表情符号存储乱码或报错；③ 字符集在建库后无法变更只能迁移，必须选对 |
| **归档模式 Archivelog** | **✅ 启用ARCHIVELOG** | ① 生产必须做热备份；② 支持PITR时间点恢复；③ 最大保护模式ADG需要；④ NOARCHIVELOG恢复只能恢复到最后冷备，丢失所有数据（生产事故） |
| **闪回恢复区 FRA** | **✅ 配置FRA大小≥数据库大小+归档** | ① 归档日志/RMAN备份集/闪回日志/控制文件自动备份默认放在FRA；② 统一备份管理；③ 备份恢复策略集中，便于监控FRA空间占用率 |
| **CDB多租户** | **✅ 创建容器数据库（CDB）+ 至少1个PDB** | ① Oracle 19c方向和未来支持：20c以后非CDB不支持；② 一个CDB承载多PDB便于整合；③ PDB快速克隆、拔插迁移便捷；④ 19c默认推荐架构 |
</details>

---

## 五、分析实操题（4题×7分=28分）

### 25.
请根据以下环境，写出完整的环境变量配置（/home/oracle/.bash_profile），并写出验证每一步生效的命令：
- ORACLE_BASE=/u01/app/oracle
- ORACLE_HOME=/u01/app/oracle/product/19.3.0/dbhome_1
- ORACLE_SID=prod
- 字符集AMERICAN_AMERICA.AL32UTF8

<details>
<summary>查看答案</summary>

```bash
# vi /home/oracle/.bash_profile 追加：
# Oracle 19c Settings
export ORACLE_BASE=/u01/app/oracle
export ORACLE_HOME=$ORACLE_BASE/product/19.3.0/dbhome_1
export ORACLE_SID=prod
export PATH=$ORACLE_HOME/bin:$PATH
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export NLS_LANG=AMERICAN_AMERICA.AL32UTF8
umask 022

# 生效（二选一）：
source /home/oracle/.bash_profile
# 或重新登录 su - oracle

# 验证命令：
echo $ORACLE_BASE      # 输出 /u01/app/oracle
echo $ORACLE_HOME      # 输出 /u01/app/oracle/product/19.3.0/dbhome_1
echo $ORACLE_SID       # 输出 prod
echo $PATH             # 包含 $ORACLE_HOME/bin
which sqlplus          # 输出$ORACLE_HOME/bin/sqlplus（找到可执行文件）
sqlplus -v             # 输出版本 19.0.0.0.0
echo $NLS_LANG         # 输出 AMERICAN_AMERICA.AL32UTF8
```
</details>

### 26.
某DBA在CentOS 7 + Oracle 19c安装完成后，配置了监听器。客户端执行：
```
sqlplus system/Oracle123@ORCL
报错：TNS-12541: TNS:no listener
```
请分析可能的5个原因，并写出对应的排查命令。

<details>
<summary>查看答案</summary>

TNS-12541含义：**监听器进程根本没运行或端口不通**。

| 序号 | 可能原因 | 排查命令 | 修复方法 |
|---|---|---|---|
| 1 | **监听器没启动**（最常见） | `lsnrctl status` → 报TNS-12541说明没启动 | `lsnrctl start` 启动监听 |
| 2 | **客户端tnsnames.ora PORT写错（写成1522，实际监听1521** | `tnsping ORCL`看Attempting connect的端口是否对得上 | 修改tnsnames.ora中PORT=1521 |
| 3 | **服务器防火墙没放行1521** | 服务器`systemctl status firewalld`；客户端`telnet server_ip 1521`→不通 | root执行`firewall-cmd --permanent --add-port=1521/tcp && firewall-cmd --reload` |
| 4 | **监听器监听地址绑错HOST（绑localhost导致外部连不上）** | listener.ora中`(HOST=localhost)`应该是实际IP/主机名 | 修改listener.ora中HOST=实际IP/0.0.0.0，然后`lsnrctl reload` |
| 5 | **SELinux未关闭/Enforcing，强制拦截Oracle监听端口** | `getenforce` → 输出Enforcing | 临时`setenforce 0`；永久改`/etc/selinux/config SELINUX=permissive` |
| 6（扩展 | **监听名非默认LISTENER，lsnrctl status没指定监听名** | `ps -ef | grep tnslsnr`看实际启动的监听名 | `lsnrctl status LISTENER2`指定监听名 |
</details>

### 27.
请写出Oracle 19c静默安装软件的完整步骤。包括：①解压、②准备response file、③执行静默安装命令、④查看日志、⑤执行root脚本、⑥验证安装成功。

<details>
<summary>查看答案</summary>

```bash
# ① 解压安装包到ORACLE_HOME（必须直接解压到HOME！19c规则）
su - oracle
mkdir -p $ORACLE_HOME
cd $ORACLE_HOME
unzip /soft/LINUX.X64_193000_db_home.zip -d $ORACLE_HOME

# ② 准备 response file（或从GUI安装时Save Response File保存的文件修改
cat > /soft/db_install_ee.rsp <<'EOF'
oracle.install.option=INSTALL_DB_SWONLY
ORACLE_HOSTNAME=db1.example.com
UNIX_GROUP_NAME=oinstall
INVENTORY_LOCATION=/u01/app/oraInventory
SELECTED_LANGUAGES=en,zh_CN
oracle.install.db.InstallEdition=EE
oracle.install.db.OSDBA_GROUP=dba
oracle.install.db.OSOPER_GROUP=oper
oracle.install.db.OSBACKUPDBA_GROUP=dba
oracle.install.db.OSDGDBA_GROUP=dba
oracle.install.db.OSKMDBA_GROUP=dba
oracle.install.db.OSRACDBA_GROUP=dba
EOF

# ③ 执行静默安装（oracle用户，cd到HOME）
cd $ORACLE_HOME
./runInstaller -silent -force -ignorePrereqFailure \
  -responseFile /soft/db_install_ee.rsp \
  -waitForCompletion
# -waitForCompletion让安装进程前台运行，便于看进度

# ④ 实时看日志（新开窗口tail日志
tail -100f /u01/app/oraInventory/logs/installActions*.log
# 成功日志尾部会显示：Successfully Setup Software.
# The installation of Oracle Database 19c was successful.
# Please execute /u01/app/oraInventory/orainstRoot.sh and $ORACLE_HOME/root.sh

# ⑤ root用户执行脚本（重要！必须root执行
su - root
sh /u01/app/oraInventory/orainstRoot.sh   # 首次安装需要
sh /u01/app/oracle/product/19.3.0/dbhome_1/root.sh
# 一路Enter默认路径

# ⑥ 验证安装成功（切回oracle
su - oracle
sqlplus -v
# SQL*Plus: Release 19.0.0.0.0 - Production
$ORACLE_HOME/bin/lsnrctl -v
# LSNRCTL for Linux: Version 19.0.0.0.0 - Production
echo $ORACLE_HOME && ls $ORACLE_HOME/bin/oracle   # oracle二进制存在即可
```
</details>

### 28.
某应用服务器JDBC连接串：`jdbc:oracle:thin:@//192.168.1.100:1521/oltp.example.com` 报 ORA-12514。数据库服务器上执行：
```
sqlplus / as sysdba 能登录
SQL> show parameter service_names;
service_names = oltp,oltp.example.com
SQL> show parameter local_listener;
local_listener = ''
```
`lsnrctl status` 显示：
```
Services Summary...
Service "orcl" has 1 instance(s).
  Instance "orcl", status READY, has 1 handler(s)...
The command completed successfully
```
请分析问题根源，为什么JDBC用`oltp.example.com`连不上，以及如何修复。

<details>
<summary>查看答案</summary>

**根源分析**：
1. SYS能登录→实例正常OPEN
2. `show parameter service_names=oltp,oltp.example.com`→数据库确实对外注册了`oltp.example.com`服务名
3. `local_listener=''`（空值）→PMON自动向默认端口1521注册服务名
4. 但是**lsnrctl status只显示Service "orcl"，不显示"oltp.example.com"**！

问题在于：监听里注册的只有**orcl**服务名，JDBC用oltp.example.com连→监听无此服务名→TNS-12514。

**为什么service_names设置了没注册到监听？**
- service_names参数动态生效可能没刷新PMON注册；或者service_names参数是刚ALTER SYSTEM SET但没触发PMON向监听重注册。

**修复方法**：
```sql
-- ① 手动触发PMON立即重注册服务名：
ALTER SYSTEM REGISTER;

-- ② 再等1分钟，看lsnrctl services应该就多了oltp.example.com：
-- lsnrctl status再次查看应该显示：
-- Service "oltp.example.com" has 1 instance(s)...

-- 如果还不生效，用静态注册listener.ora SID_LIST_段强制写死（一劳永逸：
-- listener.ora追加：
SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = oltp.example.com)
      (ORACLE_HOME = /u01/app/oracle/product/19.3.0/dbhome_1)
      (SID_NAME = orcl)
    )
  )
-- 然后 lsnrctl reload重载
```

**总结**：JDBC串的Service Name必须和lsnrctl services显示的一致，而不是和数据库参数service_names一致（PMON可能没注册成功，需要ALTER SYSTEM REGISTER触发或静态注册）。
</details>

---

## 六、综合设计题（2题×8分=16分）

### 29.
某企业部署Oracle 19c生产库，服务器配置：2颗Intel Xeon（共24核）、128GB DDR4内存、2块SSD系统盘RAID1做系统、6块SSD数据盘（4TB每块）做数据。预算充足，要求7×24小时运行，性能稳定。

请完成：① Swap分区大小规划、②内核参数kernel.shmmax/shmall/sem设置、③SGA/PGA内存分配建议、④磁盘分区/挂载规划（含ASM建议）、⑤ORACLE_BASE/HOME路径规范。

<details>
<summary>查看答案</summary>

**① Swap分区**：128GB RAM>16GB → Swap至少16GB，推荐**32GB**（128GB的25%）。独立SSD分区。

**② 内核参数 /etc/sysctl.conf**：
```
# 共享内存：128GB RAM → shmmax设为64GB（内存一半）= 68719476736字节
kernel.shmmax = 68719476736
# shmmni=共享内存段最小4096，足够
kernel.shmmni = 4096
# shmall=总可用共享内存页数（PAGE_SIZE=4096字节，128GB/4KB=33554432页
kernel.shmall = 33554432
# 信号量：semmsl设为PROCESSES+10=5010，Oracle推荐250/32000/100/128（PROCESSES默认，生产加到5010 512000 5010 2048）
kernel.sem = 5010 512000 5010 2048
# 文件句柄：百万级
fs.file-max = 6815744
# 端口范围
net.ipv4.ip_local_port_range = 9000 65500
# Socket缓冲
net.core.rmem_default = 262144
net.core.rmem_max = 4194304
net.core.wmem_default = 262144
net.core.wmem_max = 1048576
# 异步IO
fs.aio-max-nr = 1048576
```

**③ SGA/PGA内存分配建议（Oracle 19c AMM不推荐生产，推荐ASMM自动共享内存管理）**：
- 128GB内存：OS保留16-20GB（15%左右），剩余约108GB给Oracle
- MEMORY_TARGET/MEMORY_MAX_TARGET：不推荐，生产用ASMM
- SGA_TARGET/SGA_MAX_SIZE= **72GB**（66.7%）（数据库缓冲区为主
- PGA_AGGREGATE_TARGET= **36GB**（33.3%）（OLTP系统PGA通常是SGA的一半
- 后期AWR调优：SGA/PGA比例可按Buffer Cache Hit Ratio调整

**④ 磁盘规划**：
推荐**ASM**（企业生产标配），6块SSD 4TB组建磁盘组：
- `DATA磁盘组`：4块SSD做NORMAL冗余（2向镜像，可用容量~8TB）→存数据文件、控制文件、在线日志
- `FRA磁盘组`：2块SSD做NORMAL冗余（可用容量~4TB）→存归档日志、RMAN备份、闪回日志
- 系统盘2块480GB RAID1装OS+ORACLE_BASE（不放在ASM里
- ORACLE_HOME：系统盘上/u01/app/oracle/product/19.3.0/dbhome_1（软件不放在ASM，OS文件系统

**⑤ 目录规范（OFA标准）**：
- ORACLE_BASE=/u01/app/oracle（系统盘RAID1
- ORACLE_HOME=/u01/app/oracle/product/19.3.0/dbhome_1
- ASM DATA磁盘组路径：+DATA/ORCL/DATAFILE/...（数据文件
- ASM FRA磁盘组路径：+FRA/ORCL/ARCHIVELOG/...（归档、备份
- 闪回恢复区大小=FRA磁盘组大小，`DB_RECOVERY_FILE_DEST=+FRA DB_RECOVERY_FILE_DEST_SIZE=4096G`
- oraInventory=/u01/app/oraInventory
</details>

### 30.
某测试环境部署Oracle 19c，DBA执行完安装建库后，发现：
1. sqlplus / as sysdba 本地能连上；
2. `lsnrctl start`启动监听成功；
3. 但执行`sqlplus scott/tiger@ORCL`报错ORA-28000: the account is locked。

请：① 解释28000原因；② 写出解锁scott用户并设置密码的SQL；③ 说明如果报错改为ORA-01017 invalid username/password怎么处理；④ 说明如果报错改为ORA-01033 ORACLE initialization or shutdown in progress怎么处理。

<details>
<summary>查看答案</summary>

**① ORA-28000: the account is locked 原因**：
Oracle 11g后默认启用PASSWORD_VERIFY_FUNCTION（密码复杂度验证）和FAILED_LOGIN_ATTEMPTS（默认10次），scott用户默认在创建时就是**锁定状态**的。Oracle 12c以后示例用户scott/hr默认不自动创建，即使创建也是锁定状态。DBA创建时没解锁。

**② 解锁scott用户SQL**：
```sql
-- Oracle 19c SYS登录
sqlplus / as sysdba
-- 解锁+重置密码：
ALTER USER scott ACCOUNT UNLOCK;
ALTER USER scott IDENTIFIED BY Tiger123#;   -- 符合密码复杂度
-- 或者合并：
ALTER USER scott IDENTIFIED BY Tiger123# ACCOUNT UNLOCK;

-- 查看用户状态：
SELECT username, account_status FROM dba_users WHERE username='SCOTT';
-- 显示OPEN说明正常，LOCKED(TIMED)表示被临时锁定（输错多次）
```

**③ 报错ORA-01017 invalid username/password; logon denied**：
- 原因：用户名或密码错误（大小写敏感！12c+参数sec_case_sensitive_logon=true默认开启）
- 处理：
  1. 确认用户名存在：`SELECT * FROM dba_users WHERE username='SCOTT'`（注意username存大写！
  2. 重置密码：`ALTER USER scott IDENTIFIED BY 新密码`
  3. 确认远程用密码文件认证：`show parameter remote_login_passwordfile`=EXCLUSIVE
  4. 密码文件重建（损坏时：`orapwd file=$ORACLE_HOME/dbs/orapworcl password=xxx force=y entries=10`

**④ 报错ORA-01033 ORACLE initialization or shutdown in progress**：
- 含义：实例当前不是OPEN状态（在NOMOUNT或MOUNT或正关闭）
- 处理步骤：
  1. `sqlplus / as sysdba` 本地登录
  2. `SELECT status FROM v$instance` 看状态
  3. 如果是STARTED（NOMOUNT）：`ALTER DATABASE MOUNT; ALTER DATABASE OPEN;`
  4. 如果是MOUNTED：`ALTER DATABASE OPEN;`
  5. 如果OPEN报错需要介质恢复（如ORA-01113文件需要介质恢复：`RECOVER DATABASE;`然后ALTER DATABASE OPEN;
  6. 如果ORA-01589需要用RESETLOGS打开：`ALTER DATABASE OPEN RESETLOGS;`
</details>

---

## 考点统计表

| 考点 | 题号 | 分值 | 合计占比 |
|---|---|---|---|
| 软硬件环境要求（内存/kernel参数/用户组/目录结构 | 2,3,7,11,16,20,21,29 | 41 | 41% |
| 安装步骤GUI/静默/DBCA/NETCA | 1,6,10,12,15,17,23,24,27 | 45 | 45% |
| 监听与网络配置 listener/tnsnames/sqlnet | 4,5,8,9,14,18,19,22,26,28,30 | 59 | 59% |
| 环境变量ORACLE_BASE/HOME/SID/PATH/NLS_LANG | 3,13,22,25 | 23 | 23% |
| 综合部署方案 | 29,30 | 16 | 16% |

## 章节导航

- 上一级：[[MOC - Oracle数据库管理]]
- 本章知识点：[[MOC - 第2章 Oracle安装与环境配置]]
- 上一章习题：[[MOC - 第1章习题]]
- 下一章知识点：[[MOC - 第3章]]
- 下一章习题：[[MOC - 第3章习题]]
