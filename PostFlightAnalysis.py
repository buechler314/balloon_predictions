import balloon
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
plotly.tools.set_credentials_file(username='', api_key='')
plotly.offline.init_notebook_mode()

# Set flight ID and number of predictions
flightID = '01'
predictionNum = 102
plotEnsem = False

# Get all predictions data
AllData = balloon.unpackageGroup(flightID,predictionNum)

data = list()
j = 0
lat = list()
lng = list()
alt = list()
times = list()

# Iterate through predictions
for prediction in AllData:
    
    # Get actual flight path
    lat.append(AllData[prediction]['Inputs']['Lat'])
    lng.append(AllData[prediction]['Inputs']['Lon'])
    alt.append(AllData[prediction]['Inputs']['Altitude'])
    times.append(AllData[prediction]['Inputs']['Launch Time'])
    
    # Plot nominal data
    traceNom = go.Scatter3d(x = AllData[prediction]['TimeData']['Latitude'],y = AllData[prediction]['TimeData']['Longitude'],z = AllData[prediction]['TimeData']['Altitude'],mode='lines', line=dict(color='blue',width=1))
    data.append(traceNom)
    
    # Plot ensemble data
    if plotEnsem:
        for track in AllData[prediction]['Secondary Tracks']:
            traceEns = go.Scatter3d(x = AllData[prediction]['Secondary Tracks'][track]['Lat'],y = AllData[prediction]['Secondary Tracks'][track]['Lon'],z = AllData[prediction]['Secondary Tracks'][track]['Alt'],mode='lines', line=dict(color='#1f77b4',width=0.2))
            data.append(traceEns)
        
# Arrange flight data in dataframe
FlightPath = pd.DataFrame(index=times)
FlightPath['lat'] = lat
FlightPath['lon'] = lng
FlightPath['alt'] = alt
traceFlightPath = go.Scatter3d(x = FlightPath['lat'],y = FlightPath['lon'],z = FlightPath['alt'],mode='lines', line=dict(color='black',width=5),text=FlightPath.index,name='Flight Path')
data.append(traceFlightPath)
  
# Plot data      
plotly.offline.plot(data, filename='NewPlot.html')

