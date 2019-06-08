import balloon
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

payload = 6.0
balloonWeight = 1000
parachuteDia = 6.0
helium = 1.5
desiredLat = 41.961587
desiredLon = -83.802943
launchTime = '2019-06-07 20:00:00'
tolerace = 5


# Do backwards prediction calculation
launchLoc = balloon.launchPrediction(payload,balloonWeight,parachuteDia,helium,desiredLat,desiredLon,launchTime,tolerace)
print('Tolerace reached: '+str(launchLoc['Tolerace']))

# Check work
data = balloon.prediction(6.0,1000,6.0,1.5,launchLoc['Lat'],launchLoc['Lon'],-1,1,launchTime,10,0.2)
balloon.plotPrediction(data)

