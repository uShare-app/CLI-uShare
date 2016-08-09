import json
import mimetypes
import requests

from subprocess import call

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
	print( r.text )

# Download a file
# url : url of the file
def downloadFile(url):
	url = str(url)
	
	if not url.startswith('http'):
		url = urlApi + url

	call( [ 'wget', url] )
	head = requests.head(url)
	call( [ 'mv', url.split( '/' )[ -1 ] , head.headers['Uplmg-Filename'] + "." + head.headers['Uplmg-Extension']] )



#Get headers
def showHeaders(shortname):
	r = requests.head(urlApi + shortname)
	for nom, valeur in r.headers.items():
		if nom.startswith('Uplmg'):
			print( nom + ": " + valeur )

#Show Stats
def showStats():
	r = requests.get(urlApi + 'api/info/stats')
	stats = json.loads(r.text)
	for nom, valeur in stats.items():
		print( nom + ": " + str( valeur ) )