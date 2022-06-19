varInt1 = 10
varFloat1 = 10.0
varInt2 = 10
varChar1 = 'Said'
varChar2 = 'Ian'
varChar3 = 'Said'


print(f'Type of varInt1: {type(varInt1)}')
print(f'Type of varFloat1: {type(varFloat1)}')
print(f'Type of varChar1: {type(varChar1)}')

print('-'*40)

print(f'10 == 10.0: {10 == 10.0}')
print(f'varInt1 == varFloat1: {varInt1 == varFloat1}, id(varInt1): {id(varInt1)}  ***  id(varFloat1): {id(varFloat1)}')
print(f'varInt1 == varChar1: {varInt1 == varChar1}, id(varInt1): {id(varInt1)}  ***  id(varChar1): {id(varChar1)}')
print(f'varFloat1 == varChar1: {varFloat1 == varChar1}, id(varFloat1): {id(varFloat1)}  ***  id(varChar1): {id(varChar1)}')

print('-'*40)

print(f'varInt1 == varInt2: {varInt1 == varInt2}, id(varInt1): {id(varInt1)}  ***  id(varInt2): {id(varInt2)}')
print(f'varChar1 == varChar2: {varChar1 == varChar2}, id(varChar1): {id(varChar1)}  ***  id(varChar2): {id(varChar2)}')
print(f'varChar1 == varChar3: {varChar1 == varChar3}, id(varChar1): {id(varChar1)}  ***  id(varChar3): {id(varChar3)}')
print(f'varInt1 is varInt2: {varInt1 is varInt2}, id(varInt1): {id(varInt1)}  ***  id(varInt2): {id(varInt2)}')

class miClase1:
    pass

class miClase2:
    pass


obj1MiClase1 = miClase1()
obj2MiClase1 = miClase1()

obj1MiClase2 = miClase2()
obj2MiClase2 = miClase2()

print('-'*40)

print(f'Type of obj1MiClase1: {type(obj1MiClase1)}')
print(f'Type of obj2MiClase1: {type(obj2MiClase1)}')
print(f'obj1MiClase1 == obj2MiClase1: {obj1MiClase1 == obj2MiClase1}, id(obj1MiClase1): {id(obj1MiClase1)}  ***  id(obj2MiClase1): {id(obj2MiClase1)}')

print(f'obj1MiClase1 is miClase1: {obj1MiClase1 is miClase1}, id(obj1MiClase1): {id(obj1MiClase1)}  ***  id(miClase1): {id(miClase1)}')