#  Unpacking Arbitrary Number of variables: 
language=("hello","namaste","Bonjour","Hola","Konnichiwa")

#assign first elements to english and remaining to other
english,*other=language

print("english ={}, other={}".format(english,other))

#Unpacking selective elements:
#assign value to english hindi japanese discarding remaining
english,hindi,_,_,japanese=language
print("english={}, hindi={}, japanese={}".format(english,hindi,japanese))


#assign value to english and hindi
english,hindi,*_=language
print("english={}, hindi={}".format(english,hindi))


#unpacking multiple dictionaries into single
x={1:"one",2:"two"}
y={3:"three",4:"four"}
z={5:"five",6:"six",7:"seven"}

a={**x,**y,**z,8:"eight",9:"nine"}
print(a)


x=[0,1,2,3]
y=[4,5,6,7,8,9]
#unpacking multiple list to one
z=[*x,*y]
print(z)

x={1,2,3,4}
y={9,8,7}
#unpacking multiple sets to one
z={*x,*y}
print(z)


def func(a,b,c,d):
  print("a={},  b={},  c={},  d={}".format(a,b,c,d))

#passing unpacked variable to function
x=(1,2,3,4)
func(*x)

y=[11,12,13,14]
func(*y)

z="ABCD"
func(*z)

#passing unpacked dictionary to function
x1={'a':1,'b':2,'c':3,'d':4}
func(**x1)

y1={'a':"A",'b':"B",'c':"C",'d':"D"}
func(**y1)

