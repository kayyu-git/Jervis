import sys

import yaml
import speech_recognition as sr 

from assets.tts import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

name = profile_data['name']
city_name = profile_data['city_name']

tts('Welcome ' + name + ', systems are now ready to run. How can I help you?')

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

	tts(speech_text)

main()