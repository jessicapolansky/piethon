##grab argv vector from sys module
from sys import argv
##argv vector has 2 values, script and a filename
script, filename = argv
##print instructions, including the filename entered
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#provide the chance to input, but what you do doesn't mean anything
raw_input("?")
##open the file in "write" mode (also overwrites any previous text)
print "Opening the file..."
target = open(filename, 'w')
#print target.read()
##we can also truncate, or wipe clean the file. not needed, but still works
#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()
