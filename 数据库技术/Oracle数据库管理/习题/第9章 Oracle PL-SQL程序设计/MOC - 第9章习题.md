---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第9章 Oracle PL/SQL程序设计
section: 9.9 第9章习题
tags: [Oracle,习题,DBA,PLSQL,存储过程,触发器,游标,异常处理]
prerequisites: ["9.1 PL-SQL块结构", "9.2 存储过程、函数", "9.3 触发器、游标", "9.4 异常处理机制"]
---

# MOC - 第9章习题

> [!info] 习题说明
> 本习题集覆盖 [[MOC - 第9章]] 全部知识点，共 30 题，分六类：单选 10、多选 5、判断 5、简答 4、分析 4（含 PL/SQL 块阅读改错）、综合 2（存储过程+触发器+游标综合编程）。重点考查 PL/SQL 块结构与 %TYPE/%ROWTYPE、存储过程 vs 函数区别与参数模式、AUTHID 权限模型、触发器行级/语句级 + :OLD/:NEW + ORA-04091 变异表、显式游标四步与游标 FOR 循环、REF CURSOR、三类异常与 RAISE_APPLICATION_ERROR、自治事务。分析题与综合题给出完整 plsql 代码答案。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | PL/SQL 块三部分结构与匿名块 | 概念理解 |
| 单2 | 单选 | %TYPE 与 %ROWTYPE 区别 | 概念理解 |
| 单3 | 单选 | SELECT INTO 异常 NO_DATA_FOUND / TOO_MANY_ROWS | 概念理解 |
| 单4 | 单选 | 存储过程参数模式 IN / OUT / IN OUT | 概念理解 |
| 单5 | 单选 | AUTHID DEFINER vs CURRENT_USER 权限模型 | 概念理解 |
| 单6 | 单选 | 函数 RETURN 与 SQL 调用纯度规则 | 概念理解 |
| 单7 | 单选 | 行级触发器 FOR EACH ROW + :OLD/:NEW 值特点 | 概念理解 |
| 单8 | 单选 | 显式游标四步生命周期与属性 %FOUND/%NOTFOUND/%ROWCOUNT | 概念理解 |
| 单9 | 单选 | 三类异常：预定义 / 非预定义 EXCEPTION_INIT / 自定义 | 概念理解 |
| 单10 | 单选 | RAISE_APPLICATION_ERROR 错误号范围 | 综合应用 |
| 多1 | 多选 | PL/SQL 复合类型：RECORD / TABLE / VARRAY | 概念辨析 |
| 多2 | 多选 | 存储过程与函数对比：RETURN / SQL中调用 / DML | 概念辨析 |
| 多3 | 多选 | 触发器类型：DML 行级/语句级 / INSTEAD OF / DDL / 系统事件 | 概念辨析 |
| 多4 | 多选 | 游标的正确用法：隐式 SQL% / 显式 / REF CURSOR | 概念辨析 |
| 多5 | 多选 | 异常处理最佳实践：WHEN OTHERS / 自治事务 / 传播 | 概念辨析 |
| 判1 | 判断 | PL/SQL 块中 DECLARE 和 EXCEPTION 都可以省略 | 概念理解 |
| 判2 | 判断 | 存储过程参数 OUT 模式可以传入初始值并被修改 | 概念理解 |
| 判3 | 判断 | BEFORE 行级触发器中可以修改 :NEW 的列值 | 概念理解 |
| 判4 | 判断 | 显式游标 FOR 循环需要手动 OPEN / FETCH / CLOSE | 概念理解 |
| 判5 | 判断 | WHEN OTHERS THEN NULL 是良好的异常处理习惯 | 概念理解 |
| 简1 | 简答 | 简述 PL/SQL 块结构、%TYPE/%ROWTYPE、为什么 SELECT INTO 只能一行 | 分析说明 |
| 简2 | 简答 | 对比存储过程 PROCEDURE 与函数 FUNCTION 的 5 个核心差异 | 分析说明 |
| 简3 | 简答 | 行级/语句级触发器区别 + :OLD/:NEW 在 INSERT/UPDATE/DELETE 中的值 + ORA-04091 变异表原因与解决 | 分析说明 |
| 简4 | 简答 | PL/SQL 三类异常各是什么 + RAISE_APPLICATION_ERROR 使用方式 + 自治事务用途与写法 | 分析说明 |
| 分1 | 分析 | PL/SQL 匿名块阅读 + 填空输出 + 异常触发分析 | 综合应用 |
| 分2 | 分析 | 触发器代码改错（变异表 / 时机错误 / 谓词判断） | 综合应用 |
| 分3 | 分析 | 游标 LOOP 代码阅读：输出每行 + 总行数统计 + 游标属性判断 | 综合应用 |
| 分4 | 分析 | 异常传播链分析：嵌套块 + 过程调用链异常逐层传播结果 | 综合应用 |
| 综1 | 综合 | 编写 pkg_emp 包：员工工资管理（过程+函数+异常+游标） | 综合应用 |
| 综2 | 综合 | 触发器+存储过程综合：订单库存扣减 + 审计日志（含自治事务） | 综合应用 |

---

## 一、单选题（每题 2 分，共 10 题）

**1. 下列关于 PL/SQL 匿名块结构的说法，正确的是（　）。**
A. DECLARE、BEGIN、EXCEPTION 三部分都必须出现
B. BEGIN...END 是必须的，DECLARE 和 EXCEPTION 可以省略
C. 匿名块执行需要先 CREATE 再调用
D. 匿名块结尾必须写 EXIT;

**2. 关于 %TYPE 和 %ROWTYPE，下列说法正确的是（　）。**
A. %TYPE 用于继承表整行的类型，%ROWTYPE 用于继承单列类型
B. %TYPE 用于继承单列类型，%ROWTYPE 用于继承整行记录类型
C. 两者功能相同，可以互换
D. %TYPE 只能继承变量类型，不能继承表列类型

**3. PL/SQL 中 `SELECT ename INTO v_ename FROM emp WHERE job='CLERK';` 语句，当 JOB='CLERK' 的员工有 5 人时，会触发（　）异常。**
A. NO_DATA_FOUND
B. TOO_MANY_ROWS
C. VALUE_ERROR
D. INVALID_CURSOR

**4. 存储过程参数中，表示"双向传递：读入初始值，过程内可修改并传出结果"的模式是（　）。**
A. IN
B. OUT
C. IN OUT
D. NOCOPY

**5. 关于 AUTHID DEFINER 与 CURRENT_USER，下列说法正确的是（　）。**
A. 默认是 CURRENT_USER
B. DEFINER 权限下，过程以调用者身份访问对象
C. DEFINER 权限下，只要授予 EXECUTE 权限，调用者即可访问 OWNER 的底层表（不需直接给表权限）
D. CURRENT_USER 模式下，底层表的权限必须直接授予 OWNER

**6. 关于 Oracle PL/SQL 函数 FUNCTION，下列说法正确的是（　）。**
A. 函数可以没有 RETURN 子句
B. 函数在 SQL SELECT 中调用时，可以包含 INSERT/UPDATE/DELETE 等 DML
C. 函数必须有 RETURN 子句并在体内至少 RETURN 一次；纯函数可用于 SELECT（但不能有 DML/COMMIT）
D. 函数返回值个数可以多个

**7. 在 UPDATE 操作的 BEFORE 行级触发器中，关于 :OLD 和 :NEW，下列说法正确的是（　）。**
A. :OLD 和 :NEW 都是 NULL
B. :OLD 保存修改前的值（只读），:NEW 保存修改后的新值（可修改）
C. :OLD 保存修改后的值，:NEW 保存修改前的值
D. :OLD 和 :NEW 都可以被自由修改并写入数据库

**8. 显式游标操作的四步正确顺序是（　）。**
A. CLOSE → FETCH → OPEN → DECLARE
B. DECLARE → OPEN → FETCH（循环中配合 EXIT WHEN %NOTFOUND）→ CLOSE
C. OPEN → DECLARE → FETCH → CLOSE
D. DECLARE → FETCH → OPEN → CLOSE

