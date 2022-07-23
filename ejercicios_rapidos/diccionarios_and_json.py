import json

datosFam =  {
                'Said': 41, 
                'Nery': 42,
                'Said': 21, 
                'Arath': 9
            }

print(datosFam)
print(datosFam['Arath'])

datosFam['Alma'] = 63
print(datosFam)

datosFam['TBone'] = 12
print(datosFam)

del datosFam['TBone']
print(datosFam)

datosFam2 = {'N1':2, 'N2':1}

datosFam = datosFam | datosFam2
print(datosFam)

datosFam['cosas'] = {'cosa10': 12, 'cosa1' : 11, 'cosa3': 20}
print(datosFam)

print(datosFam['cosas'])
print(datosFam['cosas']['cosa3'])

#serializa un obj (dicionario) a una cadena en formato json
print('*'*30)
mi_obj_json = json.dumps(datosFam)
print(mi_obj_json)
print(type(mi_obj_json))

mi_obj_json = json.dumps(datosFam, indent=4, separators=(', ', ' : '))
print(mi_obj_json)
print('*'*5)
mi_obj_json = json.dumps(datosFam, indent=4, separators=(', ', ' : '), sort_keys=True)
print(mi_obj_json)


#otra manera de manejar diccionarios y json
print('*'*30)
print('\n')
print('JSONEncoder / JSONDecoder')
#mi_dictjson = json.loads(mi_obj_json)
print(f'Tipo de mi_dictjson: {type(mi_obj_json)}')
mi_json = json.JSONEncoder().encode(mi_obj_json)
print(f'Tipo de mi_json: {type(mi_json)}')
print(mi_json)
print('*'*5)
mi_dict = json.JSONDecoder().decode(mi_json)
print(mi_dict)
print(f'Tipo de mi_dict: {type(mi_dict)}')

print('*'*30)
print(f'Tipo de mi_obj_json: {type(mi_obj_json)}')
print(mi_obj_json)
print(f'Tipo de mi_json: {type(mi_json)}')
print(mi_json)

mi_dict1 = json.JSONDecoder().decode(mi_obj_json)
print(f'Tipo de mi_dict1: {type(mi_dict1)}')
mi_dict2 = json.JSONDecoder().decode(mi_json)
print(f'Tipo de mi_dict2: {type(mi_dict2)}')