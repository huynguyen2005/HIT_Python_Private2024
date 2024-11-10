import re
str = input("Nhap vao 1 chuoi email: ")
kt = re.search("^\w+@gmail\.\w+$",str)
if kt:
    print("Valid")
else:
    print("Invalid")