# 除了os里面带有一些基本的目录相关操作，还有一个模块叫os.path,提供了更为精细的目录操作

#import os
import os.path

if not os.path.exists("f:\\example_dir"):
    os.mkdir(r"f:\example_dir")

# 测试路径
test_path = "f:\\example_file.txt"
test_dir = "f:\\example_dir"
test_file="f:\\example_file.txt"

# 获取文件的基本信息

# (一)路径:判断,绝对or相对
print(os.path.isabs(test_path))
# (二)目录格式:判断是否是文件夹目录
print(os.path.isdir(test_dir))
# (三)文件格式:判断是否是文件格式
print(os.path.isfile(test_file))
# (四)存在:判断文件/文件夹是否存在
print(os.path.exists(test_path))
# (五)文件/文件夹大小
'''
print(os.path.getsize(test_file))
'''
# (六)输出
# <1>输出绝对路径:
print(os.path.abspath(test_file))
# <2>输出所在目录名字:
print(os.path.dirname(test_dir))


# (七)时间信息:创建create--c 时间、access--a访问时间、modify---m最后修改时间
print(os.path.getctime(test_file))
print(os.path.getatime(test_file))
print(os.path.getmtime(test_file))

# (八)路径的分割和连接

# <0>准备工作,获取文件的绝对路径:
path_abs=os.path.abspath(test_file)


# <1>分割
# 将路径分割split成两部分:强调-------文件名
print(os.path.split(test_file))
# 示例如：("C:\\Users\\PyProjects\\myproject" , 'abc.txt')


# 将路径分割在扩展名处分割splitext为两部分：强调--------文件后缀扩展名
print(os.path.splitext(test_file))
# 示例如：("C:\\Users\\PyProjects\\myproject\\abc,    'txt')


# <2>拼接
path_joined=print(os.path.join("aa","bb","cc"))
# 存入到path_joined变量的值就是aa\bb\cc



'''
这部分知识就像是linux的基础指令一样,后续陆续使用之后就会熟悉。
'''


'''
再介绍一个较为常用的连续操作。列举出目录的所有文件,然后筛选出格式为txt的文件打印出来.(思路:先使用os模块的listdir来列出所有文件)
'''
print("==================================================================================================")

path="f:\\example_dir"
list=os.listdir(path)
for list_name in list:
    position_of_dot=list_name.rfind(".")
    if list_name[position_of_dot+1:]=="txt":
    # 上面这行代码是因为python中字符串是可遍历对象,在其中用字符串的方法"rfind()",从右侧出发.找到附近点号的索引位置.
    #  [position_of_dot+1:]这里是切片访问操作：冒号右侧不写代表从规定的起始位置遍历到结尾。
        print(list_name)



print("==================================================================================================")