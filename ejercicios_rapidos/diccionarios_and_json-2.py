import json

datosFamDICT =  {
                'Said': 41, 
                'Nery': 42,
                'Saido': 21, 
                'Arath': 9
            }

datosFamSTR =  "{'Said': 41, 'Nery': 42, 'Saido': 21, 'Arath': 9}"

print(f'Tipo de datosFamDICT: {type(datosFamDICT)}')
print(f'Tipo de datosFamSTR: {type(datosFamSTR)}')

mi_json_de_DICT = json.JSONEncoder().encode(datosFamDICT)
mi_json_de_STR = json.JSONEncoder().encode(datosFamSTR)

print('*'*10)
print(f'Tipo de mi_json_de_DICT: {type(mi_json_de_DICT)}')
print(f'Tipo de mi_json_de_STR: {type(mi_json_de_STR)}')
print(mi_json_de_DICT)
print(mi_json_de_STR)
print('*'*10)

mi_obj_de_JSON_DICT = json.JSONDecoder().decode(mi_json_de_DICT)
mi_obj_de_JSON_STR = json.JSONDecoder().decode(mi_json_de_STR)

print(f'Tipo de mi_obj_de_JSON_DICT: {type(mi_obj_de_JSON_DICT)}')
print(f'Tipo de mi_obj_de_JSON_STR: {type(mi_obj_de_JSON_STR)}')