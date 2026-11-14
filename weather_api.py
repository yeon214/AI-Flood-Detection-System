from pyproj import Proj
import math
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
api_key = os.getenv("KMA_API_KEY")

url = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

location = {
  1 : {
    "name" : "내성지하차도",
    "lat" : 35.2059,
    "lon" : 129.0832
  },
  2 : {
    "name" : "만덕 진출입로",
      "lat" : 35.2125,
      "lon" : 129.0385
  }
}

projection = Proj(
    proj="lcc",
    lat_1=30,
    lat_2=60,
    lat_0=38,
    lon_0=126,
    R=6371008.77,
    units="m"
)

def convert_to_grid(lat, lon):
  x, y = projection(lon, lat)
  
  nx = math.floor(x / 5000 + 43 + 0.5)
  ny = math.floor(y / 5000 + 136 + 0.5)
  
  return nx, ny
    
now = datetime.now()

if now.minute < 40:
    base_datetime = now - timedelta(hours=1)
else:
    base_datetime = now

base_date = base_datetime.strftime("%Y%m%d")
base_time = base_datetime.strftime("%H00")

for location_id, info in location.items():
    nx, ny = convert_to_grid(info["lat"], info["lon"])

    weather_params = {
        "serviceKey": api_key,
        "dataType": "JSON",
        "base_date": base_date,
        "base_time": base_time,
        "nx": nx,
        "ny": ny
    }
    response = requests.get(url, params=weather_params, timeout=10)
    response.raise_for_status()

    data = response.json()
    items = data["response"]["body"]["items"]["item"]

    for item in items:
        if item["category"] == "RN1":
            print(info["name"], "강수량:", item["obsrValue"])