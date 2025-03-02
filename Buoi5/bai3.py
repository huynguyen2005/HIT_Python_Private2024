thisdict = {}
n = int(input('Nhap so luong phan tu cua dictionnary: '))
for i in range(n):
    key = input('Nhap key: ')
    value = eval(input('Nhap value: '))
    thisdict[key]=value
print(thisdict)
newdict = {}
for key,value in thisdict.items():
    if value in newdict:
        print('None')
    newdict[value]=key
print(newdict)