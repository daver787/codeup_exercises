# Do your work for these exercises in either a notebook or file name `model`
from aquire import get_iris_data
#from aquire import get_titanic_data
#from prepare import prep_titanic
from prepare import prep_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#ignore warnings
import warnings
warnings.filterwarnings("ignore")






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
print(lr.score(X_train,y_train))
print(confusion_matrix(y_train,pred_y))
labels=sorted(iris_df.species_name.unique())
print(pd.DataFrame(confusion_matrix(y_train,pred_y),index=labels,columns=labels))
print(classification_report(y_train,pred_y))

#3) Print and clearly label the following:Accuracy,true positive rate,false positive rate,true negative rate,false negative rate,
# false negative rate,precision,recall,f1-score,and support. 


#4) Look in the scikit-learn documentation to research the solver parameter. What is your best option
#for the particular problem you are trying to solve and the data to be used.



#5) Run through steps 2-4 using another solver
logit_fit=LogisticRegression(solver='saga')
logit_fit.fit(X_train,y_train)
pred_logit=logit_fit.predict(X_train)

#6) Which performs better on your in-sample data?
print(pred_logit.score(X_train,y_train))
print(pd.DataFrame(confusion_matrix(y_train,pred_logit),index=labels,columns=labels))
print(classification_report(y_train,pred_logit))
#7)Save the best model in logit_fit


#Decision Tree

#1)Fit the decision tree classifier to your training sample and transform(i.e. make predictions on your training sample)
dt=DecisionTreeClassifier()
dt.fit(X_train,y_train)
pred_tree=dt.predict(X_train)

#2)Evaluate your in-sample results using the model score,confusion matrix,and classification report.
print(dt.score(X_train,y_train))
print(pd.DataFrame(confusion_matrix(y_train,pred_tree),index=labels,columns=labels))
print(classification_report(y_train,pred_tree))
#3) Print and clearly label the following:Accuracy,true positive rate,false positive rate,true negative rate,false negative rate,
# false negative rate,precision,recall,f1-score,and support. 

#4)Run through 2-4 using entropy as your measure of impurity
tree_fit=DecisionTreeClassifier(criterion='entropy')
tree_fit.fit(X_train,y_train)
pred_treeg=tree_fit.predict(X_train)

print(dtg.score(X_train,y_train))
print(pd.DataFrame(confusion_matrix(y_train,pred_treeg),index=labels,columns=labels))
print(classification_report(y_train,pred_treeg))
#5) Which performs better on your in-sample data?
# They both performed the same

#6)Save the best model in `tree_fit`


#KNN

#1)Fit the K-Nearest Neighbors classifier to your training sample and transform
#(make predictions on the training sample)
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
pred_default=knn.predict(X_train)

#2)Evaluate your in-sample results using the model score,confusion matrix,and classification report.
print(knn.score(X_train,y_train))
print(pd.DataFrame(confusion_matrix(y_train,pred_default),index=labels,columns=labels))
print(classification_report(y_train,pred_default))

#3) Print and clearly label the following:Accuracy,true positive rate,false positive rate,true negative rate,false negative rate,
# false negative rate,precision,recall,f1-score,and support. 

#4)Run through steps 2-4 setting k=10
knn_10=KNeighborsClassifier(n_neighbors=10)
knn_10.fit(X_train,y_train)
pred_10=knn_10.predict(X_train)


print(knn_10.score(X_train,y_train))
print(pd.DataFrame(confusion_matrix(y_train,pred_10),index=labels,columns=labels))
print(classification_report(y_train,pred_10))

#5)Run through steps 2-4 setting k=20
knn_20=KNeighborsClassifier(n_neighbors=20)
knn_20.fit(X_train,y_train)
pred_20=knn_20.predict(X_train)

print(knn_20.score(X_train,y_train))
print(pd.DataFrame(confusion_matrix(y_train,pred_20),index=labels,columns=labels))
print(classification_report(y_train,pred_20))

#6) What are the differences in the evaluation metrics? Which performs better on your in-sample
#data? Why?

#7) Save the best model in `knn_fit`


#Random Forest

#1) Fit the Random Forest classifier to your training sample and transform(i.e. make predictions on the sample training)
#setting the random_state accordingly and setting min_samples_leaf=1 and max_depth=20.
rf=RandomForestClassifier(min_samples_leaf=1,max_depth=20)
rf.fit(X_train,y_train)
pred_default=rf.predict(X_train)

#2)Evaluate your in-sample results using the model score,confusion matrix,and classification report.
print(rf.score(X_train,y_train))
print(pd.DataFrame(confusion_matrix(y_train,pred_default),index=labels,columns=labels))
print(classification_report(y_train,pred_default))

#3) Print and clearly label the following:Accuracy,true positive rate,false positive rate,true negative rate,false negative rate,
# false negative rate,precision,recall,f1-score,and support. 

#4)Run through steps increasing your min_samples_leaf to 5 and decreasing your max_depth to 3
rf_shallow=RandomForestClassifier(min_samples_leaf=5,max_depth=3)
rf_shallow.fit(X_train,y_train)
pred_shallow=rf.predict(X_train)

print(rf.score(X_train,y_train))
print(pd.DataFrame(confusion_matrix(y_train,pred_default),index=labels,columns=labels))
print(classification_report(y_train,pred_default))
#5) What are the differences in the evaluation metrics? Which performs better on your in-sample data?
#Why?

#6) Save the best model in forest_fit





































