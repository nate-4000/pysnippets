import sys
import os
import time
import datetime

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

while True:
        print(str(datetime.datetime.now()))
        clear()
