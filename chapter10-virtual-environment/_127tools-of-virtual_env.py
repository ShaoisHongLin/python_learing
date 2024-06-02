# 上一节我们专门新建目录，并且进入特定的文件夹下如果用命令行需要active才可以激活虚拟环境

# 上节课我们要记住的操作有：#pip install virtualenv。 virtualenv  jd_env等,而且需要《进入特定目录下》才用activate脚本激活,deactivate

# 这节课我们介绍一个python中用于统一管理虚拟环境的一个工具.
'''
virtualenvwrapper

"虚拟环境打包者"工具

（一）介绍:
1.它可以统一安排我们创建过的虚拟环境在特定的统一目录下管理它们
2.不必在命令行中进入自己创建的(如:jd_env)的Script目录下,通过active脚本文件激活虚拟环境。
Linux安装:pip install virtualenvwrapper
Windows安装:pip install virtualenvwrapper-win


（二）具体下载:
<1.>pip install virtualenvwrapper-win
<2.>WORKON_HOME   这个环境变量是为virtualenvwrapper而设立的统一管理虚拟环境的文件夹。

变量名WORKON_HOME
路径:自己选一个文件夹比如:G:\python_env

设置path新条目: %WORKON_HOME%


（三）使用操作:(仍旧是在命令行中编程适用,但是好处在于"每次创建新环境和运行环境"都要不必再进入特定目录了,全局都可以通过环境变量创建。
    
    配置好之后的效果，具体使用：

1.  mkvirtualenv flask_env   就可以在任意目录打开命令行,新建出一个新的虚拟环境比如"flask_env"的虚拟环境,它会出现在你设置的WORKON_HOME的路径下
2.  workon flask_env    激活该flask_env 虚拟环境。
3.  deactivate        退出该虚拟环境。
4.  rmvirtualenv flask_env   可以在不想要时候删除该环境。




# (四).虽然有了virtualenv wrapper但是我们仍然是利用它方便创建虚拟环境,而一旦有了虚拟环境的基础上,仍旧在vscode编写python代码:


# settings------搜索-------python virtual venv

# 找到python venv path:的添加path处,在这里你可以添加本机的虚拟环境总文件夹,最终会以列表形式被vscode识别出来。

# 复制你本机的python_env(总的env文件夹放在里面)
# 之后就可以通过点击屏幕最下面小边框的左侧或右侧的Python 3.12.3 64-bit这种,点击3.12.3处即可发现上方弹出虚拟环境列表。
# 点击之后即可快速切换到虚拟环境。
# 如果没有弹出虚拟环境列表.需要重启vscode
'''