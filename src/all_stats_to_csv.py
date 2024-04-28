import json
import pandas as pd
import csv
from pathlib import Path

cwd = Path.cwd()
root = cwd.parent.absolute()

names = pd.read_csv(root / 'data' / 'nba_alias.csv')
adjusted_shooting = pd.read_csv(root / 'data' / 'players_adj_shooting_stats.csv', index_col=0)

with open(root / 'data' / 'player_2pt_defense.json') as file:
	data = json.load(file)
	defense_2s_cols = data['resultSets'][0]['headers']
	defense_2s = {player_info[1]: player_info for player_info in data['resultSets'][0]['rowSet']}

with open(root / 'data' / 'player_3pt_defense.json') as file:
	data = json.load(file)
	defense_3s_cols = data['resultSets'][0]['headers']
	defense_3s = {player_info[1]: player_info for player_info in data['resultSets'][0]['rowSet']}

with open(root / 'data' / 'player_passing_stats.json') as file:
	data = json.load(file)
	passing_cols = data['resultSets'][0]['headers']
	passing = {player_info[1]: player_info for player_info in data['resultSets'][0]['rowSet']}

with open(root / 'data' / 'players_per_game_stats.json') as file:
	data = json.load(file)
	per_game = data[0]
	per_game_cols = ['mins', 'o_reb', 'd_reb', 'stl', 'tov', 'fls', 'team']

with open(root / 'data' / 'players_advanced_stats.json') as file:
	data = json.load(file)
	advanced = data[0]
	advanced_cols = ['o_reb_pct', 'd_reb_pct', 'stl_pct', 'tov_pct', 'usg_pct']


col_names = list(adjusted_shooting.columns)+passing_cols+defense_2s_cols+defense_3s_cols+per_game_cols+advanced_cols
print(col_names)



with open(root / 'data' / 'combined_stats.csv', 'w') as file:
	writer = csv.writer(file)
	writer.writerow(col_names)
	for i in range(names.shape[0]):
		if names.iloc[i, 0] != 'Deonte Burton' and names.iloc[i, 0] != 'Tyler Dorsey' and names.iloc[i, 0] != 'Braxton Key' and names.iloc[i, 0] != 'Marko Simonovic' and names.iloc[i, 0] != 'Donovan Williams':
			bball_ref_name = names.iloc[i, 0]
			nba_com_name = names.iloc[i, 1]
			player_adj_shooting = list(adjusted_shooting[adjusted_shooting['Player'] == bball_ref_name].iloc[0])
			player_passing = passing[nba_com_name]
			player_defense_2s = defense_2s[nba_com_name]
			player_defense_3s = defense_3s[nba_com_name]
			player_per_game = [per_game[bball_ref_name]['mins'], per_game[bball_ref_name]['o_reb'], per_game[bball_ref_name]['d_reb'], per_game[bball_ref_name]['stl'], per_game[bball_ref_name]['tov'], per_game[bball_ref_name]['fls'], per_game[bball_ref_name]['team']]
			player_advanced = [advanced[bball_ref_name]['o_reb_pct'], advanced[bball_ref_name]['d_reb_pct'], advanced[bball_ref_name]['stl_pct'], advanced[bball_ref_name]['tov_pct'], advanced[bball_ref_name]['usg_pct']]
			new_row = player_adj_shooting+player_passing+player_defense_2s+player_defense_3s+player_per_game+player_advanced
			writer.writerow(new_row)