**9. 对于 Oracle 错误 ORA-00060（死锁），正确的 PL/SQL 处理方式是（　）。**
A. 直接用 WHEN ORA_00060 THEN 捕获
B. 声明 e_deadlock EXCEPTION; 然后用 PRAGMA EXCEPTION_INIT(e_deadlock, -60); 关联后 WHEN 捕获
C. 声明 e_deadlock EXCEPTION; 然后用 PRAGMA EXCEPTION_INIT(e_deadlock, 60); 关联
D. 它是预定义异常，直接 WHEN DEADLOCK THEN 捕获

**10. RAISE_APPLICATION_ERROR 自定义错误号的合法范围是（　）。**
A. -10000 到 -1
B. -20000 到 -20999
C. 1 到 9999
D. 任意负整数

---

## 二、多选题（每题 3 分，共 5 题）

**1. PL/SQL 中属于复合（组合）数据类型的有（　）。**
A. NUMBER
B. RECORD（自定义记录）
C. TABLE OF ... INDEX BY BINARY_INTEGER（关联数组）
D. VARRAY（变长数组）
E. DATE

**2. 关于存储过程 PROCEDURE 与函数 FUNCTION，下列说法正确的有（　）。**
A. 函数必须声明 RETURN 返回类型，存储过程不需要
B. 存储过程不能在 SELECT 语句中直接调用，纯函数（无副作用）可以
C. 存储过程通过 OUT/IN OUT 参数传出值，函数通过 RETURN 返回值
D. 存储过程中可以执行 COMMIT/ROLLBACK/DML，函数在 SQL 中调用时不能
E. 两者都可以有多个 RETURN 语句

**3. 下列关于 Oracle 触发器的说法，正确的有（　）。**
A. DML 触发器分为行级（FOR EACH ROW）和语句级两种
B. INSTEAD OF 触发器主要用于多表连接的复杂视图，将对视图的 DML 翻译为对基表的 DML
C. DDL 触发器可以捕获 CREATE / ALTER / DROP 等事件，用于防止误删或审计
D. BEFORE 语句级触发器中可以访问 :OLD 和 :NEW 伪记录
E. 触发器中可以直接 COMMIT，无需自治事务

**4. 关于 PL/SQL 游标，下列说法正确的有（　）。**
A. 隐式游标（SQL 游标）属性 SQL%ROWCOUNT 可获取最近 DML 影响的行数
B. 显式游标循环中 EXIT WHEN c%NOTFOUND 应放在 FETCH 之后
C. 游标 FOR 循环中需要手动写 OPEN / FETCH / CLOSE
D. SYS_REFCURSOR 是 Oracle 11g+ 内置的弱类型 REF CURSOR，可绑定任意 SELECT 并在过程间传递
E. WHERE CURRENT OF cursor_name 需要游标声明时带 FOR UPDATE

**5. PL/SQL 异常处理的最佳实践包括（　）。**
A. 逐层精确匹配：先 WHEN 具体异常（NO_DATA_FOUND 等），最后 WHEN OTHERS 兜底
B. WHEN OTHERS 中至少记录日志或 RAISE，不要只写 NULL 吞掉错误
C. 错误日志记录使用自治事务 PRAGMA AUTONOMOUS_TRANSACTION，保证日志独立提交不随主事务回滚
D. 业务错误优先用 RAISE_APPLICATION_ERROR(-20xxx, '消息')，统一分配错误号段
E. 正常流程控制（如判断记录是否存在）应优先依赖异常 NO_DATA_FOUND，而不是用 COUNT 查询

---

## 三、判断题（每题 2 分，共 5 题）

**1. PL/SQL 块的标准结构是 [DECLARE] ... BEGIN ... [EXCEPTION ...] END; /，其中 DECLARE 与 EXCEPTION 部分都可以省略，只有 BEGIN...END 必填。**

**2. 存储过程的 OUT 模式参数，在进入过程体时初始值是传入值，可被修改后传出；IN OUT 模式则进入过程时初始为 NULL。**

**3. 在 BEFORE INSERT 或 BEFORE UPDATE 的行级触发器中，给 :NEW.列 := 表达式 赋值，会真正写入表中（影响 INSERT/UPDATE 的最终结果）；但在 AFTER 行级触发器中修改 :NEW 无效。**

**4. 游标 FOR 循环（FOR r IN cursor_name LOOP...END LOOP;）中必须手动执行 OPEN 游标、FETCH 取值、EXIT WHEN 判断、CLOSE 游标四个步骤，否则报错。**

**5. 异常处理中写 `WHEN OTHERS THEN NULL;` 是推荐的做法，因为可以保证过程不会报错中断。**

---

## 四、简答题（每题 5 分，共 4 题）

**1. 简述 PL/SQL 块的三部分结构。说明 %TYPE 和 %ROWTYPE 的作用与区别。为什么 PL/SQL 中 SELECT 语句必须带 INTO？SELECT INTO 多行/零行时分别触发什么异常？如何处理多行查询？**

**2. 从以下 5 个维度对比 Oracle PL/SQL 存储过程 PROCEDURE 与函数 FUNCTION：(1) RETURN 返回声明；(2) 返回值个数与方式；(3) 是否可在 SQL SELECT/WHERE 中直接调用；(4) 在 SQL 中调用时能否执行 DML/COMMIT；(5) 典型使用场景。**

**3. 回答下列触发器相关问题：**
- (1) 行级触发器（FOR EACH ROW）与语句级触发器的本质区别（触发次数、:OLD/:NEW、适用场景）；
- (2) 分别说明 INSERT / UPDATE / DELETE 三种 DML 中行级触发器的 :OLD 与 :NEW 的值特点；
- (3) 什么是 ORA-04091 变异表错误？在什么场景下会出现？列举至少 2 种解决方法。

**4. 回答下列异常处理相关问题：**
- (1) PL/SQL 的三类异常分别是什么？各举 1 个例子与对应处理方式；
- (2) RAISE_APPLICATION_ERROR 的语法、错误号合法范围、第三个参数 keep_error_stack 的含义；
- (3) 什么是自治事务（AUTONOMOUS_TRANSACTION）？语法怎么写？99% 的使用场景是什么？为什么在写错误日志时必须用？

---

## 五、分析题（每题 8 分，共 4 题，需给出完整推导）

**1. PL/SQL 匿名块阅读与输出分析。**

给出如下 PL/SQL 块（假设 emp 表中 empno=7369 的 ename='SMITH'，sal=800；empno=9999 不存在；SET SERVEROUTPUT ON）：

```plsql
DECLARE
    v_empno NUMBER := 7369;
    v_ename VARCHAR2(10);
    v_sal   NUMBER(7,2);
    c_rate  CONSTANT NUMBER := 0.1;
BEGIN
    BEGIN
        SELECT ename, sal INTO v_ename, v_sal FROM emp WHERE empno = v_empno;
        v_sal := v_sal * (1 + c_rate);
        DBMS_OUTPUT.PUT_LINE('A: ' || v_ename || ' 新工资=' || v_sal);
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('B: 员工不存在');
    END;

    v_empno := 9999;
    SELECT ename, sal INTO v_ename, v_sal FROM emp WHERE empno = v_empno;
    DBMS_OUTPUT.PUT_LINE('C: 不会执行到这里');

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('D: 外层捕获 员工不存在 v_empno=' || v_empno);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('E: 外层兜底 ' || SQLCODE || ' ' || SQLERRM);
END;
/
```

请：
- (1) 按顺序写出 DBMS_OUTPUT 的所有输出内容（A/B/C/D/E 的哪些行会真正输出，内容具体是什么）；
- (2) 解释为什么内层块的异常不会传播到外层；内层块执行完后流程继续到哪里；
- (3) 外层 SELECT 为什么触发异常、为什么在外层 EXCEPTION 被捕获（而不是其他分支）。

