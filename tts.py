import os
import sys

def tts(message):
	"""
	takes a message in and converts it to speech depending on the OS
	"""
	if sys.platform == 'darwin':
		tts_engine = 'say'
		return os.system(tts_engine + ' ' + message)
	elif sys.platform == 'linux2' or sys.platform == 'linux':
		tts_engine = 'espeak'
		return os.system(tts_engine + ' "' + message + '"')

tts("Hello BEAN this is Jervis")