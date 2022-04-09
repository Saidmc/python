import tkinter as tk
import tkinter.font as tkFont
from tkinter import StringVar, messagebox
from pytube import YouTube
from tkinter import filedialog

global yt
global streamMP4Files
global my_string_var


def GButton_URLOrigen_command():
    print("command")


def GButton_DirectorioDestino_command():
    print("command")


def GButton_Salir_command():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def cargaListaVideos():
    global yt
    global streamMP4Files
    global my_string_var

    if not GLineEdit_URLOrigen.get():
        GLabel_MsgEstatus["fg"] = "#FF0000"
        my_string_var.set(f"No se ha especificado una URL para descargar el archivo.")
        return

    try:
        yt = YouTube(GLineEdit_URLOrigen.get())
        streamMP4Files = yt.streams.filter(file_extension='mp4') #, progressive=True
    except:
        GLabel_MsgEstatus["fg"] = "#FF0000"
        my_string_var.set(f"La URL no es valida para descargar un archivo.")
        return

    for item in streamMP4Files:
        GListBox_ListadoArchivos.insert(0, item)

    GLabel_MsgEstatus["fg"] = "#333333"
    my_string_var.set(f"La lista de archivos se cargó exitosamente.\nSe encontraron {len(streamMP4Files)} archivos para descargar.")
        
def descargaVideo():
    global yt
    global streamMP4Files

    if not len(GListBox_ListadoArchivos.curselection()):
        GLabel_MsgEstatus["fg"] = "#FF0000"
        my_string_var.set(f"No se ha cargado la lista o no se ha seleccionado un archivo para descargar.")
        return

    print(GListBox_ListadoArchivos.curselection()[0])
    dn_video = streamMP4Files[GListBox_ListadoArchivos.curselection()[0]]
    dn_video.download(f'{GLineEdit_DirectorioDestino.get()}')

    if GLineEdit_DirectorioDestino.get():
        GLabel_MsgEstatus["fg"] = "#333333"
        my_string_var.set(f"El archivo seleccionado se descargó exitosamente.")
    else:
        GLabel_MsgEstatus["fg"] = "#FF0000"
        my_string_var.set(f"No se ha seleccionado el directorio destino.")

def pideDirectorio():
    directorio = filedialog.askdirectory()
    GLineEdit_DirectorioDestino.delete(0,"end")
    GLineEdit_DirectorioDestino.insert(0, directorio + '/')

root = tk.Tk()
my_string_var = StringVar()
#setting title
root.title("File YT Downloader")
    
#setting window size
width=800
height=550
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#GLabel_Titulo=tk.Label(root)
#ft = tkFont.Font(family='Times',size=14)
#GLabel_Titulo["font"] = ft
#GLabel_Titulo["fg"] = "#333333"
#GLabel_Titulo["justify"] = "center"
#GLabel_Titulo["text"] = "File YT Downloader"
#GLabel_Titulo["relief"] = "flat"
#GLabel_Titulo.place(x=10,y=20,width=155,height=34)

GListBox_ListadoArchivos=tk.Listbox(root)
GListBox_ListadoArchivos["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GListBox_ListadoArchivos["font"] = ft
GListBox_ListadoArchivos["fg"] = "#333333"
GListBox_ListadoArchivos["justify"] = "left"
GListBox_ListadoArchivos.place(x=20,y=270,width=760,height=175)

GLabel_DirectorioDestino=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_DirectorioDestino["font"] = ft
GLabel_DirectorioDestino["fg"] = "#333333"
GLabel_DirectorioDestino["justify"] = "center"
GLabel_DirectorioDestino["text"] = "Directorio destino:"
GLabel_DirectorioDestino.place(x=20,y=150,width=107,height=30)

GLineEdit_URLOrigen=tk.Entry(root)
GLineEdit_URLOrigen["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_URLOrigen["font"] = ft
GLineEdit_URLOrigen["fg"] = "#333333"
GLineEdit_URLOrigen["justify"] = "left"
GLineEdit_URLOrigen["text"] = "URL Origen"
GLineEdit_URLOrigen.place(x=20,y=90,width=674,height=30)

GButton_URLOrigen=tk.Button(root)
GButton_URLOrigen["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_URLOrigen["font"] = ft
GButton_URLOrigen["fg"] = "#000000"
GButton_URLOrigen["justify"] = "center"
GButton_URLOrigen["text"] = "Buscar"
GButton_URLOrigen.place(x=710,y=90,width=71,height=30)
GButton_URLOrigen["command"] = cargaListaVideos

GLabel_URLOrigen=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_URLOrigen["font"] = ft
GLabel_URLOrigen["fg"] = "#333333"
GLabel_URLOrigen["justify"] = "center"
GLabel_URLOrigen["text"] = "URL origen:"
GLabel_URLOrigen.place(x=20,y=60,width=72,height=30)

GLineEdit_DirectorioDestino=tk.Entry(root)
GLineEdit_DirectorioDestino["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_DirectorioDestino["font"] = ft
GLineEdit_DirectorioDestino["fg"] = "#333333"
GLineEdit_DirectorioDestino["justify"] = "left"
GLineEdit_DirectorioDestino["text"] = "Directorio Destino"
GLineEdit_DirectorioDestino.place(x=20,y=180,width=671,height=30)

GButton_DirectorioDestino=tk.Button(root)
GButton_DirectorioDestino["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=18)
GButton_DirectorioDestino["font"] = ft
GButton_DirectorioDestino["fg"] = "#000000"
GButton_DirectorioDestino["justify"] = "center"
GButton_DirectorioDestino["text"] = "..."
GButton_DirectorioDestino.place(x=710,y=180,width=71,height=31)
GButton_DirectorioDestino["command"] = pideDirectorio

GLabel_ListadoArchivos=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_ListadoArchivos["font"] = ft
GLabel_ListadoArchivos["fg"] = "#333333"
GLabel_ListadoArchivos["justify"] = "left"
GLabel_ListadoArchivos["text"] = "Listado de archivos"
GLabel_ListadoArchivos.place(x=20,y=240,width=111,height=30)

GLabel_Estatus=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_Estatus["font"] = ft
GLabel_Estatus["fg"] = "#333333"
GLabel_Estatus["justify"] = "center"
GLabel_Estatus["text"] = "Estatus:"
GLabel_Estatus.place(x=20,y=460,width=70,height=30)

GLabel_MsgEstatus=tk.Label(root, textvariable = my_string_var)
ft = tkFont.Font(family='Times',size=10)
GLabel_MsgEstatus["font"] = ft
GLabel_MsgEstatus["fg"] = "#333333"
GLabel_MsgEstatus["justify"] = "left"
GLabel_MsgEstatus["text"] = ""
GLabel_MsgEstatus.place(x=90,y=460,width=531,height=68)

GButton_Descargar=tk.Button(root)
GButton_Descargar["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_Descargar["font"] = ft
GButton_Descargar["fg"] = "#000000"
GButton_Descargar["justify"] = "center"
GButton_Descargar["text"] = "Descargar"
GButton_Descargar.place(x=710,y=460,width=70,height=30)
GButton_Descargar["command"] = descargaVideo

GButton_Salir=tk.Button(root)
GButton_Salir["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_Salir["font"] = ft
GButton_Salir["fg"] = "#000000"
GButton_Salir["justify"] = "center"
GButton_Salir["text"] = "Salir"
GButton_Salir.place(x=710,y=500,width=70,height=30)
GButton_Salir["command"] = GButton_Salir_command




#if __name__ == "__main__":
    
root.mainloop()


#root.protocol("WM_DELETE_WINDOW", app.GButton_Salir_command())

