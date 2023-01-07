#import modules1
#print(modules1.kgs_to_lbs(70))

#from modules1 import kgs_to_lbs

#print( kgs_to_lbs(70))



def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    return max