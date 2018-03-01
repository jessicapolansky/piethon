print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""

print "-------------"
print poem
print "-------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
#creating a function, whatever is put in () works, variable or number
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    #return 3 numbers, that can be called individually!
    return jelly_beans, jars, crates

#"beans, jars, crates" is actually a single variable with 3 components
#the variable is based on running the function with the SP variable
startpoint = 10000
beans, jars, crates = secret_formula(startpoint)

print "With a starting point of: %d" % startpoint
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = startpoint / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
