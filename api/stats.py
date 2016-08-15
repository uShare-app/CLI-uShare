import json
import mimetypes
import requests
import sys

from termcolor import colored

#Show Stats
def showStats(urlApi):
	r = requests.get(urlApi + '/api/files/stats')
	stats = json.loads(r.text)
	for name, value in stats.items():
		print colored(name, 'yellow'), colored(":", 'white'), colored(str(value), 'blue')
