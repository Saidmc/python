import decimal

a = 0.1 + 0.2 + 0.3
print(a)

b = 0.1
print(b)

c = decimal.Decimal('0.1')\
     + decimal.Decimal('0.2')\
     + decimal.Decimal('0.3')
print(c)

print(a)
print(decimal.Decimal(a))

fmt = '{0:<25} {1:<25}'

print(fmt.format('Input', 'Output'))
print(fmt.format('-' * 25, '-' * 25))

# Integer
print(fmt.format(5, decimal.Decimal(5)))

# String
print(fmt.format('3.14', decimal.Decimal('3.14')))

# Float
f = 0.1
print(fmt.format(repr(f), decimal.Decimal(str(f))))
print('{:<0.23g} {:<25}'.format(
    f,
    str(decimal.Decimal.from_float(f))[:25])
)

# Tuple
t = (0, (1, 1), -2)
print('Input  :', t)
print('Decimal:', decimal.Decimal(t))
t = (1, (1, 1), -2)
print('Input  :', t)
print('Decimal:', decimal.Decimal(t))
t = (1, (1, 1, 5, 6), -2)
print('Input  :', t)
print('Decimal:', decimal.Decimal(t))
t = (1, (1, 1, 5, 6, 8, 9), -2)
print('Input  :', t)
print('Decimal:', decimal.Decimal(t))
t = (1, (1, 1, 5, 6, 8, 9), -5)
print('Input  :', t)
print('Decimal:', decimal.Decimal(t))

d = decimal.Decimal(1.1)
print('Precision:')
print('{:.1}'.format(d))
print('{:.2}'.format(d))
print('{:.3}'.format(d))
print('{:.18}'.format(d))

a = decimal.Decimal('5.1')
b = decimal.Decimal('3.14')
c = 4
d = 3.14

print('a     =', repr(a))
print('b     =', repr(b))
print('c     =', repr(c))
print('d     =', repr(d))

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print()

print('a + c =', a + c)
print('a - c =', a - c)
print('a * c =', a * c)
print('a / c =', a / c)
print()