import pandas as pd


#pip install xlrd to read excel from pandas
nutri = pd.read_excel("Data-Sets/nutrition_elderly.xls")

DICT = {1:'Male', 2:'Female'} # dictionary specifies replacement
nutri['gender'] = nutri['gender'].replace(DICT).astype('category')
nutri['height'] = nutri['height'].astype(float)


print(nutri.head(10))
nutri.info()

nutri.to_csv('nutri.csv',index=False)
