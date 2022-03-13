import math
import sys

def resuelve(a, b, c):
    partD = math.sqrt(b**2 - 4*a*c)
    x1 = (-b - partD) / (2 * a)
    x2 = (-b + partD) / (2 * a)
    return x1, x2

p1, p2, p3 = 1, 12, 4
print(f'lenargs={len(sys.argv)}')
if len(sys.argv) == 4:
    p1 = int(sys.argv[1])
    p2 = int(sys.argv[2])
    p3 = int(sys.argv[3])

print(f'p1={p1}, p2={p2}, p3={p3}')
res1, res2 = resuelve(p1, p2, p3)

print(round(res1, 2))
print(round(res2, 2))