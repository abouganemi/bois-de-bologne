import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "H:/bois-de-bologne/class - 3/test/adultoldv3.csv"

columns = ["age", "work-class", "fnlwgt", "education", "education-num",
           "marital-status", "occupation", "relationship", "race",
           "sex", "capital-gain", "capital-loss", "hours-per-week",
           "native-country", "income"]

data = pd.read_csv(path, names=columns, sep=',',
                   na_values='?', skipinitialspace=True)
print(data.head())
print("###"*20)
print(data.info())
print("number of missing values - occupation: ",
      data['occupation'].isnull().sum())
print("number of missing values - work-class: ",
      data['work-class'].isnull().sum())
print("number of missing values - native-country: ",
      data['native-country'].isnull().sum())
print("###"*20)
print("Age statistics")
print(data['age'].describe())
print("Median age: ", data['age'].median())
print("###"*20)
numeric_attributes = data.select_dtypes(include=['int64'])
print(numeric_attributes)
numeric_attributes.hist(figsize=(12, 12))
categorical_attributes = data.select_dtypes(include=['object'])
plt.figure(figsize=(12, 6))
sns.countplot(data=categorical_attributes, x="work-class")
print("###" * 20)
sns.pairplot(data, height=3, diag_kind='kde', hue='income')
corr = data.corr()
# Mettre en place la figure matplotlib
f, ax = plt.subplots(figsize=(16, 12))
# Générer une palette de couleurs personnalisée
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Dessine la carte de chaleur
_ = sns.heatmap(corr, cmap="YlGn", square=True,
                ax=ax, annot=True, linewidth=0.1)
plt.title('Correlation of Pearson', y=1.05, size=15)
plt.show()
