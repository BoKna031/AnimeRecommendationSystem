import pandas as pd
import util
import cons

anime_df = pd.read_csv(cons.ANIME_CSV_PATH)
anime_add_info_df = pd.read_csv(cons.ANIME_ADDINFO_CSV_PATH)

genres = util.get_unique_values_from_column(anime_df, 'Genres', ', ')

util.create_table_of_unique_values(anime_df, 'Genres', ', ', 'genres')
util.create_anime_genre_table()

inappropriate_mal_ids = util.remove_inappropriate_content(anime_df, 'Genres', ', ', ['Hentai'])
print('Total number of animes: ', anime_df.shape[0])
#util.create_clean_rating_csv(inappropriate_mal_ids, ['watching_status', 'watched_episodes'], 'clean_rates')

rating_df = pd.read_csv(cons.CLEAN_USER_RATINGS_CSV_PATH)
voted_anime_num = len(rating_df['anime_id'].unique())
print('Voted animes: ', voted_anime_num)
user_num = len(rating_df['user_id'].unique())
print('Users: ', user_num)
rating_count = rating_df.shape[0]
print('Rating count: ', rating_count)
density = rating_count*100/(user_num*voted_anime_num)
print('Matrix is', 'sparse' if density < 50 else 'dense', 'with density of ', round(density, 2), '%')
