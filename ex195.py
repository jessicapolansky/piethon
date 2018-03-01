def kitty(treats, catnip):
    print "Kitty is hungry for %s!" % treats
    print "Especially after having %r oz of catnip. ^^" % catnip

kitty("babies", 100)
tasty = "birds"
oz = 50
kitty(tasty, oz)
kitty(tasty + tasty, oz + 20)
print "this one"
kitty(kitty(tasty, oz), oz)
treats = raw_input('What food do we have?')
kitty(treats, 1)
kitty("cuddles" , 3 + 6)
food1 = "manatees"
food2 = "anteaters"
kitty(food1 + " and " + food2, 5)
oz = round(float(raw_input('How much catnip did you buy?!')))
kitty("meat" , oz)
kitty("oranges" , 5.5)
