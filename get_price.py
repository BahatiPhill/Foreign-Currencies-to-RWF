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
	result = exch.sell_price(currency)
	print(result)


if __name__ == '__main__':
	main()
