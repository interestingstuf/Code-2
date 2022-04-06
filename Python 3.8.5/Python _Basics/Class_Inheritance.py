

"""
class Person(object):
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
    def Display_Name(self):
        print(self.name)   
    def Display_Age(self):
        print(self.age)         

class Student(Person):
    def __init__(self, Name, Age,  Rollno, Score):
        #super().__init__(Name, Age,)
        Person.__init__(self, Name, Age)
        self.rollno = Rollno
        self.score = Score
    def Display_Rollno(self):
        print(self.rollno)
    def Display_Score(self):
        print(self.score)        
P = Person("Raj", 56)
P.Display_Name()  
P.Display_Age() 
S = Student("Parth", 11, 57, 99)
S.Display_Name()
S.Display_Age()
S.Display_Rollno()
S.Display_Score()
"""




"""

class Person(object):
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
    def Display_Name(self):
        print(self.name)   
    def Display_Age(self):
        print(self.age)         

class College_Student(Person):
    def __init__(self, Name, Age,  Rollno, Score):
        #super().__init__(Name, Age,)
        Person.__init__(self, Name, Age)
        self.rollno = Rollno
        self.score = Score
    def Display_Rollno(self):
        print(self.rollno)
    def Display_Score(self):
        print(self.score) 

class School_Student(College_Student):
    def __init__(self, Name, Age, Rollno, Score, SchoolN):
        super().__init__(Name, Age, Rollno, Score)
        #College_Student.__init__(self, Name, Age, Rollno, Score)
        self.SN = SchoolN
    def Display_School(self):
        print(self.SN)
Sn1 = School_Student("Little", 12, 123, 100, "Little School")   
Sn1.Display_School()     
Sn1.Display_Name()
"""
"""
 class Person(object):
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
    def Display_Name(self):
        print(self.name)   
    def Display_Age(self):
        print(self.age)        

class College_Student(Person):
    def __init__(self, Name, Age,  Rollno, Score):
        #super().__init__(Name, Age,)
        Person.__init__(self, Name, Age)
        self.rollno = Rollno
        self.score = Score
    def Display_Rollno(self):
        print(self.rollno)
    def Display_Score(self):
        print(self.score) 


class Professial(Person):
    def __init__(self, Name, Age, Employee_ID):
        super().__init__(Name, Age) 
        self.EID = Employee_ID
    def Display_EmployeeID(self):
        print(self.EID)
        
print("Professional")        
P = Professial("Raj", 56, 364324) 
P.Display_Name()
P.Display_Age()   
P.Display_EmployeeID()
print("Student")
S = College_Student("Parth", 11, 12, 99) 
S.Display_Name()
S.Display_Age()
S.Display_Rollno() 
S.Display_Score()   
"""

class Person(object):
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
    def Display_Name(self):
        print(self.name)   
    def Display_Age(self):
        print(self.age)        


class animal(object):
    def __init__(self, Ani_Name, Ani_Age):
        self.AN = Ani_Name
        self.AA = Ani_Age
    def Display_AniName(self):
        print(self.AN)
    def Display_Ani_Age(self):
        print(self.AA)

class home(Person, animal):
    def __init__(self, Name, Age, Ani_Name, Ani_Age, Home_Name):
        Person.__init__(self, Name, Age)   
        animal.__init__(self , Ani_Name, Ani_Age) 
        self.HN = Home_Name
    def Display_Home_Name(self):
        print(self.HN)


h = home("Raj", 56, "Litle", 13, "Little_Home")
print("Person Info")
h.Display_Name()
h.Display_Age()
print("Animal Info")
h.Display_AniName()
h.Display_Ani_Age()
print("Home Info")
h.Display_Home_Name()



#TODAY"S WORK ^^^^^^^^^^^^^^^^^^^^^^^^^^ Aug 24


