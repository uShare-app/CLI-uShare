import json
import mimetypes
import requests
import sys

from subprocess import call

urlApi = "https://uplmg.com"

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
		
		r = requests.post( urlApi + '/file/upload', files=files, data=data )
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
	for name, value in r.headers.items():
		if name.startswith( 'Uplmg' ):
			print( name + ": " + value )
			find = True

	if not find:
		print( "Shortname Not Found" )

#Show Stats
def showStats():
	r = requests.get( urlApi + '/api/files/stats' )
	stats = json.loads( r.text )
	for name, value in stats.items():
		print( name + ": " + str( value ) )


#Show Search
def showSearch():
	r = requests.get( urlApi + '/api/files/search' )
	search = json.loads( r.text )
	for i in search:
		for name, value in i.items():
			if name == "shortName":
				print name + ": " + value