
# def helloworld(name,age):
#     return name,age

# name,age=helloworld(name='Huy', age=25)
# print(name)
# print(age)

# def giaithua(n:int):
#     '''
#     Ham tinh giai thua tu 1-n
#     Args:
#         n(int): so n
#     '''
#     temp = 1
#     for i in range(1,n+1):
#         temp*=i
#     return temp

# print(giaithua(3))

# ave = lambda a,b,c: (a+b+c) / 3
# print(ave(3,5,7))
# '''
# tuong duong voi
# def ave(a,b,c):
#     return (a+b+c)/3
# '''

# def nam_nhuan(year:int) -> bool:
#     if year%100==0:
#         if year%400==0:
#             return True
#         return False
#     elif year%4==0:
#         return True
#     return False

# years=[2007,2004,2008,1979]
# for year in years:
#     print(nam_nhuan(year))

def check(str):
    b = str.split(' ')
    c = []
    max = len(b[0])
    temp = b[0]
    index_max = 0

    for i in range(1,len(b)):
        if len(b[i])>max:
            max = len(b[i])
            temp=b[i]
            index_max = i

    c.append((temp,index_max))

    min = len(b[0])
    temp1 = b[0]
    index_min = 0
    for i in range(1,len(b)):
        if len(b[i])<min:
            min = len(b[i])
            temp1=b[i]
            index_min=i
    c.append((temp1,index_min))

    print(tuple(c))
    return {
        'dai nhat' : index_max,
        'ngan nhat' : index_min
    }

n = input('Nhap 1 cau: ')
new_dict = check(n)
print(new_dict)