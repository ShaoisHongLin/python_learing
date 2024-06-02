'''
虚拟环境使用情景:

    工作中,我们手头有三个python的代码或者说python项目,它们或老或新,使用着不同的python解释器版本,需要使用不同的python解释器来维护代码。

作用简述:
    利用python的虚拟环境,可以创建出各个解释器版本之间隔离的不同虚拟环境,这就是创建不同虚拟环境的作用
'''

# 使用到的基础工具:pip install virtualenv

# 命令行中以下操作
#1 pip下载virtual env环境它会自动在python的lib目录下产生site=packages 20.26.2   0.3.8  3.14.0  4.2.2型号
#2 pip install virtualenv


'''
    如何利用virtualenv,windows上新建文件夹,并通过命令行,在里面创建出python的虚拟环境:

# 2.创建虚拟环境:新建windows文件目录,作为总的虚拟环境的文件夹

#如G:\python_env


# 在该命令行路径下 virtualenv jd_env  新建一个专门的虚拟环境,如起名为“jd_env”用于维护一个叫做jd的项目的虚拟环境

#virtualenv  jd_env
'''


'''
# (选择1):命令行加载启动运行虚拟环境,适用于在命令行中编写python代码
# 在里面的Script下可以运行active进入该命令行的python虚拟环境

# 也可以在Script的目录下pip list查看现有的虚拟环境包
#  如:    pip list
# 在这里你可以pip install 新的pip的包
#  如:   pip install mysql

#  (重要命令1)切换到命令行的python解释器所处的虚拟环境的语句:
    cd Script
    activate 

#  (重要命令2)退出命令行当前所处的虚拟环境的语句:
    cd Script
    deactivate 
'''


'''
# (选择2).利用vscode来加载你本机上的虚拟环境,适用于有了虚拟环境的基础上,在vscode编写python代码
# settings------搜索-------python virtual venv

# 找到python venv path:的添加path处,在这里你可以添加本机的虚拟环境总文件夹,最终会以列表形式被vscode识别出来。

# 复制你本机的python_env(总的env文件夹放在里面)
# 之后就可以通过点击屏幕最下面小边框的左侧或右侧的Python 3.12.3 64-bit这种,点击3.12.3处即可发现上方弹出虚拟环境列表。
# 点击之后即可快速切换到虚拟环境。
# 如果没有弹出虚拟环境列表.需要重启vscode
'''

# 4.如何在虚拟环境下运行py文件
print("HelloWorld")
# 如果你切换到新虚拟环境中运行失败，是触发了windows10以上的保护机制,不允许其它软件运行脚本程序，在下方的terminal里面输入

# power shell里面：
# 查看当前执行策略:Get-ExecutionPolicy
# 修改当前执行策略：Set-ExecutionPolicy RemoteSigned
