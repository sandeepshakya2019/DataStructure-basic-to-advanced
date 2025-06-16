class Student:
    def __init__(self, name, age, presentClass):
        self.__name = name
        self.__age = age
        self.__presentClass = presentClass
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name