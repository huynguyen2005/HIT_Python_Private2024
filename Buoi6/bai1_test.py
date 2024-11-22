x = int(input('Nhap x= '))
n = int(input('Nhap n= '))
tu=1
mau=1
sum=1
for i in range(n+1):
    if(i==0):
        sum=1
    else:
        tu=tu*x
        mau=mau*i
        sum+=tu/mau
print(f'e mu {x} = {sum}')