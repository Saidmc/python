from random import randint

histogram = [0] * 100

print(histogram)

for _ in range(100000):
    r = randint(0, 99)
    histogram[r] += 1
    print(f'r: {r}')

for h in histogram:
    print(h)