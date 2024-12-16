import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df=pd.read_csv('student_scores.csv')
df.head(5)


y=df['Scores']
x=df[['Hours']]


plt.style.use('fivethirtyeight')
plt.figure(figsize=(9,6))
plt.scatter(x,y)
plt.show()