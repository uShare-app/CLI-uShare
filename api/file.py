import json
import mimetypes
import requests
import sys
import pyperclip

from subprocess import call
from termcolor import colored

# Upload a file
# file : path of the file
def uploadFile(urlApi, file, copy):

	try:
		mimetypes.init()
		filename = file.split('/')[-1]

		try:
			mime = mimetypes.types_map['.' + filename.split('.')[-1]]
		except KeyError:
			mime = 'text/plain'

		files = {'file' : (filename, open(file , 'rb'), mime)}
		data = {'senderid' : 'cli-Uplmg'}
		
		r = requests.post(urlApi + '/file/upload', files=files, data=data)

		print colored(r.text, 'blue')
		
		if copy == True:
			pyperclip.copy(r.text)
			print colored('Copied in clipboard', 'green')

	except IOError:
		print colored('File not Found' , 'red')

	except:
		print colored('Unexpected error : ', sys.exc_info()[0], 'red')

# Download a file
# url : url of the file
def downloadFile(urlApi, url):
	url = str(url)
	
	try:
		if not url.startswith('http'):
			url = urlApi + '/' + url
			
		call(['wget', url])
		head = requests.head(url)
		call(['mv', url.split('/')[-1] , head.headers['Uplmg-Filename'] + "." + head.headers['Uplmg-Extension']])

	except KeyError:
		print colored('Key Error' , 'red')

	except:
		print colored('Unexpected error : ', sys.exc_info()[0], 'red')


#Get headers
def showHeaders(urlApi, shortname):
	r = requests.head(urlApi + '/' + shortname)
	find = False
	for name, value in r.headers.items():
		if name.startswith('Uplmg'):
			print colored(name, 'yellow'), colored(':', 'white'), colored(value, 'blue')
			find = True

	if not find:
		print colored('Shortname Not Found', 'red')