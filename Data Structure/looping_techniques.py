# looping using enumerate
for key, value in enumerate(['The', 'world', 'is', 'round', 'not', 'flat']): 
	print(value, end=' ')
 
questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 
  
# using zip() to combine two containers and print values 
for question, answer in zip(questions, answers): 
	print('What is your {0}?  I am {1}.'.format(question, answer)) 
 
d = { "Mount" : "Everest", "Mount" : "Annapurna" } 
  
# using items to print the dictionary key-value pair 
print ("The key value pair using items is : ") 
for i,j in d.items(): 
	print(i,j )
 

lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 
  
# using sorted() to print the list in sorted order 
print ("\nThe list in sorted order is : ") 
for i in sorted(lis) : 
    print (i,end=" ")  
			
print ("\nThe list in sorted order (without duplicates) is : ") 
for i in sorted(set(lis)) : 
	print (i,end=" ")  
 
lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 
  
# using revered() to print the list in reversed order 
print ("\n The list in reversed order is : ") 
for i in reversed(lis) : 
	print (i,end=" ") 
			 