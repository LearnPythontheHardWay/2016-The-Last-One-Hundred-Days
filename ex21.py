# -*- coding: utf-8 -*-

def add(a,b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# 附加练习
# 自己定义了一个函数，但感觉都不像函数
one = divide(iq, 2)
two = multiply(weight, one)
three = subtract(height, two)
four = add(age, three)

def equal(a, b):
	print "%d and %d are equal? " % (a, b)
	return a == b

# 输出的是数字，怎样才能输出变量名 what 和 four ?
results = equal(what, four)
print results