#!/usr/bin/env python3
# conding: utf-8

import sys, getopt

from api import *

sendHelp = 'Usage :\nuplmg <file>\nuplmg sendfile <file>\nuplmg download <url / shortname>\nuplmg showheaders <shortname>\nuplmg showstats'

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

	#CMD : uplmg <file>
	elif len( args ) == 1:
		uploadFile( args[ 0 ] )
		sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])
