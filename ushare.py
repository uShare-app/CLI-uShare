#!/usr/bin/env python
# conding: utf-8

import sys, getopt
import json
import requests

path = __file__[0 : -9]
sys.path.insert(0, path + 'api/')

from file import *
from search import *
from stats import *
from termcolor import colored

localVersion = "0.4-Beta"
fileVersion = json.loads(requests.get("https://update.uplmg.com/cli.json").text)

if fileVersion['version'] != localVersion:
	print colored('A new release of CLI is now available', 'red')
	print colored('You can download it on ' + fileVersion['url'], 'red')
	print colored('Update : ' + fileVersion['description'], 'red')

loadConfig(path)
loadDatabase(path)

sendHelp = colored('Commands :', 'green')
sendHelp += colored("\nuplmg <file> [-c]", 'yellow')
sendHelp += colored("\nuplmg sendfile <file> [-c]", 'yellow')
sendHelp += colored("\nuplmg download <url / shortname>", 'yellow')
sendHelp += colored("\nuplmg showheaders <shortname>", 'yellow')
sendHelp += colored("\nuplmg showstats", 'yellow')
sendHelp += colored("\nuplmg search [-p <number>] [-d <yyyy-mm-dd>]", 'yellow')
sendHelp += colored("\nuplmg history", 'yellow')


# main function
def main(argv):

	if len(sys.argv) == 1:
		print(sendHelp)
		sys.exit()
	
	opts, args = getopt.getopt(argv, 'h:')

	#Send File
	#CMD uplmg sendfile <file>
	if "sendfile" in args:
		if len(args) >= 2:
			copy = False
			if '-c' in args:
				copy = True

			uploadFile(args[1], copy)
		else:
			print(sendHelp)
		sys.exit()

	#Download File
	#CMD : uplmg downloadfile <url / shortname>
	elif "download" in args:
		if len(args) == 2:
			downloadFile(args[1])
		else:
			print(sendHelp)
		sys.exit()

	#Show headers of a uploaded file
	#CMD : uplmg showheaders
	elif "showheaders" in args:
		if len(args) == 2:
			showHeaders(args[1])
		else:
			print(sendHelp)
		sys.exit()

	#Show history
	#CMD : ushare history
	elif "history" in args:
		if len(args) == 1:
			showHistory()
		else:
			print(sendHelp)
		sys.exit()

	#Show the stats
	#CMD : uplmg showstats
	elif "showstats" in args:
		if len(args) == 1:
			showStats()
		else:
			print(sendHelp)
		sys.exit()

	#Show the search
	#CMD : uplmg search [-p <number>] [-d <date format aaaa-mm-dd>]
	elif "search" in args:
		page = 0
		date = ''
		try:
			if '-p' in args:
				page = int(args[args.index('-p') + 1])
			if '-d' in args:
				date = str(args[args.index('-d') + 1])
		except:
			print(sendHelp)
			sys.exit()

		showSearch(page=page, date=date)
		sys.exit

	#CMD : uplmg file
	elif len(args) >= 1:
		copy = False
		if '-c' in args:
			copy = True

		uploadFile(args[0], copy)
		sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])