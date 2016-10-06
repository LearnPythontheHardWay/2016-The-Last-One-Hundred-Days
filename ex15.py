# -*- coding: utf-8 -*-

# 导入 sys 模块
from sys import argv

# 将 argv 解包
script, filename = argv

# 传入文件名，将文件打开，然后赋值给变量 txt。
# 这里返回的是一个 file object，不是文件的内容。
txt = open(filename)

print "Here's your file %r:" % filename
# 读取变量 txt 里的内容，将其打印出来
print txt.read()

# 重做一遍，使用了 raw_input
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()