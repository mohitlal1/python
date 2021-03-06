Python provides two very important features to handle any unexpected error in your Python programs and to add debugging capabilities in them.

# Exception Handling:  
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error. When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits. If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.
```sh
	try:
	    fh = open("testfile", "r")
	    fh.write("This is my test file for exception handling!!")
	except IOError:
	   print "Error: can\'t find file or read data"
	else:
		print "Written content in the file successfully"
```
```sh
Output: 
	Error: can't find file or read data
```					

# Assertions: 
Instead of waiting for a program to crash midway, you can also start by making an assertion in Python. We assert that a certain condition is met. If this condition turns out to be True, then that is excellent! The program can continue. If the condition turns out to be False, you can have the program throw an AssertionError exception.
 Here it is asserted that the code will be executed on a Linux system:
```sh
Code:
	import sys
	assert ('linux' in sys.platform), "This code runs on Linux only."
```
```sh
Output:
	Traceback (most recent call last):
    File "<input>", line 2, in <module>
    AssertionError: This code runs on Linux only.
```
