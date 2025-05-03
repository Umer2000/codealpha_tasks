#Explore the Titanic dataset to:Understand its structure,Identify trends & relationships,Detect anomalies,Develop hypotheses for further analysis or modeling

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
titanic = sns.load_dataset('titanic')
#Initial Overview
# Basic info
print(titanic.info())

# Preview data
print(titanic.head())

# Summary statistics
print(titanic.describe(include='all'))
#Univariate Analysis
#Survival Count
sns.countplot(x='survived', data=titanic)
plt.title('Survival Count')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()
#Gender Distribution
sns.countplot(x='sex', data=titanic)
plt.title('Gender Distribution')
plt.show()
#Passenger Class
sns.countplot(x='pclass', data=titanic)
plt.title('Passenger Class Count')
plt.show()
#Bivariate Analysis
#Survival by Sex
sns.countplot(x='sex', hue='survived', data=titanic)
plt.title('Survival by Gender')
plt.show()
#Survival by Class
sns.countplot(x='pclass', hue='survived', data=titanic)
plt.title('Survival by Passenger Class')
plt.show()
#Age Distribution by Survival
sns.histplot(data=titanic, x='age', hue='survived', multiple='stack')
plt.title('Age Distribution by Survival')
plt.show()
print(titanic.isnull().sum())

