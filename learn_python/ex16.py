#!/usr/bin/env python2.7

### commands you can give to files ###
#close -- Closes the file. Like File->Save.. in your editor.
#read -- Reads the contents of the file. You can assign the result to a variable.
#readline -- Reads just one line of a text file.
#truncate -- Empties the file. Watch out if you care about the file.
#write('stuff') -- Writes "stuff" to the file. 

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# 'w' to open as writeable - 'r' as readable - 'a' for append
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# truncating the file is unnecessary since opening the file in write-mode will overwrite the file
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#replaced the following (6) lines with 'out = ...'
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

out = "%s\n%s\n%s\n" % (line1, line2, line3); target.write(out)

print "And finally, we close it."
target.close()