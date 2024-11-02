# a = 3
# b = 10
# condition = a>b
# print(condition)
# print(type(condition))
# if condition:
#     print("hello")
# else:
#     print("no hello")
# duyet array
# array = [1,2,3,4,5,6,'a','b','c']
#print(len(array))
#for i in array:
#   print(i)
# duyet range
#cach1
#for i in range(0,10,1):
#    print(i)

#cach2
#print(list(range(1,10,2)))

#for i in range(0,9,1):

# index = 0
# for i in range(len(array)):
#     print(index, array[i])
#     index +=1

array = [1,2,3,4,5,6,'a','b','c']
for index,i in enumerate(array):
    print(i)
    print(f'index={index}, value={i}')

# L1 = [1,2,3,4,5]
# L2 = ['a','b','c','d']
# zip_L1L2 = zip(L1,L2)
# print(list(zip_L1L2))
# for index,(i,j) in list(zip_L1L2):
#     print(index,i,j)