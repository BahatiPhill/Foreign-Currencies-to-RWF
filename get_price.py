import sys
from exchange import RWf_Exchange

def main():
	if len(sys.argv) != 2:
		print(' ')
		print("USAGE: python get_price.py [currency code]")
		print("currency codes can be either [USD, EUR, GBP]")
		print("EXAMPLE: python get_price.py USD")
		print('')
		sys.exit(1)
	currency = sys.argv[1]

	exch = RWf_Exchange()
	sells = exch.sell_price(currency)
	buys = exch.buy_price(currency)
	av = exch.average_price(currency)
	print(' ')
	print("SELLING Price: ", sells)
	print("BUYING Price: ", buys)
	print("AVERAGE Price: ", av)
	print(' ')


if __name__ == '__main__':
	main()
