# PEP8 and Documentation String:

# Maximum Line Length and Line Breaking:
PEP 8 suggests lines should be limited to 79 characters. This is because it allows you to have multiple files open next to one another, while also avoiding line wrapping.

```sh
def function(argument_1, argument_2,
            argument_3, argument_4):
    return argument_1
```
By using backslashes to break lines:
```sh
with open('/path/to/some/file/you/want/to/read') as example_1, \
    open('/path/to/some/file/being/written', 'w') as example_2:
    file_2.write(file_1.read()) 
```
PEP 8 encourages to break lines before the binary operators.	

# Do
```sh
total = ( variable_1 + variable_2 - variable_3 )
```
# Don't
```sh
total = ( variable_1 + variable_2 - variable_3 )
```
Python will assume line continuation if code is contained within parentheses, brackets, or braces:
```sh
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
```

If it is impossible to use implied continuation, then you can use backslashes to break lines instead:
```sh
from mypkg import example1, \
    example2, example3
```
# Recommended
```sh
total = (first_variable
         + second_variable
         - third_variable)
```
# Not Recommended
```sh
total = (first_variable +
         second_variable -
         third_variable)
```		 
# Identation:
Use 4 consecutive spaces to indicate indentation. Prefer spaces over tabs.		 
```sh
x = 5
if x < 10:
  print('x is less than 10') 			
```
# Identation with line break: 
The first style of indentation is to adjust the indented block with the delimiter:
```sh
def function(argument_one, argument_two,
              argument_three, argument_four):
        return argument_one
```		
# Improve readability by adding comments:
```sh
x = 10
if (x > 5 and
    x < 20):
    # If Both conditions are satisfied
    print(x)		
```
By adding extra indentation:
```sh
x = 10
if (x > 5 and
      x < 20):
    print(x)
```	
Another type of indentation is the hanging indentation by which you can symbolize a continuation of a line of code visually:
```sh
foo = long_function_name(
      variable_one, variable_two,
      variable_three, variable_four)
```
# Closing Braces in Line Continuations:
One way provided by PEP 8 is to put the closing braces with the first white-space character of the last line:
```sh
my_list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]
```	
Lining up under the first character of line that initiates the multi-line construct:
```sh
my_list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]	
```

# Blank Lines:
Using blank lines in top-level-functions and classes:
```sh
class my_first_class:
    pass
class my_second_class:
    pass
def top_level_function():
    return None
```	
Using blank lines in defining methods inside classes:
```sh
class my_class:
    def method_1(self):
        return None

    def method_2(self):
        return None
```
You can also use blank spaces inside multi-step functions.
```sh
def calculate_average(number_list):
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number
   
    average = 0
    average = sum_list / len(number_list)

   return average		
```

# Naming Conventions:


| Type | Naming Conventions | Examples |
| ------ | ------ | ------ | 
| Variable | Using short names with CapWords. | T, AnyString, My_First_Variable
| Function | Using a lowercase word or words with underscores to improve readability. | function, my_first_function
| Class | Using CapWords and do not use underscores between words. | Student, MyFirstClass
| Method | Using lowercase words separated by underscores. | Student_method, method
| Constants | Using all capital letters with underscores separating words | TOTAL, MY_CONSTANT, MAX_FLOW
| Exceptions | Using CapWords without underscores. | IndexError, NameError
| Module | Using short lower-case letters using underscores. | module.py, my_first_module.py
| Package | Using short lowercase words and underscores are discouraged. | package, my_first_package

	  
# Comments:
Limit the line length of comments and docstrings to 72 charac­ters. Use complete sentences, starting with a capital letter. Make sure to update comments if you change your code.

# Block Comments:
Indent block comments to the same level as the code they describe. Start each line with a # followed by a single space. Separate paragraphs by a line containing a single #.
```sh
for i in range(0, 10):
    # Loop iterates 10 times and then prints i
    # Newline character
    print(i, '\n')
```
# Inline Comments
Inline comments are the comments which are placed on the same line as the statement. 
```sh
x = 10  # An inline comment
y = 'JK Rowling' # Author Name
```
# Document Strings

Document strings or docstrings start at the first line of any function, class, file, module or method. These type of comments are enclosed between single quotations ( ''') or double quotations ( """ ).

```sh
def quadratic_formula(x, y, z, t):
    """Using the quadratic formula"""
    t_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    t_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)

    return t_1, t_2
    ```