**2. 触发器代码改错分析。**

某 DBA 想实现"当修改员工工资时，将员工工资变化记录到 sal_history 表，且工资涨幅不能超过 50%"的需求，编写如下触发器：

```plsql
-- 表sal_history(id, empno, old_sal, new_sal, change_time)
-- 序列seq_sal_hist
CREATE OR REPLACE TRIGGER trg_sal_change
AFTER UPDATE ON emp
FOR EACH STATEMENT
WHEN (new.sal > old.sal * 1.5)
DECLARE
    v_cnt NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_cnt FROM emp;  -- ①统计emp总数

    INSERT INTO sal_history VALUES (
        seq_sal_hist.NEXTVAL,
        :NEW.empno, :OLD.sal, :NEW.sal, SYSDATE
    );
    COMMIT;  -- ②立即提交日志

    IF INSERTING THEN  -- ③判断是INSERT操作
        RAISE_APPLICATION_ERROR(-20001, '不能插入');
    END IF;
END;
/
```

请找出该触发器代码中的至少 **5 处错误**（标 ①②③ 一定是错的，还要找其他），分别说明：
- 错误现象 / 为什么错；
- 正确写法应该是什么（给出修改后的关键代码行）。

**3. 游标代码阅读分析。**

给出如下 PL/SQL 块（假设 deptno=30 下有员工：7499 ALLEN sal=1600，7521 WARD sal=1250，7654 MARTIN sal=1250，7698 BLAKE sal=2850，7844 TURNER sal=1500，7900 JAMES sal=950，共 6 人；SET SERVEROUTPUT ON）：

```plsql
DECLARE
    CURSOR c_dept(p_deptno NUMBER) IS
        SELECT empno, ename, sal FROM emp WHERE deptno = p_deptno ORDER BY sal DESC;
    r c_dept%ROWTYPE;
    v_total_sal NUMBER(10) := 0;
    v_cnt NUMBER := 0;
BEGIN
    OPEN c_dept(30);
    DBMS_OUTPUT.PUT_LINE('ISOPEN? ' || CASE WHEN c_dept%ISOPEN THEN 'Y' ELSE 'N' END);

    LOOP
        FETCH c_dept INTO r;
        EXIT WHEN c_dept%NOTFOUND;
        v_cnt := v_cnt + 1;
        v_total_sal := v_total_sal + r.sal;
        IF c_dept%ROWCOUNT = 1 THEN
            DBMS_OUTPUT.PUT_LINE('TOP1: ' || r.ename || ' ' || r.sal);
        END IF;
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('员工数(ROWCOUNT): ' || c_dept%ROWCOUNT);
    DBMS_OUTPUT.PUT_LINE('员工数(v_cnt): ' || v_cnt);
    DBMS_OUTPUT.PUT_LINE('工资总额: ' || v_total_sal);
    DBMS_OUTPUT.PUT_LINE('平均工资: ' || ROUND(v_total_sal / NULLIF(v_cnt,0), 2));
    CLOSE c_dept;
    DBMS_OUTPUT.PUT_LINE('CLOSE后 ISOPEN? ' || CASE WHEN c_dept%ISOPEN THEN 'Y' ELSE 'N' END);
END;
/
```

请：
- (1) 写出 DBMS_OUTPUT 的所有输出（含每行具体数字与姓名）；
- (2) 说明 c_dept%ROWCOUNT 与手动计数器 v_cnt 为什么值一致；为什么取 TOP1 用 %ROWCOUNT=1 判断；
- (3) 把上述游标代码改写为**游标 FOR 循环版本**，保持输出完全相同（注意不需要手动 OPEN/FETCH/CLOSE、不需要 EXIT WHEN、不需要手动声明记录变量 r）。

**4. 异常传播链分析。**

给出如下三个过程 + 最外层匿名块的调用链：

```plsql
CREATE OR REPLACE PROCEDURE p3 IS
BEGIN
    DBMS_OUTPUT.PUT_LINE('p3 start');
    DECLARE
        v_x NUMBER := 1;
    BEGIN
        v_x := v_x / 0;   -- 抛 ZERO_DIVIDE
    EXCEPTION
        WHEN NO_DATA_FOUND THEN NULL;  -- 不匹配
    END;  -- 内层EXCEPTION没有匹配ZERO_DIVIDE → 向上抛给p3的EXCEPTION
    DBMS_OUTPUT.PUT_LINE('p3 end');  -- 不执行
EXCEPTION
    WHEN VALUE_ERROR THEN   -- 不匹配ZERO_DIVIDE
        DBMS_OUTPUT.PUT_LINE('p3 catch VALUE_ERROR');
    -- 没有WHEN ZERO_DIVIDE，也没有WHEN OTHERS → 继续向调用者p2抛
END p3;
/

CREATE OR REPLACE PROCEDURE p2 IS
BEGIN
    DBMS_OUTPUT.PUT_LINE('p2 start call p3');
    p3;
    DBMS_OUTPUT.PUT_LINE('p2 call p3 success');
EXCEPTION
    WHEN ZERO_DIVIDE THEN
        DBMS_OUTPUT.PUT_LINE('p2 catch ZERO_DIVIDE');
        RAISE;  -- 再次抛出 → 传给调用者p1
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('p2 catch OTHERS');
END p2;
/

CREATE OR REPLACE PROCEDURE p1 IS
BEGIN
    DBMS_OUTPUT.PUT_LINE('p1 start call p2');
    p2;
    DBMS_OUTPUT.PUT_LINE('p1 call p2 success');
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('p1 catch OTHERS: ' || SQLERRM);
        -- 不再RAISE，到此为止
END p1;
/

BEGIN
    DBMS_OUTPUT.PUT_LINE('=== 主块开始 ===');
    p1;
    DBMS_OUTPUT.PUT_LINE('=== 主块正常结束 ===');
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('=== 主块兜底：' || SQLERRM || ' ===');
END;
/
```

请：
- (1) 按执行顺序写出 DBMS_OUTPUT 输出的**所有行**（从"=== 主块开始 ==="到最后一行结束）；
- (2) 解释每一层捕获/传播的理由（为什么 p3 不捕获 → 为什么 p2 捕获后又 RAISE → 为什么 p1 能最终捕获 → 为什么主块能正常结束不走兜底分支）；
- (3) 如果把 p1 EXCEPTION 中的 `WHEN OTHERS THEN ... RAISE;`（加上 RAISE），那么主块最终输出是什么？整个事务会发生什么？

---

## 六、综合题（每题 10 分，共 2 题，PL/SQL 编程）

### 综合题 1：员工工资管理包 pkg_salary（10 分）

**背景：** 基于 SCOTT 用户的 emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) / dept 表。请设计一个包 `pkg_salary`，满足以下全部需求：

**包规范需要公开：**
1. 常量 `C_MAX_RAISE_RATE NUMBER := 50;`（单次最大涨薪比例 50%）、常量 `C_MIN_SAL NUMBER := 500;`（最低工资底线）；
2. 自定义异常 `e_sal_too_low EXCEPTION` 与 `e_rate_too_high EXCEPTION`；
3. 存储过程 `raise_emp_sal(p_empno NUMBER, p_rate NUMBER)`：给指定员工涨薪 p_rate 百分比（sal = sal × (1+p_rate/100)），内部校验：
   - 若 p_rate > C_MAX_RAISE_RATE，抛 e_rate_too_high 异常；
   - 若涨薪后新 sal < C_MIN_SAL，抛 e_sal_too_low 异常（注意：降薪时 p_rate 为负可能导致）；
   - 若员工不存在，抛 RAISE_APPLICATION_ERROR(-20001, '员工不存在：'||p_empno)；
   - 涨薪成功则 COMMIT，异常时 ROLLBACK；
4. 函数 `get_dept_total_sal(p_deptno NUMBER) RETURN NUMBER`：返回指定部门工资总额（纯函数，DETERMINISTIC 可选标记）；
5. 存储过程 `print_dept_emp_report(p_deptno NUMBER)`：用游标 FOR 循环打印指定部门所有员工"姓名-岗位-工资"，每行一条，最后打印"总人数/总工资/平均工资"统计行。

