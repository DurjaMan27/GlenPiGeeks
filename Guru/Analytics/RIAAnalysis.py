import pygsheets
import pandas as pd

#authorization
gc = pygsheets.authorize(service_file='/home/ec2-user/environment/GoogleCloudEval-e422de340b3a.json')

# Create empty dataframe
df = pd.DataFrame()

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
riagooglesheet = gc.open_by_key('10dS74MpTQqt1Rc2hKDaRkkeapOBBxmgC8EXkj5WUM_U')

#select the raw data sheet 
riarawdata = riagooglesheet[0]

#select the state distribution data sheet
riastates = riagooglesheet[2]

#update the first sheet with df, starting at cell B2. 
riastatesdf = riastates.get_as_df()

#riastateslist = riastatesdf.range('A1:B55')  # get a range of cells 

#print the df
print(riastatesdf)

#plot ria main office state count
riastatesdfplot = riastatesdf.plot(kind='barh', x='Main Office State', y='COUNTA of Main Office State', width=0.85, figsize=(8, 10), legend=True)
riastatesdfplotfig = riastatesdfplot.get_figure()
riastatesdfplotfig.savefig('/home/ec2-user/environment/GlenPiGeeks/Guru/riastates.png')  
