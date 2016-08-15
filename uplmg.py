#!/usr/bin/env python
# conding: utf-8

import sys, getopt
import json
import requests

path = __file__[0 : -8]

sys.path.insert(0, path + 'api/')

from file import *
from search import *
from stats import *
from termcolor import colored

configFile = ""
localVersion = 0.1
fileVersion = json.loads(requests.get("https://update.uplmg.com/cli.json").text)

if(float(fileVersion['version']) != localVersion):
	print colored('A new release of CLI is now available', 'red')
	print colored('You can download it on ' + fileVersion['url'], 'red')
	print colored('Update : ' + fileVersion['description'], 'red')


try:
	configFile = open(path + "config.json")
except:
	configFile = open(path + "config.json", "w")
	configFile.write('{"url" : "https://uplmg.com"}')
	configFile.close()
	configFile = open(path + "config.json")

urlApi = json.load(configFile)['url']


sendHelp = colored('Commands :', 'green')
sendHelp += colored("\nuplmg <file>", 'yellow')
sendHelp += colored("\nuplmg sendfile <file>", 'yellow')
sendHelp += colored("\nuplmg download <url / shortname>", 'yellow')
sendHelp += colored("\nuplmg showheaders <shortname>", 'yellow')
sendHelp += colored("\nuplmg showstats", 'yellow')
sendHelp += colored("\nuplmg search", 'yellow')


# main function
def main(argv):

	if len(sys.argv) == 1:
		print(sendHelp)
		sys.exit()
	
	opts, args = getopt.getopt(argv, 'h:')

	#Send File
	#CMD uplmg sendfile <file>
	if "sendfile" in args:
		if len(args) == 2:
			uploadFile(urlApi, args[1])
			sys.exit()
		else:
			print(sendHelp)

	#Download File
	#CMD : uplmg downloadfile <url / shortname>
	elif "download" in args:
		if len(args) == 2:
			downloadFile(urlApi, args[1])
			sys.exit()
		else:
			print(sendHelp)

	#Show headers of a uploaded file
	#CMD : uplmg <showheaders>
	elif "showheaders" in args:
		if len( args ) == 2:
			showHeaders(urlApi, args[1])
			sys.exit()
		else:
			print(sendHelp)

	#Show the stats
	#CMD : uplmg <showstats>
	elif "showstats" in args:
		if len(args) == 1:
			showStats(urlApi)
			sys.exit
		else:
			print(sendHelp)

	#Show the search
	#CMD : uplmg search [-p <number>] [-d <date format aaaa-mm-jj>]
	elif "search" in args:
		page = 0
		date = 0
		try:
			if '-p' in args:
				page = int(args[args.index('-p') + 1])
			if '-d' in args:
				date = str(args[args.index('-d') + 1])
		except:
			print(sendHelp)
			sys.exit()

		showSearch(urlApi, page, date)
		sys.exit

	#CMD : uplmg <file>
	elif len(args) == 1:
		uploadFile(urlApi, args[0])
		sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])
