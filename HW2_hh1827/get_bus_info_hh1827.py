import numpy as np
import sys
import os 
import json
import urllib as url
import csv

if not len(sys.argv) == 4:
    print("Invalid number of argumenets. Run as: get_bus_info_hh1827.py busline.csv")
    sys.exit()

site = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+ sys.argv[1]+'&VehicleMonitoringDetailLevel=calls&LineRef='+sys.argv[2]

url.urlretrieve(site,os.getenv("HOME")+"/PUIDATA/"+sys.argv[2]+".json" )
bus_data = open(os.getenv("HOME")+"/PUIDATA/"+sys.argv[2]+".json","r+")

data = bus_data.read().decode("utf-8")
data = json.loads(data)

CSV = file(sys.argv[3], "wb")
W = csv.writer(CSV)
W.writerow(["Latitude", "Longitude", "Stop Name", "Stop Status"])

bus_info = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
bus_No = len(bus_info)
for i in range(bus_No):   
    Lat = bus_info[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    Lon = bus_info[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    Status = bus_info[i]["MonitoredVehicleJourney"]["OnwardCalls"]
    if Status == None:
      Stop_Name = "N/A"
      Stop_Status = "N/A" 
    else:
      Stop_Name = Status["OnwardCall"][0]["StopPointName"]
      Stop_Status = Status["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]

    W.writerow([str(Lat), str(Lon), Stop_Name, Stop_Status])

CSV.close()

