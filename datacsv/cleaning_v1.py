# TODO: Précisez le nb de ligne suppr à chaque drop

import pandas

import pandas as pd
from cleaning_func import dropDuplicates, dropRowWithValue, dropRowsWithValues, clean_mileage

df = pd.read_csv('./datacsv/car_price_prediction.csv')

# Enlever les colonnes: ID, Levy, Airbags et Color
df = df[['Price', 'Manufacturer', 'Model', 'Prod. year', 'Category', 'Leather interior',
         'Fuel type', 'Engine volume', 'Mileage', 'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel']]

# Valeurs abérantes
print("avant suppr", str(len(df.index)))
df = dropRowsWithValues(df, ['სხვა', 'TESLA'], 'Manufacturer')  # Manufacturer
df = dropRowsWithValues(
    df, ['0', '0.1', '0.2', '0.4', '20'], 'Engine volume')  # Engine volume
df.drop(df[df['Price'] > 1000000].index, inplace=True)  # Price
df.drop(df[df['Price'] < 500].index, inplace=True)  # Price
df = clean_mileage(df, min=500, max=1000000)  # Mileage
# => Suppr total


print("après suppr", str(len(df.index)))
# ----------------------------Labos-----------------------------------
