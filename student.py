import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('dataset.csv')

X = np.array(data.iloc[:, 0:4])
Y = np.array(data.iloc[:, 4])

le = LabelEncoder()
Y = le.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

rf_model = RandomForestClassifier()
rf_model.fit(X_train, Y_train)

with open('student_dropout1.pkl', 'wb') as file:
    pickle.dump(rf_model, file)
