#OOP
#best practice is to access property through the methods 
# class Animal:
#     blood_type = 'hot'
#     count = 0

#     def __init__(self, name, lifespan, count):
#         self.name = name
#         self.lifespan = lifespan
#         self.count += 1
#     def print_animal(self):
#         print(f"I am a {self.name} I will die in {self.lifespan}")


# cat = Animal("cat", 12)
# dog = Animal("dog", 14)

# cat.print_animal()
# #here we are targeting a single property for an object
# cat.blood_type = 'cold'
# print(cat.blood_type)
# print(dog.blood_type)
# #output: cold
# # hot

# #if we need to change the class property then...
# Animal.blood_type = 'cold'

# print(cat.blood_type)
# print(dog.blood_type)


class Polygon:
    def __init__(self, number_of_sides):
        self.num_sides = number_of_sides

    def display(self):
        print(f"I have {self.num_sides} sides")
    

#inheriting polygon
class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)


t = Triangle()
t.display()

class Rectangle(Polygon):
    def __init__(self, length, bredth):
        self.length = length
        self.bredth = bredth
        super().__init__(4)

    def calc_area(self):
        calc = self.length * self.bredth
        return calc

r = Rectangle(3,4)
r.display()
print(r.calc_area())
    
        

    
