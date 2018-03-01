# this one is like your scripts with argv
def print_two(*args):
    print "%s" % (args,)
    #arg1, arg2 = args
    #print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1 %r, arg2 %r" % (arg1, arg2)

#this just does one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."
    print_one("For realz")
print_two("Zed", "Shaw","is", "a", "jerky!")
print_two_again("Two" , "Variables")
print_one("First!")
print_none()
