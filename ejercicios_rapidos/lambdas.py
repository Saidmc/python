def func(x):
    return x ** 2

for _ in range(4):
    print(func(_))

print('-'*20)

func2 = lambda x : x ** 2

for _ in range(9):
    print(func2(_))