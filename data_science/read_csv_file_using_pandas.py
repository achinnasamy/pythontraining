
import pandas as pd

#df = pandas.read_csv(filename, sep = "\t+|\s+\t+|\t+\s+", lineterminator='\r')


df = pd.read_csv('/home/dharshekthvel/Desktop/ds.csv', header=None, names=['_id','FundingAmount','FundingDate','FundingType','Industry','Location','launchAt'])

for index, row in df.iterrows():

    print row['FundingAmount']

