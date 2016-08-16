import sys

from clint.textui.progress import Bar as ProgressBar

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

def createConfigFile():
	''' Create a config file '''
	res =  '{\n'
	res += '\t"url" : "https://uplmg.com", \n'
	res += '\t"saveHistory" : true \n'
	res += '}'

	return res