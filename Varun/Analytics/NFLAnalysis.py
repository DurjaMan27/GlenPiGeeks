import pygsheets
import pandas as pd

#authorization
gc = pygsheets.authorize(service_file='/home/ec2-user/environment/GoogleCloudEval-e422de340b3a.json')

# Create empty dataframe
df = pd.DataFrame()

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
nflgooglesheet = gc.open_by_key('1Y6opDgKG19rv7w_hAsSYo-LqADKT478qztxIYSlZXyY')


#select the state distribution data sheet
nflstates = nflgooglesheet[0]

#update the first sheet with df, starting at cell B2. 
nflstatesdf = nflstates.get_as_df()

#nflstateslist = nflstatesdf.range('A1:B55')  # get a range of cells 

#print the df
print(nflstatesdf)

#plot nfl main office state count
#nflstatesdfplot = nflstatesdf.plot(kind='line', x='Team', y='Avg Age', width=0.85, figsize=(8, 10), legend=True)
nflstatesdfplot = nflstatesdf.plot(kind='line', x='Team', y='Avg Age', figsize=(8, 10), legend=True)
nflstatesdfplotfig = nflstatesdfplot.get_figure()
nflstatesdfplotfig.savefig('/home/ec2-user/environment/GlenPiGeeks/Varun/Analytics/nflstates.png')  
