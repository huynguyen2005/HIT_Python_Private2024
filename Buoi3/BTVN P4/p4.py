import re
str = input("Nhap vao 1 chuoi email: ")
kt = re.search("^\w+@gmail\.\w{2,}$",str)
if kt:
    print("Valid")
else:
    print("Invalid")