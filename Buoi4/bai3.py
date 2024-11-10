n = int(input("Nhap len mang 1: "))
a = [int(input()) for i in range(n)]
m = int(input("Nhap len mang 2: "))
b = [int(input()) for i in range(m)]
c = []
for i in range(n):
    if (a[i] in b) :
        c.append(a[i])
print(c)