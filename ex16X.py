# -*- coding: utf-8 -*-
# 当 script, filename = argv 只有一个变量时运行出错
# filename = argv
# 因为运行脚本是：python ex16X.py ex16X.txt
# 需要输入两个参数

from sys import argv
script, filename = argv

text = raw_input("input some text: ")
a = open(filename, 'w')
a.write(text)
a.close()