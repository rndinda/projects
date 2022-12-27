# def greet_user():
#     print('Hey! there')
#     print("Welcome")


# greet_user()

# PARAMETERS
# def my_name(name):
#     print('My name is ' + name)
# my_name("Rose")

from inspect import Arguments


#ABITRARY ARGUMENTS
#-when you have no idea the number of arguments to be passed

# def my_things(*items):
#     print(f"Thats my  {items[1]}")

# my_things('pen','cup','bike')

#KEY WORD ARG AND ABITRARYKEY WORD ARG
#-ARGUMENTS ARE Passed as adictionary

# def name(**majina):
#     print('My last name is '+majina['lname'])


# name(fname='Rose',lname='Ndinda')


#EMOJI CONVERTER FUNCTION

#def emoji_converter():
# age = int(input('Age: '))
# print(age)


def my_me():
    x = 13
    print(x)


x = 30
my_me()


print(x)