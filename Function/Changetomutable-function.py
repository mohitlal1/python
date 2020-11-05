def try_to_change(list1,list2):
    list1.append(3)
    # reassign mutable object
    list2 = [40,50,60]
 
list1 = [1,2]
list2 = [4,5,6]
 
# change to mutable objects
try_to_change(list1,list2)
 
print(list1)
print(list2)