from library import small_talk

def brain(name, speech_text):
	def check_message(check):
		words = speech_text.split()
		if set(check).issubset(set(words)):
			return True
		else:
			return False

	if check_message(['who', 'are', 'you']):
		small_talk.who_are_you()

	elif check_message(['how', 'am', 'i']):
		small_talk.how_am_i()

	elif check_message(['who', 'is', 'tony', 'stark']):
		small_talk.who_is_tony_stark()

	elif check_message(['how', 'are', 'you']):
		small_talk.how_are_you()

	else:
		small_talk.undefined()