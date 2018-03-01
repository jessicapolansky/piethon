i = 0
numbers = []
def numberBuild(i):
    limit = 5
    numbers = []
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
print(numberBuild(5))
#print("The numbers: ")
#for num in numbers:
 #   print(num)