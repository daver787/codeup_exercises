# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:14:31 2019

@author: daver
"""

from pydataset import data
faithful=data('faithful',show_doc=True)
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
import matplotlib.pyplot as plt
from math import sqrt

corr=pearsonr(faithful.waiting,faithful.eruptions)
reg=linear_model.LinearRegression()
reg.fit(faithful[['waiting']],faithful.eruptions)#need a dataframe for x,not series
y_actual=reg.predict(faithful[['waiting']])
rms=sqrt(mean_squared_error(faithful.eruptions,y_actual))

plt.scatter(faithful.waiting,faithful.eruptions,c="blue")
plt.plot(faithful.waiting,y_actual,c="red")
plt.title("Predicted time between eruptions")
plt.ylabel("#of eruptions")
plt.yticks(range(1,7))
plt.text(50,5.5,'RMSE:{:.2}'.format(rms))
plt.show()

