import json
import mimetypes
import requests
import sys

from utils import *
from tabulate import tabulate

def showSearch(page = 1, date = '0000-00-00'):
	'''
	Search file with a page or a date
	ROUTE = (GET) /api/files/search

	urlApi	= (String) Url of the server, example : https://uplmg.com
	page	= (Integer) Number of the page (Optionnal)
	date	= (String) Format : aaaa-mm-dd Date of the file (Optional)
	'''
	
	urlApi = getConfig()['url']
	headers = ['shortName', 'originalFileName', 'size', 'encoding', 'mimetype', 'extension', 'senderid', 'views']
	datas = []
	req = urlApi + '/api/files/search'

	if date != '0000-00-00':
		split = date.split('-')
		if len(split) == 3 and len(split[0]) == 4 and len(split[1]) == 2 and len(split[2]) == 2:
			req += '/' + str(date)

	if page != 0:
		req += '/' + str(page)

	r = requests.get(req)
	search = json.loads(r.text)
	for i in search:
		value = []
		value.append(i['shortName'])
		value.append(i['originalFileName'][0: 45])
		value.append(i['size'])
		value.append(i['encoding'])
		value.append(i['mimetype'])
		
		try:
			value.append(i['extension'])
		except KeyError:
			value.append('Not Found')

		value.append(i['senderid'])
		value.append(i['views'])

		datas.append(value)

	print(tabulate(datas, headers=headers, tablefmt='orgtbl'))
