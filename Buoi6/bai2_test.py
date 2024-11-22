word = input('Nhap 1 tu: ')
a = list(word)
dict = {}
for x in a:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
print(dict)