# jemalloc

## ����

�������룺[jemalloc/INSTALL.md at dev �� jemalloc/jemalloc (github.com)](https://github.com/jemalloc/jemalloc/blob/dev/INSTALL.md)

����debug�ͷ�����

```bash
./configure --enable-debug --enable-prof
make -j16
```

## ʹ��

ʹ�÷�ʽ��[Getting Started �� jemalloc/jemalloc Wiki (github.com)](https://github.com/jemalloc/jemalloc/wiki/Getting-Started)

```bash
# ����libjemalloc·������ֱ����������
export LD_PRELOAD=/lib/<libjemalloc.so>


```

## �ڴ����

�ڴ������[Use Case: Leak Checking �� jemalloc/jemalloc Wiki (github.com)](https://github.com/jemalloc/jemalloc/wiki/Use-Case%3A-Leak-Checking)

���ѷ�����[jemalloc�ڴ�й©���� - ���� (jianshu.com)](https://www.jianshu.com/p/4f9689ffca2d)

```base

#�������е��ԡ�lg_prof_interval:20�е�20��ʾ1MB(2^20)��prof:true�Ǵ�profiling
export MALLOC_CONF=prof_leak:true,lg_prof_sample:0,prof_final:true,prof:true,lg_prof_interval:30,prof_prefix:jeprof.out
#����libjemalloc��w��ʾд��dump
export LD_PRELOAD=/lib/<libjemalloc.so> w

#����jeprof.out.${pid}.heap dump�ļ���ʹ��jeprof�����ڴ�
#�鿴�ڴ����
jeprof --show_bytes `which w` jeprof.${pid}.${index}.heap
#����pdf�ĵ����ļ�
jeprof --show_bytes --pdf `which w` jeprof.out.${pid}.${index}.heap > ${pid}.pdf
#�Ƚ������ڴ���䣬��ʹ��top�鿴�����С
jeprof ${program_name}--base=jeprof.out.${pid}.${index}.heap jeprof.out.${pid}.${index}.heap


```
