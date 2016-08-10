#!/usr/bin/env python3
# conding: utf-8

import sys, getopt

sys.path.insert(0, './api/')

from file import *
from search import *
from stats import *

sendHelp = 'Commands :'
sendHelp += "\nuplmg <file>"
sendHelp += "\nuplmg sendfile <file>"
sendHelp += "\nuplmg download <url / shortname>"
sendHelp += "\nuplmg showheaders <shortname>"
sendHelp += "\nuplmg showstats"
sendHelp += "\nuplmg search"

# main function
def main( argv ):

	if len( sys.argv ) == 1:
		print ( sendHelp )
		sys.exit()
	
	opts, args = getopt.getopt( argv, 'h:')

	#Send File
	#CMD uplmg sendfile <file>
	if "sendfile" in args:
		if len( args ) == 2:
			uploadFile( args[ 1 ] )
			sys.exit()
		else:
			print( sendHelp )

	#Download File
	#CMD : uplmg downloadfile <url / shortname>
	elif "download" in args:
		if len( args ) == 2:
			downloadFile( args[ 1 ] )
			sys.exit()
		else:
			print( sendHelp )

	#Show headers of a uploaded file
	#CMD : uplmg <showheaders>
	elif "showheaders" in args:
		if len( args ) == 2:
			showHeaders( args[ 1 ] )
			sys.exit()
		else:
			print( sendHelp )

	#Show the stats
	#CMD : uplmg <showstats>
	elif "showstats" in args:
		if len ( args ) == 1:
			showStats()
			sys.exit
		else:
			print( sendHelp )

	elif "search" in args:
		if len ( args ) == 1:
			showSearch()
			sys.exit
		else:
			print( sendHelp )

	#CMD : uplmg <file>
	elif len( args ) == 1:
		uploadFile( args[ 0 ] )
		sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])
