import pygsheets
import pandas as pd

#authorization
gc = pygsheets.authorize(service_file='/home/ec2-user/environment/GoogleCloudEval-e422de340b3a.json')

# Create empty dataframe
df = pd.DataFrame()

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open_by_key('10dS74MpTQqt1Rc2hKDaRkkeapOBBxmgC8EXkj5WUM_U')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
df = wks.get_as_df()

print(df.count())