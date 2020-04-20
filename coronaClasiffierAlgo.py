
#importing
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus as py



#reading XL file as data frame to 'data'
file = r'C:\Users\97250\Desktop\לימודים\R ,python\corona\corona copy clean.xlsx'
xl = pd.ExcelFile(file)
data = xl.parse('Sheet1')

#preparing data
data.loc[data["gender"] == 'female',"gender"] = 0
data.loc[data["gender"] == 'male',"gender"]   = 1

"""
important row for now : how to change a specific column(gender) value(7,2)
from data(data) where some condition(gender==7)    :   
data.loc[data["gender"]==7,"gender"]=2
"""

#choosing columns to work with
col =  ["age","gender","from Wuhan","visiting Wuhan"]  #simple, significant, adjustable.
X   =  data[col]
y   =  data["death"]
y2  =  data["recovered"]

#splitting to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#tree classifier
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#pruned Tree
clf = DecisionTreeClassifier(criterion="entropy", max_depth=2)
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

"""
The same model can be made on the variable y2 - "recovered"
"""

#logistic model
glm = LogisticRegression()
glm = glm.fit (X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


#a graphic tree model
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = col,class_names=['0','1'])
graph = py.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')  #doesn't work here
Image(graph.create_png())  






