# x = lambda y : y + 12
# print(x(4))


def my_fun(f):
    return lambda g: g * f

my_doubler = my_fun(2)
my_tripler = my_fun(3)

print(my_doubler(20))
print(my_tripler(30))