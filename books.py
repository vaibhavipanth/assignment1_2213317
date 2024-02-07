books (1).py
""books.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/15y-BkzIwYK8FPCOQ2VkoAfb8ULmaSEp3
"""

from google.colab import drive
drive.mount('/content/drive')

#To use the methods in the libraries we import them
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as snb

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/dataset+based+on+uwb+for+clinical+establishments/books.csv")
#here we read the file to work on the data

df.head()
#To take a look at the data

df.tail()
#To see the last half of the data

df.describe()
#To understand the relation between the data

df.info()
#To see the data types used in the dataset

df.isnull()
#To check if any value is null or not

df.duplicated()
#To see if any value is duplicated or not

df['rating'].plot(kind='hist', bins=20, edgecolor='black')
plt.title('Histogram of genere to rating')
plt.xlabel('Rating')
plt.ylabel('No of books')
plt.show()
#to make the histogram of number of books vs rating

x = df[df['genre'] == 'Childrens'].index
#To select all the index of the entries with children as there genre

df.drop(x, inplace=True)
#To delete entries with children as there genre

from sklearn.model_selection import train_test_split

X = df.drop('genre', axis=1)
y = df['genre']

#To Split the dataset into a training set (80%) and a test set (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
