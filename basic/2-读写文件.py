# -*- coding: UTF-8 -*-
import sys
import os

#打开文件的时候可以指定读取模式（‘r’）、写入模式（‘w’）、附加模式（‘a'）或者读写模式（‘r+’）
filename = '2.txt'
with open(filename,'w') as file_object:
    file_object.write("i love programming.\n")
    file_object.write("i love travelling.\n")
#这里要注意的是，如果要写入的文件不存在，函数open则会自动创建，以（‘w’）模式打开文件的时候千万要小心，因为如果文件已经存在，python将会清空该文件。
#使用附加模式（‘a'）打开文件的时候，python不会清空源文件，而是你附加的内容都会添加到文件的末尾，如果指定的文件不存在，python将为你创建一个空文件。

with open(filename) as f:
    T = f.read()
    print(T)
    #i love programming.
    #i love travelling

with open(filename) as f:
    T = f.readline()
    while T:
        print(T)
        T = f.readline()
with open(filename) as f:
    T = f.readlines()

    print(T)
    #['i love programming.\n', 'i love travelling.\n']


for line in open(filename,'r'):
    print(line)