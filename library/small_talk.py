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

def i_am_the_bone_of_my_sword():
	tts('I am the bone of my sword. Steel is my body and fire is my blood. I have created over a thousand blades, unknown to death nor known to life. Have withstood pain to create many weapons yet those hands will never hold anything. So, as I pray. Unlimited Blade Works.')

def undefined():
	tts('Im afraid I dont understand.')