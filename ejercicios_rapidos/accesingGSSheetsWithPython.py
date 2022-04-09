import gspread
import pandas as pd

from  oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('devpythonandgssheets-8f99341409e2.json', scope)
client = gspread.authorize(creds)


#sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1E3LJGpa6TYRM1-JVuxnuG2SpGLV5tWIuU1CLHFtKynY/edit#gid=0')
sheet = client.open_by_key('1eIHe7tlp17Orh1KzOWAe1t8bF4kyZb_pNkEP-OOzqxg')
#sheet = client.open('commentary data')
sheet_instance = sheet.get_worksheet(0)

print(sheet.list_permissions)

numCols = sheet_instance.col_count
print(f'Numero de Columnas: {numCols}')
numRows = sheet_instance.row_count
print(f'Numero de Filas: {numRows}')

valueCell = sheet_instance.cell(col=3, row=2)
print(f'Celda(3,2): {valueCell}')

valueCell = sheet_instance.cell(col=1, row=1)
print(f'Celda(1,1): {valueCell}')

valueCell = sheet_instance.cell(col=2, row=2)
print(f'Celda(2,2): {valueCell}')

records_data = sheet_instance.get_all_records()

#print(records_data)

# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
print(records_df.head())

runs = records_df.groupby(['Batsman_Name'])['Runs'].count().reset_index()
print(runs)

sheet.add_worksheet(title='runs', rows=20, cols=2)
sheet_runs = sheet.get_worksheet(1)

sheet_runs.insert_rows(runs.values.tolist())