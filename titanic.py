"""TITANIC PROJECT
 This project will try to answer these questions:
(1)Who were the passengers on titanic?[Ages, Gender, Class, ... etc]
(2)What deck were the passengers and how does that relate to their class?
(3)Where did the passengers come from?
(4)Who was alone and who was with family?
(5)What factors helped someone survive the sinking? """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read the csv file
titanic_df = pd.read_csv("titanic.csv")
print(titanic_df.head())

#Visualize the distribution of ages of
# the passengers
plt.figure(figsize=(10, 6))
sns.histplot(data=titanic_df, x = 'age', hue='sex')
plt.title('Age distribution by Gender')
plt.show()

#Analyze survival rates based on
#passenger class
plt.figure(figsize=(10, 6))
sns.barplot(data=titanic_df, x = 'pclass', y='survived', hue='sex')
plt.title('Survival rate by passenger class and gender')
plt.show()

#Analyze survival rate based on 
#embarkation port
plt.figure(figsize=(10, 6))
sns.boxplot(data=titanic_df, x='pclass', y='fare', hue='survived')
plt.ylim(0, 300) #limitin y-axis for better vizualisation
plt.title('Fare distribution by passenger class and survival')
plt.show()

#Analyze survival count based on 
#family size
titanic_df['family_size'] = titanic_df['sibsp'] + titanic_df['parch']
plt.figure(figsize=(10, 6))
sns.countplot(data=titanic_df, x='family_size', hue='survived')
plt.title('Survival count based on family size')
plt.show()

#Analyze survival rates based on 
#number of siblings and spouses 
#aboard the ship
plt.figure(figsize=(10, 6))
sns.countplot(data=titanic_df, x='sibsp', hue='survived')
plt.title('Survival count based on number of siblings/spouses aboard')
plt.show()