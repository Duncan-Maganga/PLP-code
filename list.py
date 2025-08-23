# Creating empyty list
my_list = []
print("Empty list:", my_list)
 
 # Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List after appending elements:", my_list)
my_list.insert(1, 15)
print("List after inserting 15 at index 1:", my_list)
my_list.remove(30)
print("List after removing 30:", my_list)
my_list.insert(3, 30)
print("List after inserting 30 at index 3:", my_list)
# Removethe lasyy=t element from my_list
my_list.pop()
print("Print after removing the last element:", my_list)
# Extending my list by another list
my_list.extend([50, 60, 70])
print("List after extending with another list:", my_list)
# Sort the list in ascending order 
my_list.sort()
print("Sorted list in ascending order:", my_list)
# Find the index of value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30 in the list:", index_of_30)
# FInal list
print("Final list:", my_list)
