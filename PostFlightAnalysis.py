import balloon
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import plotly
#import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import math
import plotly.express as px
from datetime import datetime

# Set plotly credentials 
#plotly.tools.set_credentials_file(username='buechler', api_key='vuufJ1JuwTnkkVnX8gbk')
plotly.offline.init_notebook_mode()

# Set flight ID and number of predictions
flightID = '01'
predictionNum = 2
plotEnsem = False       # Simplifies plot a lot if this is false

# Get all predictions data
AllData = balloon.unpackageGroup(flightID,predictionNum)

# Initialize variables 
data = list()
j = 0
lat = list()
lng = list()
alt = list()
times = list()

# DEV:
DDataFrame = pd.DataFrame()
first = 1
vectors = list()


# 3D scatter plot


# Iterate through predictions
for prediction in AllData:
    ID = str(AllData[prediction]['Inputs']['Status']) + ',' + str(math.trunc(AllData[prediction]['Inputs']['Altitude']))
    
    # Get actual flight path
    lat.append(AllData[prediction]['Inputs']['Lat'])
    lng.append(AllData[prediction]['Inputs']['Lon'])
    alt.append(AllData[prediction]['Inputs']['Altitude'])
    times.append(AllData[prediction]['Inputs']['Launch Time'])
    
    
    # Plot nominal prediction data
    traceNom = go.Scatter3d(x = AllData[prediction]['TimeData']['Latitude'],y = AllData[prediction]['TimeData']['Longitude'],z = AllData[prediction]['TimeData']['Altitude'],mode='lines', line=dict(color='blue',width=1),name = str(AllData[prediction]['Inputs']['Status']) + ',' + str(math.trunc(AllData[prediction]['Inputs']['Altitude'])))
    data.append(traceNom)
    
    # DEV:
    Local = pd.DataFrame()
    Local['lat'] =  AllData[prediction]['TimeData']['Latitude']
    Local['lng'] =  AllData[prediction]['TimeData']['Longitude']
    Local['alt'] =  AllData[prediction]['TimeData']['Altitude']
    Local['ID'] = ID
    #Local['Time'] = AllData[prediction]['TimeData'].index
    Local['Time'] = (AllData[prediction]['TimeData'].index.values - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
    #Local[str(AllData[prediction]['Inputs']['Status']) + ',' + str(math.trunc(AllData[prediction]['Inputs']['Altitude']))] = Local['lat'].map(str) + ',' + Local['lng'].map(str) + ',' + Local['alt'].map(str)
    #vectors.append(Local[str(AllData[prediction]['Inputs']['Status']) + ',' + str(math.trunc(AllData[prediction]['Inputs']['Altitude']))])
    #vectors.append(Local['lat_'+ID])   
    #vectors.append(Local['lng_'+ID])   
    #vectors.append(Local['alt_'+ID])  
    DDataFrame = DDataFrame.append(Local)
    
    
       
    # Plot ensemble data
    if plotEnsem:
        for track in AllData[prediction]['Secondary Tracks']:
            traceEns = go.Scatter3d(x = AllData[prediction]['Secondary Tracks'][track]['Lat'],y = AllData[prediction]['Secondary Tracks'][track]['Lon'],z = AllData[prediction]['Secondary Tracks'][track]['Alt'],mode='lines', line=dict(color='#1f77b4',width=0.2))
            data.append(traceEns)
        
# DEV:        
#DDataFrame = pd.concat(vectors, axis=1)


        
# Arrange flight data in dataframe
FlightPath = pd.DataFrame(index=times)
FlightPath['lat'] = lat
FlightPath['lon'] = lng
FlightPath['alt'] = alt
traceFlightPath = go.Scatter3d(x = FlightPath['lat'],y = FlightPath['lon'],z = FlightPath['alt'],mode='lines', line=dict(color='black',width=5),text=FlightPath.index,name='Flight Path')
data.append(traceFlightPath)
  
# Plot data      
#plotly.offline.plot(data, filename='NewPlot.html')



# dev:
#DDataFrame['index'] = DDataFrame.index

fig = px.line_3d(DDataFrame, x='lat', y='lng', z='alt', line_group = 'ID', animation_frame='Time')
plotly.offline.plot(fig, filename='dev.html')





