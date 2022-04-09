from tkinter import *

def funcCall():
    lab = Label(root, text = 'Botón presionado')
    lab.pack()
    boton['bg'] = 'blue'
    boton['fg'] = 'white'

root = Tk()
root.geometry('200x400+500+200')

li = 'Said Muñoz Chávez Ian Arath Sayato Mamá'.split()
pelis = ['AI', 'Depredador', 'Interestelar', 'Aladin', 'Megamente', 'Dragon Ball']

listb = Listbox(root)
for item in li:
    listb.insert(0, item)

listb2 = Listbox(root)
for item in pelis[::-1]:
    listb2.insert(0, item)

boton = Button(root, text='Presine aquí', command=funcCall)

listb.pack()
listb2.pack()
boton.pack()

root.mainloop()
