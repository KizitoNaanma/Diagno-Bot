import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('static/data/clean/Training.csv')

# df.info()
# df['prognosis'].unique()

X = df.iloc[:, :-1]
y = df['prognosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)

rf_clf = RandomForestClassifier()
rf_clf.fit(X_train, y_train)

print("Accuracy on split test: ", rf_clf.score(X_test,y_test))

symptoms_dict = {}

for index, symptom in enumerate(X):
    symptoms_dict[symptom] = index

input_vector = np.zeros(len(symptoms_dict))

with open('mod.pkl', 'wb') as f:
    pickle.dump(df, f)
    pickle.dump(rf_clf, f)
    pickle.dump(symptoms_dict, f)
