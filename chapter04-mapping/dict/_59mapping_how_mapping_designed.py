# 理解层面：针对dict的底层实现。

''
# 1.怎么理解将一个键值对，传到dict里的原理过程
'''
 1.字典对象背后原理：
 
 <0>利用散列表。
 (hash)散列-(table)表

 <1>散列表，什么是散列表？-----具有快速查找和检索功能的表，散列表。
散列表概念：hash-table，是一种用于快速查找和检索数据的数据结构

 <2>散列表怎么实现快速定位？-----散列函数、以及散列函数需要搭配的稀疏矩阵。

 <3>散列函数，是干什么的？dict的原理，散列表，散列表利用散列函数，将你的dict的表里面里面存放的'键、值对'，转化为一种"数组结构"，以方便查找、修改，实现快速定位。

通俗讲一下这句话：散列函数将具体的键值对，转化为'整数的索引"，该索引会映射到实际存储中'稀疏矩阵'的对应bucket位置。

  <4>稀疏矩阵：前面解释散列表时候，提到散列表是将"键值对"转化为"特定的数组结构"以方便快速定位，
 所提到的"特定的数组结构"，就是---"稀疏矩阵"，这个概念与普通数组，即稠密矩阵，二者做区分。
  
  # 稠密矩阵的回顾(普通的数组即稠密矩阵，连续的内存存着一连串的数据)：
   0.是确定好存储内容的一片空间，空白位置也占内存，存储为'空白'，  
   1.大小、扩容问题：二者都无法动态调整，如果容量不够，则需要新的内存空间来将原来的内容拷贝过去。
   （因此，虽然它们都可能涉及复制数据到新的内存区域，但稀疏矩阵的扩容过程可能比数组复杂得多，尤其是当其存储结构需要调整时。）
   2.插入和删除：组中插入、删除会导致数据整体移动，影响效率。
   3.查找速度不佳：不如散列表的查找速度是O(1)，二分查找和线性都不如散列表的散列函数查找。
   

  # 稀疏矩阵的特征：
   0.是大量空白元素的空间，不过只存储实际的值，它不是连续的，而且不对空白做存储，。
   1.稀疏数组（或稀疏矩阵）可以视为一种灵活、不规则的结构。
   (相比数组是类似规则的长方形，稀疏数组只存储非空元素的位置和值，因此在视觉上可能看起来“七扭八歪”)。  
'''


# 2.结合代码理解："将一个键值对，传到dict里的原理过程"
a={}   #建立了空字典 假设生成了   "为2的n次方的散列表"   假设生成了长度为8的稀疏矩阵形成散列表。
a["name"]="shaohl" # 进行键的传入--->背后是对散列表进行散列函数得到一个散列值，决定存在稀疏矩阵的哪个位置。
b=bin(hash("name"))
print(b)
# 可以看到超长的一串hash值，如0b111001101011010110111010000111111010010011101000001000111111000，它叫做散列值，从右向左，每次取三位进行对比，
# (后面的内容叫"开放寻址")
# 如末3位：000=0，数组0号位看是否空闲，将name键存到该位置。
# 如果末尾000对应的0号位被占用，那么再向左看三位，直到找到一个能存放的位置。
# (描述的是线性探查)其实还有二次探查或双重散列等方式

# 平常是键-值。如果一个键被引用两次存入内容，那么就会变成“键-链表”来使得该键对应多个值，值间略有区分。
# 散列表以这种方式解决散列冲突。

# 由于稀疏矩阵一直是稀疏的，一般达到了2/3容量时候就会自动进行扩容。

# 另外虽说散列表称之为存储“键-值”，"键和值"处都放置的是"键的hash值和值的hash值"


# 3.a.get("name")从字典里取出一个键。
# 跟hash("name")的流程是一样的，利用同样的hash值，检验哪里是空的，从而确定它当时被安放在哪里，进入并取出。


'''
2.为什么要使用这种散列表和稀疏矩阵的设计模式？
因为追求"以内存空间，换取速度" 稀疏矩阵在扩容和自身都比较占据内存，但是相应的可以应用这种迅速查找的散列查询提升查询速度。

'''

# 另外要注意，不要对dict进行遍历增加键值对的操作。因为dict每次增加你就好好加，不要连续这种操作因为：
# 指不定你哪次添加键值对到dict内dict很容易就会自动扩容稀疏矩阵，这是一个复杂的变化过程，原有的次序会变化，因此一边遍历一边进行添加操作会混乱出现大量错误。


# 键必须是一种可散列对象，后面会将什么是可散列对象。
