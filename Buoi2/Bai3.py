a = "Chao mung den CLB Tin Hoc HIT"
print(a)
b = "CLB Tin Hoc HIT truc thuoc Khoa CNTT  - 10 diem"
print(b)
c = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
temp=[]
temp1=[]
for ki_tu in c:
    if ki_tu.isupper():
        temp.append(ki_tu)
    else:
        temp1.append(ki_tu)
print("Nhung ky tu in hoa la: ", " ".join(temp))
print("Nhung ky tu in thuong la: ", " ".join(temp1))
ktra = "CNTT" in c
if(ktra):
    print("YES")
else:
    print("NO")
tem = ""
for ki_tu in c:
    if ki_tu.isupper():
        tem+=ki_tu.lower()
    else:
        tem+=ki_tu.upper()
print(tem)
