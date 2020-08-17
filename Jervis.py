import speech_recognition as sr
import os
import wikipedia
from gtts import gTTS
import datetime
import random
import calendar
import warnings

warnings.filterwarnings('ignore')

def recordAudio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Say something!')
		audio = r.listen(source)
		
	data = ''
	try:
		data = r.recognize_google(audio)
		print('You said ' + data)
	except sr.UnknownValueError:
		print('Google speech recognition could not understand what you said')
	except sr.RequestError as e:
		print('Request Error from Google Speech Recogntion Services ' + e)
	return data
recordAudio()

def assistantResponse(text):
	print(text)
	my_Obj = gTTS(text=text, lang='en', slow=False)
	my_Obj.save('assistant_Response.mp3')
	os.system('start assistant_Response.mp3')
text = 'experiment'
assistantResponse(text)
def wakWord(text):
	WAKE_WORDS = ['hey computer', 'okay Computer']
	text=text.lower()
	for phrase in text:
		return True
	return False
def getDate():
	now = datetime.datetime.now()
	my_date = datetime.datetime.today()
	weekday = calendar.day_name[my_date.weekday()]
	monthNum = now.month
	dayNum = now.day
	month_names = ['January', 'February', 'March', 'April', 
				   'May', 'June', 'July', 'August', 'September', 'October','November', 'December'] 
	ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th' '10th', '11th',
					   '12th', '13th', '14th', '15th', '16th', '17th' '18th', '19th', '20th', '21st',
					   '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']`
	return 'Today is ' + weekday + ' '  + month_names[monthNum-1]+ ' the '	+ ordinalNumbers[dayNum -2]+ '.'  
print(getDate())					   
def get_greeting(text):
	GREETING_INPUTS = ['hey','hello','hi','greetings']
	GREETING_OUTPUTS = ['Greeting Sir',' Hello Sir', 'How can I help you sir?', 
						'What may I assist you with Sir?', 'What may I do for you sir?']
	for word in text.split():
		if word.lower() in GREETING_INPUTS:
			return random.choice(GREETING_OUTPUTS) + '.' 
	return ''
def getPerson(text):
	wordList = text.split()
	for i in range(0, len(wordList)):
		if i + 3< = len(wordList)-1 and wordList[i].lower() == 'who' and wordList[i+1].lower() =='is':
			return wordList[i+2]+' '+wordList[i+3]		
while True:
	text = recordAudio()
	response= ''
	if(wakeWord(text) == True):
		response = response + greeting(text)
		if('date' in text):
			get_date= getDate()
			response = response + ' ' get_date
		if('time' in text):
			now = datetime.datetime.now()
			time =""
			if now.hour>=12:
				time = 'p.m.'
				hour = now.hour -12
			else:
				time = 'a.m.'
				hour = now.hour
			if now.minute < 10:
				minute = '0' + str(now.minute)
			else:
				minute = str(now.minute)
			response = response + ' ' + 'It is ' + str(hour) + ':' + minute + ' ' + time
		
		
		if('who is' in text):
			person = getPerson(text)
			wiki = wikipedia.summary(person, sentences = 2)
			response = response + ' ' + wiki
			
			   
	
