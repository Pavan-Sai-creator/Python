#No indexing in dictionaries
# Kyes can only be integer or string. Values can be of any data type (values can be of list data type also)
dict1 = {"Pavan":21,"Ajay":18,"Rahul":20,"Vijay":22}
keys = dict1.keys() #keys is a list of all keys in the dictionary
values = dict1.values()

print("Length of dictionary is ",len(dict1))
print("The dictionary is ",dict1)
print("The list of keys is ",keys)
print("The list of values is ",values)

del dict1["Vijay"] # deleting "Vijay" and it's corresponding value from the dictionary
print("Dictionary after deleting Vijay is ",dict1)

dict1["Rahul"]=21 # Updating values
print("Dictionary after updating Rahul's age is ",dict1)

dict1["Chanu"]=21 # Adding another key-value pair
print("Dictionary after adding another key-value pair is ",dict1)

ajay_age = dict1["Ajay"] # Fetching value from dictionary with it's key
print("Ajay's age is ",ajay_age)

print("Checking availability of Rahul in the dictionary...")
if("Rahul" in dict1):
	print("Available")
else:
	print("Not available")

# Printing data from dictionary using for loop

for item in dict1:
	print(item," -> ",dict1[item])