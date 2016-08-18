import sys
import json
import os
import sqlite3 as sql

from clint.textui.progress import Bar as ProgressBar
from tabulate import tabulate

def create_callback(encoder):
	''' 
	Create a callback, and create a progress bar for the upload file
	encoder = an instance of MultipartEncoder
	'''

	encoder_len = encoder.len
	bar = ProgressBar(expected_size=encoder_len, filled_char='#')

	def callback(monitor):
		bar.show(monitor.bytes_read)

	return callback

def loadConfig(path):
	'''
	Load Config File
	Create config.json if not exist
	'''
	global configFile

	if not os.path.exists(path + "config.json"):

		res =  '{\n'
		res += '\t"url" : "https://uplmg.com", \n'
		res += '\t"saveHistory" : true \n'
		res += '}'

		configFile = open(path + "config.json", "w")
		configFile.write(res)
		configFile.close()

	configFile = open(path + "config.json")
	configFile = json.load(configFile)


def loadDatabase(path):
	'''
	Load Database
	Create database.db and Table History if not exist
	'''
	
	global database

	database = path + "database.db"
	con = sql.connect(database)
	c = con.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS History(shortName, dateOfUpload, file, ndd)')
	con.commit()
	c.close()

def addHistory(shortName, dateOfUpload, file):
	'''
	Add new line in database.db

	'''
	con = sql.connect(database)
	c = con.cursor()
	c.execute('INSERT INTO History VALUES("' + shortName + '", "' + dateOfUpload + '", "' + file + '", "' + configFile['url'] + '")')
	con.commit()
	c.close()

def showHistory():
	'''
	Show the history
	'''

	headers = ['shortName', 'dateOfUpload', 'filename', 'link']
	datas = []

	con = sql.connect(database)
	c = con.cursor()
	c.execute('SELECT * FROM History')

	for row in c:
		value = []
		value.append(row[0])
		value.append(row[1])
		value.append(row[2])
		value.append(row[3] + "/" + row[0])
		datas.append(value)

	print(tabulate(datas, headers=headers, tablefmt='orgtbl'))

def getConfig():
	return configFile

def getDatabase():
	return database