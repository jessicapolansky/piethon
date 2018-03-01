# of cars available
cars = 100
# how many passengers fit in each car
space_in_a_car = 4.0
#how many drivers are available
drivers = 30
#how many passengers
passengers = 90
# of cars that won't be used
cars_not_driven = cars - drivers
# of cars that will be used
cars_driven = drivers
# how many passengers can be driven
carpool_capacity = cars_driven * space_in_a_car
number of passengers that will fit per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have" , passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
