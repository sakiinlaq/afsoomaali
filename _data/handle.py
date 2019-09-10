import lxml
import requests
from urllib.request import urlopen
import re
#import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
links=[]

url="http://dspace-roma3.caspur.it/handle/2307/729/browse?type=dateissued&sort_by=2&order=ASC&rpp=100&etal=5&year=-1&month=-1&starts_with=1970"

page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table', attrs={'class':'miscTable'})
for row in table.findAll('tr'):
	for item in row.findAll('a'):
		if "handle" in item.get('href'):
			links.append(item.get('href')[13:17])	

print(links)




