# Module: 
A module is a piece of software that has a specific functionality. For example, when building a ping pong game, one module would be responsible for the game logic, and another module would be responsible for drawing the game on the screen. Each module is a different file, which can be edited separately.
	
# Writing modules: 
Modules in Python are simply Python files with a .py extension. The name of the module will be the name of the file. 

```sh 
Code: hello.py
def print_func( var ):
   print "Hello : ", var
   return
```
# The import Statement:
We can use any Python source file as a module by executing an import statement in some other Python source file. 
```sh 
# Import module hello
import hello

# Now you can call defined function that module as follows
hello.print_func("Jon Snow")
```
```sh 
Output: Hello : Jon Snow
```
# Writing packages: 
Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist. Each package in Python is a directory which MUST contain a special file called __init__.py. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.	
```sh 
Code: Arya.py
    def Arya():
       print "I'm Arya Stark"

Code: Jon.py
    def Jon():
        print "I'm Jon Snow"

Code: __init__.py
    from Arya import Arya
    from Jon import Jon
```    
After you add these lines to __init__.py, you have all of these classes available when you import the GOT package which is the parent folder for Arya.py, Jon.py and __init__.py.
```sh 
Code:
    import GOT
    
    GOT.Arya()
    GOT.Jon()
``` 
```sh 
Output: I'm Arya Stark
        I'm Jon Snow
```