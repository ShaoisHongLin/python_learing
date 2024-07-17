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
读取操作:
导入python中 csv的模块
open注明r-读取模式:
    创建csv的reader"阅读器对象",即csv.reader(file),"csv阅读器对象"会对于文件对象进行解析,它是一个迭代器对象,为了方便遍历读取。
    csv.reader这个阅读器对象 是一个迭代器对象,这个迭代器的每个元素都是一个列表,供我们进行一次遍历的操作
    每个列表又容纳了每行的所有字符。
    csv_readiterator=csv.reader(f)

写入操作:
open注明w-写入模式:
    创建csv的reader"写入器对象",即csv.writer(file),"csv写入器对象",它和阅读器对象不同,不是迭代器,内置writerow和writerows进行写入操作。
    csv_writerobject=csv.writer(f)

    把准备好的数据,用writerow()和writerows()来进行写入。

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


import csv

header=['姓名', '年龄', '职业', '薪水']  # 标题行
rows=[('小明', '21', '程序员', '4500'),('小王', '23', '程序员', '7000')] # 其他行
with open(r"f:\new.csv","w",encoding="utf-8")as f:
    csv_writerobject=csv.writer(f)
    csv_writerobject.writerow(header)
    csv_writerobject.writerows(rows)