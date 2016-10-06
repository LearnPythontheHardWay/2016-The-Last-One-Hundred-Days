# -*- coding: utf-8 -*-

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
onr comprehend passion from intuition
and requires an explanation
\n\t\twhere is none.
"""

# 试试 print 后加逗号和不加的区别
print "--------------",
print poem
print "--------------"


five = 10-2+3-6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
# 这个倒是个新句子，有点像js的数组
# 运行后提示 unpack，和之前的 argv 是同类？
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)