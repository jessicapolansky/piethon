#pull the argv module from the sys library
#from sys import argv
#parse the input from argv to 2 variables
#script, filename = argv
#assign the open function to variable txt, with it opening the filename
filename = input("What file should I read?")
txt = open(filename)
#This is the variable filename, then reads it with the .read() function
print(f"Here's your file, {filename}:")
print(txt.read())
#Request the input again, using the input function
#print("Type the filename again:")
#file_again = input("> ")
#assign the open function to a new variable that pulls the 'new' filename
#txt_again = open(file_again)
#read the file with the variable that opens the file
#print(txt_again.read())
