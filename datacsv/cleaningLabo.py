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
# Reste à vérif => (levy),cylinders, gear box type, drive wheels, wheel
# Valeurs abbérantes trouvés:
# Vérif format et type de données de chaques colonnes
# ------------------------------------------------------------------

liste_price = []
for elt in df['Doors'].unique():
    liste_price.append(elt)

liste_price.sort()
# print(liste_price)
# print(df)
print(df.loc[df['Model'].str.contains("ა|ბ|გ|დ|ე|ვ|ზ|თ|ი|კ|ლ|მ|ნ|ო|პ|ჟ|რ|ს|ტ|უ|ფ|ქ|ღ|ყ|შ|ჩ|ც|ძ|წ|ჭ|ხ|ჯ|ჰ"
                                      )])
# Faire un split puis un join


def split_and_join(value: list):
    print("value=>", value)
    print(type(value))
    listFinal = []
    for elt in value:
        myArray: list = elt.split(" ")
        myArray.pop(-1)
        finalValue = " ".join(myArray)
        listFinal.append(finalValue)
    print(listFinal)
    return listFinal


# final = split_and_join("ceci est un test")
# print(final)
# print(len(final))
print("avant===========>", len(df.index))
georgian_alphabet_condition = "ა|ბ|გ|დ|ე|ვ|ზ|თ|ი|კ|ლ|მ|ნ|ო|პ|ჟ|რ|ს|ტ|უ|ფ|ქ|ღ|ყ|შ|ჩ|ც|ძ|წ|ჭ|ხ|ჯ|ჰ"
df['Model'].mask(
    df['Model'].str.contains(georgian_alphabet_condition), other=split_and_join(df['Model'].loc[df['Model'].str.contains(georgian_alphabet_condition)].to_list()), inplace=True)
print("après===========>", len(df.index))

print(df.loc[df['Model'].str.contains("ა|ბ|გ|დ|ე|ვ|ზ|თ|ი|კ|ლ|მ|ნ|ო|პ|ჟ|რ|ს|ტ|უ|ფ|ქ|ღ|ყ|შ|ჩ|ც|ძ|წ|ჭ|ხ|ჯ|ჰ"
                                      )])
