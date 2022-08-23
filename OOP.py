class Student:
    no_of_students = 0
    def __init__(self, name, age=0, courses="None"): #.self hiya lmota3araf 3liha momkin nbda bli bghit
        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.no_of_students += 1

    def describe(self):
        #is two methode to do that
        print(f"my name is {self.__name} and my age is {self.__age} and I have experience in this courses {self.__courses}")
        #print("my name is {} and my age is {} and I have experience in this courses {}".format(self.name, self.age, self.courses))
    def get_name(self): #getter function
        return self.__name

    def set_name(self, new_name): #setter function
        self.__name = new_name

    def get_age(self): #getter function
        return self.__age

    def set_age(self, new_age): #setter function
        self.__age = new_age

    def is_old (self,num):
        if self.__age <= num:
            print("Student is not old")
        else:
            print("Student is old")

student_1 = Student("Ali", 28, ['javascript', 'css', 'c++'])
student_2 = Student("Said", 28, ['css', 'java'])
#student_2.describe()
#student_2.is_old(50)
#print(student_2.get_name())
#student_1.change_name("Omar")
#print(student_1.get_name())

#print(student_2.get_name())


