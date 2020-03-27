import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

with open("recording.wav", "wb") as f:
	f.write(audio.get_wav_data())

#when run from terminal should print Say something!
#will use microphone to pick up audio
#save it as recording.wav

#Python program stops recording when it detects a pause 
#in your speech for a certain amount of time.