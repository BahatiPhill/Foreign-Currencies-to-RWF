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
	result = exch.get_exchange_rates(currency)

	print(' ')
	print("SELLING Price: ", result[1])
	print("BUYING Price: ", result[2])
	print("AVERAGE Price: ", result[3])
	print(' ')


if __name__ == '__main__':
	main()
