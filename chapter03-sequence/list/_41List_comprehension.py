# 讲解如何利用range推导式生成出一个列表
a=[x*2 for x in range(5)]
print(a)
# 如何去看这个长串?
'''
for代表着循环操作，看它右侧是对一个0-4的range对象进行循环，for左侧是对其进行的循环指令：x*2。


[expression  for   variable  in   range]
'''



# 还可以继续加上if在这个长串内筛选。
b=[x*2 for x in range(50) if x%4==0]
print(b)

# 另外，为什么要把它推导式生成，叫做comprehension呢，因为它的"理解"的意思，更接近于通过"理解"一个函数表达式，来生成一个新序列的行为。它是"函数式编程"的讨论领域的专有名词。



# 注意这节课我们讲的是range推导式生成，英文叫做comprehension，它有三种形式，分别用于list、dict、set三种数据存储结构的初始化操作，它们的外层括号分别是list用中括号[],dict和set都用花括号{}
# 在其它对象中我们可能也会遇到类似的写法expression+for+variable+in+range这种格式的地方，可能是generate expression，但是外面是括号形式，(x*2 for x in range(3)),这种叫做生成器表达式，它以外层是小括号为特征
# generate expression的生成对象是generate，生成器对象，内部只有一个指针，指针只能前进到结尾不能回到开头，因此当遍历生成器对象generate到末尾之后，指针指向"空“，该生成器对象成为空对象。









