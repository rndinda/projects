# class Point:
#     def move(self):
#         print('Move')

#     def draw(self):
#         print('draw')

# #objects
# point1 = Point()
# point1.draw()
# point1.h = 20
# print(point1.h)

# class Person:
#     def __init___(self,name):
#         self.name = name

#     def talk():
#         print("SAy something to me")

# pepe = Person()
# pepe.talk()



# class Person:
#     def __init__(self,name):
#         self.name = name

#     def talk(self):
#         print('say something')

# pep = Person('John')
# print(pep.name)
# pep.talk()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def calling(self):
#         print(f'Hey are you calling {self.name}')

#     def miaka(self):
#         print(f"Type your age here: {self.age}")
    
# poppy = Person('Rita',30)
# poppy.calling()
# poppy.miaka()

#INHERITANCE

# class Mammal:
#     def walk(self):
#         print("They love to walk")
    
# class Dog(Mammal):
#     def bark(self):
#         print('woo woo woo')

#     def tail(self):
#         print('It has a tail')


# class Cat(Mammal):
#     def meaow(self):
#         print("Meao meao")


# dog1 = Dog()
# dog1.bark()

# cat1 = Cat()
# cat1.meaow()



# __str__ vs __repr__

class Food:
    def __init__(self,size,price):
        self.size = size
        self.price = price

    def __str__(self):
        return f"The {self.size} one is {self.price}"

    def __repr__(self):
        return '__repr__ is for  debbugging'

pi = Food('small',20)
print(str(pi))
print(repr(pi))













