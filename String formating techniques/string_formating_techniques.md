# String formating techniques: 
# String Formatting (% Operator): 
Strings in Python have a unique built-in operation that can be accessed with the % operator.  the %s format specifier here to tell Python where to substitute the value of name, represented as a string.
```sh 									
        Code: 
             'Hello, %s' % name
```								
```sh
        Output: 
            	"Hello, Jon Snow"
```									
#  String Formatting (str.format):  
This string formatting gets rid of the %-operator special syntax and makes the syntax for string formatting more regular. Formatting is now handled by calling .format() on a string object. 			
```sh 
        Code:
	        'Hello, {}'.format(name)
```
```sh 									
		Output:
		    	'Hello, Jon Snow'
```
# String Interpolation / f-Strings:  
This formatting strings lets you use embedded Python expressions inside string constants.	
```sh 
			Code: 
				def greet(name, question):
					return f"Hello, {name}! Are you watching {question}?"
				greet('Arya', 'Game of Thrones')
```									
```sh 
            Output:
				"Hello, Arya! Are you watching Game of Thrones?"
```									
# Template Strings: 
Template strings are not a core language feature but theyâ€™re supplied by the string module in the standard library.
```sh 
			Code:
				templ_string = 'Hey $name, there is a $question next episode coming!'
				Template(templ_string).substitute(name = name, question = question)
```	
```sh 
			Output:
				'Hey Arya, there is a Game of Thrones next episode coming!'
```