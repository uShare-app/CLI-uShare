import requests
import json

urlApi = 'https://uplmg.com/'

# Upload a file
# file : path of the file
def uploadFile(file):
	files = { 'file' : open(file , 'rb') }
	data = { 'senderid' : 'cmdUplmg' }
	headers = {'Content-Type' : 'image/png'}
	r = requests.post(urlApi + 'file/upload', files=files, data=data)
	print r.text

def showHeaders(shortname):
	r = requests.head(urlApi + shortname)
	print r.headers