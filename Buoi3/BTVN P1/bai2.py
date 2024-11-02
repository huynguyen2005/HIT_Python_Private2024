def gt(n):
    temp=1
    for i in range(1,n+1):
        temp*=i
    return temp

n = int(input("Nhap n= "))
sum = 0
for i in range(1,n+1):
    sum+= (1/gt(i))
print(sum)