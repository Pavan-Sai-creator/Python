import random

r = random.randint(1,20)
print("Guess the number: ")

while(True):
	inp = int(input())
	if(inp<r):
		print("Try greater number")
	elif(inp>r):
		print("Try lesser number")
	else:
		print("Congratulations")
		break;