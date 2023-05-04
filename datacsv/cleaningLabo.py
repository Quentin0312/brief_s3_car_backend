# V1: Utiliser seulement ces colonnes=>
# Toutes sauf levy, airbags et color

import pandas as pd

df = pd.read_csv('./datacsv/car_price_prediction.csv')
# print(df.info())

print(len(df.index))
# Vérif les doublons ID -----------Pas de doublon-------------------
df.drop_duplicates(subset=['ID'], keep='first', inplace=True)
print(len(df.index))

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


# TODO:
# Reste à vérif => (levy)
# ------------------------------------------------------------------

liste_price = []
for elt in df['Fuel type'].unique():
    liste_price.append(elt)

liste_price.sort()
print(liste_price)
print(df)
