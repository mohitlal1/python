from functools import reduce
    
def add(x, y):
    return x + y

list = [2, 4, 7, 3]
print(reduce(add, list))

print(reduce(lambda x, y: x + y, list))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))