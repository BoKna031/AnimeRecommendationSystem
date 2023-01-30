import pandas as pd
import util
import cons

anime1_df = pd.read_csv("dataset/anime_1.csv")
anime2_df = pd.read_csv("dataset/Anime.csv")

print(anime2_df.info())
genres = util.get_unique_values_from_column(anime1_df, 'Genres', ',')

tags = util.get_unique_values_from_column(anime2_df, 'Tags', ',')
print("Genres\n", cons.PRINT_SEP)
print(*genres, sep='\n')
print('\n     size = ', len(genres), '\n', cons.PRINT_SEP)

print("Tags\n", cons.PRINT_SEP)
print(*tags, sep='\n')
print('\n     size = ', len(tags), '\n', cons.PRINT_SEP)




