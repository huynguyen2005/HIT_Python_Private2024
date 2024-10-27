a = int(input("a="))
b = int(input("b="))
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)
print(a, "^", b, "=", a**b)
print(a, "%", b, "=", a%b)
if(a>b):
    print(a,">",b)
elif(a<b):
    print(a,"<",b)
else:
    print(a,"=",b)
print(a, "AND", b, "=", a and b)
print(a, "OR", b, "=", a or b)
print(a, "XOR", b, "=", a ^ b)
print(a, "NOT", b, "=", not (a==b))
print(a, "DICH PHAI 5 bit ", a>>5)
print(a, "DICH TRAI 5 bit ", a<<6)
temp = ""
while(a>0):
    tem = a%2
    temp += str(tem)
    a=a//2;
print(temp)