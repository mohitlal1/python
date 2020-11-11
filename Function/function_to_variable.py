def Hulk():
    print('Hulk Smash')

def Thor():
    print('Bring me Thanos')
 
sorts = []
 
sort = Hulk # assign function to a variable
sorts.append(sort)
sort = Thor # assign function to a variable
sorts.append(sort)
 
for i in range(len(sorts)):
    sorts[i]()