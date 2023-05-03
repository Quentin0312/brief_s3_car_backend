import pandas as pd


def dropDuplicates(df, column):
    # print("avant=> ", len(df.index))
    df.drop_duplicates(subset=[column], keep='first')
    # print("après drop_duplicates=> ", len(df.index))
    return df


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
