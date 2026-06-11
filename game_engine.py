import random 
import pandas as pd

df = pd.read_csv("app_data.csv")

slot_to_position = {
    "QB" : "QB",
    "RB1" : "RB",
    "RB2" : "RB",
    "WR1" : "WR",
    "WR2" : "WR",
    "TE" : "TE",
    "FLEX" : ["RB", "WR", "TE"]
}

def initialize_game(df):
    season = random.randint(2000, 2024)
    week = random.randint(1, 14)

    roster = {
        "QB" : None,
        "RB1" : None,
        "RB2" : None,
        "WR1" : None,
        "WR2" : None,
        "TE" : None,
        "FLEX" : None
    }
    df = df[df["season"] == season]
    df = df[df["week"] == week]

    teams = df["recent_team"].unique().tolist()
    return season, week, df, teams, roster

def spin_wheel(teams):
    selected_team = random.choice(teams)
    teams.remove(selected_team)
    return selected_team

def get_best_players(roster, selected_team, df):
    best_selection = {}
    seen_positons = set()
    for key, value in roster.items():
        if value is None  and key != "FLEX" and slot_to_position[key] not in seen_positons:
            filtered = df[(df["position"] == slot_to_position[key]) & (df["recent_team"] == selected_team)]
            best_player = filtered.loc[filtered["fantasy_points_ppr"].idxmax(), ["player_display_name", "fantasy_points_ppr"]]
            best_selection[slot_to_position[key]] = best_player
            seen_positons.add(slot_to_position[key])
    return best_selection

def update_roster(current_roster, best_selection, position, selection):
    if position == slot_to_position[selection] or (selection == "FLEX" and position in slot_to_position[selection]):
        player_data = best_selection[position]
        current_roster[selection] = player_data

def calculate_score(finished_roster):
    total = 0
    for key, value in finished_roster.items():
        if value is not None:
            total += value["fantasy_points_ppr"]
    return total

season, week, df, teams, roster = initialize_game(df)
selected_team = spin_wheel(teams)
best_roster = get_best_players(roster, selected_team, df)
print(roster)
print()
update_roster(roster, best_roster, 'RB', "FLEX")
print(roster)
print()
'''
selected_team = spin_wheel(teams)
best_roster = get_best_players(roster, selected_team, df)
print(best_roster)
print()
update_roster(roster, best_roster, "RB", 'FLEX')
print(roster)
print()
selected_team = spin_wheel(teams)
best_roster = get_best_players(roster, selected_team, df)
print(best_roster)
print()
update_roster(roster, best_roster, "WR", 'WR2')
print(roster)
print()
points = calculate_score(roster)
print(points)
'''