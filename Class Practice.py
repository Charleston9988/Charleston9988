import pandas as pd
import numpy as np
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import graphviz
from sklearn import tree
import matplotlib.pyplot as plt

titanic = pd.read_csv("C:/Users/EMEKA/Downloads/My Code/Data/titanic.csv")
titanic_2 = pd.read_csv("C:/Users/EMEKA/Downloads/My Code/Data/titanic.csv")
noise = ["Name", "Cabin", "Ticket", "Unnamed: 0"]
titanic = titanic.drop(noise, axis=1)
# These columns were dropped because they seem to have nothing to do with a passenger's death in the titanic ship.
titanic = titanic.dropna()
# Dropped all the missing values rows. rows reduced from 891 to 712. This can adversely affect my research.

dummies = []
cols = ["Sex", "Embarked"]
for columns in cols:
    dummies.append(pd.get_dummies(titanic[cols]))
titanic_dummies = pd.concat(dummies, axis=1)
# Dummies are used for categorical data. And data with recurring numerical data.
titanic = pd.concat((titanic, titanic_dummies), axis=1)
# Used to add the new columns in the data
titanic = titanic.drop(["Sex", "Embarked"], axis=1)
# Drop the initial columns that dummies were applied to.
titanic_2["Age"] = titanic_2["Age"].interpolate()
# The interpolate function predicts and fill in the missing values in a column using the column's available data
print(titanic.info())
print(titanic.head())
print(titanic_2.info())


titanic_new = pd.read_csv ("C:/Users/EMEKA/Downloads/My Code/Data/titanic.csv")

titanic_new['Sex'] = titanic_new['Sex'].apply(lambda x: 1 if x == "male" else 0)
numeric_columns = titanic_new.select_dtypes(include = np.number).columns
titanic_new = titanic_new.fillna(titanic_new[numeric_columns].mean())

titanic_new = titanic_new[numeric_columns]
X = titanic_new.drop("Survived", axis = 1)
y = titanic_new["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# Splits data into train and test data in an automated manner.


model_improved = DecisionTreeClassifier(max_depth = 3)
# NOTE: The Decision Tree Classifier is used for classifying and not predicting.

model_improved.fit(X_train, y_train)
print('train score...' , accuracy_score(y_train, model_improved.predict(X_train)))
print('test score...', accuracy_score(y_test, model_improved.predict(X_test)))

dot_data= tree.export_graphviz(model_improved, out_file=None,impurity=False,
                    feature_names=X_test.columns,
                      filled=True, rounded=True)

graph2=graphviz.Source(dot_data)
print(graph2)
print(X_test.columns)

plot_tree(model_improved)
plt.show()
