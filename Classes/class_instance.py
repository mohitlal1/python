class Hero:
    heroCount = 0

    def __init__(self, name, heroname):
        self.name = name
        self.heroname = heroname
        Hero.heroCount += 1
   
    def displayCount(self):
        print("Total Heroes %d" % Hero.heroCount)

    def displayHero(self):
        print("Name : ", self.name,  ", Hero Name: ", self.heroname)
        
emp1 = Hero("Tony Stark", "Iron Man")
emp2 = Hero("Steve Rogers", "Captain America")

emp1.displayHero()
emp2.displayHero()
print("Total number of Heroes %d" % Hero.heroCount)        