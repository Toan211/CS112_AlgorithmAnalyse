def perfect_binary_tree(data):
    middle = len(data)//2
    root = data[middle]
    lft_array = data[:middle]
    if len(lft_array) > 1:
        perfect_binary_tree(lft_array)
    elif len(lft_array) == 1:
        print(lft_array[0])
    rgt_array = data[middle+1:]
    if len(rgt_array) > 1:
        perfect_binary_tree(rgt_array)
    elif len(rgt_array) == 1:
        print(rgt_array[0])
    print(root)
data = []
try:
    while True:
        tmp = input()
        data.append(tmp)
except EOFError:
    pass
perfect_binary_tree(data)

import cProfile
from numpy import random
n = 10000
a= random.randint(100000000000000000, size=n)

data1 = []
data1.append(a)