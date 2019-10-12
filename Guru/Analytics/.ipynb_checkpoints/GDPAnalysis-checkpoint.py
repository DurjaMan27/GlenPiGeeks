import pandas
import matplotlib

#use this for non interactive back-end for AWS Cloud9
matplotlib.use("Agg")

#read world bank data for gdp per capita and life expectancy
gdppc_df = pandas.read_csv('GDPPC2018.csv', index_col='Country Code')
lifeexp_df = pandas.read_csv('LIFEEXP2018.csv', index_col='Country Code')

#plot gdp per capita and save picture
gdppcplot = gdppc_df.plot(legend=True)
gdppcfig = gdppcplot.get_figure()
gdppcfig.savefig('/home/ec2-user/environment/GlenPiGeeks/Guru/gdppc.png')  

#plot life expectancy and save picture
lifeexpplot = lifeexp_df.plot(legend=True)
lifeexpfig = lifeexpplot.get_figure()
lifeexpfig.savefig('/home/ec2-user/environment/GlenPiGeeks/Guru/lifeexp.png')
