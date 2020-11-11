# Data Structures:
A data structure is a particular way of organizing data in a computer so that it can be used effectively.

Types of Data Structure
- Built-in Data Structures (List, Dictionary, Tuple, Set)
- User Defined Data Structures (Stack, Queue, Linked List, Hashmap, Tree, Graph)

# Stack:
Stack is a data structure that follows the LIFO (Last In First Out) principle. This include 2 operations: Push and Pop.
	
# Queue: 
A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. This include 2 operations: enqueue and dequeue

# Comprehensions: 
It is a short way to construct new sequences (such as lists, set, dictionary etc.) using sequences that are already defined. Python supports 4 different type of comprehensions:
- List Comprehensions: List comprehensions provide ways to create new lists.
	Syntax of List Comprehension
```sh
[expression for item in list]
```
- Dictionary Comprehensions: We can also create a dictionary using dictionary comprehensions. The basic structure of a dictionary comprehension looks like below.
```sh
	output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}
 ```
- Set comprehensions: Set comprehensions are pretty similar to list comprehensions. The only difference between them is that set comprehensions use curly brackets { }.
				
- Generator Comprehensions: Generator Comprehensions are very similar to list comprehensions. One difference between them is that generator comprehensions use circular brackets whereas list comprehensions use square brackets. The major difference between them is that generators don't allocate memory for the whole list. Instead, they generate each value one by one which is why they are memory efficient. 
				
# Nested Comprehensions:  
Nested List Comprehensions are nothing but a list comprehension within another list comprehension which is quite similar to nested for loops.

# Sequences unpacking:  
Python allows unpacking of any sequence(iterable) into variables using a simple assignment operation. Unpacking can be done by assigning sequence(iterable) to comma separated variables .

#  Unpacking Arbitrary Number of variables: 
Python * expression can be used to assign arbitrary number of elements to single variable. Arbitrary number of variables will be stored in the form of list.

# Unpacking selective elements:
Throwaway variable _(underscore) can be used to select and discard elements during sequence unpack. _ acts as temporary variable for sequence unpack.

# Unpacking Multiple sequences: 

# Passing Unpacked sequence as function parameters:
 
** expression can be used to unpack dictionary elements and pass it as keyword arguments to function.

# Looping Techniques in Python: 
1. Using Enumerate: 
Enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.

2. Using zip: Zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially. The loop exists only till the smaller container ends.
			
3. Using iteritem: iteritems() is used to loop through the dictionary printing the dictionary key-value pair sequentially.		

4. Using items(): items() performs the similar task on dictionary as iteritems() but have certain disadvantages when compared with iteritems().It is very time-consuming. Calling it on large dictionaries consumes quite a lot of time. It takes a lot of memory. Sometimes takes double the memory when called on a dictionary.		
				  
		
5. Using sorted():  sorted() is used to print the container in sorted order. It doesnâ€™t sort the container but just prints the container in sorted order for 1 instance. The use of set() can be combined to remove duplicate occurrences.
	
6. Using reversed(): reversed() is used to print the values of the container in the reversed order. It does not reflect any changes to the original list