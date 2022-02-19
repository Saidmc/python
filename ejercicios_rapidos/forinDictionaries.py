#Using for in, in dictionaries

CountriesCaps = {
    'México' : 'Ciudad de México',
    'Guatemala' : 'Guatemala',
    'Belice' : 'Belmopán'
}

for country in CountriesCaps:
    print('The capital of ' + country + ' is ' + CountriesCaps[country])