from cleaning_func import dropRowsWithValues, clean_mileage, clean_price, clean_engine_volume
import pandas as pd
import pandas
alphabet_georgien = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო',
                     'პ', 'ჟ', 'რ', 'ს', 'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']


df = pd.read_csv('./datacsv/car_price_prediction.csv')

# Enlever les colonnes: ID, Levy, Airbags et Color
df = df[['Price', 'Manufacturer', 'Model', 'Prod. year', 'Category', 'Leather interior',
         'Fuel type', 'Engine volume', 'Mileage', 'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel']]

# Valeurs abérantes
print("avant suppr", str(len(df.index)))

df = dropRowsWithValues(df, ['სხვა', 'TESLA'],
                        'Manufacturer')  # Manufacturer => 3 lignes
# 0.5 ; 0.7 ; 0.8 ; 0.3 à ajouter comme valeurs abérantes ? => Faire autrement =>
# extraire turbo dans une nouvelle colonne puis mettre des limites min et max
# df = dropRowsWithValues(
#     df, ['0', '0.1', '0.2', '0.4', '20'], 'Engine volume')  # Engine volume => 47 lignes
df = clean_price(df, min=500, max=1000000)  # Price => 1664 lignes
df = clean_mileage(df, min=500, max=1000000)  # Mileage => 805 lignes
df = clean_engine_volume(df, 0.5, 8)  # Engine volume => 28 lignes
# => Suppr total: 2396

print("après suppr", str(len(df.index)))
# ----------------------------Labos-----------------------------------
# Colonne Model contient des mots en géorgien ... =>
# ces mots sont à suppr sans suppr la ligne !
