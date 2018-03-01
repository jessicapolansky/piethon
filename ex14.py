from sys import argv

script, title, user_name = argv
promt = '= '

print "Hi %s %s, I'm the %s script." % (title, user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s %s?" % (title, user_name)
likes = raw_input(promt)
print "Where do you live, %s %s?" % (title, user_name)
lives = raw_input(promt)

print "What kind of computer do you have, %s?" % title
computer = raw_input(promt)

print """
    Alright, so you said %r about liking me.
    You live in %s. Not sure where THAT is.
    And you have a %s computer. Nice!
    """ % (likes, lives, computer)
