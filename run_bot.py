import bot
import keyboard

setup = True
bot.test_import()

while setup:
	user_input = input("""
	
		1) Setup Positions
		2) Load Positions
	
	""")
	if user_input == '1':
		bot.key_setup()
		setup = False
	else:
		bot.load_coords()
		setup = False