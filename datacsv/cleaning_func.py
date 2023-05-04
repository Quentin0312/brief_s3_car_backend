import pandas as pd
from typing import Union

# TODO:
# Factoriser les drop selon limites haute et basse
# Et autre
# Utiliser que des masks ou que .loc ?
# Utiliser inplace true le plus possible


def dropRowWithValue(df: pd.DataFrame, value: Union[int, str], column: str):
    df.drop(df[df[column] == value].index, inplace=True)
    return df


def dropRowsWithValues(df: pd.DataFrame, values: list[str], column: str):
    for elt in values:
        df = dropRowWithValue(df, elt, column)
    return df


def clean_mileage(df: pd.DataFrame, min: int, max: int):
    # Remplacer les valeurs str par int
    df['Mileage'] = df['Mileage'].mask(
        df['Mileage'].notnull(), other=df['Mileage'].str[:-3])

    # Typecast la series en int
    df['Mileage'] = df['Mileage'].astype(int)

    # Suppr les valeurs abérantes
    df.drop(df[df['Mileage'] < min].index, inplace=True)
    df.drop(df[df['Mileage'] > max].index, inplace=True)
    return df


def clean_price(df: pd.DataFrame, min: int, max: int):
    df.drop(df[df['Price'] < min].index, inplace=True)
    df.drop(df[df['Price'] > max].index, inplace=True)
    return df


def clean_engine_volume(df: pd.DataFrame, min: float, max: float):
    # Créer une nouvelle colone turbo remplit
    df.loc[df['Engine volume'].str.contains('Turbo'), 'Turbo'] = True
    df.loc[df['Turbo'] != True, 'Turbo'] = False

    # Nettoyer la colonne modèle
    df['Engine volume'].mask(
        df['Engine volume'].str.contains('Turbo'), other=df['Engine volume'].str[:-6], inplace=True)

    # Changer le type de la serie
    df['Engine volume'] = df['Engine volume'].astype(float)

    # Supprimer les valeurs abérantes
    df.drop(df[df['Engine volume'] < min].index, inplace=True)
    df.drop(df[df['Engine volume'] > max].index, inplace=True)
    return df


def clean_doors(df: pd.DataFrame):
    for elt in [['02-Mar', '3'], ['04-May', '5'], ['>5', '5']]:
        df['Doors'] = df['Doors'].mask(
            df['Doors'].str.contains(elt[0]), other=elt[1])
    return df


def clean_model(df: pd.DataFrame):
    # TODO: 2 valeurs encore à nettoyer
    georgian_alphabet_condition = "ა|ბ|გ|დ|ე|ვ|ზ|თ|ი|კ|ლ|მ|ნ|ო|პ|ჟ|რ|ს|ტ|უ|ფ|ქ|ღ|ყ|შ|ჩ|ც|ძ|წ|ჭ|ხ|ჯ|ჰ"

    def split_and_join(value: list[str]):
        listFinal = []
        for elt in value:
            myArray: list = elt.split(" ")
            myArray.pop(-1)
            finalValue = " ".join(myArray)
            listFinal.append(finalValue)
        return listFinal

    df['Model'].mask(
        df['Model'].str.contains(georgian_alphabet_condition), other=split_and_join(df['Model'].loc[df['Model'].str.contains(georgian_alphabet_condition)].to_list()), inplace=True)
    # print(df.loc[df['Model'].str.contains("ა|ბ|გ|დ|ე|ვ|ზ|თ|ი|კ|ლ|მ|ნ|ო|პ|ჟ|რ|ს|ტ|უ|ფ|ქ|ღ|ყ|შ|ჩ|ც|ძ|წ|ჭ|ხ|ჯ|ჰ"
    #                                       )])

    return df


def clean_cylinders(df: pd.DataFrame, min: float, max: float):
    df.drop(df[df['Cylinders'] < min].index, inplace=True)
    df.drop(df[df['Cylinders'] > max].index, inplace=True)
    return df
