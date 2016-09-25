# -*- coding: utf-8 -*-

name   = 'AwThink'
age    = 19     # not a lie
height = 74     # inches
weight = 180    # lbs
eyes   = 'Black'
teeth  = 'White'
hair   = 'Brown'
in2cm  = 2.54
cm2in  = 0.393700787

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# 试做单位换算
print "1 inches equal how many centimetre? %r" % in2cm
print "1 centimetre equal how many inches? %r" % cm2in
print "74 inches equal %r centimetre. " % (74*in2cm)
print "%d centimetre equal %r inches. " % (180, 180*cm2in)