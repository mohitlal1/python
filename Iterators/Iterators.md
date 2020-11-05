# Iterators:
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

The for loop actually creates an iterator object and executes the next() method for each loop.

# Infinite Iterators

It is not necessary that the item in an iterator object has to be exhausted. There can be infinite iterators (which never ends). 
