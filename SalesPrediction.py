

#Load libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#collect the data
data = pd.read_csv('SalesDataProductWise.xlsx-Sheet1.csv')
print(data.head())
print("-------------------------------------------------------")
print("Data Discription:")
print(data.describe())
print("-------------------------------------------------------")
print("data iformation:")
print(data.info())
print("-------------------------------------------------------")

plt.plot(data.isnull())
