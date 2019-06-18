import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data

#Exercise 0
iris = sns.load_dataset('iris')
iris.head()
#Exercise 0.1
sns.distplot(iris.petal_length)
#Exercise 0.2
sns.relplot(x='petal_length',y='petal_width',data=iris)
#Exercise 0.3
sns.relplot(x='sepal_width',y='sepal_length',hue='species',data=iris)
#Exercise 0.4
sns.pairplot(iris,hue='species')


#Exercise 1
anscombe=sns.load_dataset('anscombe')
anscombe.head()

#Exercise 1.1
anscombe.groupby('dataset').describe()

#Exercise 1.2
sns.relplot(x='x',y='y',col='dataset',data=anscombe)

#Exercise 2
insects=data('InsectSprays',show_doc=True)