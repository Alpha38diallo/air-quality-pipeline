import requests
import pandas as pd

URL = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
    "?latitude=45.1885"
    "&longitude=5.7245"
    "&hourly=pm10,pm2_5,nitrogen_dioxide,ozone"
)

response = requests.get(URL)
data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "pm10": data["hourly"]["pm10"],
    "pm25": data["hourly"]["pm2_5"],
    "no2": data["hourly"]["nitrogen_dioxide"],
    "ozone": data["hourly"]["ozone"]
})

df.to_csv("air_quality_raw.csv", index=False)

print("Extraction terminée")
print(df.head())