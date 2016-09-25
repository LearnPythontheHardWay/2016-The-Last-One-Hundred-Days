# -*- coding: utf-8 -*-

# 定义变量 x ，x这个变量中包含有格式化字符串。
# 但是为什么在这里使用格式化字符串？10这个数字是固定的常量了。
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# 定义变量 y ，y中又包含有格式化字符串。这两个格式化字符串又用到了上两行定义的变量。
# 类似于在ex5X中的用法
y = "Those who konw %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "Ialso said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# % 在这里不是取模。整句的意思其实是把上面的两个变量拼接了起来，变成了下面这样：
# print "Isn't that joke so funny?! %r" % hilarious
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# 由此知道，+ 可以用于拼接字符串
# 参考ex3，字符串和算式拼接用了“,”
print w + e