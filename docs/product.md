# Game Overview
- The game starts with an empty roster of seven positions and a randomly selected NFL week and season
- Each turn, a team wheel is spun and a player must be selected, based on their PPR fantasy points from that team to fill any open position in the roster.
- After a selection, the player and their points are saved in the selected roster slot and a new team is spun; this repeats until the roster is full.
- The goal of the game is to have the points for each position on the filled roster add up to 200.
# Roster Structure
- The roster is made of seven slots based on player position
- There is one QB, two RB's, two WR's, one TE, and one FLEX.
- The FLEX position can be filled by any RB, WR, or TE
# Game Initialization
- An empty roster is created.
- A random week from 1-14, and season-year from 2000-2024, are chosen and will not be changed for the rest of the round. Each selection will be based off the selected week and season.
- The team wheel contains all available NFL teams from the selected season, and a jackpot spin.
# Core Gameplay
- Every turn, a team is selected from spinning the team wheel and the highest scoring PPR player for each open position is displayed from the selected team, week, and season.
- Only one player can be selected each turn and they can only go in open roster slots.
- At least one player must be selected each turn.
- After a selection, the previous team is removed from the wheel and the team wheel is spun again, repeating until the roster is filled.
# Special Mechanics
- The jackpot spin is an option on the team wheel which allows any player with the highest points across all teams for one open slot, removing the team constraint. It can only be spun once per round and is removed from the team wheel after it is spun; it is also not guaranteed and has an equal chance to be spun as any other team on the wheel.
- The bonus round happens after the roster is filled: it spins a new season, week, and team, and gives the ability to replace a slot on the roster with a higher scoring player if available. This round is guaranteed after the roster is filled but it is not guaranteed that a higher selection will be available.
# Scoring
- Each player on the roster has a corresponding score based on their real-life performance in the selected game. The scores from each player will be totaled up to the final roster score. The target score for this game is 200 points.
- Fantasy Football PPR scoring format is used to determine the players' points.
# Edge Cases
- Given the event that a player appears twice as an option during a round because of a mid-season trade, they can be added to the roster.
- During the bonus round, the player selected can be the same as one already on the roster and on the same team.
- If the bonus round has no available improvements, then the current roster continues as the final roster. There is only one bonus round no matter what it shows.
- If there is no eligible player given the open roster slots or the player is missing recorded points during a spin, the behavior is TBD.
# Persistent Tracking
- The users highest score ever achieved, total number of rounds played, the number of 200+ point runs, and their all-time highest scoring roster.