**要求：**
- (1) 写出完整的 **包规范** CREATE PACKAGE 代码；
- (2) 写出完整的 **包体** CREATE PACKAGE BODY 代码（包含私有辅助方法可选），异常处理必须完整（不允许 WHEN OTHERS THEN NULL）；
- (3) 写出 3 段调用示例代码：① 正常涨薪员工 7369 涨 10%；② 异常场景：员工 7369 涨 60% 超过最大比例 → 捕获异常并输出；③ 调用 print_dept_emp_report(20) 打印 20 号部门报告。

---

### 综合题 2：订单-库存触发器 + 存储过程综合（10 分）

**背景：** 有以下三张业务表（请先给出建表 SQL + 序列）：

```sql
-- 商品库存表
CREATE TABLE t_stock (
    goods_id   NUMBER PRIMARY KEY,
    goods_name VARCHAR2(50) NOT NULL,
    stock_qty  NUMBER NOT NULL CHECK (stock_qty >= 0),   -- 剩余库存数量
    unit_price NUMBER(10,2) NOT NULL
);
-- 订单主表
CREATE TABLE t_order (
    order_id   NUMBER PRIMARY KEY,
    user_id    NUMBER NOT NULL,
    amount     NUMBER(12,2) NOT NULL,   -- 订单总金额
    status     VARCHAR2(20) DEFAULT 'CREATED',  -- CREATED/PAID/CANCELLED
    create_time DATE DEFAULT SYSDATE
);
-- 订单明细
CREATE TABLE t_order_item (
    item_id    NUMBER PRIMARY KEY,
    order_id   NUMBER NOT NULL REFERENCES t_order(order_id),
    goods_id   NUMBER NOT NULL REFERENCES t_stock(goods_id),
    buy_qty    NUMBER NOT NULL CHECK (buy_qty > 0),
    subtotal   NUMBER(12,2) NOT NULL
);
-- 操作审计日志（任何情况下都必须保留，不能随事务回滚丢失）
CREATE TABLE t_audit_log (
    log_id     NUMBER PRIMARY KEY,
    op_type    VARCHAR2(20),
    op_desc    VARCHAR2(500),
    op_user    VARCHAR2(30),
    op_time    DATE DEFAULT SYSDATE
);
CREATE SEQUENCE seq_order START WITH 1000;
CREATE SEQUENCE seq_item START WITH 2000;
CREATE SEQUENCE seq_log START WITH 3000;
```

**需求：**
1. **存储过程 `p_create_order(p_user_id NUMBER, p_goods_id NUMBER, p_qty NUMBER, p_order_id OUT NUMBER)`**：下单流程
   - 校验 p_qty > 0，否则 RAISE_APPLICATION_ERROR(-20101, '购买数量必须为正');
   - 从 t_stock 查询库存（FOR UPDATE 锁行），若库存不足（stock_qty < p_qty），抛 RAISE_APPLICATION_ERROR(-20102, '库存不足：现有'||v_stock||'，需要'||p_qty);
   - 计算明细小计 subtotal = p_qty × unit_price；
   - 扣减库存（UPDATE t_stock SET stock_qty = stock_qty - p_qty）；
   - 插入订单主表 + 订单明细；
   - 返回生成的 order_id（用 seq_order）给 OUT 参数；
2. **行级触发器 `trg_stock_check` BEFORE UPDATE OF stock_qty ON t_stock**：防止库存扣成负数
   - 当 :NEW.stock_qty < 0 时，抛 RAISE_APPLICATION_ERROR(-20103, '库存不能为负：goods_id='||:OLD.goods_id||'，扣减后='||:NEW.stock_qty);
3. **行级触发器 `trg_order_audit` AFTER INSERT OR UPDATE OF status ON t_order**：写审计日志（用自治事务）
   - INSERT 操作：记录 op_type='CREATE_ORDER'，op_desc='创建订单，金额='||金额；
   - UPDATE STATUS 操作：记录 op_type='UPDATE_STATUS'，op_desc='订单'||:OLD.order_id||'状态：'||:OLD.status||' → '||:NEW.status；
   - 审计日志必须用自治事务独立 COMMIT，确保不管订单事务成功与否日志都保留；
4. 编写一段**测试匿名块**：用户 1001 购买商品 1（假设先 INSERT 测试数据：goods_id=1, name='iPhone', stock=10, price=5999），购买数量 2 → 成功下单；再购买数量 9 → 触发"库存不足"异常被捕获；最后查询 t_order、t_order_item、t_stock、t_audit_log 验证结果。

**要求：**
- 写出建表 SQL（如上述结构，你需补充或直接引用）+ 建序列 SQL；
- 写出完整的存储过程 `p_create_order` 代码，含异常处理（不允许 WHEN OTHERS THEN NULL，必须 RAIAISE 或记录日志）；
- 写出完整的 2 个触发器代码（`trg_stock_check`、`trg_order_audit`，后者用自治事务）；
- 写出完整的测试匿名块（包含初始化测试数据、两次下单：一次成功 + 一次库存不足捕获异常、最后 SELECT 验证；SET SERVEROUTPUT ON）。

---

## 答案与解析

<details>
<summary>单选题答案与解析</summary>

1. **B**。DECLARE（声明）和 EXCEPTION（异常处理）是可选的，BEGIN...END 必填。匿名块是即时执行的，不需要 CREATE。
2. **B**。%TYPE 继承单列类型，%ROWTYPE 继承整行记录。
3. **B**。SELECT INTO 多于 1 行抛 TOO_MANY_ROWS；零行抛 NO_DATA_FOUND。
4. **C**。IN 只读输入；OUT 只出不进（初始 NULL）；IN OUT 双向。
5. **C**。DEFINER（默认）= 以创建者身份执行，调用者只需 EXECUTE 权限即可访问创建者的表（封装权限）。CURRENT_USER = 以调用者身份执行，调用者需自己有表权限。
6. **C**。函数必须有 RETURN 返回声明，且体内至少 RETURN 一次。纯函数在 SQL 中调用不能有 DML/COMMIT/ROLLBACK/DDL。
7. **B**。UPDATE 中 :OLD 是修改前只读值，:NEW 是修改后的值，BEFORE 中修改 :NEW 会真正写回表。
8. **B**。DECLARE → OPEN → FETCH（LOOP 中配合 EXIT WHEN %NOTFOUND）→ CLOSE。
9. **B**。死锁 ORA-00060 是非预定义异常，EXCEPTION_INIT 第二个参数是 **-60**（负数），不能写 60。
10. **B**。RAISE_APPLICATION_ERROR 的错误号必须在 -20999 ~ -20000 之间（共 1000 个号段，Oracle 保留给用户）。

</details>

<details>
<summary>多选题答案与解析</summary>

1. **BCD**。RECORD / TABLE OF...INDEX BY / VARRAY 都是复合类型。NUMBER、DATE 是标量类型。
2. **ABCD**。E 错误：函数只能 RETURN 一次值（虽可写多个 RETURN 分支，但每次调用仅执行一个 RETURN），过程无 RETURN 语句。
3. **ABC**。D 错误：语句级触发器没有行上下文，不能访问 :OLD/:NEW；E 错误：触发器不能直接 COMMIT，必须用自治事务。
4. **ABDE**。C 错误：游标 FOR 循环**自动**完成 OPEN/FETCH/EXIT/CLOSE，不需要手写。
5. **ABCD**。E 错误：正常流程不要靠异常驱动（性能差、语义不清晰），判断记录是否存在应该用 COUNT 或带 MAX 的 SELECT，NO_DATA_FOUND 仅作为"真的找不到"的异常情况。

</details>

<details>
<summary>判断题答案与解析</summary>

