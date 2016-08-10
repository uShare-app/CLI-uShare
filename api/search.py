import json
import mimetypes
import requests
import sys

#Show Search
def showSearch( urlApi ):
	r = requests.get( urlApi + '/api/files/search' )
	search = json.loads( r.text )
	for i in search:
		for name, value in i.items():
			if name == "shortName":
				print name + ": " + value