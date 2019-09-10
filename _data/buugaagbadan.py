import lxml
import requests
from urllib.request import urlopen
#import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd


#cinwaan=qoraa=sanad=luqad=maado=handle=pdf=magaalo=madbacad=""
#id="821"


links=['5601', '3366', '4821', '2748', '4390','4822', '4461', '4832', '4441', '4180','4179', '3037', '5511', '4430', '4337', '4489', '4182', '2228', '4842', '4840', '2404', '4431', '4432', '4419', '4250', '4257', '4181', '770', '3488', '746', '821', '2843', '845', '846', '809', '741', '4830', '912', '4251', '4417', '4340', '775', '2561', '849', '4253', '4497', '2488', '908', '2544', '4254', '4252', '794', '782', '5661', '2051', '2130', '4835', '839', '3489', '2600', '4255', '902', '878', '882', '884', '5301', '5316', '835', '780', '813', '815', '816', '824', '826', '828', '872', '892', '894', '5678', '906', '4341', '1610', '5317', '2183', '4490', '909', '873', '4201', '4202', '927', '910', '918', '900', '893', '889', '886', '4694', '863', '862', '817']
def tijaabo(id):
	link='/handle/'
	download='/bitstream/'
	site='http://dspace-roma3.caspur.it'
	#for item in links:
	url=site+link+"2307/"+ id
	page = urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	table = soup.find('table', attrs={'class': 'itemDisplayTable'})
	cinwaan=qoraa=sanad=luqad=maado=handle=pdf=magaalo=madbacad=""
	for row in table.findAll('tr'):
		label = row.find('td', attrs={'class': 'metadataFieldLabel'}).text.strip()
		value = row.find('td', attrs={'class': 'metadataFieldValue'}).text.strip()
		if label == "Title:": 			cinwaan=value
		elif label == "Authors:": 		qoraa=value
		elif label == "Issue Date:": 	sanad=value
		elif label == "Location:": 	magaalo=value
		elif label == "URI:": 			handle=value
		elif label == "Language:": 	luqad=value
		pdf=site+download+"2307/"+id+"/1/"+cinwaan+".pdf"

	return "- cinwaan: " +cinwaan+"\n\tqoraa: " +qoraa+"\n\tsanad: " +sanad+"\n\tluqad: " +luqad+"\n\thandle: " +handle+"\n\tpdf: " +pdf+"\n\tmagaalo: " +magaalo+"\n\n"

buugaag= []

for item in links[71:100]:
	buugaag.append(tijaabo(item))

file=open("buugaagbadadn1.txt", "w")
for i in buugaag:
	file.write(i)

file.close()



# print("- cinwaan: " +cinwaan)
# print("  qoraa:" +qoraa)
# print("  sanad: " +sanad)
# print("  luqad: " +luqad)
# print("  handle: " +handle)
# print("  pdf: " +pdf)
# print("  magaalo: " +magaalo)








