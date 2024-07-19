# 想使用第三方库,我们就需要用pip来下载各种第三方库，pip的全称是Pip Installs Packages。pip包管理工具。

# 如果我们用过linux的相关包管理工具yum（CentOS）或者apt(Ubuntu)

# 就会很容易理解它做的是什么工作。就是把某个库(软件)的安装包,下载到本地统一的地方，

'''
很简单,我们想下载一个软件的安装包:
"pip+安装包名"就可以将其下载到本地了.



下载软件的"源":下载的软件最终是一样的，不过为了提高下载过程的速度,我们往往挂梯子加速器下载或者通过修改下载源头为本地的镜像网站来下载.
如果

你的python是linux上办公使用,需要去~/pip/pip.conf里面增加新配置内容

你的python是windows上办公使用,需要去 C:/user/你的用户/新建pip文件夹/pip.ini文件,在里面增加新配置内容


[global] 
index-url = http://mirrors.aliyun.com/pypi/simple/ 
[install] 
trusted-host=mirrors.aliyun.com 



可以简单地在命令行尝试pip的使用:

pip list

和尝试下载python版的mysql

pip install pymysql
    C:\Users\M>pip install pymysql
    Looking in indexes: http://mirrors.aliyun.com/pypi/simple/
    Collecting pymysql
    Downloading http://mirrors.aliyun.com/pypi/packages/0c/94/e4181a1f6286f545507528c78016e00065ea913276888db2262507693ce5/PyMySQL-1.1.1-py3-none-any.whl (44 kB)
        ---------------------------------------- 45.0/45.0 kB 445.3 kB/s eta 0:00:00
    Installing collected packages: pymysql
    Successfully installed pymysql-1.1.1

    [notice] A new release of pip is available: 24.0 -> 24.1.2
    [notice] To update, run: G:\Python\python.exe -m pip install --upgrade pip
'''