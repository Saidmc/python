def divide(x, y):
    assert y != 0 #expresión falsa == ERROR
    return x / y

a = divide(100, 10)
print(a)

a = divide(100, 0)
print(a)