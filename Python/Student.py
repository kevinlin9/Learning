class Student:
    
    def __init__(self, fname, mi, lname, age, sname, lv, gpa, **kwargs):
        self.first_name = fname
        self.middle_initial = mi
        self.last_name = lname
        self.age = age
        self.school_name = sname
        self.grade_level = lv
        self.gpa = gpa

        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

    """
    Instantiation Method
    """

def new_student():
    """ returns student """
    first_name = input("What is your first name? ")
    middle_initial = input("What are your middle initials? ")
    last_name = input("What is your last name? ")
    age = input("How old are you? ")
    school_name = input("What school do you go to? ")
    grade_level = input("What grade level are you in? (if you are a college student, add the number of years to 12 for your grade) ")
    gpa = input("What grade or gpa do you have? ")
    return Student(first_name, middle_initial, last_name, age, school_name, grade_level, gpa)
def showInfo(student):
    print(student.first_name)
    print(student.middle_initial)
    print(student.last_name)
    print(student.age)
    print(student.school_name)
    print(student.grade_level)
    print(student.gpa)

me = new_student()
showInfo(me)
