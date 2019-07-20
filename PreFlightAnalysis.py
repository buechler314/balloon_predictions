import balloon
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

payload = 6.0
balloonWeight = 1000
parachuteDia = 6.0
helium = 1.5
desiredLat = 42.290977
desiredLon = -83.717548
launchTime = 'now'
tolerace = 5

# Do animation
data = balloon.prediction(payload,balloonWeight,parachuteDia,helium,desiredLat,desiredLon,-1,1,launchTime,50,0.2)
#balloon.PredictionAni(data,0)

## Do backwards prediction calculation
#launchLoc = balloon.launchPrediction(payload,balloonWeight,parachuteDia,helium,desiredLat,desiredLon,launchTime,tolerace)
#print('Tolerace reached: '+str(launchLoc['Tolerace']))
## Check work
#data = balloon.prediction(6.0,1000,6.0,1.5,launchLoc['Lat'],launchLoc['Lon'],-1,1,launchTime,10,0.2)
#balloon.plotPrediction(data)

