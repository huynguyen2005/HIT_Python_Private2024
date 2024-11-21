a = input("Nhap cac phan tu cua tuple A: ")
A = tuple(map(int,a.split(',')))
b = input("Nhap cac phan tu cua tuple B: ")
B = tuple(b.split(','))
tbc = 0
for i in range(len(A)):
    tbc+=A[i]
sum=tbc/len(A)
dem=0
for i in range(len(A)):
    if A[i]>sum:
        dem+=1
print('So luong cac phan tu lon hon trung binh cong trong tuple A: ',dem)
C = tuple(x for x in A if x%2==0)
D = tuple(x for x in A if x%2!=0)
print(f'Tuple con thu nhat: {C}')
print(f'Tuple con thu hai: {D}')
k = input("Nhap vao 1 ki tu: ")
count1=0
for i in B:
    if k==i:
        count1+=1
print(f'so lan xuat hien cua {k} trong {B} la: {count1}')
result = tuple(i for i in B if len(i)>=5)
print(f'Cac phan tu cua tuple B co do dai lon hon hoac bang 5 ki tu la: {result}')
E =tuple((A[i],B[i]) for i in range (min(len(A),len(B))))
print(f'tuple moi khi gop A+B: {E}')