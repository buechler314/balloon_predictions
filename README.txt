Property of Michigan Balloon Recovery and Satellite Testbed 

---------------- Balloon.py -------------------------------------

Contains multiple functions that can be called.
Import balloon on any script that uses one of these functions

- APRS_data = APRS(callsign)
	- Function to get aprs data. 
	- Returns dictionary with lots of info from the aprs packet

- send_slack(messageString,messageType,recipient)
	- Function to send a slack message
	- Inputs are:
		- messageString (string)
		- 'dm' for direct message, 'channel' for channel
		- recipient - name of person like 'Robby', or channel like '#predictions'

- package(dataset,prediction_ID)
	- Function to save a variable with any nesting degree
	- Inputs are variable name and prediction ID (string) (which will be set as the filename)

- dataset = unpackage(prediction_ID)
	- Function to read in a saved variable
	- Input is filename (string) without extension
	- Returns new variable

- data = prediction(payload weight,balloon mass,parachute diameter,helium tanks,latitude,longitude,current altitude,status,query time,# of ensembles, error in ensembles)
	- payload weight        - lbs (float)
	- balloon mass          - grams (float)
	- parachute diameter    - ft (float)
	- helium tanks          - # of tanks (float)
	- latitude              - deg (float)
	- longitude             - deg (float)
	- current altitude      - ft (float)
	- status                - ascent (1) or descent (-1) (int)
	- query time            - string: 'now' or 'YYYY-MM-DD hh:mm:ss'
	- # of ensembles 	      - Number of ensembles to run (int). -1 if none. 
	- error in ensembles    - Amount of error to run with each ensemble (float). Usually between 0 and 1.

	Function returns a dictionary, which consists of keys:
	..['Ascent Rate']         - ft/s
	..['Burst Altitude']      - ft
	..['Burst Latitude']      - deg
	..['Burst Longitude']     - deg
	..['Landing Lat']         - deg
	..['Landing Lon']         - deg
	..['Landing Time']        - Timestamp (when balloon is predicted to land, absolute time)
	..['Launch Time']         - Timestamp (what time the prediction was preformed at, absolute time)
	..['TimeData']            - Timeseries Dataframe, consisting of status (ascent or descent), lat (deg), long (deg), and altitude (ft) as a function of absolute future time
	..['Landing Devaiations'] - Dataframe with final landing locations of non-nominal ensembles. Columns of 'Lat' and 'Lon'. Number of elements = number of ensembles. 
	..['Secondary Tracks']    - Dictionary. Each element is a dataframe. Each dateframe is a complete track of ['Lat'], ['Lon'], and ['Alt'] as a function of absolute future time for a single ensemble

	Example:

	data = balloon.prediction(6.0,1000,6.0,1,41.64,-83.243,40000,1,'now',110,0.2)
