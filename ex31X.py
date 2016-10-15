# -*- coding: utf-8 -*-
print "你被关在一个房间里，房间里有两个门，现在你走出去。你是选择从1号门出去还是2号门出去？"

door = raw_input("> ")

if door == "1":
	print "打开门口，你看到一只巨大的熊在吃芝士蛋糕。你怎么办？"
	print "1. 拿走芝士蛋糕。"
	print "2. 冲着熊大吼试图赶走熊……"

	bear = raw_input("> ")

	if bear=="1":
		print "熊一巴掌pia死你，拜拜……"
	elif bear=="2":
		print "熊制杖般看着你……"
	else:
		print "喵喵喵？你 %s，熊跑掉了……" % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"