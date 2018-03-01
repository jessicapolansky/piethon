name = 'Jessica Robinson'
age = 28 #my age as of Jan 30, 3018
height = 65.00 # inches
cm = round(height * 2.54)
weight = 158 # lbs
eyes = 'green'
teeth = 'white'
hair = 'light brown'

print "Let's talk about %s." % name
print "She's about %fcm tall." % cm
print "She's about %dlbs heavy" % weight
print "That's not bad."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are %s except after coffee." % teeth

# random math
print "If I add %d, %d, and %d I get %r" % (age, height, weight, age + height + weight)
