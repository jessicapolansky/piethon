#import the argv vector from the sys module so we can get input for our functions
from sys import argv
#specifically, take 2 values, the script and a value (the file to read)
script, input_file = argv
#read the input file and print out its contents on screen
def print_all(f):
    print f.read()
#"rewind" the file? can't print it again until we get to the beginning
#as we work on a file, we 'advance' thru it, have to seek to get back
def rewind(f):
    f.seek(0)
#print a single line from the file, as determined by line_count and current pos
def print_a_line(f):
    print f.readline(),
    #print "line_count = %d" % line_count
#let's grab a file!
current_file = open(input_file)

print "First let's print the whole file:\n"
#Use our 1st function to display its contents
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#seek back to the first line of the file
rewind(current_file)

print "Let's print three lines:"
#declare a line and have it display
current_line = 1
print_a_line(current_file)
#declare the line to now be the next one in the file and print that
#print "current_line = %d" % current_line
current_line += 1
print_a_line(current_file)
#print "current_line = %d" % current_line
current_line += 1
print_a_line(current_file)
#print "current_line = %d" % current_line
