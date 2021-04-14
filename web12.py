'''Write a Python program to get the number of people visiting a U.S. government website right now'''


import requests
url = 'https://analytics.usa.gov/data/live/realtime.json'
j = requests.get(url).json()
print("Number of people visiting a U.S. government website-")
print("Active Users Right Now:")
print(j['data'][0]['active_visitors'])
  