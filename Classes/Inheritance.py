class Hero:
    def __init__(self, name, heroname):
        self.name = name
        self.heroname = heroname
  
    def printname(self):
        print(self.name, self.heroname)

class Avenger(Hero):
    def __init__(self, name, heroname, power):
        super().__init__(name, heroname)
        self.power = power
        
    def welcome(self):
        print("Welcome", self.name, self.heroname, " have power of ", self.power)

x = Avenger("Tony Stark", "Iron Man", "Iron Suit")
x.welcome()
			