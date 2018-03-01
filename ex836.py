#define a string with 4 empty variables
formatter = "{} {} {} {}"
x = "one"
y = "two"
z = "three"
a = "four"
#display the string, but format those empty variables with the numbers passed by the 'format' command
print (formatter.format(1, 2, 3, 4))
#enter strings as part of the longer string to display
print(formatter.format(x, y, z, a))
#Add boolean values into the string's variables and print
print(formatter.format(1 == 1, 2 >= 3, 5 < 1, 9 != 2))
#add the strings to the variables in the string for stringception!
print(formatter.format(formatter, formatter, formatter, formatter))
# still pass 4 variables, which are strings, just add some line breaks
print(formatter.format(
    "Try your\n",
    "Own Song OUT\n",
    "Maybe a dance number too\n",
    "Keep things lively\n"
))
