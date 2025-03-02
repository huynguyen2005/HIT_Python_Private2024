# class Sinhvien:
    # def __init__(self,ten,msv,lop):
    #     self.ten = ten
    #     self.msv = msv
    #     self.lop = lop
    # def output(self):
    #     print("Name:",self.ten)
    #     print("Ma sinh vien:",self.msv)
    #     print("Lop:",self.lop)
#     @staticmethod
#     def tinhDiem(gpa,mon):
#         print("Tong diem cua ban la:",gpa*mon)

# NewSinhvien = Sinhvien("Nguyen Huy",2005,"12A2")
# NewSinhvien.ten = "Duc Thinh"
# NewSinhvien.output()
# Sinhvien.tinhDiem(3.2,9)
# class A:
#     def output(self):
#         print("hello Wolrd")
# class B:
#     def ouput(self):
#         print("Hello World")
# class C(A,B):
#     def ouput(self):
#         B().ouput()
# c = C()
# c.ouput()
from typing import List
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def _output(self):
        print("Name:",self.__name,"Age:",self.__age)
class Sinhvien(Person):
    def __init__(self, name, age, msv, diem):
        super().__init__(name, age)
        self.msv = msv
        self.diem = diem
    def output(self):
        super()._output()
        print("Ma sinh vien:", self.msv,",Diem:", self.diem)
class Lophoc:
    list = []
    list.append(Sinhvien("Huy", 19, 2023600834, 3.34))
    list.append(Sinhvien("Manh", 19, 2023600888, 3.34))
    list.append(Sinhvien("Vinh", 19, 2023600877, 3.34))
    def output(self):
        print(list)

lophoc = Lophoc()
lophoc.output()



            
