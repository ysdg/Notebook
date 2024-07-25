# jemalloc

## 编译

正常编译：[jemalloc/INSTALL.md at dev · jemalloc/jemalloc (github.com)](https://github.com/jemalloc/jemalloc/blob/dev/INSTALL.md)

允许debug和分析：

```bash
./configure --enable-debug --enable-prof
make -j16
```

## 使用

使用方式：[Getting Started · jemalloc/jemalloc Wiki (github.com)](https://github.com/jemalloc/jemalloc/wiki/Getting-Started)

```bash
# 设置libjemalloc路径，可直接启动程序
export LD_PRELOAD=/lib/<libjemalloc.so>


```

## 内存分析

内存分析：[Use Case: Leak Checking · jemalloc/jemalloc Wiki (github.com)](https://github.com/jemalloc/jemalloc/wiki/Use-Case%3A-Leak-Checking)

网友分析：[jemalloc内存泄漏分析 - 简书 (jianshu.com)](https://www.jianshu.com/p/4f9689ffca2d)

```base

#设置运行调试。lg_prof_interval:20中的20表示1MB(2^20)，prof:true是打开profiling
export MALLOC_CONF=prof_leak:true,lg_prof_sample:0,prof_final:true,prof:true,lg_prof_interval:30,prof_prefix:jeprof.out
#设置libjemalloc，w表示写入dump
export LD_PRELOAD=/lib/<libjemalloc.so> w

#生成jeprof.out.${pid}.heap dump文件后，使用jeprof分析内存
#查看内存分配
jeprof --show_bytes `which w` jeprof.${pid}.${index}.heap
#生成pdf的调用文件
jeprof --show_bytes --pdf `which w` jeprof.out.${pid}.${index}.heap > ${pid}.pdf
#比较两个内存分配，可使用top查看分配大小
jeprof ${program_name}--base=jeprof.out.${pid}.${index}.heap jeprof.out.${pid}.${index}.heap


```
