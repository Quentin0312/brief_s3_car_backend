import pandas as pd
from typing import Union

# TODO:
# Factoriser les drop selon limites haute et basse


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
    df['Engine volume'] = df['Engine volume'].mask(
        df['Engine volume'].str.contains('Turbo'), other=df['Engine volume'].str[:-6])

    # Changer le type de la serie
    df['Engine volume'] = df['Engine volume'].astype(float)

    # Supprimer les valeurs abérantes
    df.drop(df[df['Engine volume'] < min].index, inplace=True)
    df.drop(df[df['Engine volume'] > max].index, inplace=True)
    return df
