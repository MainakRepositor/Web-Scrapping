''' Write a Python program to get the number of datasets currently listed on data.gov.'''

from lxml import html
import requests
response = requests.get('http://www.data.gov/')
doc_gov = html.fromstring(response.text)
link_gov = doc_gov.cssselect('small a')[0]
print("Number of datasets currently listed on data.gov:")
print(link_gov.text)
