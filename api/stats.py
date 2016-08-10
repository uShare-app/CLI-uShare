import json
import mimetypes
import requests
import sys

#Show Stats
def showStats( urlApi ):
	r = requests.get( urlApi + '/api/files/stats' )
	stats = json.loads( r.text )
	for name, value in stats.items():
		print( name + ": " + str( value ) )
