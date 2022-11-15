import pandas as pd

urlprefix = 'https://vincentarelbundock.github.io/Rdatasets/csv/'
dataname = 'datasets/iris.csv'
iris = pd.read_csv( urlprefix + dataname )
iris.head()

iris = iris.drop("Unnamed: 0", 1)
