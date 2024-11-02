import math
n = int(input("Nhap vao 1 so nguyen duong: "))
count = 0
for i in range(2,n):
    if (math.isqrt(i)**2==i):
        count+=1
print(count)