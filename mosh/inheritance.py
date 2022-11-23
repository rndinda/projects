# # class Mammal:
# #     def walk(self):
# #         print('walk')


# # class Dog(Mammal):
# #     def bark(self):
# #         print("They bark")


# # class Cat(Mammal):
# #     def meaow(self):
# #         print('meaow meaow')

# # dog = Dog()
# # dog.walk()
# # dog.bark()

# # cat = Cat()
# # cat.meaow()
# #  cat.walk()
# # class Employee:
# #     #no_of_emps = 0
# #     raise_amount = 1.04

# #     def __init__(self,first,last,pay):
# #         self.first = first
# #         self.last = last
# #         self.pay = pay
# #         self.email = first + '.' + last + '@company.com'

# #         #Employee.no_of_emps += 1

# #     def full_name(self):
# #         return '{} {}'.format(self.first,self.last)


# #     def apply_raise(self):
# #         self.pay =int(self.pay * self.raise_amount)


# # class Developers(Employee):
# #     pass


# # employee_1 = Developers('Rose','Ndinda',60000)
# # employee_2 = Developers('Rita','Mwende',70000)


# # print(employee_1.pay)
# # employee_1.apply_raise()
# # print(employee_1.pay)

# # employee_1.raise_amount = 1.78
# # print(employee_2.pay)
# # employee_2.apply_raise()
# # print(employee_2.pay)
# # print(employee_1.__dict__)
# # print(employee_2.__dict__)
# # print(Employee.no_of_emps)// ThE number of employees
# # print(employee_1.full_name())
# # print(employee_2.full_name())

# # print(employee_1.email)
# # print(employee_2.email)

# # #THESE DO THE SAME THING
# # print(employee_1.full_name())
# # print(Employee.full_name(employee_2))



# class Employee:
#     #no_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#         #Employee.no_of_emps += 1

#     def full_name(self):
#         return '{} {}'.format(self.first,self.last)


#     def apply_raise(self):
#         self.pay =int(self.pay * self.raise_amount)

    
# #clasmethods,take class as parameter 
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
#         return amount


#     @classmethod # an alternative contructor/additional constructor  -watu wanapenda kuziandika na from
#     def from_string(cls,emp_str):
#         first ,last,pay = emp_str.split('-')
#         return cls(first,last,pay)

#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True


# import datetime
# my_date = datetime.date(2022, 11, 15)

# print(Employee.is_workday(my_date))

# #emp_3 = Employee("Ndinda",'rose',70000)
# #print(emp_3.full_name())
# #Employee.set_raise_amount()

# # emp_str1 = 'John-Mwanyolo-80000'
# # emp_str2 = 'Lucy-Nduva-80000'

# # new_emp2 = Employee.from_string(emp_str2)
# # new_emp3 = Employee.from_string(emp_str1)
# # print(new_emp2.full_name())
# # print(new_emp2.pay)
# # print(new_emp2.email)
# # print(new_emp3.last)
# # print(new_emp3.email)

# class Developers(Employee):#Subclasses DEVELOPERS is a subclass of the class Employee

#     raise_amount = 1.10
#     # adding a new parameter for the developers class
#     def __init__(self, first, last, pay,language ):
#         super().__init__(first, last, pay)
#         self.language = language
# # print(employee_1.email)
# # print(employee_2.pay)
# #print(help(Developers)) show method resolution order                                                   


# class Manager(Employee):
#     def __init__(self,first, last, pay,employees = None):
#         super().__init__(first,last,pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees

#     #adding employees
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     #kutoa employees
#     def remove_emp(self, emp):
#         #self.emp = emp
#         if emp in self.employees:
#             self.employees.remove(emp)

    
#     def print_emps(self):
#         for emp in self.employees:
#             print(">", emp.full_name())



# dev1 = Developers("Ndinda",'rose',70000 , 'Python')
# dev2 = Developers("NDegs",'waweru',90000,'java')
# dev3 = Developers('Tim','Nduva',95000,'Php')
# dev4 = Developers('Mavu','Nduva',98000,'html')

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# print(dev1.language)

# mng1 = Manager("robby",'Muthe',90000, [dev1])#ekw dev1 kwa []
# mng2 = Manager("Nduva",'Raph',80000, [dev3,dev2])
# # print(mng1.email)
# #mng1.print_emps()
# mng2.print_emps()
# mng2.add_emp(dev4)
# print(mng2.email)
# mng2.print_emps()
# print('Hey give some space')
# mng2.remove_emp(dev3)
# mng2.print_emps()

#build in functions
#isinstance() and issubclass()
# print(isinstance(mng2, Developers))
# print(issubclass(Developers, Employee))


#MAGIC /SPECIAL METHODS
# class Employee:
#     #no_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#         #Employee.no_of_emps += 1

#     def full_name(self):
#         return '{} {}'.format(self.first,self.last)


#     def apply_raise(self):
#         self.pay =int(self.pay * self.raise_amount)


#     def __repr__(self):#developers
#         return "Employee('{}' , '{}' ,'{}')".format(self.first,self.last,self.pay)# creating a string to recreate the object

    
#     def __str__(self):
#         return '{} - {}'.format(self.full_name(), self.email)


#     def __add__(self, other):
#         return self.pay + other.pay

    
#     def __len__(self):
#         return len(self.full_name())



# emp_4 = Employee('Njenje','Ndis',80000)
# emp_5 = Employee('mumbe','spencer',86000)

# # print(repr(emp_4))
# # print(str(emp_4))

# #print(emp_4 + emp_5)

# print(len(emp_5))
# print(len(emp_4))

#property decorators
class Employee:
    #no_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
        

    @property
    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first= first 
        self.last = last

    
emp_4 = Employee('Njenje','Ndis',80000)
emp_5 = Employee('mumbe','spencer',86000)

emp_4.first = 'Agatha'
emp_5.full_name = 'Carol Mumbe'
print(emp_5.full_name)

print(emp_5.first)
print(emp_5.email)
print(emp_5.full_name)





























