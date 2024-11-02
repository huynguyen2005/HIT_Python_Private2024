m = int(input("Nhap so luong dong vat: "))
arr1 = []
arr2 = []
sum = 0
dem = 0
index = 0
for i in range(m):
    name = input("Nhap ten: ")
    arr1.append(name)
    eat = int(input("Nhap khoi luong thuc an: "))
    arr2.append(eat)
for i in range(m):
    print(arr1[i]," ",arr2[i])
for i in range(m):
    if arr2[i] > 100:
        break
    elif arr2[i] >= 5:
        sum+=arr2[i]
print("Tong luong thuc an ma tat ca cac loai can moi ngay: ", sum) 
maxx = arr2[0]
for i in range(1,m):
    if arr2[i] > maxx:
        maxx = arr2[i]
        index = i 
print("Loai an nhieu thuc an nhat ", arr1[index])
for i in range(m):
    if arr2[i]<5:
        print("Loai so ", i, "an it nhat")
    else:
        dem+=1
if(dem==m):
    print("Khong co")