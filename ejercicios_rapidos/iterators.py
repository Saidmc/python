#Using iterator
import time

inicio = time.time()

mi_lista = ['Sayato', 'Aratho', 'Reny']

nombre = iter(mi_lista)

n = next(nombre)
print(n)

n = next(nombre)
print(n)

n = next(nombre)
print(n)

mi_lista2 = mi_lista[::-1]

nombre = iter(mi_lista2)

m = next(nombre)
print(m)

m = next(nombre)
print(m)

m = next(nombre)
print(m)

time.sleep(2)

print('A continuación vamos a ocupar la cama para dormir')

fin = time.time()

print(f'El tiempo de ejecucución de este programa es de {fin - inicio} segundos')