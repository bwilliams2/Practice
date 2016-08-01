"""Problem statment
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

http://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
"""

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))

g=(a,b,c)
if a > b:
	if a > c:
		print(a," is the largest")
	else:
		print(c," is the largest")
else:
	if b > c:
		print(b, "is the largest")
	else:
		print c, "is the largets"

x = sorted(g)
print x[-1],"is the largest"
		
	
