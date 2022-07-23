import json
from base64 import b64decode
import sys
from datetime import datetime

nombreArchivo = sys.argv[1]

with open(nombreArchivo,'r') as fileB64:   
    data = json.load(fileB64)
    fileB64.close()

    varB64 = data.get('document').get('data')
    poliza = data.get('document').get('id')
    bytes = b64decode(varB64, validate=True)

    if bytes[0:4] != b'%PDF':
        raise ValueError('Missing the PDF file signature')

    filePDF = open(poliza + '-' + datetime.today().strftime('%Y%m%d%H%M%S') + '.pdf', 'wb')
    filePDF.write(bytes)
    filePDF.close()