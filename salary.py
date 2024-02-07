"""salary.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/19n8n-cG0CZh5kBeUdPRNtcxzi2AEg6ZT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
#to be used for various functions

#to read the file and get the data
df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/dataset+based+on+uwb+for+clinical+establishments/salaries_clean.csv")

df.head()
#To view the data that we have just loaded

df.tail()
#To see the lower part of the data

df.info()
#To check all the Items and their data types

df.describe()
#To see if there is any corelation between any 2 columns

df.isnull()
#To check if there is any value missing

df.duplicated()
#To see I any values have been duplicated and remove them so that the data could yeild more accuracy

type_counts = df['Company_Size'].value_counts()
#To see how many employes are there from each cap company

print(type_counts)

category_L_rows = df[df['Company_Size'] == 'L'].index
category_M_rows = df[df['Company_Size'] == 'M'].index
category_S_rows = df[df['Company_Size'] == 'S'].index
#To get the indexes of all diffrent types of company into diffrent variable

mean_valueL = df.loc[category_L_rows, 'Salary_USD'].mean()
mean_valueM = df.loc[category_M_rows, 'Salary_USD'].mean()
mean_valueS = df.loc[category_S_rows, 'Salary_USD'].mean()
#To get the avrage value of salary given in each cap of company

print(mean_valueL)
print(mean_valueM)
print(mean_valueS)

Avrage_salary = {
    'Large cap':113857.28282828283,'Mid cap':111625.3282208589,'small cap':74126.31325301205
}
salary = list(Avrage_salary.keys())
value = list(Avrage_salary.values())
#made a dictionary manually and 2 list from it to show visually

plt.bar(salary, value, color ='Orange',
        width = 0.4)

plt.xlabel("Diffrent types of companies")
plt.ylabel("avrage salaries")
plt.title("salary comparison")
plt.show()
#made a bar graph to show the diffrence in pay of diffrent caps of company

from sklearn.model_selection import train_test_split
features = df.drop(['Designation','Experience','Salary_USD'], axis=1)
target = df['Salary_USD']
X_train , X_test , y_train , y_test = train_test_split(features, target, test_size=0.2, random_state=42)
print("testing set shape:", X_train.shape, y_train.shape)
print("trainig set shape:", X_test.shape, y_test.shape)
