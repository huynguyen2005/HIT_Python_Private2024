dict = eval(input("Nhập dictionary: "))
ndict = {}
for key, val in dict.items():
    if val in ndict:
        print("None")
    ndict[val] = key
print(ndict)