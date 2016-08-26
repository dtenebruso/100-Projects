#!/usr/bin/python3

import ntplib
from time import ctime

connection = ntplib.NTPClient()

response = connection.request('us.pool.ntp.org', version=3)
print(ctime(response.tx_time))