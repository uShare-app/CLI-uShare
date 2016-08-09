import requests
import json

urlApi = 'https://uplmg.com/'

# Upload a file
# file : path of the file
def uploadFile(file):
	files = { 'file' : ( 'capture.png', open(file , 'rb'), 'image/png' ) }
	data = { 'senderid' : 'cmdUplmg' }
	r = requests.post(urlApi + 'file/upload', files=files, data=data)
	print r.text

#Get all header
def showHeaders(shortname):
	r = requests.head(urlApi + shortname)
	for nom, valeur in r.headers.items():
		if nom.startswith('Uplmg'):
			print nom + ": " + valeur