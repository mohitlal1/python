# A function with a function body containing single return expression statement is called Lambda funciton also Anonymous function.

x = lambda a : a + 10
print(x(5)) 



# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)
