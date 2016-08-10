import json
import mimetypes
import requests
import sys

urlApi = "https://uplmg.com"


#Show Stats
def showStats():
	r = requests.get( urlApi + '/api/files/stats' )
	stats = json.loads( r.text )
	for name, value in stats.items():
		print( name + ": " + str( value ) )
