#class Point:
 #   def __init__(self,x,y):
  #      self.x = x
   #     self.y = y
#
 #   def move(self):
  #      print('if you move, i move')
#
#point = Point(10,20)
#print(point.x)

class Person:

    def __init__(self,name):
        self.name = name

    def talk(self):
        print('I can talk')

    def say(self):
        print(f"i am {self.name}")

pp = Person('rita')
pp.name = 'Rose'
print(pp.name)
pp.talk()
pp.say()

