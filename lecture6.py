list1 = [1,2,3,4,5,6,6,6,6]
print("List-1 is ",list1)
sliced_list = list1[1:4]
print("Sliced list is ",sliced_list)

list1.append(10) # adding 10 to end of list1
print("List-1 after appending 10 is ",list1)

list2 = [34,56]
print("List-2 is ",list2)
list1.extend(list2)
print("Extending List-1 with List-2...")
print("\n")
print("List-1 after extending is ",list1)
list1.insert(2,100)
print("After inserting 100 at 2nd index, List-1 is ",list1)
list1.sort()
print("List-1 after sorting is ",list1)
list1.pop(1)
print("After popping element of List-1 at index 1, List-1 is ",list1)
count = list1.count(6)
print("6 occured ",count," times in List-1")
print("Length of List-1 is ",len(list1))
print("Sum of all elements in List-1 is ",sum(list1))
duplicate_list = list2*3
print("The List with 3 duplicates of List-2 is ",duplicate_list)

#Creating empty list and getting user input into it.

print("Enter 5 numbers to create your own list:")
n=5
own_list=[] #This is empty list
for i in range(n):
	num = int(input())
	own_list.append(num)

print("Your List is ",own_list)