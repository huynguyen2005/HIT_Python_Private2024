a = input("Nhap data: ")
data = list(a.split(',')) 

names, ages, scores, cities = [], [], [], []

for x in data:
    if 'name=' in x:
        names.append(x.split('name=')[1])  
    elif 'age=' in x:
        ages.append(x.split('age=')[1])  
    elif 'score=' in x:
        scores.append(x.split('score=')[1]) 
    elif 'city=' in x:
        cities.append(x.split('city=')[1]) 

new_dict = {
    'name': names,
    'age': ages,
    'score': scores,
    'city': cities
}

print(new_dict)
