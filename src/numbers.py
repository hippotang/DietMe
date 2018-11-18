import os
import pandas as pd
import math
from fractions import Fraction 
from pandas import ExcelWriter
from pandas import ExcelFile

from bs4 import BeautifulSoup


file = "ABBREV.xlsx"
df = pd.read_excel('ABBREV.xlsx', sheetname='ABBREV')

urls = []
with open("urls.txt") as f:
        for line in f:
            urls.append(line[:-1])


#print(urls)

def getUrlIngredients(urls):
    urlIngredients = {}
    for url in urls:
        ingStr = []
        page = requests.get(url)
        #print(page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')
        #sleep(0.5)
        ingredients = soup.find_all(class_= "ingredient")
        for i in ingredients:
            ingStr.append(i.decode_contents())
        urlIngredients[url] = ingStr
        #print(ingStr)
    return urlIngredients; 

"""arr = getUrlIngredients(urls)
for key in arr:
    print(arr[key])"""


#


def getNumber(ingredientString):
    stringArr = ingredientString.split()
    i = 0
    x = ""
    for c in ingredientString:
        if (is_number(c) or c == '/' or c == " "):
            i=i+1
        else:
            break
    
    tempString = ingredientString.substring(0,i)
    return(mixed_to_float(tempString))

def mixed_to_float(tempString):
    # "1 1/2 asdfasdfasdfsa
    # 1
    # 1/2
    index = 0
    """while (tempString[index].is_number or tempString[index] == " " or tempString[index] == '/'):
        index = index + 1
    tempString = tempString.substring(0,index)
    tempString.trim()"""

    stringArr = tempString.split()
    tempSum = 0.0

    for i in stringArr:
        try:
            tempSum = tempSum + eval(i)
        except:
            break
    
    return tempSum
    


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getUnit(description):
    # description is under GmWt_Desc2 in the dataframe
    try:
       if (description.index("cup")>=0):
           return "cup"
    except ValueError:
        print("")

    try:
       if (description.index("tablespoon")>=0 or description.index("tbsp")>=0):
           return "tablespoon"
    except ValueError:
        print("")

    try:
       if (description.index("oz")>= 0 or description.index("ounce")>=0):
           return "ounce"
    except ValueError:
        print("")
        
def getMultiplier(df,ingredientString):
    # ingredient string is the ingredient as it is listed on epicurious 
    # i.e. "5 tablespoons of butter"
    index = 0
    multiplier = 1
    tempString = ingredientString.split()[0]
    for i in df.index:
        if(df['Shrt_Desc'][i].split()[0] == ingredientString):
            index = i
    
    measurement = ""
    print(df['GmWt_Desc2'][index])
    unit = getUnit(df['GmWt_Desc2'][index])
    unit2 = getUnit(ingredientString)

    if (unit != unit2):
        multiplier = 1
    else:
        multiplier = df['GmWt_2'][index] * mixed_to_float(ingredientString)
    
    return multiplier
    


ingredients = "1 1/2 cheese fresh orange juice"
print(mixed_to_float(ingredients))

print(getMultiplier(df, ingredients))



