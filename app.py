import streamlit as st
import pandas as pd
from game_engine import initialize_game, spin_wheel, get_best_players, update_roster, calculate_score, slot_to_position

if "season" not in st.session_state:
    st.session_state.season = None
if "week" not in st.session_state:
    st.session_state.week = None
if "roster" not in st.session_state:
    st.session_state.roster = None
if "df" not in st.session_state:
    st.session_state.df = None
if "teams" not in st.session_state:
    st.session_state.teams = None
if "current_team" not in st.session_state:
    st.session_state.current_team = None
if "game_phase" not in st.session_state:
    st.session_state.game_phase = "init"
if "current_selection" not in st.session_state:
    st.session_state.current_selection = None
if "is_bonus" not in st.session_state:
    st.session_state.is_bonus = False
if "full_df" not in st.session_state:
    st.session_state.full_df = pd.read_csv("app_data.csv")


if st.session_state.week is not None:
    st.write("Season: ", st.session_state.season)
    st.write("Week: ", st.session_state.week)
    for pos, val in st.session_state.roster.items():
        if val is None:
            st.write(f"{pos}: Empty")
        else:
            st.write(f"{pos}: {val['player_display_name']} - {val['fantasy_points_ppr']} pts")
    if st.session_state.is_bonus == True:
        st.title("Bonus Round")

if st.session_state.game_phase == "init":
    st.title("Fantasy Football Game")
    st.write("Build a roster of NFL players from team wheel spins to total 200 fantasy football points")
    if st.button("Start Game"):
        st.session_state.season, st.session_state.week, st.session_state.df, st.session_state.teams, st.session_state.roster = initialize_game(st.session_state.full_df)
        st.session_state.game_phase = "spinning"
        st.rerun()

elif st.session_state.game_phase == "spinning":
    if st.button("Spin Wheel"):
        st.session_state.current_team = spin_wheel(st.session_state.teams)
        st.session_state.game_phase = "selecting"
        st.rerun()

elif st.session_state.game_phase == "selecting":
    if st.session_state.is_bonus == False:
        st.title("Player Selection")
    st.write("Selected Team: ", st.session_state.current_team)
    if st.session_state.is_bonus == True:
        empty_roster = {
        "QB" : None,
        "RB1" : None,
        "RB2" : None,
        "WR1" : None,
        "WR2" : None,
        "TE" : None,
        "FLEX" : None
    }
        best_selection = get_best_players(empty_roster, st.session_state.current_team, st.session_state.df)
    else:
        best_selection = get_best_players(st.session_state.roster, st.session_state.current_team, st.session_state.df)
    if best_selection == False:
        st.session_state.game_phase = "spinning"
        st.rerun()
    if st.session_state.current_selection is None:
        position_order = ["QB", "RB", "WR", "TE"]
        empty_bonus = True
        for position in position_order:
            if position in best_selection and (st.session_state.is_bonus == False or any(
                (slot_to_position[slot] == position or (slot == "FLEX" and position in slot_to_position[slot])) and best_selection[position]["fantasy_points_ppr"] > val["fantasy_points_ppr"] for slot, val in st.session_state.roster.items()
            )):
                st.write(position, best_selection[position])
                empty_bonus = False
                if st.button("Select Player", key = position):
                    st.session_state.current_selection = position
                    st.rerun()
        if empty_bonus == True and st.session_state.is_bonus == True:
            st.session_state.game_phase = "complete"
            st.session_state.is_bonus = False
            st.rerun()
    else:
        for pos, val in st.session_state.roster.items():
            col1, col2, col3 = st.columns([1, 1, 5])
            button_name = None
            with col1:
                st.write(f"**{pos}**")
            with col2:
                st.write(":")
            with col3:
                if val is not None and st.session_state.is_bonus == False:
                    st.write(val)
                elif val is None or st.session_state.is_bonus == True:
                    if st.session_state.is_bonus == True:
                        st.write(val)
                        if (best_selection[st.session_state.current_selection]['fantasy_points_ppr'] > st.session_state.roster[pos]['fantasy_points_ppr']) and (slot_to_position[pos] == st.session_state.current_selection or (pos == "FLEX" and st.session_state.current_selection in slot_to_position[pos])):
                            button_name = "Replace"
                    else:
                        button_name = "Select"
                    if button_name is not None and st.button(button_name, key = pos):
                        valid_update = update_roster(st.session_state.roster, best_selection, st.session_state.current_selection, pos, st.session_state.is_bonus)
                        if valid_update == True:
                            if st.session_state.is_bonus == True:
                                st.session_state.game_phase = "complete"
                                st.session_state.is_bonus = False
                            else:
                                if (all(value is not None for value in st.session_state.roster.values())):
                                    st.session_state.game_phase = "bonus"
                                else:
                                    st.session_state.game_phase = "spinning"
                            st.session_state.current_selection = None
                            st.rerun()
elif st.session_state.game_phase == "bonus":
    st.title("Bonus Round")
    st.session_state.is_bonus = True
    if st.button("Start Bonus Round"):
        st.session_state.season, st.session_state.week, st.session_state.df, st.session_state.teams, empty_roster = initialize_game(st.session_state.full_df)
        st.session_state.game_phase = "spinning"
        st.rerun()
elif st.session_state.game_phase == "complete":
    st.title("Game Complete")
    final_score = calculate_score(st.session_state.roster)
    st.write("Final Score: ", final_score)
    if final_score >= 200:
        st.write("Crossed 200 points")
    else:
        st.write("Under 200 points")
    if st.button("Restart"):
        st.session_state.game_phase = "init"
        st.session_state.week = None
        st.session_state.current_team = None
        st.session_state.current_selection = None
        st.rerun()