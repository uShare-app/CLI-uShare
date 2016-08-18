import json
import mimetypes
import requests, grequests
import sys
import pyperclip
import time

from subprocess import call
from termcolor import colored
from utils import *
from time import sleep
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

def uploadFile(file, copy):
	'''
	Upload a file
	ROUTE	= (POST) /file/upload

	file 	= (String) Path of the file to send 
	copy 	= (Boolean) True for copy in the clipboard,
	'''

	urlApi = getConfig()['url']

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

		r = requests.post(urlApi + '/file/upload', data = monitor, headers={'Content-Type': monitor.content_type})
		
		print colored('\n' + r.text, 'blue')

		if copy == True:
			pyperclip.copy(r.text)
			print colored('Copied in clipboard', 'green')

		if bool(getConfig()['saveHistory']):
			addHistory(r.text.split('/')[-1], time.strftime("%Y-%m-%d"), filename)			

	except IOError as e:
		print colored('IOError' , 'red')
		print e.message

	except TypeError as e:
		print colored('TypeError : ' , 'red')
		print e.message

def downloadFile(url):
	'''
	Download a file
	ROUTE	= (HEAD) /:url
	
	urlApi 	= (String) Url of the server, example : https://uplmg.com
	url 	= (String) ShortName of the file, or the complete url
	'''
	urlApi = getConfig()['url']
	url = str(url)

	try:
		if not url.startswith('http'):
			url = urlApi + '/' + url
			
		call(['wget', url])
		head = requests.head(url)
		call(['mv', url.split('/')[-1] , head.headers['Uplmg-Filename'] + "." + head.headers['Uplmg-Extension']])

	except KeyError as e:
		print colored('Key Error' , 'red')
		print e.message
	except:
		print colored('Unexpected error : ', 'red')
		print(sys.exc_info()[0])


def showHeaders(shortname):
	'''
	Show the headers of a file
	ROUTE		= (HEAD) /:shortname

	urlApi		= (String) Url of the server, example : https://uplmg.com
	shortname 	= (String) ShortName of the file
	'''

	urlApi = getConfig()['url']
	r = requests.head(urlApi + '/' + shortname)
	find = False
	for name, value in r.headers.items():
		if name.startswith('Uplmg'):
			print colored(name, 'yellow'), colored(':', 'white'), colored(value, 'blue')
			find = True

	if not find:
		print colored('Shortname Not Found', 'red')