import pandas as pd
from sklearn.linear_model import LinearRegression

csv = "2015stats.csv"
data = pd.read_csv(csv)

data.tail()

