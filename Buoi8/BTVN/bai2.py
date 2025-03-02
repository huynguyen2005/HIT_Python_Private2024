class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
    def describe(self):
        print('Name: ' + self.name + " - yob: " + str(self.yob), end = '')

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    def describe(self):
        print('Student - ', end = '')
        super().describe()
        print(' - Grade: ' + self.grade)

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
    def describe(self):
        print('Teacher - ', end = '')
        super().describe()
        print(' - subject:  ' + self.subject)

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
    def describe(self):
        print("Doctor - ", end="")
        super().describe()
        print("- specialist: " + self.specialist)

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []
    def addPerson(self, person):
        self.people.append(person)
    def describe(self):
        for x in self.people:
            x.describe()
    def countDoctor(self):
        dem=0
        for i in self.people:
            if(isinstance(i, Doctor)):
                dem+=1
        return dem
    def sortAge(self):
        #Cach 1
        # for i in range(len(self.people)):
        #     for j in range(len(self.people)-1-i):
        #         if (2024-self.people[j].yob) > (2024-self.people[j+1].yob):
        #             self.people[j], self.people[j+1] = self.people[j+1],self.people[j]
        #Cach 2
        self.people.sort(key = lambda person: 2024-person.yob)
    def aveTeacherYearOfBirth(self):
        dem=0
        sum=0
        for i in self.people:
            if(isinstance(i,Teacher)):
                sum+=i.yob
                dem+=1
        return sum//dem

# 2(a)
student1 = Student("studentA", 2010, "7")
student1.describe()
teacher1 = Teacher("teacherA",1969,"Math")
teacher1.describe() 
doctor1 = Doctor("doctorA", 1945,"Endocrinologists")
doctor1.describe()
# 2(b)
print()
teacher2 = Teacher("teacherB", 1995, "History")
doctor2 = Doctor("doctorB", 1975, "Cardiologists")
ward1 = Ward("Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1.addPerson(doctor2)
ward1.describe()
print("số lượng doctor trong ward: ", ward1.countDoctor())
print("Danh sach sau khi sap xep: ")
ward1.sortAge()
ward1.describe()
print("trung bình năm sinh của các teachers trong ward: ", ward1.aveTeacherYearOfBirth())