#Danh sach cac ban dang ki tham gia sinh nhat HIT
a = { "Malloc", "Alice", "Lumbu", "Karixi", "Murad"}
#Cac ban da checkin tai buoi sinh nhat
b = {"Alice", "Malloc", "Lumbu"}
for i in a:
    if i not in b:
        print(f'Danh sach cac ban chua check-in: {i}')
dem=0
for i in a:
    if i in b:
        dem+=1
print(f'Tong cong co tat ca {dem} da dang ki va da checkin.')
sort = list(a)
for i in range (len(sort)):
    for j in range (len(sort)-i-1):
        if sort[j] > sort[j+1]:
            sort[j],sort[j+1]=sort[j+1],sort[j]
print('{',', '.join(sort),'}')
