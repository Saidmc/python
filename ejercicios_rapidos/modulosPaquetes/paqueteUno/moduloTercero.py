from asyncio.windows_events import NULL


def funcModuloTercero():
    print('Hola Mundo desde Módulo Tercero')
    print(__name__)
    print('-'*10)
    return NULL