import streamlit as st
import pandas as pd
from game_engine import initialize_game, spin_wheel, get_best_players, update_roster, calculate_score


#init — game hasn't started yet
#spinning — ready to spin the wheel
#selecting — team has been spun, player selection is shown
#bonus — roster is full, bonus round
#complete — final score is shown



if "season" not in st.session_state:
    st.session_state.season = None
if "week" not in st.session_state:
    st.session_state.week = None
if "roster" not in st.session_state:
    st.session_state.roster = None
if "df" not in st.session_state:
    st.session_state.df = pd.read_csv("app_data.csv")
if "teams" not in st.session_state:
    st.session_state.teams = None
if "current_team" not in st.session_state:
    st.session_state.current_team = None
if "game_phase" not in st.session_state:
    st.session_state.game_phase = "init"
if "current_selection" not in st.session_state:
    st.session_state.current_selection = None


if st.session_state.week is not None:
    st.write("Season: ", st.session_state.season)
    st.write("Week: ", st.session_state.week)
    for pos, val in st.session_state.roster.items():
        if val is None:
            st.write(f"{pos}: Empty")
        else:
            st.write(f"{pos}: {val['player_display_name']} - {val['fantasy_points_ppr']} pts")

if st.session_state.game_phase == "init":
    st.title("Fantasy Football Game")
    st.write("Build a roster of NFL players from team wheel spins to total 200 fantasy football points")
    if st.button("Start Game"):
        st.session_state.season, st.session_state.week, st.session_state.df, st.session_state.teams, st.session_state.roster = initialize_game(st.session_state.df)
        st.session_state.game_phase = "spinning"
        st.rerun()

elif st.session_state.game_phase == "spinning":
    if st.button("Spin Wheel"):
        st.session_state.current_team = spin_wheel(st.session_state.teams)
        st.session_state.game_phase = "selecting"
        st.rerun()

elif st.session_state.game_phase == "selecting":
    st.title("Player Selection")
    st.write("Selected Team: ", st.session_state.current_team)
    best_selection = get_best_players(st.session_state.roster, st.session_state.current_team, st.session_state.df)
    if st.session_state.current_selection is None:
        for position, stats in best_selection.items():
            st.write(position, stats)
            if st.button("Select Player", key = position):
                st.session_state.current_selection = position
                st.rerun()
    else:
        for pos, val in st.session_state.roster.items():
            col1, col2, col3 = st.columns([1, 1, 5])
            with col1:
                st.write(f"**{pos}**")
            with col2:
                st.write(":")
            with col3:
                if val is not None:
                    st.write(val)
                else:
                    if st.button(" ", key = pos):
                        vaild_update = update_roster(st.session_state.roster, best_selection, st.session_state.current_selection, pos)
                        if vaild_update == True:
                            st.session_state.current_selection = None
                            st.session_state.game_phase = "spinning"
                            st.rerun()



    