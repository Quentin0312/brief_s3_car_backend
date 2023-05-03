import pandas as pd
# TODO: simplifier ou suppr les fonct
# tout typer ?


def dropDuplicates(df, column):
    # print("avant=> ", len(df.index))
    df.drop_duplicates(subset=[column], keep='first')
    # print("après drop_duplicates=> ", len(df.index))
    return df

# TODO: Remplacement par NA inutile !


def dropRowWithValue(df, value, column, replaceWith='NA'):
    df.replace(value, replaceWith, inplace=True)
    df.drop(df[df[column] == replaceWith].index, inplace=True)
    # print("après replace ", value, "=>", replaceWith,
    #   " puis drop=> ", len(df.index))
    return df


def dropRowsWithValues(df, values, column):
    for elt in values:
        df = dropRowWithValue(df, elt, column)
    return df


def clean_mileage(df: pd.DataFrame, min, max):
    # Remplacer les valeurs str par int
    df['Mileage'] = df['Mileage'].mask(
        df['Mileage'].notnull(), other=df['Mileage'].str[:-3])
    # Typecast la series en int
    df['Mileage'] = df['Mileage'].astype(int)
    # Suppr les valeurs abérantes
    df.drop(df[df['Mileage'] < min].index, inplace=True)
    df.drop(df[df['Mileage'] > max].index, inplace=True)
    return df
