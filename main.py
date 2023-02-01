import pandas as pd
import util
import cons

anime1_df = pd.read_csv("dataset/anime_1.csv")
anime2_df = pd.read_csv("dataset/Anime.csv")

genres = util.get_unique_values_from_column(anime1_df, 'Genres', ', ')

print(anime1_df.info())

#inappropriate_content = anime1_df[anime1_df['Genres'].contains('Hentai')].index

util.create_table_of_unique_values(anime1_df, 'Genres', ', ', 'genres')
util.create_anime_genre_table()

tags = util.get_unique_values_from_column(anime2_df, 'Tags', ', ')
print("Genres\n", cons.PRINT_SEP)
print(*genres, sep='\n')
print('\n     size = ', len(genres), '\n', cons.PRINT_SEP)

print("Tags\n", cons.PRINT_SEP)
print(*tags, sep='\n')
print('\n     size = ', len(tags), '\n', cons.PRINT_SEP)




