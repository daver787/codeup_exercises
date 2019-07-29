# Do your work for these exercises in either a notebook or file name `model`
from aquire import get_iris_data
from aquire import get_titanic_data
from prepare import prep_titanic
from prepare import prep_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1) Fit the logistic regression classifier to your training sample and transform,i.e. make predictions
#on the training sample
iris_df=prep_iris(get_iris_data())
y=iris_df[['species']]
X=iris_df[['petal_length','petal_width','sepal_length','sepal_width']]
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=.7,random_state=123)
lr=LogisticRegression()
lr.fit(X_train,y_train)
pred_y=lr.predict(X_train)
#2)Evaluate your in-sample results using the model score,confusion matrix and classification report.
