n = int(input("Nhap so luong sinh vien: "))
arr1 = []
arr2 = []
arr3 = []
for i in range(n):
    name = input("Nhap ten: ")
    arr1.append(name)
    b1 = int(input("Diem bai 1: "))
    b2 = int(input("Diem bai 2: "))
    sum = b1+b2
    arr2.append(sum)
    if(sum>=190):
        arr3.append("Xuat sac")
    elif(sum>=150):
        arr3.append("Gioi")
    elif(sum>=100):
        arr3.append("Kha")
    else:
        arr3.append("Yeu")
for i in range(n):
    print(i+1, arr1[i], arr2[i], arr3[i])
