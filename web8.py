'''Write a Python program to get 90 days of visits broken down by browser for all sites on data.gov.'''

import requests
r = requests.get("https://analytics.usa.gov/data/live/browsers.json")
print("90 days of visits broken down by browser for all sites:")
print(r.json()['totals']['browser'])
