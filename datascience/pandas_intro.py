import pandas as pd


master_file = pd.ExcelFile('/home/dharshekthvel/ac/code/scalatrainingintellij/data/sample.xls')

sheets =  master_file.sheet_names

survey = master_file.parse('choices')

# Copy data in memory
survey2 = survey.copy(deep=True)


# print rows from 0 to 13
# print survey2[0:13]


# remove a column
# del survey2['name']

#print survey2[0:10]

new_survey = survey2.drop('caption', axis = 1)

print new_survey[0:10]