1. **√**。DECLARE 与 EXCEPTION 是可选的，只有 BEGIN...END 是必填。最简单 PL/SQL 块就是 `BEGIN NULL; END; /`。
2. **×**。正好弄反：OUT 模式进入时初始值为 NULL（不管传进来什么都丢弃）；IN OUT 模式进入时保留传入初始值，过程内可读可改。
3. **√**。BEFORE 行级触发器修改 :NEW 能影响最终写入数据库的值（常用于自动填充字段、规范化数据）；AFTER 时行已写入，再改 :NEW 也不会回写。
4. **×**。游标 FOR 循环由 PL/SQL 自动隐式完成 OPEN、FETCH、EXIT WHEN %NOTFOUND、CLOSE 所有步骤。
5. **×**。WHEN OTHERS THEN NULL 会**吞掉所有错误**不记录不处理，是极差的实践（也是很多线上事故的根源）。必须至少记录日志或 RAISE 抛出。

</details>

<details>
<summary>简答题参考答案</summary>

**1. PL/SQL 块结构与 SELECT INTO：**
- **块结构三部分**：DECLARE（可选）声明变量/常量/类型/游标；BEGIN（必填）可执行 SQL 与 PL/SQL 语句；EXCEPTION（可选）WHEN 捕获异常。以 `END;` + `/` 结束。
- **%TYPE**：继承某个列或变量的**单个类型**（`v_sal emp.sal%TYPE`），表结构变更自动适配无需改代码。**%ROWTYPE**：继承整张表或游标 SELECT 的**整行记录**（`r_emp emp%ROWTYPE` 拥有 emp 所有列作为字段）。用途：只处理少数列用 %TYPE，整行读写或过程间传整行用 %ROWTYPE。
- **SELECT 必须带 INTO**：PL/SQL 是过程化语言，SELECT 结果必须赋值给 PL/SQL 变量才能后续处理。
- **零行 → NO_DATA_FOUND；多行 → TOO_MANY_ROWS。**
- **处理多行查询**：使用**游标**（显式 DECLARE → OPEN → FETCH → CLOSE，或直接游标 FOR 循环）。

**2. PROCEDURE vs FUNCTION 对比：**
| 维度 | PROCEDURE 存储过程 | FUNCTION 函数 |
| ---- | ---- | ---- |
| RETURN 声明 | ❌ 没有 RETURN 子句 | ✅ 必须有 `RETURN 返回类型` |
| 返回方式 | 通过 OUT/IN OUT 参数传出 0~N 个 | RETURN 返回**一个**值（OUT 虽允许但反模式） |
| 在 SQL（SELECT 等）中调用 | ❌ 不能，只能 EXEC / PL/SQL 块调 | ✅ 纯函数可以，像内置函数一样用 |
| SQL 调用时 DML/COMMIT | 无此限制（本来就是调过程） | ❌ 严格禁止 DML/DDL/COMMIT/ROLLBACK，否则 ORA-14551 |
| 典型场景 | 执行业务流程、修改数据（批量更新、转账扣款） | 计算返回一个值（get_sal / calc_tax / get_total） |

**3. 触发器相关：**
- **(1) 行级 vs 语句级：**
  | 维度 | 行级（FOR EACH ROW） | 语句级（默认） |
  | ---- | ---- | ---- |
  | 触发次数 | 每影响 1 行触发 1 次（100 行 = 100 次） | 整条 DML 触发 1 次（无论多少行） |
  | :OLD/:NEW | ✅ 可用 | ❌ 不可用（无行上下文） |
  | 场景 | 行级校验、字段填充、行级审计 | 语句级汇总、表级整体校验 |
- **(2) :OLD/:NEW 值特点：**
  | 操作 | :OLD | :NEW |
  | ---- | ---- | ---- |
  | INSERT | 全 NULL（没有前值） | 保存待插入的新行（BEFORE 可改） |
  | UPDATE | 修改前值（只读） | 修改后值（BEFORE 可改） |
  | DELETE | 删除前值（只读） | 全 NULL（没有后值） |
- **(3) ORA-04091 变异表：**
  - **含义**：table XX is mutating, trigger/function may not see it。行级触发器中不能对**自己所在的触发表**执行 SELECT 或 DML（否则查询到的是"正在变化中"的表，结果不一致）。
  - **场景**：emp 的 BEFORE/AFTER 行级触发器中 SELECT COUNT(\*) FROM emp 就会报。
  - **解决方法**：① 11g+ **复合触发器（COMPOUND TRIGGER）**，在 BEFORE STATEMENT 收集行数据，AFTER STATEMENT 再统一 SELECT/DML；② 用**语句级触发器**（如果不需要行值）；③ 用**自治事务**（有副作用，查询到的是触发器开始前的数据，不推荐作业务逻辑）；④ 临时表 + 行级触发器写入 + 语句级读取。

**4. 异常处理：**
- **(1) 三类异常：**
  | 类别 | 例子 | 处理方式 |
  | ---- | ---- | ---- |
  | 预定义异常（~20+） | NO_DATA_FOUND、DUP_VAL_ON_INDEX、ZERO_DIVIDE | 无需声明，直接 WHEN XXX THEN |
  | 非预定义异常 | ORA-00060 死锁、ORA-02292 删除父行有子引用 | 声明 e EXCEPTION; + `PRAGMA EXCEPTION_INIT(e, -错误号);` 后 WHEN 捕获 |
  | 自定义异常 | 业务逻辑错误"工资不能为负""余额不足" | ① DECLARE e EXCEPTION; + RAISE e；② 更常用：直接 `RAISE_APPLICATION_ERROR(-20xxx, '消息')` |
- **(2) RAISE_APPLICATION_ERROR：**
  ```plsql
  RAISE_APPLICATION_ERROR(
      error_number  IN NUMBER,     -- 必须 -20999 ~ -20000 之间
      error_message IN VARCHAR2,   -- 错误消息（最长 2048 字节）
      keep_error_stack IN BOOLEAN DEFAULT FALSE  -- TRUE=把此错误追加到原堆栈，FALSE=替换原堆栈
  );
  ```
  客户端（JDBC 等）能拿到标准 SQLException，getErrorCode() 拿到 -20xxx，getMessage() 拿到自定义消息。
- **(3) 自治事务：**
  - **含义**：`PRAGMA AUTONOMOUS_TRANSACTION;` 声明本子程序是独立事务，与外层主事务完全隔离——它的 COMMIT/ROLLBACK 只影响自己的 DML，外层主事务的回滚不会把它撤销。
  - **写法**：声明区第一行写 `PRAGMA AUTONOMOUS_TRANSACTION;`，最后必须显式 COMMIT/ROLLBACK。
  - **99% 场景**：写**错误日志 / 审计日志**。因为主事务失败会回滚，如果日志在主事务里就一起被撤销，无法事后排查。用自治事务则无论主事务成功/失败，日志永远保留。

</details>

<details>
<summary>分析题参考答案</summary>

**1. 匿名块阅读：**
- **(1) 输出：**
  ```
  A: SMITH 新工资=880    ← 内层块SELECT成功，正常计算后打印A
  D: 外层捕获 员工不存在 v_empno=9999  ← 外层SELECT 9999无行抛NO_DATA_FOUND，被外层EXCEPTION匹配
  ```
  B 不打印（内层 empno=7369 存在，没进异常）；C 不打印（外层 SELECT 抛异常直接跳转 EXCEPTION）；E 不打印（外层 WHEN NO_DATA_FOUND 先匹配到了）。
- **(2) 内层块有自己的 EXCEPTION 并匹配到 NO_DATA_FOUND 时异常会被"消化"，不会再向外传播。内层块执行完后，流程继续到外层 BEGIN 中 v_empno := 9999; 这一行（紧接内层 END; 之后）。**
- **(3) 外层 SELECT empno=9999 不存在 → 触发 NO_DATA_FOUND。外层 EXCEPTION 第一个 WHEN 就是 NO_DATA_FOUND，所以被它捕获（而不是 WHEN OTHERS）。只有前面的 WHEN 都没匹配到，才会进入 OTHERS。**

