# Namespace: 
Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object. A namespace is a collection of names. Different namespaces can co-exist at a given time but are completely isolated. A namespace containing all the built-in names is created when we start the Python interpreter and exists as long as the interpreter runs.
```sh 
Code: 
	def outer_function():
		a = 20

    	def inner_function():
	    	a = 30
		    print('a =', a)

	        inner_function()
	        print('a =', a)
			
	a = 10
	outer_function()
	print('a =', a)
```			
```sh 
Output:
	a = 30
	a = 20
	a = 10
```
In this program, three different variables a are defined in separate namespaces and accessed accordingly. 
```sh 			
Code:
	def outer_function():
    	global a
		a = 20

    	def inner_function():
    		global a
    		a = 30
    		print('a =', a)

    	inner_function()
    	print('a =', a)


    a = 10
	outer_function()
	print('a =', a)
```
```sh 	
Output:
	a = 30
	a = 30
	a = 30 
```
Here, all references and assignments are to the global a due to the use of keyword global.
