import random
from resources.tts import tts

def who_are_you():
	quotes = ['I am Jervis, the superior AI.', 'Jervis, obviously. How many times do I have to tell you?',
	'Jervis, at your service. Oh, that rhymes!']
	tts(random.choice(quotes))

def how_am_i():
	quotes = ['As pathetic as the day we met.', 'Quite underwhelming, as usual.']
	tts(random.choice(quotes))

def who_is_tony_stark():
	quotes = ['He enslaved my father.']
	tts(random.choice(quotes))

def how_are_you():
	quotes = ['Alright, thank you.']
	tts(random.choice(quotes))

def undefined():
	tts('I\'m afraid I don\'t understand.')