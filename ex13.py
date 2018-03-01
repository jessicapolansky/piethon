from sys import argv

script, first = argv

print "This script is called: ", script
print "Your first variable is: ", first
#print "Your second variable is:", second
#print "Your fourth variable is:", fourth
wat = raw_input ("Thoughts? ")
print 'This script is called: %s. Your first variable is: %s. Your reaction was %r' % (script, first, wat)
