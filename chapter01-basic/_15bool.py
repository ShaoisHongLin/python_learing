# bool对象的详细解释：

'''
python3里面才加入了bool对象，之前都是0和1表示false|true，
因此底层本质上True和False完全就是1和0.
'''

'''  
特殊布尔值，<如果以bool类型表示以下内容>，  

认为是False：  
  False自身，0，0.0、空值None、  
  空序列对象(包括空列表、空元组、空集合、空字典、空字符串)  
  空range对象、空迭代对象。  
  其余布尔值，都认定是True：  
'''
a = True
b = 3
print(a + 3)  # 因为最底层就是0和1因此，bool可以加减。

print(bool(""))  # 空字符串
print(bool([]))  # 空列表
print(bool(None))  # None
print(bool(0))  # 0
print(bool(0.0))  # 0.0
print(bool(False))  # False自身

print(bool("12314564646"))  # 任何除了特殊bool值表示False的，都表示True

'''
思考：
print(bool("False"))的结果是True还是False
'''
print(bool("False"))  # 是什么呢？