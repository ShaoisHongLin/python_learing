# 介绍csv   comma separated values  被逗号分隔开的文件格式：

# excel表格的输出形式，或者文本以标准的空格来分隔的规整表格形式内容。

# 以下是一个excel表格的导出csv格式的示例：
'''
姓名,年龄,工作,薪水
小明,21,测试,6000
小王,22,开发,7000
'''

# 我们要学习简单的对csv进行读写的操作
'''
(一)
导入python中 csv的模块
创建csv的reader"阅读器对象",即csv.reader(file),"csv阅读器对象"会对于文件对象进行解析,
解析的结果将会是一个迭代器,这个迭代器的每个元素都是一个列表,供我们进行一次遍历的操作
每个列表又容纳了每行的所有字符。
csv_iterator=csv.reader(f)

(二)
对迭代器进行next获取标题信息栏。之所以使用next来获取是因为迭代器对象默认的内置指针指在首地址处,是迭代器的本身信息:
<_csv.reader object at 0x...>，而不是 CSV 文件的标题行。

因此使用"next()",移动可迭代对象的指针位置并获取移动后指向的内容。

(三)
另外,注意encode的方式,以及遍历迭代器对象进行输出迭代器内部的列表。
'''
import csv

with open(r"f:\12345.csv","r",encoding="utf-8")as f:
    csv_iterator=csv.reader(f)
    header_row=next(csv_iterator)
    print(header_row)
    for row in csv_iterator:
        print(row)