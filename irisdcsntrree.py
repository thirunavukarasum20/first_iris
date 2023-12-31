# -*- coding: utf-8 -*-
"""irisdcsntrree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UbLJoms2X-1LDg3HfXKbTnIoXnTsOHOn
"""

## Importing the necessary libraries

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset

iris = load_iris ()

#Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split ( iris.data, iris. target, test_size=0.2, random_state=42)

# Create a decision tree classifier

clf = DecisionTreeClassifier()

#Train the classifier on the training data
clf.fit(X_train, y_train)
# Make predictions on the testing data
predictions = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)