import pandas as pd
abalone = pd.read_csv('Data-Sets/abalone.data',header = None)

abalone.columns = ['Sex', 'Length', 'Diameter', 'Height',
'Whole weight','Shucked weight', 'Viscera weight', 'Shell weight',
'Rings']

print(abalone.head(3))