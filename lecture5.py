name = "Pavan Sai"
length = len(name)
print(length)

#slicing the name from index 1 to 4
name2 = name[1:5]
print(name2)

#slicing the name from index 0 to 4
name3 = name[:5]
print(name3)

#slicing the name from index 0 to end
name4 = name[0:]
print(name4)

string = "a"
count = name.count(string) # a.count(b) -> returns no.of occurences of b in a 
print("There are ",count," occurrences of ",string," in ",name)

string2 = "Sai"
index = name.find(string2) # a.find(b) -> returns starting index of b in a. if not found, returns -1
print(string2," starts at index ",index," in ",name)

modified_name = name.replace("Sai","Kalyan") # a.replace("whatever you want to replace","what do u want to replace it with")
print("Modified version of ",name," is ",modified_name)

if("P" in name):
	print("P is there in Pavan Sai")
else:
	print("P is not there in PAvan Sai")

for char in name:
	print(char,end="")

print("\n")

capital_name = name.upper()
lower_name = name.lower()
print("Capital name is ",capital_name)
print("Lowe name is ",lower_name)