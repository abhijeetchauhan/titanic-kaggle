# import matplotlib.pyplot as plt
#matplotlib inline
# import numpy as np
# Pandas is used to deal with csv file
import pandas as pd
# import statsmodels.api as sm
# from statsmodels.nonparametric.kde import KDEUnivariate
# from statsmodels.nonparametric import smoothers_lowess
# from pandas import Series, DataFrame
# from patsy import dmatrices
# from sklearn import datasets, svm
# from KaggleAux import predict as ka # see github.com/agconti/kaggleaux for more details

# --------------------------------------------Loading Files----------------------------------------------
# Data loaded in a dictionary
df = pd.read_csv("train.csv") 
# Ticket and cabin are not very important so we will drop them
df = df.drop(['Ticket','Cabin'], axis=1) 
# Remove NaN values
df = df.dropna() 
# print df
# --------------------------------------------Visualizing the Data----------------------------------------