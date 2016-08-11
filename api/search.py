import json
import mimetypes
import requests
import sys

from tabulate import tabulate

#Show Search
def showSearch( urlApi ):
	headers = ['shortName', 'originalFileName', 'size', 'encoding', 'mimetype', 'extension', 'senderid', 'views']
	datas = []
	r = requests.get( urlApi + '/api/files/search' )
	search = json.loads( r.text )
	for i in search:
		data = []
		data.append(i['shortName'])
		data.append(i['originalFileName'][0: 45])
		data.append(i['size'])
		data.append(i['encoding'])
		data.append(i['mimetype'])
		
		try:
			data.append(i['extension'])
		except KeyError:
			data.append('Not Found')

		data.append(i['senderid'])
		data.append(i['views'])

		datas.append(data)

	print(tabulate(datas, headers=headers, tablefmt='orgtbl'))