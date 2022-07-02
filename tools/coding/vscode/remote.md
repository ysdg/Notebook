# 远程连接服务器docker

本文目的在于远程服务器中的容器。vscode中，自带Remote-Container插件，实现连接容器功能。但在实践和资料中发现，此插件仅可连接本机的容器，不可连接远程服务器容器。基于连接远程服务器docker的需求，目前寻找到此解决方案。今后（2022-07-02），如果Remote-Container完善远程容器功能，此方案并非最佳方案。

本文参考[《VSCode连接远程服务器里的docker容器》(doubleZ)](https://zhuanlan.zhihu.com/p/361934730), 实现vscode远程服务器中的容器。基本是对原文章的摘抄，主要修改点：

1. 使用ubuntu举例；
2. 使用ssh连接，而非用户名密码；

## 概述

本方案基于如下思想：

1. 容器允许远程；
2. 将容器作为服务器，进行ssh远程；

## 方案

本方案基于参考文献方案，梳理逻辑及使用调整。因此，仅仅作为简要步骤，需要一定linux及docker基础，并非零基础的手把手教程。如有需要，请仔细阅读参考文献。

下面简要描述方法步骤：

1. 创建容器。此处基于ubuntu镜像，建立一个代码调试环境。使用[docker-compose](https://docs.docker.com/compose/gettingstarted/)进行搭建，配置文件docker-compose.yml如下所示：

   ```yml
   version: "3"

   services:
     leetcode:
       image: ubuntu:latest
       ports:
         - "6789:22"
       tty: true
       # make (ubuntu based)container don't exit, other image may don't need.
       command: /bin/bash -c "service ssh restart && /bin/bash"
   ```

   上述docker-compose基于最新的ubuntu镜像，启动容器，并将容器的22端口映射至宿主机的6789端口，为ssh远程备用。且使用命令，自启动ssh服务（需在容器安装ssh服务，见步骤2）
2. 容器内下载并安装ssh，详见参考文献[1]；
3. 制作密钥，并在docker中安装公钥，详见[设置SSH密钥登录](https://www.runoob.com/w3cnote/set-ssh-login-key.html)；
4. 使用 `docker-compose up -d`命令，重启启动并隐藏容器；
5. 使用本地vscode的Remote-SSH插件，免密登录容器，详见参考文献[1]；

## 参考文献

[[1] VSCode连接远程服务器里的docker容器](https://zhuanlan.zhihu.com/p/361934730 "VSCode连接远程服务器里的docker容器")
