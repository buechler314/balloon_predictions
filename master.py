import balloon
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Import Flight Data
data = balloon.prediction(6.0,1000,6.0,1,41.64,-83.243,40000,1,'now',500,0.2)

# Plot Nominal Data
fig = plt.figure(figsize=(40,35))
ax = fig.gca(projection='3d')
ax.plot(data['TimeData']['Latitude'], data['TimeData']['Longitude'], data['TimeData']['Altitude'])

for ensembles in data['Secondary Tracks']:
    ax.plot(data['Secondary Tracks'][str(ensembles)]['Lat'],data['Secondary Tracks'][str(ensembles)]['Lon'],data['Secondary Tracks'][str(ensembles)]['Alt'])

plt.show()
