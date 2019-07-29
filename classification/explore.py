# Do your work for these exercises in a file named explore
from aquire import get_iris_data
from aquire import get_titanic_data
from prepare import prep_titanic
from prepare import prep_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1) Split data in to train (70%)& test (30%) samples. You should end up with 2 data frames:
#`train_df` and `test_df`
iris_df=prep_iris(get_iris_data())
y=iris_df[['species']]
X=iris_df[['petal_length','petal_width','sepal_length','sepal_width']]
X_train,y_train,X_test,y_test=train_test_split(X,y,train_size=.7,random_state=123)

#Create a swarmplot where the x-axis is each of the independent variable names(petal_length,petal_width,etc.)
#The y-axis is the value of the variable. Use color to represent species as another dimension.
#Hint:You will need to melt the dataframe into a 'long' dataframe to accomplish this. What are your takeaways
#from this visualization?
melted_iris=iris_df.melt(id_vars='species_name',value_vars=['sepal_length','sepal_width','petal_length','petal_width'],var_name='measurement')
sns.swarmplot(x='measurement',y='value',hue='species_name',data=melted_iris)
# 3)Create 4 subplots(2rows*2 columns)of scatterplots
#sepal_length*sepal_width
#petal_length*petal_width
#sepal_area*petal_area
#sepal_length*petal_length
iris_df['petal_area']=iris_df['petal_length']*iris_df['petal_width']
iris_df['sepal_area']=iris_df['sepal_length']*iris_df['sepal_width']
_, ax = plt.subplots(nrows=2, ncols=2, figsize=(14,8))
sns.scatterplot(x='sepal_length',y='sepal_width',data=iris_df,ax=ax[1])
sns.scatterplot(x='petal_length',y='petal_width',data=iris_df,ax=ax[2])
sns.scatterplot(x='sepal_area',y='petal_area',data=iris_df,ax=ax[3])
sns.scatterplot(x='sepal_length',y='petal_length',data=iris_df,ax=ax[4])
#4) Make a heat map for each variable layering the correlation coefficent on top
plt.figure(figsize=(8,4))
sns.heatmap(iris_df.corr(), cmap='Reds', annot=True)
# 5) Create a scatter matrix visualizing the interaction of each variable
from matplotlib import cm
cmap = cm.get_cmap('gnuplot')
axes = pd.plotting.scatter_matrix(
    iris_df, marker='o', s=40,
    hist_kwds={'bins':15},  figsize=(9,9), cmap=cmap)
#6) Is the sepal length significantly different in virginica than versicolor? Run an experiment to do this.
# Must include null hypothesis,alternative hypothesis,t-test,results,summary
# H0:The difference in sepal length between virginica and versicolor is insignificant
# HA:The difference between virginica and versicolor is substantial.
# We will test if the sepal length of viriginica is significantly different than that of versicolor    
#If there is a difference ,then variable sepal_length is a good choice to keep as a feature
#We can use a t-test here as sepal is somewhat normally distributed
import scipy as sp 
import numpy as np

sp.stats.ttest_ind(
    iris_df[iris_df.species_name=="virginica"].sepal_length,
    iris_df[iris_df.species_name=="versicolor"].sepal_length)
#Good choice to keep as a variable since p-value less than .05    
