import json
import mimetypes
import requests
import sys

from tabulate import tabulate

#Show Search
def showSearch( urlApi, page, date ):
	headers = ['shortName', 'originalFileName', 'size', 'encoding', 'mimetype', 'extension', 'senderid', 'views']
	datas = []
	req = urlApi + '/api/files/search'

	if date != 0:
		split = date.split('-')
		if len( split ) == 3 and len( split[0] ) == 4 and len ( split[1] ) == 2 and len ( split[2] ) == 2:
			req += '/' + str ( date )

	if page != 0:
		req += '/' + str( page )

	r = requests.get( req )
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