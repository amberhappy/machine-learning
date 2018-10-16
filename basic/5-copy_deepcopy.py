#什么是id？一个对象的id值在CPython解释器里就代表它在内存中的`地址
#所谓浅拷贝就是对引用的拷贝，所谓深拷贝就是对对象的资源的拷贝
import copy
a = [1,2,3]
b = a
print(id(a))
print(id(b))
#以上，当改变a或者改变b后，另一个也随之变化

#浅拷贝
#当使用浅拷贝时，python只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已
#浅拷贝仅仅复制了容器中元素的地址

c = copy.copy(a)
print(id(c))
c[1]= 222
print(a)
#以上，当改变c时，a不变

#深拷贝
#深拷贝是在另一块地址中创建一个新的变量或容器，
# 同时容器内的元素的地址也是新开辟的，仅仅是值相同而已，是完全的副本。也就是说（ 新瓶装新酒 ）
d = copy.deepcopy(a)
print(id(d))

a[2]= 333
print(d)

#需要注意的是，赋值和浅拷贝时，字符串为不可变的，需重新开辟空间，list可变，不需重新开辟空间

a = [1,2,[3]]
cc = copy.copy(a)
print(a)
print(id(a))
print([id(i) for i in a])

print(cc)
print(id(cc))
print([id(i) for i in cc])

a[2].append(5)
print([id(i) for i in a])
print([id(i) for i in cc])
print(cc)
print(a)
