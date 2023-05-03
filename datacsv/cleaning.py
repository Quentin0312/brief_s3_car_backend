import pandas as pd
from cleaning_func import dropDuplicates, dropRowWithValue, dropRowsWithValues

df = pd.read_csv('./datacsv/car_price_prediction.csv')
# print(df.info())


# Vérif les doublons ID -----------Pas de doublon-------------------
df = dropDuplicates(df, 'ID')


# valeurs manquantes-------------------------------------
df.dropna(inplace=True)
# print("après dropna=> ", len(df.index))

# Ici il y a des valeurs manquantes mais elle ne sont pas vide => "_"
# df = dropRowWithValue(df, '-', 'Levy')

# Valeurs abérantes
# df = dropRowsWithValues(df, ['სხვა', 'TESLA'], 'Manufacturer')
# print(len(df.index))
# df = dropRowsWithValues(df, ['0', '0.1', '0.2', '0.4', '20'], 'Engine volume')
# df = dropRowWithValue(df, '>5', 'Doors')
# print(len(df.index))

# Vérifier les valeurs distinctes
columns = ['Manufacturer', 'Prod. year', 'Category', 'Leather interior', 'Fuel type',
           'Engine volume', 'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color', 'Airbags']
for column in columns:
    pass
    print(column, "=>", df[column].unique())


# Nettoyer les valeurs abbérantes
#
# TODO:

# Reste à vérif => price, levy, mileage, model
# Valeurs abbérantes trouvés:
# Créer une nouvelle colonne bool turbo
