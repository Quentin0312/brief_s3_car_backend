import pandas as pd

df = pd.read_csv('./datacsv/car_price_prediction.csv')
# print(df.info())


# Vérif les doublons ID -----------Pas de doublon-------------------
print("avant=> ", len(df.index))
df.drop_duplicates(subset=['ID'], keep='first')
print("après drop_duplicates=> ", len(df.index))


# valeurs manquantes-------------------------------------
df.dropna(inplace=True)
print("après dropna=> ", len(df.index))

# Ici il y a des valeurs manquantes mais elle ne sont pas vide => "_"
df.replace('-', 'NA', inplace=True)
df.drop(df[df['Levy'] == 'NA'].index, inplace=True)
print("après replace '-'=>'NA' puis drop=> ", len(df.index))

# TODO:
# Valeurs abérantes
