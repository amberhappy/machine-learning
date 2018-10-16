import sys
import os

try:
    file = open('3.txt','r+')
except Exception as e:
    print("there is no file named 3.txt")
    response = input('do you want to cerad a new file(Y or N):')
    if response =='Y':
        file = open('3.txt','w')
    else:
        pass
else:
    file.write('ssss\n')
file.close()