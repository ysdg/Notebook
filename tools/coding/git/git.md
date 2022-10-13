| 命令         | 参数                                   | 用途                           |
| ------------ | -------------------------------------- | ------------------------------ |
| git merge    | -i HEAD~3                              | 合并提交                       |
| git rebase   | -i HEAD~3                              | 重置提交                       |
| git pull     | --allow-unrelated-histories            | 拉取代码，带参数即允许放弃本地 |
| git checkout | -b `<name>` `<remoteName>/<name`> | 拉取远端分支                   |

# 子模块

参考[《Git中submodule的使用》](https://zhuanlan.zhihu.com/p/87053283)

## 添加子模块

```bash
git submodule add {url} {dir_name}
```

## 更新子模块

方式一： 主模块执行

```bash
# 主模块执行
git submodule init
git submodule update
```

方式二：主模块克隆带--recurse-submodules

方式三：子模块中，执行pull或clone

### 更新.gitmodules

1. 编辑.gitmodules，如url；
2. 执行：`git submodule sync --recursive`

## 删除子模块

```bash
git submodule deinit {sub-project}
git rm {sub-project}
```

## 拆分子模块

在已有代码库中，按文件夹拆分子仓库，参考[《Git - 现有项目拆分子模块》](https://juejin.cn/post/6915229332147453966)

执行如下BAT脚本（需替换变量）：

```bat
@REM MAIN_PROJ_PATH: 需要被拆分的主工程路径
@REM SUB_PROJ_RELATIVE_PATH: 需要拆分出来的子工程相对于主工程的路径
@REM SUB_PROJ_NAME: 子工程项目名
@REM GIT_REMOTE_URL: 子工程指向的仓库地址

set MAIN_PROJ_PATH=./i-SYS7.1
set SUB_PROJ_RELATIVE_PATH=iCore/
set SUB_PROJ_NAME=i-SYS-icore-depends
set GIT_REMOTE_URL=http://yuanquan@gerrit.supos.ai:80/a/i-SYS-icore-depends

cd %MAIN_PROJ_PATH%
git subtree split -P %SUB_PROJ_RELATIVE_PATH% -b %SUB_PROJ_NAME%

cd ..
git clone -b %SUB_PROJ_NAME% %MAIN_PROJ_PATH% %SUB_PROJ_NAME%

cd %SUB_PROJ_NAME%
git branch -m master
git remote remove origin
git remote add origin %GIT_REMOTE_URL%
git push -f origin HEAD:refs/heads/master

cd %MAIN_PROJ_PATH%
pause
@REM git branch -D %SUB_PROJ_NAME%

```
