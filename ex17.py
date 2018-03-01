from sys import argv
#from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
#indata = open(from_file)

#print "The input file %d bytes long" % len(indata)

#print "does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

out_file = open(to_file, 'w')
out_file.write(from_file)

print "Alright, all done."
#print "does the output file exist? %r" % exists(to_file)
out_file.close()
#in_file.close()
