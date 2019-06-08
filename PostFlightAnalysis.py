import balloon
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Set flight ID and number of predictions
flightID = '01'
predictionNum = 6

# Get all predictions data
AllData = balloon.unpackageGroup(flightID,predictionNum)


# Initialize plot
fig = plt.figure(figsize=(40,35))
ax = fig.gca(projection='3d')

# Plot all nominal data

j = 0
for prediction in AllData:
    
    # Plot all nominal data
    lineWidth = 5
    Alpha=1
    ax.plot(AllData[prediction]['TimeData']['Latitude'], AllData[prediction]['TimeData']['Longitude'], AllData[prediction]['TimeData']['Altitude'],color='C'+str(j%10),linewidth=lineWidth,alpha=Alpha)
    
    # Plot all ensembles
    lineWidth = 1
    Alpha=0.2
    for track in AllData[prediction]['Secondary Tracks']:
        ax.plot(AllData[prediction]['Secondary Tracks'][track]['Lat'],AllData[prediction]['Secondary Tracks'][track]['Lon'],AllData[prediction]['Secondary Tracks'][track]['Alt'],color='C'+str(j%10),linewidth=lineWidth,alpha=Alpha)
    j = j + 1

plt.show()