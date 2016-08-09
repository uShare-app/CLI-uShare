#!/usr/bin/env python
# conding: utf-8

import sys, getopt

from api import *

sendHelp = 'Usage :\nuplmg sendfile <file>\nuplmg showheaders <shortname>\nuplmg showstats'

# main function
def main( argv ):

	if len( sys.argv ) == 1:
		print sendHelp
		sys.exit()

	
	opts, args = getopt.getopt( argv, 'h:')

	#Send File	
	if "sendfile" in args:
		if len( args ) == 2:
			uploadFile( args[ 1 ] )
			sys.exit()
		else:
			print sendHelp

	#Show headers of a uploaded file
	elif "showheaders" in args:
		if len( args ) == 2:
			showheaders( args[ 1 ] )
			sys.exit()
		else:
			print sendHelp

	#Show the stats
	elif "showstats" in args:
		if len ( args ) == 1:
			showStats()
			sys.exit
		else:
			print sendHelp

	#else send help
	else:
		print sendHelp

if __name__ == "__main__":
	main(sys.argv[1:])