---

**2. 触发器改错（至少 5 处）：**
- **错误 A（触发器级别错）：AFTER UPDATE ... `FOR EACH STATEMENT` → 题目是"修改每个员工工资时记录变化"，要用**行级 `FOR EACH ROW`**。语句级时影响多行会只触发一次，且 :NEW/:OLD 无法使用（语句级不能访问），WHEN (new.sal > ...) 也会因为没有行上下文报错。
- **错误 B（WHEN 子句语法错）：WHEN 条件里应该不带冒号写 `new.sal > old.sal * 1.5`，WHEN 括号里不能写 :NEW/:OLD（只有在触发器体 BEGIN...END 内才写冒号）。**
- **错误 C（①行）：SELECT COUNT(\*) FROM emp; 在**行级触发器**中查询自己的触发表 → 抛 ORA-04091 变异表错误。应删除无意义的 COUNT 查询或用复合触发器。**
- **错误 D（②行）：`COMMIT;` → 触发器中直接 COMMIT 抛 ORA-04092: cannot COMMIT in a trigger。必须：要么不要 COMMIT（COMMIT 由调用方事务统一提交）；要么写审计日志时加 `PRAGMA AUTONOMOUS_TRANSACTION;` 自治事务。**
- **错误 E（③行）：`IF INSERTING THEN ...` → 本触发器是 `AFTER UPDATE ON emp` 事件，**INSERTING 永远是 FALSE**（不可能触发 INSERT 事件）。应该用 `UPDATING` 或 `UPDATING('SAL')`。或者把触发器事件改成 `BEFORE INSERT OR UPDATE OF sal ON emp`。**
- **错误 F（逻辑错误）：题目还需"涨幅不能超 50%" → 原触发器 WHEN 条件只判断 new > 1.5×old，但没有阻止（INSERT 历史不影响主操作）。应该改为 BEFORE 行级触发器，在条件不满足时直接 `RAISE_APPLICATION_ERROR(-20002, '涨幅超过 50%')` 阻止修改（AFTER 触发器抛错虽然也会回滚，但 BEFORE 更及时）。**

**关键修改后代码：**
```plsql
CREATE OR REPLACE TRIGGER trg_sal_change
BEFORE UPDATE OF sal ON emp
FOR EACH ROW
WHEN (new.sal > old.sal * 1.5 OR new.sal < old.sal)   -- WHEN里不要写冒号
DECLARE
    PRAGMA AUTONOMOUS_TRANSACTION;
BEGIN
    -- ① 先校验（BEFORE中不通过就RAISE，直接阻止UPDATE）
    IF :NEW.sal > :OLD.sal * 1.5 THEN
        RAISE_APPLICATION_ERROR(-20002,
            '涨幅不能超过50%: '||:OLD.sal||'→'||:NEW.sal);
    END IF;

    -- ② 写审计日志（自治事务COMMIT）
    INSERT INTO sal_history VALUES(
        seq_sal_hist.NEXTVAL,
        :NEW.empno, :OLD.sal, :NEW.sal, SYSDATE);
    COMMIT;  -- 自治事务内合法

    -- ③ 谓词判断用UPDATING
    IF UPDATING('SAL') THEN
        DBMS_OUTPUT.PUT_LINE('sal列被UPDATE');
    END IF;
END;
/
```

---

**3. 游标分析：**
- **(1) 输出：**
  ```
  ISOPEN? Y
  TOP1: BLAKE 2850
  员工数(ROWCOUNT): 6
  员工数(v_cnt): 6
  工资总额: 9400
  平均工资: 1566.67
  CLOSE后 ISOPEN? N
  ```
  （工资排序：BLAKE 2850 → ALLEN 1600 → TURNER 1500 → WARD 1250 → MARTIN 1250 → JAMES 950，总和 = 2850+1600+1500+1250+1250+950 = 9400，平均 9400/6 ≈ 1566.67）
- **(2) c_dept%ROWCOUNT 统计的是"截至目前 FETCH 成功的累计行数"，循环中每次 FETCH 成功自动+1，与手动 v_cnt := v_cnt + 1 结果一致。%ROWCOUNT=1 时对应 FETCH 到的第 1 行，由于 ORDER BY sal DESC，第一行就是工资最高的 TOP1。**
- **(3) 游标 FOR 循环改写：**
  ```plsql
  DECLARE
      v_total_sal NUMBER(10) := 0;
      v_cnt NUMBER := 0;
  BEGIN
      -- FOR循环自动：声明记录变量r、OPEN、每次FETCH到r、EXIT WHEN NOTFOUND、CLOSE
      FOR r IN (SELECT empno, ename, sal FROM emp WHERE deptno = 30 ORDER BY sal DESC)
      LOOP
          v_cnt := v_cnt + 1;
          v_total_sal := v_total_sal + r.sal;
          IF v_cnt = 1 THEN   -- 注意FOR循环中没有%ROWCOUNT可直接用，改用v_cnt判断
              DBMS_OUTPUT.PUT_LINE('TOP1: ' || r.ename || ' ' || r.sal);
          END IF;
      END LOOP;

      DBMS_OUTPUT.PUT_LINE('员工数(v_cnt): ' || v_cnt);
      DBMS_OUTPUT.PUT_LINE('工资总额: ' || v_total_sal);
      DBMS_OUTPUT.PUT_LINE('平均工资: ' || ROUND(v_total_sal / NULLIF(v_cnt,0), 2));
  END;
  /
  ```
  注意：FOR 循环内记录变量 r 是 PL/SQL 隐式声明的，循环外不可见；无法直接访问游标%ROWCOUNT属性，用自己的计数器 v_cnt 替代即可。

---

**4. 异常传播链分析：**
- **(1) 完整输出：**
  ```
  === 主块开始 ===
  p1 start call p2
  p2 start call p3
  p3 start
  p2 catch ZERO_DIVIDE
  p1 catch OTHERS: ORA-01476: divisor is equal to zero
  === 主块正常结束 ===
  ```
- **(2) 传播链理由：**
  ① p3 内层块除零抛 ZERO_DIVIDE → 内层 EXCEPTION 只有 WHEN NO_DATA_FOUND，**不匹配** → 异常向外层传播到 p3 的 EXCEPTION；
  ② p3 的 EXCEPTION 只有 WHEN VALUE_ERROR → **不匹配** ZERO_DIVIDE，也没有 WHEN OTHERS → 异常继续向 p3 的调用者 **p2** 传播；
  ③ p2 的 EXCEPTION 有 WHEN ZERO_DIVIDE → **匹配成功**，打印"p2 catch ZERO_DIVIDE"，但 p2 写了 **RAISE** → 再次把同异常抛给 p2 的调用者 **p1**；
  ④ p1 的 EXCEPTION 有 WHEN OTHERS → **匹配**（捕获 ZERO_DIVIDE），打印"p1 catch OTHERS: ORA-01476..."，**没有再 RAISE** → 异常到此终止，流程正常继续 p1 结束 → 返回主块；
  ⑤ 主块 p1 调用正常返回，没有抛异常 → 打印"=== 主块正常结束 ==="，不走 EXCEPTION。
- **(3) 如果 p1 WHEN OTHERS 最后加 `RAISE;` → p1 会把异常再次抛出给主块 → 主块 EXCEPTION 的 WHEN OTHERS 捕获 → 输出改为：**
  ```
  === 主块开始 ===
  p1 start call p2
  p2 start call p3
  p3 start
  p2 catch ZERO_DIVIDE
  p1 catch OTHERS: ORA-01476: divisor is equal to zero
  === 主块兜底：ORA-01476: divisor is equal to zero ===
  ```
  同时，因为异常最终到达主块且未被处理就结束（或被 WHEN OTHERS 捕获但主事务本身没写 COMMIT），**所有未提交的 DML 事务会被回滚**。

</details>

<details>
<summary>综合题参考答案</summary>

