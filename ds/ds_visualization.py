

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/dharshekthvel/Desktop/ds.csv', header=None, names=['_id','FundingAmount','FundingDate','FundingType','Industry','Location','launchAt'])

for index, row in df.iterrows():
    print row['FundingAmount']

df.FundingAmount = df.FundingAmount.astype(float)
df._id = df._id.astype(float)


df.plot(x='Industry', y='FundingAmount')


plt.show()