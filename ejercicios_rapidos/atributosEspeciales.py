from turtle import clear
import sys
import os

os.system('cls')
print(f'Nombre del namespace desde donde se ejecuta este código: {__name__}')
print(sys.ps1)