#!/usr/bin/python3

import http.client, json, argparse

base = '/data/2.5/weather?zip='
cap = '&APPID='


def zip_country_code(zipc, country, appid):
	path = '{}{},{}{}{}'.format(base, zipc, country, cap, appid)
	print('\n\nRequest ', path,' has been sent\n\n')
	connection = http.client.HTTPConnection('api.openweathermap.org')
	connection.request('GET', path)
	rawreply = connection.getresponse().read()

	reply = json.loads(rawreply.decode('utf-8'))

#	Uncomment to capture the json response and write to local file
#	with open('reply.txt', 'wb') as f:	
#		f.write(rawreply)
#		f.close()

	print('Today will be mainly',reply['weather'][0]['main'],'\n'+reply['name']+' is looking at a humidity of',reply['main']['humidity'])

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Find your local weather')
	parser.add_argument('zipcode', metavar='zipc', help='your local zip code(14533)')
	parser.add_argument('countrycode', metavar='country', default='us', help='your country acronym (ex. us, uk or ru)')
	parser.add_argument('apikey', metavar='appid', help='your api.openweathermap.org api key')

	args = parser.parse_args()
	zip_country_code(args.zipcode, args.countrycode, args.apikey)



