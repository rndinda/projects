class School_data:

    def __init__(self,name,place,age):
        self.name = name
        self.place = place
        self.age = age
        self.intro = "My name is" + ' '+ name + "," + 'from'+' ' + place


    def about_student(self):
        return f'I am {self.name}, from {self.place}'
        # return 'Am {} years from {}'.format(self.name,self.place)

    
class Teachers(School_data):
    def __init__(self, name, place,age,subject):
        super().__init__(name,place,age)
        self.subject = subject


    def tr_intro(self):
        return f'My name is {self.name} from {self.place} and i teach {self.subject}'


    @classmethod #Tunachukua data ya walimu if entered in kama string
    def from_string(cls, tr_str):
        name,place,age,subject = tr_str.split('-')
        return cls(name,place,age,subject)
        """this class method up here:->when data is filled inform of a string,
        it takes the data and splits it into various variables"""




student_1 = School_data("Mwesh","Malindi",20)
# print(student_1.intro)
# print(student_1.about_student())

tr_1 = Teachers("Tom",'Kitui',30,'Kiswahili')
# print(tr_1.subject)
# print(tr_1.tr_intro())

tr_str1 = 'Lucy-Malindi-49-BS'#the tr_str variable
new_trstr1 = Teachers.from_string(tr_str1)#This can
print(new_trstr1.tr_intro())