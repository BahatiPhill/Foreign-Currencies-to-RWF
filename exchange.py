import requests
import bs4
import re

class RWf_Exchange:



    #US Dollar = 'USD'
    #uero   = 'EUR'
    #Pound sterling   = 'GBP'



    def __init__(self):
        self.currencies = {'EUR': 0, 'GBP': 1, 'USD':2}



    def get_exchange_rate(self, currency):

        BNR = requests.get('https://www.bnr.rw/')
        soup = bs4.BeautifulSoup(BNR.text, "html.parser")
        elements = soup.select('#ticker01 li')
        currency_index = self.currencies.get(currency)
        #print(elements[currency_index].getText())
        return elements[currency_index].getText()

    def extract_prices(self, string):
        result  = re.findall(r'\b\d+\b', string)
        print(result)


    def buy_price(self, currency):
        price = self.get_exchange_rate(currency)
        print(price)

    def sell_price(self, currency):
        price = self.get_exchange_rate(currency)
        print(price)
