import json
import mimetypes
import requests
import sys

from tabulate import tabulate

#Show Search
def showSearch( urlApi ):
	headers = ['mimetype', 'extension', 'encoding', 'views', 'senderid', 'shortName', 'originalFileName', 'size']
	datas = []

	r = requests.get( urlApi + '/api/files/search' )
	search = json.loads( r.text )
	for i in search:
		data = []
		for name, value in i.items():
			if name == 'senderid':
				data.append(value)
			if name == 'size':
				data.append(value)
			if name == 'mimetype':
				data.append(value)
			if name == 'encoding':
				data.append(value)
			if name == 'originalFileName':
				data.append(value)
			if name == 'shortName':
				data.append(value)
			if name == 'extension':
				data.append(value)
			if name == 'views':
				data.append(value)
		datas.append(data)

	print(tabulate(datas, headers=headers, tablefmt='orgtbl'))