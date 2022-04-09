from random import randint

data = set()

n = 0

while n < 20:
    r = randint(0, 25)
    print(f'r: {r}')
    if r not in data:
        n += 1
        data.add(r)


print(len(data))
print(data)