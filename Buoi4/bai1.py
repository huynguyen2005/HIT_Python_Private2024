k = int(input("Nhap so phan tu k: "))
a = [int(input()) for i in range(k)]
n = int(input("Nhap n= "))
m = int(input("Nhap m= "))
if(n*m>k):
    print("Ta khong the xay dung ma tran duoc")
else:
    mt = []
    index=0
    for i in range(n):
        hang = []
        for i in range(m):
            hang.append(a[index])
            index+=1
        mt.append(hang)
    print(mt)
