# System Overview
- The frontend is built using streamlit, a python library, that allows for data to be displayed to the user. It will include a visualization of game functions like updating roster and team wheel spin. The primary frontend file is "app.py".
- The backend is the logic side and where the data is actually stored. All the data filtration, game rules, and score calculations happens on the backend. The primary backend file is "game_engine.py".
- The dataset used was imported from "nfl_data_py", which stores real and historical NFL stats, contains all essential data like player names, points, and teams. The pandas library is used to filter the dataset and access specific data points. The primary data filtration file is "data_pipeline.py" and the data handling file is "game_engine.py".
# Data Flow
1. The data is imported from "nfl_data_py" and filtered into a csv file in "data_pipeline.py", which contains all the data needed for the game.
2. The csv file is then used in "game_engine.py" to be further filtered and for accessing specific data points to build the game functions.
3. The data is then displayed on the UI using streamlit and the game state is managed using Streamlit session state, which persists data like the current roster and remaining teams between user interactions.
# State Management
- When the round starts a random week and NFL season are selected and stored in the Streamlit session state until the bonus round.
- The empty roster is stored in the Streamlit session state and updated each time a selection is made with the player name and PPR points.
- The team wheel is stored in the Streamlit session state and the team that was spun gets removed from the state after a selection.
# Deployment
- The app will be hosted on Streamlit Cloud Platform and will be accessible by url. To see the source code and run the app locally, clone this repository and see "requirements.txt" for dependencies.
- The command to run the app locally is "streamlit run app.py". Make sure all dependencies are in place before trying to run the app.