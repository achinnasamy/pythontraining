


# Pandas loading a file
import pandas as pd

df = pd.read_csv(filepath_or_buffer="/home/dharshekthvel/ac/code/scalatrainingintellij/data/vs1.csv", sep=",")

# Pick the needed columns
needed_columns_df = df[['GPS_LONGITUDE','GPS_LATITUDE']]
needed_columns_df = needed_columns_df.fillna(method='ffill')

from sklearn import decomposition

pca = decomposition.PCA(n_components=1)
pca.fit(needed_columns_df)
needed_columns_df = pca.transform(needed_columns_df)

print needed_columns_df

#
#
# import numpy as np
# dataset = np.loadtxt('/home/dharshekthvel/ac/code/scalatrainingintellij/data/vs1.csv', delimiter=",")