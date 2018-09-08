import requests
import re
from bs4 import BeautifulSoup


class RWf_Exchange:


	def get_exchange_rates(self, currency):
		bnr = requests.get('https://www.bnr.rw/index.php?id=23')
		soup = BeautifulSoup(bnr.text, 'html.parser')
		
		l = []

		#find all data in <td> tags, that's where currencies data are rendered
		for tdd in soup.find_all('td'):
			l.append(str(tdd.string).strip())

		#check if  the parameter(currency) exist
		if currency in l:
			#get the index position of currency in list
			currency_index = int(l.index(currency))
			currency_code = l[currency_index]
			average = l[currency_index + 1]
			buying = l[currency_index + 2]
			selling = l[currency_index + 3]
			
			return (currency_code, average, buying, selling)

		else:
			return None

	