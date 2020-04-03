from library import small_talk

def brain(name, speech_text):
	def check_message(check):
		if speech_text == check:
			return True
		else:
			return False

	if check_message('who are you'):
		small_talk.who_are_you()
	else:
		small_talk.undefined()