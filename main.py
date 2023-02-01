import pandas as pd
import util
import cons

anime_df = pd.read_csv(cons.ANIME_CSV_PATH)
anime_add_info_df = pd.read_csv(cons.ANIME_ADDINFO_CSV_PATH)
old_size = anime_df.size
print("anime_df size before drop: ", old_size)

genres = util.get_unique_values_from_column(anime_df, 'Genres', ', ')

util.create_table_of_unique_values(anime_df, 'Genres', ', ', 'genres')
util.create_anime_genre_table()
util.remove_inappropriate_content(anime_df, 'Genres', ', ', ['Hentai'])

print("anime_df size after drop: ", anime_df.size)
print("difference: ", old_size-anime_df.size)

inappropriate_df = pd.read_csv(cons.INAPPROPRIATE_CSV_PATH)
print("inappropriate content size: ", inappropriate_df.size)
#tags = util.get_unique_values_from_column(anime_add_info_df, 'Tags', ', ')
'''
print("Genres\n", cons.PRINT_SEP)
print(*genres, sep='\n')
print('\n     size = ', len(genres), '\n', cons.PRINT_SEP)



print("Tags\n", cons.PRINT_SEP)
print(*tags, sep='\n')
print('\n     size = ', len(tags), '\n', cons.PRINT_SEP)
'''



