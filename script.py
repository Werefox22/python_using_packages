import pprint
from urllib import request
import requests
from matplotlib import pyplot as plt
from datetime import datetime

# format PrettyPrinter
pp = pprint.PrettyPrinter(indent=4)

API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/'
city = 'cary'
r = requests.get(API_URL + city)
response = r.json()

forecast_list = response['forecast']
today = datetime.now().strftime("%b-%d-%Y")

to_graph = {}
count = 1

for day in forecast_list:
	current_date = int(today[4:6]) + count
	this_day = f"{today[0:4]}{current_date}{today[6:]}"
	count += 1

	to_graph[this_day] = day['wind']
print(to_graph)

plt.xlabel("Date")
plt.ylabel("Wind Speed km/h")

plt.scatter(to_graph.keys(), to_graph.values())
plt.show()