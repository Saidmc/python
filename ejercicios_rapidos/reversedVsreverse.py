a = ['alpha', 'beta', 'gamma']

b = reversed(a)
b = list(b)
print(a)

c = a.reverse()
print(a)

print('-' * 50)
print(b)

print('-' * 50)
d = repr(a)
print(type(d))
print(d)
