import pandas as pd
import requests as req

# city = 'bengaluru'
city = input("Enter the City name : ")

res = req.get(f'https://api.waqi.info/feed/{city}/?token=e1e03932b8e4a7156d975cc19f0e88062cf887ea')

json = res.json()

print(json['data']['aqi'])  