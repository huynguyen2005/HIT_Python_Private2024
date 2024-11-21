#Khoi tao tu dien
sinhvien = {
    '2023600000' : 'Luong The Vinh',
    '2021789999' : 'Dang Huu Long',
    '2019001001' : 'Nguyen Duc Thinh',
    '2026330333' : 'Nguyen Van Manh',
    '2020601001' : 'Nguyen The Vinh'
}
#In danh sach tu dien ra man hinh
print("Danh sach tu dien:")
for id, name in sinhvien.items():
    print(f"id: {id}, name: {name}")
#ktra xem co sinh vien co ma... co trong tu dien hay khong
ktra = 2020601001
if ktra in sinhvien:
    print("SINH VIEN: id: {id}, name: {name}")
else:
    print("Khong co!!!")
