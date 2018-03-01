# Variables containing strings that comprise a bad joke
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# print bad joke
print x + y
print y
#print joke again, with additional text in the string
print "I said: %r" % x
print "I also said: '%s'" % y
# variables with new string and boolean value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# print combined string and boolean value
print joke_evaluation % hilarious
# more variables, each containing a new string
w = "This is the left side of..."
e = "a string with a right side."
#print the combined strings as a whole sentence
print w + e
