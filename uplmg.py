#!/usr/bin/env python
# conding: utf-8

import requests
import sys, getopt

# fonction principal
def main(argv):

	#Si la longuer de l'argument est egale a 1 on exit
	if len(sys.argv) == 1 :
		print './uplmg.py -f <file to upload>'
		sys.exit()

	#On essaye de recuper les parametres
	try:
		opts, args = getopt.getopt(argv, 'hf:', ["file="])
	
	except getopt.GetoptError:
		print './uplmg.py -f <file to upload>'
		sys.exit(2)

	#Pour chauque argument dans la commande
	for opt, arg in opts:
		#Si c'est -h on envoie l'aide
		if opt == '-h':
			print './uplmg.py -f <file to upload>'
			sys.exit()
		#SI c'est -f ou --file on upload le fichier
		elif opt in ("-f", "--file"):
			files = { 'file' : open(arg , 'rb') }
			data = { 'senderid' : 'cmdUplmg' }
			r = requests.post('https://uplmg.com/file/upload', files=files, data=data)
			print r.text
			sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])
