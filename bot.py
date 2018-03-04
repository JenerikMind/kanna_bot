import pyautogui as pa
import keyboard
import time

buff_timer = 4
kishin_spawn_timer = 2
teleport_delay = 1.5
def test_import():
	print('Imported successfully')

def run_bot(buffs, teleport, kishin, df):
	print('Running the bot now')
	try:
		timer_sec = 0
		while True:
			# Press esc to break the loop
			if keyboard.is_pressed('esc'):
				print('Escape button pressed.')
				break
		
			# if its a fresh run of the program or
			# every 2 minutes
			if timer_sec == 0 or timer_sec % 120 == 0:
				pa.click(buffs) # apply buffs
				time.sleep(buff_timer)	# buff delay timer so you dont miss any buffs
				pa.click(kishin) # spawn kishin
				time.sleep(kishin_spawn_timer)	# delay for kishin
			
			# teleport with 1.5 sec delay default
			pa.click(teleport)
			time.sleep(teleport_delay)
			
			if timer_sec % 9 == 0: # timing for demon force
				pa.click(df)
			timer_sec += 1.5 # adding 1.5 seconds to account for frame delay of skill
			print(timer_sec)
			
	except KeyboardInterrupt:
		print('done')