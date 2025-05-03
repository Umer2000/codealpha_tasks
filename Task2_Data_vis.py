#Create clear and compelling visualizations of the Titanic dataset to uncover survival patterns and insights.import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset from seaborn
titanic = sns.load_dataset('titanic')

# View first few rows
print(titanic.head())
plt.figure(figsize=(6, 4))
sns.countplot(data=titanic, x='survived', palette='Set2')
plt.title('Survival Count')
plt.xticks([0, 1], ['Not Survived', 'Survived'])
plt.ylabel('Count')
plt.show()
plt.figure(figsize=(6, 4))
sns.countplot(data=titanic, x='sex', hue='survived', palette='pastel')
plt.title('Survival by Sex')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()
plt.figure(figsize=(6, 4))
sns.countplot(data=titanic, x='pclass', hue='survived', palette='muted')
plt.title('Survival by Passenger Class')
plt.xlabel('Passenger Class (1 = Upper, 3 = Lower)')
plt.show()
plt.figure(figsize=(8, 5))
sns.histplot(data=titanic, x='age', hue='survived', multiple='stack', palette='coolwarm', bins=30)
plt.title('Age Distribution by Survival')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(data=titanic, x='pclass', y='age', palette='Accent')
plt.title('Age Distribution per Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()

