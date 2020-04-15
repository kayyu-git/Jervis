import re

import wikipedia

from GreyMatter.SenseCells.tts import tts

def define_subject(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('define')
	cleaned_message = ' '.join(words_of_message)
	try:
		wiki_data = wikipedia.summary(cleaned_message, sentences=5)

		regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
		m = regEx.match(wiki_data)
		while m:
			wiki_data = m.group(1) + m.group(2)
			m = regEx.match(wiki_data)

		wiki_data = wiki_data.replace("'","")
		wiki_data = wiki_data.replace('=',"")
		wiki_data = wiki_data.split("\n")
		failsafe = wiki_data[0]
		while len(wiki_data) > 1 and len(wiki_data[0]) < 75:
			if len(wiki_data[0]) > len(failsafe):
				failsafe = wiki_data[0]
			wiki_data = wiki_data[1:]
		tts(wiki_data[0])
	except wikipedia.exceptions.DisambiguationError as e:
		tts('Can you please be more specific? You may choose something from the following.')
		print("Can you please be more specific? You may choose something from the following.; {0}".format(e))