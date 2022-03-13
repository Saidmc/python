#Using strings formatting

name = 'Said'
print('Hello ' + name + '!!')


#Old format
print('Hello %s!!' %name)

#Another format with f-strings (interpolation of strings)
print(f'Hello {name}!!')

#New format
print('Hello {}!!'.format(name))


#Formatting using indices
a = 10
b = 20

print('Suma de {0} + {1} = {1} + {0}'.format(a, b))