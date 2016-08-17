import json
import mimetypes
import requests
import sys
from utils import *

from termcolor import colored

def showStats():
	'''
	Show Stats
	ROUTE	= (GET) /api/files/stats

	'''
	
	urlApi = getConfig()['url']

	r = requests.get(urlApi + '/api/files/stats')
	stats = json.loads(r.text)
	for name, value in stats.items():
		print colored(name, 'yellow'), colored(":", 'white'), colored(str(value), 'blue')
