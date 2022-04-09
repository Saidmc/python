#yield, convert the function in a generator
#object that keeps the state between calls

def func():
    for i in range(1,11):
        yield i

'''
Can create more than one generator behave independently
'''
g = func()
h = func()

print(type(g))
print(g)
print(next(g))
print(next(g))
print(next(h))
print(next(g))
print(next(h))
print(next(g))
print(next(g))
print(next(h))
print(next(h))