Balloon.py contains multiple functions that can be called.
- APRS_data = APRS(callsign)
	- Function to get aprs data. Returns dictionary with lots of info from the aprs packet
- send_slack(messageString,messageType,recipient)
	- Function to save a variable with any nesting degree.
	- Inputs are variable name and prediction ID (which will be set as the filename).
- package(dataset,prediction_ID)
	- Function to read in a saved variable
	- Input is filename without extension
	- Returns new variable.
.
.
.
not done yet

