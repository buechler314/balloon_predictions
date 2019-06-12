Property of Michigan Balloon Recovery and Satellite Testbed and Aaron J Ridley
University of Michigan, Ann Arbor MI
Last Updated: 06/11/2019

---------------- Balloon.py -------------------------------------
DESCRIPTION:
- Contains multiple functions that can be called from external scripts.
- Import balloon on any script that uses one of these functions.

MODULES NEEDED:
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import sys
import random
import time
import pandas
import json
import requests
import pickle
import math
import gmplot 
import statistics


FUNCTIONS:
- APRS_data = APRS(callsign)
	- Function to get aprs data. 
	- Returns dictionary with lots of info from the aprs packet
	- callsign is a string

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

- allPredictions = unpackageGroup(flightID,numPredictions)
	- Function to read in multiple saved variables.
	- Input is flightID (str) and number of predictions (int)
	- Returns dictionary filled with prediction elements

- launchLoc = launchPrediction(payload,balloon,parachute,helium,lat,lon,launchTime,tolerance)
	- Function to run prediction backwards
	- Outputs launching location based on desired landing location
	- payload	- 
	- balloon 	- 
	- parachute	- 
	- helium	- 
	- lat		- 
	- lon		- 
	- launchTime	- 
	- tolerace	-

- plotPrediction(data)
	- Function to plot one prediction worth of data statically in 3D space
	- Input is data structure returned by prediction().

- PredictionAni(PredData,saving)
	- Function to animate one prediction in 3D space as time progresses.
	- PredData	- Data structure returned by prediction()
	- saving	- 1 (save animation as GIF), or 0 (don't).
			- Saving GIF takes significant time and memory allocation.

- heatMap(data)
	- Function to create a 2D heatmap of landing probabilities overlaid on google maps
	- Saves an html file to local directory.
	- Requires google maps api key. 

- get_args(argv,queryTime)
	- Referenced by other functions
	- Function to figure out prediction arguments 

- get_station(longitude, latitude)
	- Referenced by other functions
	- Determine which station(s) is(are) closest to the given latitude and longitude

- read_rap(file,args,IsNam)
	- Referenced by other functions
	- Reads RAP file

- KaymontBalloonBurst(BalloonMass)
	- Referenced by other functions

- calculate_helium(NumberOfTanks)
	- Referenced by other functions

- calc_ascent_rate(RapData, NumberOfHelium, args, altitude)
	- Referenced by other functions

- calc_descent_rate(RapData, args, altitude)
	- Referenced by other functions

- get_temperature_and_pressure(altitude,RapData)
	- Referenced by other functions

- get_wind(RapData,altitude)
	- Referenced by other functions

- data = prediction(payload weight,balloon mass,parachute diameter,helium tanks,latitude,longitude,current altitude,status,query time,# of ensembles, error in ensembles)
	- payload weight        - lbs (float)
	- balloon mass          - grams (float)
	- parachute diameter    - ft (float)
	- helium tanks          - # of tanks (float)
	- latitude              - deg (float)
	- longitude             - deg (float)
	- current altitude      - ft (float)
	- status                - ascent (1) or descent (-1) (int)
	- query time            - string: 'now' or 'YYYY-MM-DD hh:mm:ss'. 
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
	..['TimeData']            - Timeseries Dataframe, consisting of (below) as a function of absolute future time
					- Status (ascent or descent)
					- Latitude (deg)
					- Longitude (deg)
					- Altitude (ft) 
	..['Inputs']		- Data used to preform prediction. Consists of keys:
				..['Launch Time']				
					- Timestamp (what time the prediction was preformed at, absolute time)	
				..['Altitude']
					- ft
				..['Lat']
					- deg
				..['Lon']
					- deg
				..['Status']
					- 1 or 0, Ascent or Descent
				..['ForcastFile']
					- str, name of file used to do prediction
				..['ForcastTime']
					- str, rounded hour used for prediction
	..['Landing Devaiations']	- Dataframe with final landing locations of non-nominal ensembles. Columns of:
						- 'Lat'
						- 'Lon'
					- Number of elements = number of ensembles. 
	..['Secondary Tracks']	- Dictionary. 
				- Each element is a dataframe. 
				- Each dateframe is a complete track of (below) as a function of absolute future time for a single ensemble
					- ['Lat']
					- ['Lon']
					- ['Alt'] 
	..['SecTracksTimeDomain']	- Same data as ['Secondary Tracks']
					- Saved as a dataframe synchronized in the time domain 
	
	Example:
	data = balloon.prediction(6.0,1000,6.0,1,41.64,-83.243,40000,1,'now',110,0.2)


---------------- StationList.txt -------------------------------------
- Contains a list of weather stations
- Does not need to be altered.

---------------- StationListWorld.txt -------------------------------------
- Contains a list of weather stations
- Does not need to be altered.

---------------- PreFlightAnalysis.py -------------------------------------
- under development 

---------------- postFlightAnalysis.py -------------------------------------
- under development 



