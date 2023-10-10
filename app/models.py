from pybaseball import statcast, playerid_lookup
from pybaseball.cache import enable

# Enable caching
enable()


def fetch_player_stats(last_name, first_name, start_date, end_date):
    try:
        player_ids = playerid_lookup(last_name, first_name)
    except ValueError:
        return None

    player_id = player_ids.iloc[0]['key_mlbam']

    data = statcast(start_dt=start_date, end_dt=end_date)


    player_data = data[data['batter'] == player_id]

    return player_data.to_dict(orient='records')
