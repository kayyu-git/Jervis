from resources.tts import tts

def who_are_you():
	message = 'I am Jervis, the superior AI.'
	tts(message)

def undefined():
	tts('I don\'t know what you mean.')