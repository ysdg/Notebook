# 内存

#### [top 命令中的VIRT，RES，SHR　，MEM区别](https://www.cnblogs.com/hustcpp/p/11097646.html)

| 分类 | 全称                                                          | 说明                                                                                                                                                                                                                                |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VIRT | virtual memory space                                          | 表示进程的虚拟(地址)空间大小，其包含进程实际使用的大小(申请的堆栈)， 使用mmap映射的大小，包括外设RAM， 还有映射到本进程的文件（例如动态库)，还有进程间的共享内存。所以VIRT 表示的是当前这个进程能够访问到的所有空间大小             |
| RES  | resident set size                                             | 表示进程的常驻内存大小，准确表示当前有多少物理内存被这个进程消费，这个和MEM是对应的， 这个大小永远要比VIRT小，因为程序大部分使用到c库                                                                                               |
| SHR  | amount of resident memory that is shared with other processes | 表示多少VIRT 实际可以共享的（包括内存和动态库），举例动态库，SHR的值不总代表整个库都是常驻内存的，因为有些程序使用到c库的部分函数，但整个库是被映射到进程的，并且计算到VIRT和SHR，但是只有该库的一部分被使用到，即被装载并记入到RES |


# crash

在ubuntu server 20.04LTS版本，基于apport服务，生成crash（类似core）文件。

1. 确保/etc/sysctl.conf中，无配置。

   验证：

   ```
   #执行
   sysctl kernel.core_pattern
   #显示: |usr/share/apport/apport -p%p -s%s -c%c -d%d -P%P -u%u -g%g -- %E

   ```
2. 确保/etc/sercurity/limits.conf文件，添加配置：

   ```
   * hard core unlimited
   * soft core unlimited
   root hard core unlimited
   root soft core unlimited

   ```

   验证：重启机器，执行 `ulimit -c`，显示unlimited
3. 在~/.config/apport/settings中（不存在则创建），写入：

   ```
   [main]
   unpackaged=true
   ```

   重启apport（执行 `systemctl stop apport, systemctl start apport`）
4. 测试验证，对程序${PID}，执行：

   ```
   kill -s SIGSEGV ${PID}
   ```

   在/var/crash/目录下，存在XXX .crash文件。需使用crash查看

## 参考文件

[1] [Finding Your Core Dumps](https://www.logikalsolutions.com/wordpress/information-technology/core-dumps/)

[2] [在 Linux 生成 core dump 文件](http://senlinzhan.github.io/2017/12/31/coredump/)

[3] [apport unpackage](https://stackoverflow.com/questions/14204961/how-to-change-apport-default-behaviour-for-non-packaged-application-crashes)
