# WinDBG简介

## 概述

WinDBG是windows下的强大调试器，功能丰富，支持各种调试任务：

- 用户态调试
- 内核态调试
- 调试转储文件（DUMP）文件
- 远程调试

本文档基于《WinDBG用法详解》，记录学习使用WinDBG的过程，并作为命令查询的参考。

## WinDBG介绍

### 工作空间

WinDBG使用工作空间（Workspace)来描述和存储一个调试项目的属性、参数及调试器设置等信息，类似于集成开发环境的项目文件，工作空间信息存储于注册表。

### 命令概览

WinDBG基于命令工作，分为如下3大类

- 标准命令
- 元命令
- 拓展命令

#### 标准命令

标准命令通常为一两个字符，提供适用于各种调试目标的基本调试功能，不区分大小写。问号（?）显示标准命令的列表和简单介绍，如下表所示：

| 命令             | 含义                                                         |
| ---------------- | ------------------------------------------------------------ |
| 控制调试目标执行 | g: 恢复运行  <br/>t: 跟踪<br/>p: step over                   |
| r                | 观察和修改寄存器                                             |
| 内存数据         | d：观察<br/>e：编辑<br/>s：搜索                              |
| k                | 观察栈                                                       |
| 设置和维护断点   | BP：软件断点<br/>BA：硬件断点<br/>BL：列出所有断点<br/>BC：清除断点<br/>BD：禁止断点<br/>BE：重新启动断点 |
| ~                | 显示和控制线程                                               |
| \|               | 显示进程                                                     |
| ?                | 显示表达式<br>??：显示C++表达式                              |
| a                | 汇编<br>u：反汇编                                            |
| dg               | 显示段选择子                                                 |
| $                | 执行命令文件                                                 |
| sx               | 设置调试事件处理方式                                         |
| version          | 显示调试器和调试目标版本                                     |
| 符号             | x：检查<br>ln：搜索<br>lm：显示模块列表                      |
| q                | 结束调试会话                                                 |

#### 元命令

提供标准命令没有提供的调试功能，所有元命令都以点（.）开始，输入.help可列出所有元命令和简单说明。

| 命令分类                     | 命令说明                                                     |
| ---------------------------- | ------------------------------------------------------------ |
| 显示或设置调试会话、调试选项 | 符号选项：.symopt<br>符号路径：.sympath, .symfix<br>源程序文件：.srcpath, .srcnoise, .srcfix<br>拓展命令模块路径：.extpath<br>匹配拓展命令：.extmatch<br>可执行文件：.exepath<br>设置反汇编选项：.asm<br>控制表达式评估器：.expr |
| 控制调试会话或调试目标       | 重新开始调试会话：.restart<br>放弃用户态调试目标（进程）：.abandon<br>创建新进程：.create<br>附加到存在进程：.attach<br>打开转储文件：.opendump<br>分离调试目标：.detach<br>杀掉进程：.kill |
| 管理拓展命令模块             | 加载模块：.load<br>卸载模块：.unload, unloadall<br>显示已加载模块：.chain |
| 管理调试器日志文件           | 显示信息：.logfile<br>打开：.logopen<br>追加：.logappend<br>关闭：.logclose |
| 远程调试                     | 启动remote.exe服务：.remote<br>启动引擎服务器：.server<br>列出可用服务器：.servers<br>向远程服务器发送文件：.send_file<br>结束远程进程服务器：.endpsrv<br>结束引擎服务器：.endsrv |
| 控制调试器                   | 睡眠：.sleep<br>唤醒：.wake<br>启动另一个调试器来调试当前调试器：.dbgdbg |
| 编写命令程序                 | C语言关键字，如.if, .else, .elsif, .foreach等，详情见**命令程序** |
| 显示或者转储目标数据         | 产生转储文件：.dump<br>将原始内存数据写到文件：.writemem<br>显示调试会话时间：.time<br>显示线程时间：.ttime<br>显示任务列表：.tlist<br>以不同格式显示数据：.formats |

#### 拓展命令

拓展命令用于拓展调试功能，非内建于WinDBG中，而是在动态加载的拓展模块中。拓展命令以叹号（!）开始，完整格式是：

<center>![拓展模块名].<拓展命令名> [参数]</center>



## 总结

### 分析DUMP简述

前提：正确加载符号路径和代码文件路径

1. 分析dump：!analyze -v
2. 显示异常相关上下文记录：.excr
3. 查看崩溃的堆栈：kbn

经过上述步骤分析，已可以查看到崩溃的代码，需结合代码进一步分析崩溃原因

## 参考资料

[1] WinDBG用法详解.pdf
