#   Numero de argumentos arbitrario y keyword arguments

#   Apartado 1: Numero de argumentos arbitrarios

def max(*args):
    max = args[0]
    for item in args[1:]:
        if item > max:
            max = item
    return max

#Se puede resolver del mismo modo pasandole una lista de n elementos
def max2(listNumbers):
    max = listNumbers[0]
    for item in listNumbers[1:]:
        if item > max:
            max = item
    return max


print(max(1,2,8,12,6))
print(max(345,3534,346476,3453,32454,6746,346,467))
print('-------------------')
print(max2([1,2,8,12,6]))
print(max2([345,3534,346476,3453,32454,6746,346,467]))


#   Apartados 2: Keywords Aruments

def funcClaveValor(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} --> {valor}')


funcClaveValor(nombre = 'Said', apPat = 'Munoz', apMat = 'Chavez')
print('-------------------')
funcClaveValor(nombre = 'Renic')


#   Apartado 3: Usando funciones con numero arbitrario de argumentos y kwordarguments

def miFunc2(nombre, *args, **kwargs):
    print(f'El nombre es: {nombre}')

    print(f'este es el listado de no se ques:')
    for item in args:
        print(f'- {item}')

    print(f'este es el listado de no se ques:')
    for clave, valor in kwargs.items():
        print(f'{clave} ---> {valor}')

    
miFunc2('Said', 'uno', 'dos', 'tres', 'cuatro', ApPat='Munoz', ApMat='Chavez')