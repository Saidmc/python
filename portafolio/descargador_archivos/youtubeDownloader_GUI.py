from typing import Any
from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

global yt
global streamMP4Files

def cargaListaVideos():
    global yt
    global streamMP4Files

    yt = YouTube(urlVideo.get())
    streamMP4Files = yt.streams.filter(file_extension='mp4') #, progressive=True

    for item in streamMP4Files:
        lstListado.insert(0, item)
        
def descargaVideo():
    global yt
    global streamMP4Files

    print(lstListado.curselection()[0])
    dn_video = streamMP4Files[lstListado.curselection()[0]]
    dn_video.download('D:\\rec\\')

def Close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app.destroy()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app.destroy()

app = tk.Tk()
app.protocol("WM_DELETE_WINDOW", on_closing)
app.title("Descarga videos youtube")
app.geometry('800x400+500+200')
tagTitle = tk.Label(app, text='Escribe o pega la URL del video:')
tagTitle.pack()
urlVideo = tk.Entry(app, textvariable='', font="lucida 14", bg='light gray')
urlVideo.pack(fill=tk.X)

btnListado = tk.Button(app, text='Buscar descargables', command=cargaListaVideos)
lstListado = tk.Listbox(app)
btnListado.pack()
lstListado.pack(fill=tk.X)
btnDescarga = tk.Button(app, text='Descargar archivo seleccionado', command=descargaVideo)
btnDescarga.pack()

# Button for closing
exit_button = tk.Button(app, text="Exit", command=Close)
exit_button.pack(pady=20)

app.mainloop()


print(" video was donwloaded successfully!! ")