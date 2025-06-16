# class Empty:
#     pass

# e = Empty()
# print(e.__sizeof__())       # Outputs: 16
# import sys
# print(sys.getsizeof(e))     # Outputs: 32


class Hero:
    def __init__(self, name, health):
        self.name = name;
        self.health = health;
        self.level = 1
    
    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level
    
    def defense(self):
        print(f"{self.name} is defensing at health {self.health}")

    def attack(self):
        print(f"{self.name} is attacking at health {self.health}")

    
h = Hero("sandeep", 100)
print(h.__sizeof__())

print(object.__init__   )