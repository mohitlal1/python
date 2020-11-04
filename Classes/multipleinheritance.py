class Hero:
    def show_Hero(self):
        print("This is our Hero:")

class Testing(Hero):
    TestingName = ""

    def show_Testing(self):
        print(self.TestingName)
 
class Alias(Hero):
    AliasName = ""

    def show_alias(self):
        print(self.AliasName) 
 
# Sprint class inherited from Testing and Hero classes
class SuperHero(Testing, Alias):
    def show_parent(self):
        print("Name :", self.TestingName)
        print("Alias :", self.AliasName)

s1 = SuperHero()  # Object of Sprint class
s1.TestingName = "Tony Stark"
s1.AliasName = "Iron Man"
s1.show_Hero()
s1.show_parent()