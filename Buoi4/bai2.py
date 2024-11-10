n = int(input("Nhap n= "))
a = [int(input()) for i in range(n)]
m = int(input("Nhap m= "))
b = [(input()) for i in range(m)]
c = []
for i in range(max(n,m)):
    if i < n:
        c.append(a[i])
    if i < m:
        c.append(b[i])
print(c)