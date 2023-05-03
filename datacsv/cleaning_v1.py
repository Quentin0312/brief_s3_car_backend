import pandas

import pandas as pd
from cleaning_func import dropRowsWithValues, clean_mileage, clean_price

df = pd.read_csv('./datacsv/car_price_prediction.csv')

# Enlever les colonnes: ID, Levy, Airbags et Color
df = df[['Price', 'Manufacturer', 'Model', 'Prod. year', 'Category', 'Leather interior',
         'Fuel type', 'Engine volume', 'Mileage', 'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel']]

# Valeurs abérantes
print("avant suppr", str(len(df.index)))

df = dropRowsWithValues(df, ['სხვა', 'TESLA'],
                        'Manufacturer')  # Manufacturer => 3 lignes
df = dropRowsWithValues(
    df, ['0', '0.1', '0.2', '0.4', '20'], 'Engine volume')  # Engine volume => 47 lignes
df = clean_price(df, min=500, max=1000000)  # Price => 1664 lignes
df = clean_mileage(df, min=500, max=1000000)  # Mileage => 805 lignes
# => Suppr total: 2368


print("après suppr", str(len(df.index)))
# ----------------------------Labos-----------------------------------
