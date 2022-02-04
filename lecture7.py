# Taking input when it is a string of format -> "insert 0 25 3"
print("Enter your command: ")
cmd = input()
if(cmd.find("insert")>=0):
	sliced_cmd = cmd[7:] # slice the command to see if it is insert, remove, append, etc...
	x,y,z = sliced_cmd.split() # splits the remaining string and store 1st value in x, 2nd value in y and so on..
	x = int(x) # convert x from string to int
	y=int(y)
	z=int(z)
	print("You want to insert ",y," at ","index ",x," and you want to do this ",z," times.")