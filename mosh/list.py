#EXCEPTIONS
try:
    age = int(input('Age: '))
    income = 30000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('cant with zero')
except ValueError:
    print('In numbers please')

