import nfl_data_py as nfl
import pandas as pd

data = nfl.import_weekly_data(list(range(2000, 2025)))
data = data[data["week"] <= 14]
data = data[data["position"].isin(["QB", "RB", "WR", "TE"])]
data = data[["player_display_name", "position", "recent_team", "week", "season", "opponent_team", "fantasy_points_ppr"]]
data.to_csv("app_data.csv", index = False)