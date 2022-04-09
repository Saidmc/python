from tkinter import *

def hacerClick():
    try:
        _valor = int(entrada_texto.get())
        _valor = _valor * 5
        etiqueta2.config(text = _valor)
    except ValueError:
        etiqueta2.config(text = "Introduce un numero!!")
        

app = Tk()
app.title("Aplicación gráfica DOS")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(20,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta2 = Label(vp, text="Valor")
etiqueta2.grid(column=2, row=2, sticky=(W,E))

boton2 = Button(vp, text="OK DOS!!", command=hacerClick)
boton2.grid(column=1, row=1)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)

app.mainloop()