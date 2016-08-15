import json
import mimetypes
import requests, grequests
import sys
import pyperclip

from subprocess import call
from termcolor import colored
from utils import *
from time import sleep
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

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

		encoder = MultipartEncoder(
		{
			'senderid': 'cli-Uplmg', 
			'file':  (filename, open(file, 'rb'), mime)
		})
		
		callback = create_callback(encoder)
		monitor = MultipartEncoderMonitor(encoder, callback)

		r = requests.post
		(
			urlApi + '/file/upload', 
			data=monitor, 
			headers=
			{
				'Content-Type': monitor.content_type
			}
		)

		print colored('\n' + r.text, 'blue')

		if copy == True:
			pyperclip.copy(r.text)
			print colored('Copied in clipboard', 'green')

	except IOError as e:
		print colored('IOError' , 'red')
		print e.message

	except TypeError as e:
		print colored('TypeError : ' , 'red')
		print e.message

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
		print colored('Unexpected error : ', 'red')
		print(sys.exc_info()[0])


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

