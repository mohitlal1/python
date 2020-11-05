def try_to_change(x,str):
    x = x + 1
    str = " my message inside function "

a = 1
s = " my message outside function "

try_to_change(a,s)
print(a)
print(s)