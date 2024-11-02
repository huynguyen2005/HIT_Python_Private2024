def gt(n):
    temp=1
    for i in range(1,n+1):
        temp*=i
    return temp

x = int(input("Nhap x= "))
n = int(input("Nhap n= "))
sum = 1
mau=1
tu=1
if n==0:
    print(sum)
else:
    for i in range(1,n+1):
        tu = pow(x,i)
        mau = gt(i)
        sum+= (tu/mau)
    print(sum)


