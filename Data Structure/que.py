from multiprocessing import Queue
L = Queue()   
  
# Data is inserted in 'L' at the end using put()   
L.put(9)   
L.put(6)   
L.put(7)   
L.put(4)   

# get() takes data from the head of the Queue   
print(L.get())   
print(L)
print(L.get())   
print(L.get())   
print(L.get())   
