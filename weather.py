import os
import requests
import json
from datetime import date, timedelta
from darksky import forecast
import sys
API_KEY="58ce87e229a6183b47a82b013ead67b6"
url = 'http://photon.komoot.de/api/?q='
def weather(address,query):
    #Get the latitude and longitude
    resp=requests.get(url=url+address)
    data=json.loads(resp.text)
    latitude  = data['features'][0]['geometry']['coordinates'][1]
    longitude = data['features'][0]['geometry']['coordinates'][0]
    answer    = forecast(API_KEY,latitude,longitude)
       
    if query=='temperature':
        return int((5.0/9)*(answer['hourly']['data'][2]['temperature']-32))
    elif query=='humidity':
        return(answer['hourly']['data'][2]['humidity'])
    else:
        return(answer['hourly']['data'][2]['summary'])
        
if sys.argv[2] == "1":
    print(str(weather(sys.argv[1],"temperature"))+" degrees C")
elif sys.argv[2] == "2":
    print(str(weather(sys.argv[1],"humidity")))
else:
    print(str(weather(sys.argv[1],"summary")))

