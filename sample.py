import datetime
import balloon
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Define what predictions you want 
flightID = '01'
predictionNum = 5
deltaHour = 8

# Get list of times and convert to strings
timeList = list()
start = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
timeList.append(str(start))
new = start
for predictionNum in range(1,predictionNum+1):
    last = new
    new = last + datetime.timedelta(hours=deltaHour)
    timeList.append(str(new))
    
# Import Flight Data for each time and record to pickle file
i = 1
for times in timeList:
    data = balloon.prediction(6.0,1000,6.0,1,41.64,-83.243,50000,-1,times,100,0.2)
    balloon.package(data,'p_'+flightID+'_'+str(i))
    i = i + 1