### 综合题 1：pkg_salary 包

**(1) 包规范：**
```plsql
CREATE OR REPLACE PACKAGE pkg_salary
AUTHID DEFINER
IS
    C_MAX_RAISE_RATE CONSTANT NUMBER := 50;
    C_MIN_SAL       CONSTANT NUMBER := 500;

    e_sal_too_low   EXCEPTION;
    e_rate_too_high EXCEPTION;

    PROCEDURE raise_emp_sal(p_empno NUMBER, p_rate NUMBER);
    FUNCTION get_dept_total_sal(p_deptno NUMBER) RETURN NUMBER DETERMINISTIC;
    PROCEDURE print_dept_emp_report(p_deptno NUMBER);
END pkg_salary;
/
```

**(2) 包体：**
```plsql
CREATE OR REPLACE PACKAGE BODY pkg_salary
IS
    -- 私有辅助函数：查询员工sal（未找到抛异常）
    FUNCTION f_get_sal(p_empno NUMBER) RETURN NUMBER
    IS
        v_sal emp.sal%TYPE;
    BEGIN
        SELECT sal INTO v_sal FROM emp WHERE empno = p_empno;
        RETURN v_sal;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, '员工不存在：' || p_empno);
    END f_get_sal;

    -- ====== 公开过程实现 ======
    PROCEDURE raise_emp_sal(p_empno NUMBER, p_rate NUMBER)
    IS
        v_old_sal NUMBER(7,2);
        v_new_sal NUMBER(7,2);
    BEGIN
        SAVEPOINT sp_raise;
        v_old_sal := f_get_sal(p_empno);   -- 不存在就抛-20001

        IF p_rate > C_MAX_RAISE_RATE THEN
            RAISE e_rate_too_high;
        END IF;

        v_new_sal := v_old_sal * (1 + p_rate / 100);
        IF v_new_sal < C_MIN_SAL THEN
            RAISE e_sal_too_low;
        END IF;

        UPDATE emp SET sal = v_new_sal WHERE empno = p_empno;
        COMMIT;
        DBMS_OUTPUT.PUT_LINE('员工'||p_empno||'涨薪成功：'||v_old_sal||' → '||v_new_sal);
    EXCEPTION
        WHEN e_rate_too_high THEN
            ROLLBACK TO sp_raise;
            RAISE_APPLICATION_ERROR(-20002,
                '涨薪比例'||p_rate||'%超过上限'||C_MAX_RAISE_RATE||'%');
        WHEN e_sal_too_low THEN
            ROLLBACK TO sp_raise;
            RAISE_APPLICATION_ERROR(-20003,
                '涨薪后工资'||v_new_sal||'低于最低工资底线'||C_MIN_SAL);
        WHEN OTHERS THEN
            ROLLBACK;
            RAISE;
    END raise_emp_sal;

    FUNCTION get_dept_total_sal(p_deptno NUMBER) RETURN NUMBER
    DETERMINISTIC
    IS
        v_total NUMBER(12,2);
    BEGIN
        SELECT NVL(SUM(sal),0) INTO v_total FROM emp WHERE deptno = p_deptno;
        RETURN v_total;
    EXCEPTION
        WHEN OTHERS THEN RETURN 0;
    END get_dept_total_sal;

    PROCEDURE print_dept_emp_report(p_deptno NUMBER)
    IS
        v_cnt   NUMBER := 0;
        v_total NUMBER(12,2) := 0;
        v_dname dept.dname%TYPE;
    BEGIN
        SELECT dname INTO v_dname FROM dept WHERE deptno = p_deptno;
        DBMS_OUTPUT.PUT_LINE(RPAD('=',40,'='));
        DBMS_OUTPUT.PUT_LINE('部门报告：' || p_deptno || ' - ' || v_dname);
        DBMS_OUTPUT.PUT_LINE(RPAD('=',40,'='));

        FOR r IN (SELECT ename, job, sal FROM emp WHERE deptno = p_deptno ORDER BY sal DESC)
        LOOP
            DBMS_OUTPUT.PUT_LINE(RPAD(r.ename,10) || RPAD(r.job,10) || TO_CHAR(r.sal,'99999.99'));
            v_cnt   := v_cnt + 1;
            v_total := v_total + r.sal;
        END LOOP;

        DBMS_OUTPUT.PUT_LINE(RPAD('-',40,'-'));
        DBMS_OUTPUT.PUT_LINE('总人数：'   || v_cnt);
        DBMS_OUTPUT.PUT_LINE('总工资：'   || v_total);
        DBMS_OUTPUT.PUT_LINE('平均工资：' || ROUND(v_total / NULLIF(v_cnt,0), 2));
        DBMS_OUTPUT.PUT_LINE(RPAD('=',40,'='));
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('部门不存在：' || p_deptno);
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('生成报告失败：' || SQLERRM);
            RAISE;
    END print_dept_emp_report;
END pkg_salary;
/
SHOW ERRORS;
```

**(3) 调用示例：**
```plsql
SET SERVEROUTPUT ON SIZE UNLIMITED;

-- 示例① 正常涨薪
BEGIN
    pkg_salary.raise_emp_sal(7369, 10);
END;
/

-- 示例② 异常场景：涨60%超上限
BEGIN
    pkg_salary.raise_emp_sal(7369, 60);
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('捕获异常：' || SQLCODE || ' - ' || SQLERRM);
END;
/

-- 示例③ 打印20号部门报告
BEGIN
    pkg_salary.print_dept_emp_report(20);
END;
/
```

---

### 综合题 2：订单库存

**建表 + 序列 SQL：**
```sql
-- 建表（如果不存在）
CREATE TABLE t_stock (
    goods_id   NUMBER PRIMARY KEY,
    goods_name VARCHAR2(50) NOT NULL,
    stock_qty  NUMBER NOT NULL CHECK (stock_qty >= 0),
    unit_price NUMBER(10,2) NOT NULL
);
CREATE TABLE t_order (
    order_id   NUMBER PRIMARY KEY,
    user_id    NUMBER NOT NULL,
    amount     NUMBER(12,2) NOT NULL,
    status     VARCHAR2(20) DEFAULT 'CREATED',
    create_time DATE DEFAULT SYSDATE
);
CREATE TABLE t_order_item (
    item_id    NUMBER PRIMARY KEY,
    order_id   NUMBER NOT NULL REFERENCES t_order(order_id),
    goods_id   NUMBER NOT NULL REFERENCES t_stock(goods_id),
    buy_qty    NUMBER NOT NULL CHECK (buy_qty > 0),
    subtotal   NUMBER(12,2) NOT NULL
);
CREATE TABLE t_audit_log (
    log_id   NUMBER PRIMARY KEY,
    op_type  VARCHAR2(20),
    op_desc  VARCHAR2(500),
    op_user  VARCHAR2(30),
    op_time  DATE DEFAULT SYSDATE
);
CREATE SEQUENCE seq_order START WITH 1000;
CREATE SEQUENCE seq_item  START WITH 2000;
CREATE SEQUENCE seq_log   START WITH 3000;
```

