tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = 'I"m \\ a \\ cat.'

fat_cat = '''
I'll do a list:
\t* Cat's food
\t* Fishies 'or something'
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print "Raw string %r" % fat_cat
print "This is a \"test\""
print tabby_cat + backslash_cat
