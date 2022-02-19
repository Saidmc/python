#Using while - else

from tkinter import X


x = 1

while x != 10 and x < 20:
    print(x)
    x += 1
else:
    print("x es igual a 10")
    x += 1

#Desde el primer instante que no se cumple la condición
#sale del ciclo while y ejecuta el else