#!/usr/bin/env python

import re
import httplib, urllib, urllib2, cookielib

# Open a connection to backdoor ctf server, send a GET request
# for the challenege page. Then read the text from the response.
connection = httplib.HTTPConnection("hack.bckdr.in")
response = connection.request("GET", 'http://hack.bckdr.in/2013-MISC-75/misc75.php')
response = connection.getresponse()
pageText = response.read()

#Pull the number we need to compute from the pageText
numsOnPage = [int(i) for i in pageText.split() if i.isdigit()]
numToCompute = numsOnPage[1]

# Function definition to compute our prime sum
def primeNumSum(numToCompute):
	sum = 0
	n = 0
	primeNum = 1
	while n < numToCompute:
		if primeNum > 1:
			for i in range(2, primeNum):
				if (primeNum % i) == 0:
					break
			else:
				sum += primeNum
				n = n + 1
		primeNum = primeNum + 1
	return sum

questionAnswer = primeNumSum(numToCompute) # Call the above function

#setup the header and response
pageHeader = response.getheaders()
pageCookie = pageHeader[2][1]

pageHeader = {"Content-type": "application/x-www-form-urlencoded"
			, "Cookie": pageCookie
			, "Host": "hack.bckdr.in"
			, "Connection" : "keep-alive"
			, "Cache-Control" : "max-age=0"
			, "Origin": "http://hack.bckdr.in"
			, "Referer": "http://hack.bckdr.in/2013-MISC-75/misc75.php"
			, "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36"}

pageParams = urllib.urlencode({'answer': questionAnswer, 'submit': 'Submit'}) # setup the forum to submit our data.

response = connection.request("POST", 'http://hack.bckdr.in/2013-MISC-75/misc75.php', pageParams, pageHeader) # send our calculated answer back to the server.
response = connection.getresponse() # get the data the server sends back to us.
print(response.read()) # print the response.
