# reminder practise in jupyter notebook
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

muslims_data = pd.read_csv('muslims.csv')
X = muslims_data.drop(columns=['country'])
y = muslims_data['country']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)
score