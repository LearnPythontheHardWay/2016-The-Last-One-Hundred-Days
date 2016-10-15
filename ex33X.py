
# while i < 6:
# 	print "At the top i is %d" %i
# 	numbers.append(i)

# 	i += 1
# 	print "Numbers now:", numbers
# 	print "At the bottom i is %d" % i


# print "The numbers:"

# for num in numbers:
# 	print num

i = 0
numbers = []
def do_while(num,plus):
	

	while i < num:
		print "At the top i is %d" %i
		numbers.append(i)

		i += plus
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

a = raw_input()
do_while(10,1)
print a
do_while(10,2)
print a
do_while(10,3)