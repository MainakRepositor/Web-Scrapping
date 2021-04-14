'''Write a Python program to list all language names and number of related articles in the order they appear in wikipedia.org.'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.wikipedia.org/')
bs = BeautifulSoup(html, "html.parser")
nameList = bs.findAll('a', {'class' : 'link-box'})
for name in nameList:
  print(name.get_text())
  