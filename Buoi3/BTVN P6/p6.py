import math
def binary(x):
    if x<0:
        return 0
    else:
        return 1
def sigmoid(x):
    return 1/(1+math.exp(-x))
def elu(x):
    if(x<0):
        return 0.01*(math.exp(x)-1)
    else:
        return x
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
x = input("Nhap x = ")
if(is_number(x)==False):
    print("x must be a number")
else:
    x = float(x)
    while True:
        name = input("Nhap ten kich hoat ( binary | sigmoid | elu ): ")
        if(name=="binary" or name=="sigmoid" or name=="elu"):
            break
        else:
            print(name, "is not supported")
if(name=="binary"):
    print(name, ": f(",x,") = ", binary(x))
elif(name=="sigmoid"):
    print(name, ": f(",x,") = ", sigmoid(x))
else:
    print(name, ": f(",x,") = ", elu(x))