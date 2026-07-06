# MVP Checklist
- [x] Data Pipeline and CSV Generation - Filter data from nfl_data_py to required data points and upload it into a CSV file
- [x] Game Initialization - Randomly generate an NFL week (1-14) and season (2000-2024) for the beginning of a round
- [x] Team Wheel Spin - Randomly select a team from all nfl teams for a selection spin and remove it from the options after a selection is made
- [x] Player Selection Per Position - Give options of best players, given the game initialization and team spin, for each open position on the roster and allow only one selection per spin
- [x] Roster Management - Track all filled and open positions in the roster to only allow selections to go in allowed positions
- [x] Score Calculation - Track the points associated with each player selection and add all of them together at the end of the round to calculate the final roster score
- [x] Basic UI in Streamlit - Build functioning UI that allows users to see their roster, spin the team wheel, and make a player selection
# Future Features
- [ ] Jackpot Spin - Have a selection in the team wheel that allows a selection of the highest scoring players for open positions and from the round constraints, but regardless of team
- [x] Bonus Round - Have a round after all roster positions are filled where a new random week, season, and team are selected, showing the best available player for each position, allowing the replacement of a player on the roster with a higher scoring one
- [ ] Persistent Tracking - Save the number of times a user has scored at least 200 points in a game, their all time highest score, and their all time highest scoring roster
- [ ] K and D/ST Addition - Find data for kickers and D/ST so they can be positions on the game roster. Possible solution is to find an API that has all required data including K and D/ST
- [ ] Deployment to Streamlit Cloud - Have to fully functioning game be accessible for anyone to play and access on the internet on Streamlit Cloud
- [ ] Visual Team Wheel - A visual wheel spin showing all available teams should be spun each selecting in the game UI
- [ ] AI Roster Coach - An optional feature that gives an AI generated suggestion for each selection during the round
# Engineering Improvements
- [ ] Automated testing - Write unit tests for game_engine.py functions covering core logic, edge cases, and known bug scenarios using pytest
- [ ] OOP Refactor - Restructure game_engine.py using Python classes to improve state management and reduce parameter passing across functions
- [ ] CI/CD Pipeline (Github Actions) - Automatically run pytest test suite on every push to main branch
- [ ] API Caching - Implement st.cache_data decorator to replace current session state CSV loading approach with idiomatic Streamlit caching
# Technical Debt
- [x] Empty data points and NaN Values - Some data points for a player do not have recorded data that could break game logic and points calculation
- [x] Invalid Player Assignment - Selected players can be placed anywhere on the roster but should only be placed in their assignment position or other valid positions
- [ ] Data Re-downloading - Every time a game is played, the entire dataset is re-downloaded even if no data is changed, causing redundancy and memory issues
- [x] FLEX last-selection handling - If flex was the last open slot on the roster, it would not be evaluated and did not show player selectionsro
- [x] Bonus Round Logic Fixes - Multiple bugs discovered: RB1/RB2 not evaluated independently for replace eligibility, replace buttons appearing for non-matching positions, and positions with no valid upgrade still showing in bonus selection list
- [x] Trade Rule Compliance - If a midseason trade occurs, a player can still be selected on the roster under a different team