**存储过程 p_create_order：**
```plsql
CREATE OR REPLACE PROCEDURE p_create_order(
    p_user_id   IN  NUMBER,
    p_goods_id  IN  NUMBER,
    p_qty       IN  NUMBER,
    p_order_id  OUT NUMBER
)
AUTHID DEFINER
IS
    v_stock   NUMBER;
    v_price   NUMBER(10,2);
    v_subtotal NUMBER(12,2);
    v_order_id NUMBER;
BEGIN
    -- 参数校验
    IF p_qty <= 0 THEN
        RAISE_APPLICATION_ERROR(-20101, '购买数量必须为正：' || p_qty);
    END IF;

    SAVEPOINT sp_order;

    -- 查询库存与价格（FOR UPDATE锁行，防止并发超卖）
    SELECT stock_qty, unit_price INTO v_stock, v_price
      FROM t_stock WHERE goods_id = p_goods_id
      FOR UPDATE NOWAIT;   -- NOWAIT=如果被锁立即报错，可选WAIT 3

    IF v_stock < p_qty THEN
        RAISE_APPLICATION_ERROR(-20102,
            '库存不足：现有='||v_stock||'，需要='||p_qty);
    END IF;

    -- 计算小计
    v_subtotal := p_qty * v_price;

    -- 扣减库存（BEFORE UPDATE OF stock_qty 触发器会二次校验不能为负）
    UPDATE t_stock SET stock_qty = stock_qty - p_qty WHERE goods_id = p_goods_id;

    -- 生成订单号
    v_order_id := seq_order.NEXTVAL;

    -- 插入订单主表
    INSERT INTO t_order(order_id, user_id, amount, status)
         VALUES (v_order_id, p_user_id, v_subtotal, 'CREATED');

    -- 插入订单明细
    INSERT INTO t_order_item(item_id, order_id, goods_id, buy_qty, subtotal)
         VALUES (seq_item.NEXTVAL, v_order_id, p_goods_id, p_qty, v_subtotal);

    p_order_id := v_order_id;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('下单成功：订单号='||v_order_id||'，金额='||v_subtotal);
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK TO sp_order;
        ROLLBACK;
        RAISE;   -- 原样抛出错误给调用方
END p_create_order;
/
SHOW ERRORS;
```

**触发器 1 —— 库存负数校验（行级，BEFORE UPDATE OF stock_qty）：**
```plsql
CREATE OR REPLACE TRIGGER trg_stock_check
BEFORE UPDATE OF stock_qty ON t_stock
FOR EACH ROW
BEGIN
    IF :NEW.stock_qty < 0 THEN
        RAISE_APPLICATION_ERROR(-20103,
            '库存不能为负：goods_id='||:OLD.goods_id||
            '（'||:OLD.goods_name||'），扣减后='||:NEW.stock_qty);
    END IF;
END;
/
```

**触发器 2 —— 订单审计（自治事务写日志）：**
```plsql
CREATE OR REPLACE TRIGGER trg_order_audit
AFTER INSERT OR UPDATE OF status ON t_order
FOR EACH ROW
DECLARE
    PRAGMA AUTONOMOUS_TRANSACTION;   -- 自治事务，日志独立COMMIT
    v_desc VARCHAR2(500);
    v_type VARCHAR2(20);
BEGIN
    IF INSERTING THEN
        v_type := 'CREATE_ORDER';
        v_desc := '创建订单'||:NEW.order_id||' 用户='||:NEW.user_id||' 金额='||:NEW.amount||' 状态='||:NEW.status;
    ELSIF UPDATING('STATUS') THEN
        v_type := 'UPDATE_STATUS';
        v_desc := '订单'||:OLD.order_id||' 状态变更：'||:OLD.status||' → '||:NEW.status;
    END IF;

    INSERT INTO t_audit_log(log_id, op_type, op_desc, op_user)
         VALUES (seq_log.NEXTVAL, v_type, v_desc, USER);
    COMMIT;   -- 自治事务必须显式COMMIT
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;   -- 日志失败不影响主业务
END;
/
```

**测试匿名块：**
```plsql
SET SERVEROUTPUT ON SIZE UNLIMITED;
DECLARE
    v_order_id NUMBER;
BEGIN
    -- 第一步：清空旧测试数据 + 初始化库存
    DELETE FROM t_order_item;
    DELETE FROM t_order;
    DELETE FROM t_stock;
    DELETE FROM t_audit_log;
    INSERT INTO t_stock(goods_id, goods_name, stock_qty, unit_price)
         VALUES (1, 'iPhone 15 Pro', 10, 5999);
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('=== 初始化完成，iPhone库存10台 ===');

    -- 第二步：正常购买 2 台（库存够）
    DBMS_OUTPUT.PUT_LINE('--- 测试①：用户1001买2台iPhone ---');
    BEGIN
        p_create_order(1001, 1, 2, v_order_id);
        DBMS_OUTPUT.PUT_LINE('返回订单号：' || v_order_id);
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('下单失败：' || SQLERRM);
    END;

    -- 第三步：再购买 9 台（现有库存 10-2=8，8<9 → 库存不足）
    DBMS_OUTPUT.PUT_LINE('--- 测试②：用户1001再买9台 ---');
    BEGIN
        p_create_order(1001, 1, 9, v_order_id);
        DBMS_OUTPUT.PUT_LINE('返回订单号：' || v_order_id);
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('预期捕获异常：' || SQLCODE || ' - ' || SQLERRM);
    END;

    -- 第四步：模拟更新订单状态（触发第二次审计日志）
    DBMS_OUTPUT.PUT_LINE('--- 测试③：更新订单状态为PAID ---');
    UPDATE t_order SET status = 'PAID' WHERE order_id = (SELECT MIN(order_id) FROM t_order);
    COMMIT;

    DBMS_OUTPUT.PUT_LINE(CHR(10) || '=== 查询验证结果 ===');
    DBMS_OUTPUT.PUT_LINE(RPAD('-',70,'-'));
END;
/

-- 查询验证：
SELECT * FROM t_stock;
SELECT * FROM t_order;
SELECT * FROM t_order_item;
SELECT * FROM t_audit_log ORDER BY log_id;
```

**预期结果：**
- t_stock：iPhone 库存 = 8（扣了 2 台，第二单失败没扣）
- t_order：1 条，订单号 1000，用户 1001，金额 11998（2×5999），状态 PAID
- t_order_item：1 条关联
- t_audit_log：至少 2 条 —— CREATE_ORDER（创建订单） + UPDATE_STATUS（PAID）；注意：第二单失败时 INSERT 到 t_order 被回滚，但 trg_order_audit 是**自治事务**，如果第二单 INSERT t_order 后抛异常之前触发器已执行 INSERT 日志，那么日志会保留（Oracle 行级触发器 AFTER INSERT 在语句完成后才触发；但我们的库存不足异常发生在 INSERT t_order 之前，所以不会触发 CREATE_ORDER 日志，这点要理解清楚——如果要把"下单失败"也写日志，应在 p_create_order 的 WHEN OTHERS 中用自治事务单独写）。

</details>

---

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | PL/SQL块结构、%TYPE/%ROWTYPE、SELECT INTO异常、参数模式、AUTHID权限、函数纯度、触发器:OLD/:NEW、游标四步、三类异常、RAISE_APPLICATION_ERROR号段 |
| 多选 | 5 | 15 | PL/SQL复合类型、过程vs函数对比、触发器分类、游标使用细节、异常最佳实践 |
| 判断 | 5 | 10 | 块结构可选项、OUT/IN OUT初始值、BEFORE修改:NEW、游标FOR循环、WHEN OTHERS THEN NULL陷阱 |
| 简答 | 4 | 20 | 块+类型+SELECT INTO；过程vs函数5维度对比；触发器行级/语句级+OLD/NEW+变异表；三类异常+RAISE_APPLICATION_ERROR+自治事务 |
| 分析 | 4 | 32 | 匿名块嵌套异常传播+输出、触发器代码改错5处+修复、游标属性与FOR循环改写、过程调用链异常传播逐层分析 |
| 综合 | 2 | 20 | pkg_salary 包：规范+体+过程+函数+游标报告+异常；订单库存场景：建表+存储过程+库存校验触发器+自治事务审计日志触发器+测试脚本 |
| 合计 | 30 | 117 | 覆盖第9章全部核心考点，重在 PL/SQL 代码实际编写与陷阱排查 |

---

## 章节导航

- 上级 MOC：[[MOC - Oracle数据库管理]]
- 本章知识点 MOC：[[MOC - 第9章]]（[[9.1 PL-SQL块结构|9.1 PL/SQL块结构]]、[[9.2 存储过程、函数]]、[[9.3 触发器、游标]]、[[9.4 异常处理机制]]）
- 上一章习题：[[MOC - 第8章习题]]
- 下一章习题：[[MOC - 第10章习题]]
