import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

file = "ABBREV.xlsx"


df = pd.read_excel('ABBREV.xlsx', sheetname='ABBREV')
 
#print("Column headings:")
#print(df.columns)

#print(df['Water_(g)'])

ingredients = {}


def getDescriptions(df, column, value):
    for i in df.index:
        if ((abs(df[column][i] - value)) < 0.5))
            name = df['Shrt_Desc'][i]
            ingredients[name] = df[column][i]
    return;

getDescriptions(df, 'Water_(g)')

print (ingredients)

query = "recipe with "
for i in ingredients:
    query += ingredients[i]
print (query)
#search(query, tld="com", num=10, stop=1, pause=2)
