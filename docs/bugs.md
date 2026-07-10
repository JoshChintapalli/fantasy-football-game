# Data Bugs
**Empty Dataframe / Missing Position Data**
- Description: The function to get the best player for each position on a team crashed when a team had no recorded stats for any open position in the selected parameters.
- Reproduction: Confirmed with "NE", week 7, 2018 - no TE data recorded.
- Fix: Added "filtered.empty' check in 'get_best_players()" to skip positions with no data and only return "False" if no positions at all were found.
- Status: Fixed.
# Game Logic Bugs
**Invalid Roster Slot Assignment**
- Description: Any slot-position combination was accepted without validation, allowing players to be placed in slots that did not match with their valid positions.
- Reproduction: Calling "update_roster()" with a mismatched position and slot, like selecting QB and placing it in a WR slot.
- Fix: Added position-to-slot compatibility check returning True/False, including special FLEX handling.
- Status: Fixed.

**FLEX Excluded from Selection Logic**
- Description: FLEX handling was temporarily blocked off in "get_best_players()" because of other existing FLEX bugs, causing a black screen when FLEX was the last open slot.
- Reproduction: Fill all non-FLEX slots and attempt to spin - no player option appeared.
- Fix: Added a separate FLEX branch that evaluates eligible positions only when their dedicated slots are all filled.
- Status: Fixed.

**Short-Circuit Evaluation Ordering Bug**
- Description: Selection validation check failed when the position was FLEX because FLEX had a list of eligible positions which was unhashable and cannot be checked against a set of seen positions.
- Reproduction: Any spin where FLEX appeared in the roster loop before all positions were filled.
- Fix: Reordered condition to check if current key in the loop was FLEX first, short-circuiting before the list was evaluated.
- Status: Fixed.

**FLEX Crash with List as Dictionary Key**
- Description: Using a list of eligible positions for FLEX as a key to look up in the filtered dataset caused a TypeError since a list is unhashable.
- Reproduction: Triggered during bonus round slot display when position was FLEX.
- Fix: Replaced "best_selection[slot_to_position[pos]]" with "best_selection[st.session_state.current_selection]" for the points lookup.
- Status: Fixed.

**Filled Slots Overridden when not in the Bonus Round**
- Description: A manual call of the "update_roster" function in "game_engine.py" could cause an already filled slot in the roster to be overridden when it is not the bonus round. Slots can only be overridden during the bonus round.
- Reproduction: Found while writing unit test for checking successful and unsuccessful roster changed.
- Fix: Add a condition inside "update_roster" to check if it is not the bonus round and the selected slot is empty, or it is the bonus round (in which case, the slot should be filled and overridden if valid).
- Status: Fixed.
# Bonus Round Bugs
**RB1/RB2 Not Evaluated Independently**
- Description: RB2 was skipped in the bonus round check to evaluate eligible positions to upgrade because RB was a seen position.
- Reproduction: Enter bonus round with RB1 scoring higher than the bonus round RB selection but RB2 scoring lower, RB selection would not appear.
- Fix: Moved upgrade comparison to slot level in "app.py", evaluating each slot independently against the single best player for that position.
- Status: Fixed.

**Replace Buttons Showing for Non-Matching Positions**
- Description: After selecting a position in the bonus round, replace buttons appeared for all slots on the roster even if the selection was not eligible to go in that slot.
- Reproduction: Select QB in the bonus round and see replace buttons for every slot.
- Fix: Add position-matching condition before rendering replace buttons, including FLEX compatibility check.
- Status: Fixed.

**Non-Upgradable Positions SHowing in Bonus Selection**
- Description: The bonus player selection screen showed positions where no roster slot would actually improve, leaving the user stuck with no valid replace buttons.
- Reproduction: Spin a bonus team where the best available player scores lower than all matching roster slots.
- Fix: Added "any()" check filtering the selection list to only positions where at least one matching slot would be improved.
- Status: Fixed.
# UI/State Bugs
**Bonus Round Title Persisting into Complete Phase**
- Description: The "Bonus Round" total continued showing on the complete phase screen be cause the bonus boolean was not reset before the page rerun was triggered.
- Reproduction: "Bonus Round" title still showed even after the bonus selection was made and the final score displayed.
- Fix: Set the bonus round boolean to false right before the rerun that caused the complete phase.
- Status: Fixed.
