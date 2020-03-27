import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

#recognize speech using Google Speech Recognition
try:
	print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(3))

#If i say "Hello my name is andrew"
#prints "Google Speech Recognition thinks you said hello my name is Andrew"