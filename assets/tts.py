import os
import sys

def tts(message):
	
	if sys.platform == 'darwin':
		tts_engine = 'say'
		return os.system(tts_engine + ' ' + message)
	elif sys.platform == 'linux2' or sys.platform == 'linux':
		tts_engine = 'espeak'
		return os.system(tts_engine + ' "' + message + '"')
	elif sys.platform == 'win32':
		tts_engine = 'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\''
		return os.system(tts_engine + message + '\');"')