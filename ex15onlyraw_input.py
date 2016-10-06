# -*- coding: utf-8 -*-

print "Here's your file :"
filename = raw_input("> ")
txt = open(filename)
print txt.read()

# 重做一遍，使用了 raw_input
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()