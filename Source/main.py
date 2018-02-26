import pandas as pd

trainDataFrame = pd.read_csv('../Data/train.csv')

survivedSeries = trainDataFrame['Survived']
trainDataFrame = trainDataFrame.drop('Survived', axis=1)