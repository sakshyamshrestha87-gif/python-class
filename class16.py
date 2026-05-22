# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,3,5,7,11]
# x1 = [6,7,8,9,10]
# y1 = [2,3,5,7,11]

# plt.plot(x,y, marker='o',linestyle='--',color='b',label='Prime Number')
# plt.plot(x1,y1, marker='o',linestyle='-',color='r',label='Number')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.title('Priime Number Plot')
# plt.legend()
# plt.show()

# square = lambda x:x**2
# print(square(5))

# add = lambda a,b: a + b
# print(add(3,4))

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x:x**2, numbers))

# numbers = [1,2,3,4,5,6,8,9]

# def cal(x):
#     result1 = x + 1
#     result2 = result1 **2
#     return result2

# value = list(map(cal,numbers))q
# print(value)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = list(filter(lambda x:x % 2 == 0, numbers))
# print(even_numbers)


# from functools import reduce
# numbers = [1,2,3,4,5]
# sun = reduce(lambda x, y : x + y, numbers)
# print(sun)

# import os
# current_dir = os.getcwd()
# files = os.listdir(current_dir)
# print(files)

# import random
# random_number = random.randint(1, 10)
# my_list = [1,2,3,4,5]
# random.shuffle(my_list)
# print(random.shuffle)


import math
sqrt_value = math.sqrt(25)
factorial_value = math.factorial(5)