#!/usr/bin/env python
# conding: utf-8

import sys, getopt

from api import *

sendHelp = '--sendfile <file to upload>\n--showHeaders <shortname>'

# main function
def main(argv):

	if len(sys.argv) == 1 :
		print sendHelp
		sys.exit()

	try:
		opts, args = getopt.getopt(argv, 'h:', ["sendfile=", "showHeaders="])
	
	except getopt.GetoptError:
		print sendHelp
		sys.exit(2)

	for opt, arg in opts:

		if opt == '-h':
			print sendHelp
			sys.exit()

		elif opt == '--sendfile':
			uploadFile(arg)
			sys.exit()

		elif opt == '--showHeaders':
			showHeaders(arg)
			sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])
