# Map-Filter-Reduce: 
The map(), filter() and reduce() functions bring a bit of functional programming to Python. 

# map(): 
The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.

The syntax is:
```sh 
        map(function, iterable(s))
```
```sh 
Code: 
	def starts_with_A(s):
		return s[0] == "A"

	fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
	map_object = map(starts_with_A, fruit)

	print(list(map_object))
```
```sh 
Output: ["Apple", "Apricot"]
```
```sh 
Code:
	circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
	result = list(map(round, circle_areas, range(1,7)))
	print(result)
```		
```sh 
Output: [3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]
```
# filter():  
filter() forms a new list that contains only elements that satisfy a certain condition, i.e. the function we passed returns True.
			
The syntax is:
```sh 
		filter(function, iterable(s))
```
```sh 
Code:
	def starts_with_A(s):
    	return s[0] == "A"

	fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
	filter_object = filter(starts_with_A, fruit)

	print(list(filter_object))
```
```sh 
	Output: ['Apple', 'Apricot']
```			
```sh 	
Code: 
	dromes = ("demigod", "rewire", "madam", "freer", "tivit", "kiosk")

	palindromes = list(filter(lambda word: word == word[::-1], dromes))

	print(palindromes)
```
```sh 
    Output : ['madam', 'tivit']
```
# Reduce(): 
reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value. reduce() isn't a built-in function anymore, and it can be found in the functools module.

The syntax is:
```sh     
    	reduce(function, sequence[, initial])
```
```sh 
Code:
	from functools import reduce
    
    def add(x, y):
		return x + y

	list = [2, 4, 7, 3]
	print(reduce(add, list))
```			
```sh 
Output: 16
```			
```sh 
Code: 
    from functools import reduce
	list = [2, 4, 7, 3]
	print(reduce(lambda x, y: x + y, list))
	print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))
```			
```sh 
Output: 16
```