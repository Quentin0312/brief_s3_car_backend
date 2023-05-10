# TODO: Suppr les poublons
#  Certains model nom doublé ex (x-trail x-trail)
# fmt: off
from cleaning_func import clean_manufacturer, clean_mileage, clean_price, clean_engine_volume, clean_doors, clean_model, clean_cylinders, clean_wheel, clean_leather_interior
import pandas as pd
import pandas
alphabet_georgien = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ',
                     'ო', 'პ', 'ჟ', 'რ', 'ს', 'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ',
                     'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']


df = pd.read_csv('./datacsv/original.csv')

# Colonnes enlevés: ID, Levy, Airbags et Color
df = df[['Price', 'Manufacturer', 'Model', 'Prod. year', 'Category', 'Leather interior',
         'Fuel type', 'Engine volume', 'Mileage', 'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel']]

print(len(df.index))

# fmt: on
# Valeurs abérantes
print("avant suppr", str(len(df.index)))

df = clean_manufacturer(
    df, ["სხვა", "TESLA"], "Manufacturer"
)  # Manufacturer => 3 lignes
df = clean_price(df, min=500, max=1000000)  # Price => 1664 lignes
df = clean_mileage(df, min=500, max=1000000)  # Mileage => 677 lignes
df = clean_engine_volume(df, 0.5, 8)  # Engine volume => 28 lignes
df = clean_cylinders(df, min=3.0, max=12)  # Cylinders => 37 lignes
df = clean_doors(df)  # Doors => 0 lignes
df = clean_model(df)  # Model => 0 lignes
df = clean_wheel(df)  # Wheel => 0 lignes
df = clean_leather_interior(df)  # Leather interior => 0 lignes
print("après suppr", str(len(df.index)))
# => Suppr total: 2409

# No need to clean "Gear box type", "Drive wheels", "Prod. year", "Category", "Fuel type"

# ---------------------------------------------------------------------------------------------
# Labo mini poc

# enregistrer un échantillon propre du csv avec les colonnes: "Manufacturer", "Mileage" et "Prod. year"
print(df.info())
mini_poc_df = df.iloc[:, [0, 1, 3, 8]].copy()
print(mini_poc_df.dtypes)

# Enregistrer le nouveau csv
# mini_poc_df.to_csv("./datacsv/mini_poc.csv", index=False)
df["ID"] = df.index
print(df.head())
df.to_csv("./datacsv/cleaned_v1.csv", index=False)
