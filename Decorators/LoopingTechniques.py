# Using Enumerate
for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']): 
    print(key, value) 
    
for key, value in enumerate(['The', 'world', 'is', 'round', 'not', 'flat']): 
	print(value, end=' ') 
	
#  Using zip
# initializing list 
questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 
  
# using zip() to combine two containers and print values 
for question, answer in zip(questions, answers): 
	print('What is your {0}?  I am {1}.'.format(question, answer))                                                                                                        
 
    
#Using iteritem
d = { "Mount" : "Everest", "Mount" : "Annapurna" } 
  
# using iteritems to print the dictionary key-value pair 
print ("The key value pair using items is : ") 
for i,j in d.items(): 
	print (i,j)  
			                                                                                        
			