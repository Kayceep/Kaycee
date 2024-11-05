# class Computer:
#     def __init__(self):
#         self.name = "kayceep"
#         self.age = 25
    
#     # to update the age
#     def update(self):
#         self.age = 40


#     # to compare two objects
#     def compare(self, other):
#             if self.age == other.age:
#                 return True
#             else:
#                 return False
            

# c1 = Computer()
# c2 = Computer()

# # c1.name = "prince"

# print(c1.name)
# print(c1.age)

# c1.update()
# print(c1.age)

# print(c2.name)
# print(c2.age)

# if c1.compare(c2):
#      print("same")
# else:
#      print("not")



# class Car:
#      wheels = 4
#      def __init__(self):
#           self.name = "volvo"
#           self.speed = "10km/h"


# c1 = Car()
# c2 = Car()


# c1.name = "Honda"
# Car.wheels = 25

# print(c1.name, c1.speed, c1.wheels)
# print(c2.name, c2.speed, c2.wheels)




class Student:
    school_name = "Divine Grace"   #static/class variable
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def ave(self): # instance method
        return (self.m1 + self.m2 + self.m3) / 3
    