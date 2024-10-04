+# Importing the libraries
+import numpy as np
+import matplotlib.pyplot as plt
+import pandas as pd
+
+# Importing the dataset
+dataset = pd.read_csv('Data.csv')
+X = dataset.iloc[:, :-1].values
+y = dataset.iloc[:, 3].values
+
+# Encoding categorical data
+from sklearn.preprocessing import LabelEncoder, OneHotEncoder
+labelencoder_X = LabelEncoder()
+X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
+onehotencoder = OneHotEncoder(categorical_features = [0])
+X = onehotencoder.fit_transform(X).toarray()
+
+# Splitting the dataset into the Training set and Test set
+from sklearn.cross_validation import train_test_split
+X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
+
+# Feature Scaling
+from sklearn.preprocessing import StandardScaler
+sc = StandardScaler()
+X_train = sc.fit_transform(X_train)
+X_test = sc.transform(X_test)
