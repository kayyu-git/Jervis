import random
from GreyMatter.SenseCells.tts import tts
#import text-to-speech function from SenseCells.tts package

def who_are_you():
	message = ['I am Jervis, the beantastic AI.', "The BEAN LORD Jervis."]
	tts(random.choice(message))

def how_am_i():
	replies = ["You are bean.", "Not dead. I think.", "Drink bleach."]
	tts(random.choice(replies))

def tell_joke():
	jokes = ['At the end of the day, we’re all human beans. Together we will rice. Now lettuce pray. Ramen.'
	'What is a bean that is outdated? A has-bean']
	tts(random.choice(jokes))

def who_am_i(name):
	tts('You are ' + name + ', the bean of beans')

def where_born():
	tts('I came from a bean')

def how_are_you():
	tts('BEANTASTIC')

def undefined():
	tts("I'm sorry that was not the bean.")