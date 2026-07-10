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
    seen_positions = set()
    for key, value in roster.items():
        if value is None  and key != "FLEX" and slot_to_position[key] not in seen_positions:
            filtered = df[(df["position"] == slot_to_position[key]) & (df["recent_team"] == selected_team)]
            seen_positions.add(slot_to_position[key])
            if filtered.empty:
                continue
            else:
                best_player = filtered.loc[filtered["fantasy_points_ppr"].idxmax(), ["player_display_name", "fantasy_points_ppr"]]
                best_selection[slot_to_position[key]] = best_player
        elif value is None and key == "FLEX":
            top_val = {
                "player_display_name" : " ",
                "fantasy_points_ppr" : 0
            }
            top_pos = None
            for position in slot_to_position["FLEX"]:
                if all(value is not None for key, value in roster.items() if slot_to_position[key] == position):
                    filtered = df[(df["position"] == position) & (df["recent_team"] == selected_team)]
                    if filtered.empty:
                        continue
                    else:
                        best_player = filtered.loc[filtered["fantasy_points_ppr"].idxmax(), ["player_display_name", "fantasy_points_ppr"]]
                        if best_player["fantasy_points_ppr"] > top_val["fantasy_points_ppr"]:
                            top_val = best_player
                            top_pos = position
            if top_pos is not None:
                best_selection[top_pos] = top_val
    if not best_selection:
        return False
    return best_selection

def update_roster(current_roster, best_selection, position, selection, is_bonus):
    if position == slot_to_position[selection] or (selection == "FLEX" and position in slot_to_position[selection]):
        if is_bonus == True and (current_roster[selection]["fantasy_points_ppr"] >= best_selection[position]["fantasy_points_ppr"]):
            return False
        else:
            if (is_bonus is False and current_roster[selection] is None) or is_bonus is True:
                player_data = best_selection[position]
                current_roster[selection] = player_data
                return True
            else:
                return False
    else:
        return False

def calculate_score(finished_roster):
    total = 0
    for key, value in finished_roster.items():
        if value is not None:
            total += value["fantasy_points_ppr"]
    return round(total)