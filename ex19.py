#create new function that prints with 2 variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheeses!" % cheese_count
    print "you have %d boxes of crackers!" % boxes_of_crackers
    print "man that's enough for a party!"
    print "Get a blanket.\n"
#run function with numbers directly entered for variables
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#assign numbers to new variables, then enter those variables to be inputted into the actual function Variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#run function, but make it do math to figure out the variable amounts
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#math to get variables, but do math using numbers assigned to variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
