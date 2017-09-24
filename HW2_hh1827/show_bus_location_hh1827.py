import numpy as np
import sys
import os 
import json
import urllib as url

if not len(sys.argv) == 3:
    print("Invalid number of argumenets. Run as: show_bus_location_hh1827.py")
    sys.exit()

site = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+ sys.argv[1]+'&VehicleMonitoringDetailLevel=calls&LineRef='+sys.argv[2]

url.urlretrieve(site,os.getenv("HOME")+"/PUIDATA/"+sys.argv[2]+".json" )
bus_data = open(os.getenv("HOME")+"/PUIDATA/"+sys.argv[2]+".json","r+")

data = bus_data.read().decode("utf-8")
data = json.loads(data)

bus_info = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
bus_No = len(bus_info)
print('Bus Line: '+sys.argv[2])
print('Number of Active Buses:{}'.format(bus_No))

for i in range(bus_No):   
    Lat = bus_info[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    Lon = bus_info[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    print("Bus {} is at latitude {} and longitude {}".format(i, Lat, Lon))











