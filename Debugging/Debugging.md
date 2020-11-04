# Debugging: 
Python has a built-in debugger called pdb. The easiest way to use pdb is to call it in the code you're working on.

Import pdb for python
```sh    
    import pdb
```
Put the set_trace where you want to start tracing
```sh
    pdb.set_trace()
```
- list(l): The list(l) command will show you the code line the Python interpreter is currently on.

- up ( p ) and down(d): These are the two commands needed to navigate through the call stack

- step(s) and next(n): These, help you continue the execution of the application line by line.

- break(b): The break(b) command allows you to set up new breakpoints without changing the code.

To execute the application with the debugger, use the command python -m pdb <python script>.
