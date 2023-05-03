# V1: Utiliser seulement ces colonnes=>
# Toutes sauf levy, airbags et color

import pandas as pd
from cleaning_func import dropRowWithValue, dropRowsWithValues

df = pd.read_csv('./datacsv/car_price_prediction.csv')
# print(df.info())


# Vérif les doublons ID -----------Pas de doublon-------------------
# df.drop_duplicates(subset=['ID'], keep='first', inplace=True)


# valeurs manquantes---------------Aucune-----------
# df.dropna(inplace=True)

# Ici il y a des valeurs manquantes mais elle ne sont pas vide => "-"
# df = dropRowWithValue(df, '-', 'Levy')

# Valeurs abérantes
# df = dropRowsWithValues(df, ['სხვა', 'TESLA'], 'Manufacturer')
# df = dropRowsWithValues(df, ['0', '0.1', '0.2', '0.4', '20'], 'Engine volume')
# print(len(df.index))

# Vérifier les valeurs distinctes
columns = ['Manufacturer', 'Prod. year', 'Category', 'Leather interior', 'Fuel type',
           'Engine volume', 'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color', 'Airbags']
for column in columns:
    pass
    # print(column, "=>", df[column].unique())


# Nettoyer les valeurs abbérantes
#
# TODO:
# remplacer les valeur par 02-Mar=>3 ; 04-May=>5 ; >5 => 5
# Reste à vérif => (levy), model
# Valeurs abbérantes trouvés:
# Créer une nouvelle colonne bool turbo
# Vérif format et type de données de chaques colonnes
# Utiliser df.plot.hist()
# Faire un notebook
# -----------------------------------------------------------------
# print(df['Price'].unique())
# liste_price = []
# for elt in df['Mileage'].unique():
#     liste_price.append(int(elt[:-3]))

# liste_price.sort()
# print(liste_price)

# df['Mileage'] = df['Mileage'].mask(df['Mileage'].notnull(),
#                                    other=df['Mileage'].str[:-3])

# print(df.dtypes)
# df['Mileage'] = df['Mileage'].astype(int)
# print(df.dtypes)
# print(df.head())
# ------------------------------------------------------------------
liste_price = []
for elt in df['Model'].unique():
    liste_price.append(elt)

liste_price.sort()
print(liste_price)
