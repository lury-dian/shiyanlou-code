#! /usr/bin/env python3
import sys
if len(sys.argv) <3:
    print("Wrong parameter")
    print("./copyfile.py file1 file2")
    sys.exit(1)
    #这个地方首先判断使用脚本的人有没有接上相应的参数，如果没有要报错，并且告诉他要后面要接上两个文件名
    #这里的sys.exit(1)是程序异常退出，后面的都不会再执行了，因为你的参数输入有误，所以这里要异常退出，1表示异常，0表示正常
f1 = open(sys.argv[1])
s = f1.read()
f1.close()
f2 = open(sys.argv[2],'w')
f2.write(s)
f2.close()
'''
在命令行输入$ ./copyfile.py file1 file2
sys.argv 这里能够得到命令行输入的参数和命令的列表['./copyfile.py','file1','file2']
'''
