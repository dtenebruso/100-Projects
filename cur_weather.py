#!/usr/bin/python3

import http.client, json, argparse

base = '/data/2.5/weather?zip='
cap = '&APPID='


def zip_country_code(zipc, country, appid):
	path = '{}{},{}{}{}'.format(base, zipc, country, cap, appid)
	print(path)
	connection = http.client.HTTPConnection('api.openweathermap.org')
	connection.request('GET', path)
	rawreply = connection.getresponse().read()
	reply = json.loads(rawreply.decode('utf-8'))
	print('Today will be mainly',reply['weather']['main'],'\n', reply['name'][0],'is looking at a humidity of',reply['main']['humidity'])

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Find your local weather')
	parser.add_argument('zipcode', metavar='zipc', type=int, help='your local zip code(14533)')
	parser.add_argument('countrycode', metavar='country', default='us', help='your country acronym (ex. us, uk or ru)')
	parser.add_argument('apikey', metavar='appid', help='your api.openweathermap.org api key')

	args = parser.parse_args()
	zip_country_code(args.zipcode, args.countrycode, args.apikey)



