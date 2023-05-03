import pandas as pd
from typing import Union


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
