# 本节教学 写入和 读取文本文件。

# 首先是写入：可以使用write(""),writelines(["" , "","" ,"" ])
with open(r"f:\123456.txt","w",encoding="utf-8")as f:
    s=["字符串1","字符串2\n","字符串3\n","字符串4"]
    f.writelines(s)

# 然后是读取：read(size)读取size个字符,readline()读取一行字符,readlines将每一行作为一个string存入字符串列表。

# read(size)如果不写size，那么读取整个文件，如果读取到了结尾，就会返回空字符串。

# readline()如果读取到结尾，返回空字符串。

# readlines()每一行作为字符串，存入字符串列表，返回字符串列表。

'''
之所以会返回空字符串那两个,是因为读取是利用一个指针,从头部读取到尾部,如果指针已经在结尾处,那么再用read读取的结果就是空字符串。
'''

with open(r"f:\123.txt","r",encoding="utf-8") as f:
    s1=f.read()
    s2=f.read()
    print("第一次读取内容:",s1)
    print("第二次读取内容:",s2)  # 可以发现s2由于s1的操作时候将指针移到了尾部,s2的读取结果将会是空值

with open(r"f:\123.txt","r",encoding="utf-8") as f:
    s3=f.readline() # 每次调用指针就会下移一行
    s4=f.readline()
    s5=f.readline()
    print("第三次,单行读取内容:",s3)
    print("第四次,单行读取内容:",s4)
    print("第五次,单行读取内容:",s5)

with open(r"f:\123.txt","r",encoding="utf-8") as f:
    s6=f.readlines() # 读取整个文件的各行存入列表。
    print("第六次,整体读取内容存入字符串列表:",s6)

'''
如果一个较小的文件,我们可以readlines直接读取到列表里面.
但是如果是一个很多很多很多行的文本文件,我们直接使用readlines将会产生一个很消耗资源的列表,这是不推荐的。

因此我们要分步进行,多次使用readlines使得内容输出到多个列表当中,需要"循环"

python中----文件对象可以被迭代,且文本数据里面的每个行"line"是专有的,相当于每行的数据,常常用于遍历。

for line in f-------------最常见的读取文本文件的方式。
'''

with open(r"f:\123.txt","r",encoding="utf-8") as f:
    for line in f:
        print("逐行:",line,end="")



print()
print()
'''
如果就像利用函数的方式,readline()调用。那就用函数的思想.

写一个默认的循环,并且遍历它。
'''
with open(r"f:\123.txt","r",encoding="utf-8") as f:
    while True:
        line=f.readline()
        if not line:
            break
        else:
            print(line,end="")