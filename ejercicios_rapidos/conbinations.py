from itertools import product

x = [[1,2],[3,4]]

print(list(product(*x, repeat=0)))