import json
import mimetypes
import requests
import sys

from subprocess import call

urlApi = 'https://uplmg.com/'

# Upload a file
# file : path of the file
def uploadFile( file ):

	try:
		mimetypes.init()
		filename = file.split( '/' )[ -1 ]

		try:
			mime = mimetypes.types_map[ '.' + filename.split( '.' )[ -1 ] ]
		except KeyError:
			mime = "text/plain"

		files = { 'file' : ( filename, open( file , 'rb' ), mime ) }
		data = { 'senderid' : 'cmdUplmg' }
		
		r = requests.post( urlApi + 'file/upload', files=files, data=data )
		print( r.text )

	except IOError:
		print( "File not Found" )

	except:
		print( "Unexpected error : ", sys.exc_info()[ 0 ] )

# Download a file
# url : url of the file
def downloadFile( url ):
	url = str( url )
	
	try:
		if not url.startswith( 'http' ):
			url = urlApi + url

		call( [ 'wget', url] )
		head = requests.head( url )
		call( [ 'mv', url.split( '/' )[ -1 ] , head.headers[ 'Uplmg-Filename' ] + "." + head.headers[ 'Uplmg-Extension' ] ] )

	except KeyError:
		print( "" )

	except:
		print( "Unexpected error : ", sys.exc_info()[ 0 ] )


#Get headers
def showHeaders( shortname ):
	r = requests.head( urlApi + shortname )
	find = False
	for nom, valeur in r.headers.items():
		if nom.startswith( 'Uplmg' ):
			print( nom + ": " + valeur )
			find = True

	if not find:
		print( "Shortname Not Found" )

#Show Stats
def showStats():
	r = requests.get( urlApi + 'api/info/stats' )
	stats = json.loads( r.text )
	for nom, valeur in stats.items():
		print( nom + ": " + str( valeur ) )