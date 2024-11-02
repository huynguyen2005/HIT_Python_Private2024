bai = input("Nhap bai ban muon lam: ")
array = ['sin', 'cos', 'sinh', 'cosh']
for bai in array:
    if bai == 'sin':
        n = int(input("n= "))
        x = int(input("x= "))
        tu = 1
        mau = 1
        sum = 0
        for i in range(1,2*n+2):
            if (i%2) != 0 : 
                tu = tu * x
                mau = mau*i
                sum += pow(-1,n)*tu/mau
            else:
                tu = tu*x
                mau = mau*i
        print(sum)
            