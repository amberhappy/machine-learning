###zip函数接受任意多个（包括0个和1个）序列作为参数，合并后返回一个tuple列表,请看示例：
a = [1,2,3]
b = [2,4,6]
c = [2,7]
ab = zip(a,b,c)
print(list(ab))#需要加list来可视化这个功能

a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))
for i,j in zip(a,b):
    print(i,j)
     #print(i/2,j*2)

##lambda定义一个简单的函数，实现简化代码的功能，看代码会更好理解。
#fun = lambda x,y : x+y, 冒号前的x,y为自变量，冒号后x+y为具体运算。
fun = lambda x,y:x+y
x = int(input("x="))
y = int(input("y="))
print(fun(x,y))

#map是把函数和参数绑定在一起。
def fun(x,y):
    return x+y

print(list(map(fun,[1,3],[2,5])))
#list(map(fun,[1],[2]))