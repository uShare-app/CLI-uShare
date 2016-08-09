import requests
import json
import mimetypes

urlApi = 'https://uplmg.com/'

# Upload a file
# file : path of the file
def uploadFile(file):

	mimetypes.init()
	filename = file.split('/')[-1]

	mime = mimetypes.types_map['.' + filename.split('.')[-1]]
	
	files = { 'file' : ( filename, open(file , 'rb'), mime ) }
	data = { 'senderid' : 'cmdUplmg' }
	
	r = requests.post(urlApi + 'file/upload', files=files, data=data)
	print r.text

#Get headers
def showHeaders(shortname):
	r = requests.head(urlApi + shortname)
	for nom, valeur in r.headers.items():
		if nom.startswith('Uplmg'):
			print nom + ": " + valeur