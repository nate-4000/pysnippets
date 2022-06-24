import pran
import time
s = ("0." + input("Input a float under one. 0."))
d = bool(int(input("Do you want progress info? (use 0 for no and 1 for yes) ")))
i = 0
j = 0
cs = pran.snrr(0)
spin = ["|","/","-","\\"]
while not str(cs).__contains__(str(s)):
    i = i + 1
    cs = pran.snrr(i)
    if d:
        print(str(i) + " " + str(cs) + "\r", end="", flush=True)
    else:
        j = j + 1
        if j == 16:
                j = 0
        print("Calculating..." + spin[int((j/4)%4)],end="\r",flush=True)
print()
print("The seed containing " + str(s) + " is equal to " + str(i) + ".")
input("Press enter to exit...")
