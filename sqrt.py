import math
try:
        x = float(input("Input a number: "))
except ValueError:
        print("You did not input a number. You must now die. Say goodbye to your computer!")
i = 0
y = x
while (x > 1):
	x = math.sqrt(x)
	print(str(i) + ": " + str(x))
	i+=1
print("It took " + str(i-1) + " tries for " + str(y) + " to stop at 1.")
input("Press any key to exit... ")
