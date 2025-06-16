# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print(f"{self.name} is running at age {self.age}")

# class Male(People):
#     def __init__(self, name, age, isFather, isEmployed):
#         super().__init__(name, age)
#         self.isFather = isFather
#         self.isEmployed = isEmployed
#         self.salary = 0

#     def setSalary(self, salary):
#         if self.isEmployed:
#             self.salary = salary
#             print(f"{self.name} has a salary of rs {self.salary}")
#         else : print(f"{self.name} you are not employed")

# m1 = Male("Sandeep", 24, False, True)
# m1.run()
# m1.setSalary(500000)

class A: pass
class E: pass
class B(E): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
