from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
print "Type the filename:"
file_raw = raw_input ("> ")
txt_raw = open(file_raw)
print txt_raw.read()
txt.close()
txt_raw.close()
