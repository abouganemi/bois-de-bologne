import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Verification des donnees
path = "test/adultoldv3.csv"

columns = ["age", "work-class", "fnlwgt", "education", "education-num", "marital-status",
            "occupation", "relationship","race", "sex", "capital-gain", "capital-loss", "hours-per-week",
            "native-country", "income"]
data = pd.read_csv(path, names=columns, sep=',', na_values='?', skipinitialspace=True)

print(data.head())

#Qualite des donnees
print(data.info())
print("nombre de valeurs manquantes - occupation: ", data['occupation'].isnull().sum())
print("nombre de valeurs manquantes - work-class: ", data['work-class'].isnull().sum())
print("nombre de valeurs manquantes - native-country: ", data['native-country'].isnull().sum())

#Statistiques des donnees
print("Statistiques d'age")
print(data['age'].describe())
print("Age Median: ", data['age'].median())
#on fait la meme chose pour les autres attributs


#Visualisation des donnees -- 1
attributs_numerique = data.select_dtypes(include=['int64'])
print(attributs_numerique)
attributs_numerique.hist(figsize=(12,12))
plt.show()

#Visualisation des donnees -- 2
attributs_categoriques = data.select_dtypes(include=['object'])
plt.figure(figsize=(12,6))
sns.countplot(data = attributs_categoriques, x = "work-class")
#on fait la meme chose pour les autres attributs
# Il faut enlever cette ligne de la section précédente pour avoir tous les graphiques
plt.show()

#Relations des donnees
# Explorez les relations entre les attributs, en excluant l'attribut de categorie
# selon la version du module le paramètre height n’est pas nécessaire
sns.pairplot(data, height=3, diag_kind = 'kde', hue='income')
# Calculer la matrice de corrélation
corr = data.corr()
# Mettre en place la figure matplotlib
f, ax = plt.subplots(figsize=(16, 12))
# Générer une palette de couleurs personnalisée
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Dessine la carte de chaleur
_ = sns.heatmap(corr, cmap="YlGn", square=True, ax = ax, annot=True, linewidth = 0.1)
plt.title('Corrélation de Pearson', y=1.05, size=15)
# Il faut enlever cette ligne de la section précédente pour avoir tous les graphiques
plt.show()