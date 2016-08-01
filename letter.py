"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime

name = input("What is your first name? ")
age = float(input("What is your age? "))

cur = datetime.datetime.now()
diff = 100-age
year = cur.year + diff

print("You will be 100 in the year %d" % (year))

repeat = int(input("How many times should this repeat? "))

for num in range(0, repeat):
	print("You will be 100 in the year %d" % (year))
