def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")
#Run the function with numbers instead of variables
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
#Create some variables to use as arguments for the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#Don't just put numbers, make python do math before using the arguments
print("We can even do math inside them too:")
cheese_and_crackers(10 + 20, 5 + 6)
#turn the variables into numbers and do math on them before they are arguments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
