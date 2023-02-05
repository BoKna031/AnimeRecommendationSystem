import pandas as pd
import util
import cons

anime_df = pd.read_csv(cons.ANIME_CSV_PATH)
anime_add_info_df = pd.read_csv(cons.ANIME_ADDINFO_CSV_PATH)

genres = util.get_unique_values_from_column(anime_df, 'Genres', ', ')

util.create_table_of_unique_values(anime_df, 'Genres', ', ', 'genres')
util.create_anime_genre_table()

inappropriate_mal_ids = util.remove_inappropriate_content(anime_df, 'Genres', ', ', ['Hentai'])
util.create_clean_rating_csv(inappropriate_mal_ids, ['watching_status', 'watched_episodes'], 'clean_rates')




