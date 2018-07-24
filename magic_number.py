
def gen_magic_number():
	return 4

def get_user_number():
	return int(input("Guess a number between 0 and 12: "))

def magic_number():

	if (get_user_number() == gen_magic_number()):
		print("Correct!")
	else:
		print("Try Again")

magic_number()