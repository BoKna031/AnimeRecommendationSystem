import os

import pandas as pd
import cons


def get_unique_values_from_column(dataframe, column_name, separator):
    collection = set()
    for column_value in dataframe[column_name]:
        values = str(column_value).split(separator)
        collection.update(values)
    result = []
    for value in collection:
        result.append(str.strip(value))
    result.sort()
    return result


def create_table_of_unique_values(dataframe, column_name, separator, filename):
    values = get_unique_values_from_column(dataframe, column_name, separator)
    df = pd.DataFrame(values)
    columns = [column_name]
    df.to_csv(cons.DATASET_FOLDER + os.sep + filename + '.csv', index_label='Id', header=columns)


def create_anime_genre_table():
    anime_df = pd.read_csv(cons.ANIME_CSV_PATH)
    genre_df = pd.read_csv(cons.GENRES_CSV_PATH)
    GEN_COL = 'Genres'
    genre_dict = genre_df.set_index(GEN_COL).T.to_dict('list')
    anime_genre_rows = []
    for ins, anime in anime_df.iterrows():
        gen_keys = str(anime[GEN_COL]).split(', ')
        for key in gen_keys:
            anime_genre_rows.append([anime['MAL_ID'], genre_dict[key][0]])
    pd.DataFrame(anime_genre_rows, columns=['MAL_ID', 'GEN_ID']).to_csv(cons.ANIME_GENRE_CSV_PATH, index=False)


# noinspection SpellCheckingInspection
def remove_inappropriate_content(df, column, separator, inappropriate_content):
    df[column] = df[column].str.split(separator)
    mask = df[column].apply(lambda content: any(inap_cont in content for inap_cont in inappropriate_content))
    inappropriate_df_index = df[mask].index
    df.drop(inappropriate_df_index, inplace=True)
