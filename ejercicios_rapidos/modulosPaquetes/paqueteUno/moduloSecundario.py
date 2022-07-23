from asyncio.windows_events import NULL
from paqueteUno import moduloTercero

def funcModuloSecundario():
    print('Hola mundo desde MODULO SECUNDARIO!!')
    print(__name__)
    print('-'*10)
    moduloTercero.funcModuloTercero()
    return NULL
