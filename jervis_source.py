import sys

import yaml
import speech_recognition as sr 

from brain import brain
from library.resources.tts import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

name = profile_data['name']
city_name = profile_data['city_name']

tts('Welcome ' + name + ', thanks for waking me up. How can I help you?')

def main():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)

	try:
		speech_text = r.recognize_google(audio).lower().replace("'", "")
		print("Jervis thinks you said '" + speech_text + "'")
	except sr.UnknownValueError:
		print("Jervis could not understand")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

	brain(name, speech_text)

main()