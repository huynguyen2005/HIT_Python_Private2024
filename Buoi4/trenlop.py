# a = [1,3,5,7,9]
# for i in range(len(a)):
#     print(a[i]," ")
# b = [2*i for i in range(1,51)]
# for i in range(len(b)):
#     print(b[i])
# n = int(input("Nhap n= "))
# c = []
# for i in range(n):
#     element = int(input("Nhap phan tu thu {i}: "))
#     c.append(element)
# sumc=sum(c)
# print(sumc)
# n = int(input("Nhap n= "))
# a = [int(input()) for i in range(n)]
# print("Mang sau khi sap xep")
# a.sort()
# for i in range(n):
#     print(a[i])
# print("max a = ",max(a))
# print("min a = ",min(a))
# dem=0
# for i in range(n):
#     if(a[i]%2==0):
#         dem=i
#         break
# print("vi tri chan dau tien: ", dem)
# dem1=0
# for i in range(n):
#     if(a[i]==3):
#         dem+=1
# if dem1==0:
#     print("Mang chua so 3")
# else:
#     print("Mang khong chua so 3")
# k = int(input("Nhap vi tri muon chen: "))
# a.insert(k,11)
# a = [x for x in a if x%2!=0]
# print(a)
# m = int(input("Nhap m= "))
# b = [int(input()) for i in range(m)]
# b = b*2
# b.reverse()
# c = b + a
# print(c)
m = int(input("Nhap m= "))
b = [int(input()) for i in range(m)]
for i in b[::-1]:
    if(i%2==0):
        b.remove(i)
print(b)