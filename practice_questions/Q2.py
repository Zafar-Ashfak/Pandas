# Write a function in which a player has scored the most runs against 3 teams.

import pandas as pd

df = pd.read_csv('../deliveries.csv')

def get_scores(player_name):
    mask = df['batsman'] == player_name
    return df[mask].groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head(3).index[0]

def main():
    player_name = input("Enter a player name: ")
    res = get_scores(player_name)
    print(f"{player_name} has scored the most runs against {res}")

main()