import random

# for i in range(8):
#     print(random.random())

# for i in range(3):
#     print(random.randint(10,40))

# members = ['Rose','Rita','Robby']
# leader = random.choice(members)
# print(leader)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice_1 = Dice()
print(dice_1.roll())