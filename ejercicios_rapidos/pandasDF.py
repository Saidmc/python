import pandas

df = pandas.DataFrame({'x':[1, 2, 3], 'y':[3, 4, 5]})

print(df)

print('*'*50)
df.iloc[1] = {'x': 7, 'y': 77}

print(df)

print('*'*50)
df.iloc[0] = {'x': 88, 'y': 8}

print(df)

print('*'*50)
#df.loc['1']
print('*'*50)
print(df.iloc[2,1])

print('*'*50)

mask = df['y'] == 77
print(mask)
find = df.loc[mask, 'x']
print(find)