'''Write a Python program to that retrieves an arbitary Wikipedia page of "Python" and creates a list of links on that page'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
  if 'href' in link.attrs:
    print(link.attrs['href'])
