import pyautogui as pa
import keyboard
import time
import os
from ast import literal_eval

buff_timer = 5
kishin_spawn_timer = 2
teleport_delay = 1.52

def test_import():
	print('Imported successfully')
	
### CHECK FOR SAVED COORDS ###
def load_coords():
	if os.path.exists('saved_coords.txt'):
		f = open("saved_coords.txt", "r")
		loaded_coords = f.read()
		print(loaded_coords)
		
		# break the string into the proper tuples
		split_coords = loaded_coords.split("\n")
		
		# then reassign them
		buff_coords = literal_eval(split_coords[0])
		kishin_coords = literal_eval(split_coords[1])
		tele_coords = literal_eval(split_coords[2])
		df_coords = literal_eval(split_coords[3])
		
		# then send it to the run command
		run_bot(buff_coords, tele_coords, kishin_coords, df_coords)
	else:
		key_setup()
		

### SAVE THE OSK COORDS ###
def save_coords(buff_coords, kishin_coords, tele_coords, df_coords):
	key_locs = [buff_coords, kishin_coords, tele_coords, df_coords]
	saved_coords = open("saved_coords.txt", "w")
	coords_buffer = ""
	for key in key_locs:
		coord = str(key) + '\n'
		coords_buffer += coord
	saved_coords.write(coords_buffer)
	saved_coords.close()
	
def run_bot(buffs, teleport, kishin, df):
	print('Running the bot now, 5 seconds to make sure Maple is clicked')
	time.sleep(5)
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
				print('pressed buffs')
				timer_sec += buff_timer
				time.sleep(buff_timer)	# buff delay timer so you dont miss any buffs
				
				pa.click(kishin) # spawn kishin
				print('pressed kishin')
				timer_sec += kishin_spawn_timer
				time.sleep(kishin_spawn_timer)	# delay for kishin
			
			# teleport with 1.5 sec delay default
			pa.click(teleport)
			print('pressed teleport')
			time.sleep(teleport_delay)
			
			if timer_sec % 9 == 0: # timing for demon force
				pa.click(df)
				print('pressed demon force')
			timer_sec += 1.5 # adding 1.5 seconds to account for frame delay of skill
			print(timer_sec)
			
	except KeyboardInterrupt:
		print('done')

def key_setup():

	#### Key locs ####
	buff_coords = 0
	tele_coords = 0
	kishin_coords = 0
	df_coords = 0

	#########
	### FIND COORDS FOR BUFF MACRO ###
	print('Hover the mouse over the buff macro, then press enter: ')
	while True:
		if keyboard.is_pressed('return'):
			buff_coords = pa.position()
			print (buff_coords)
			break

	print('Coords set to {0}'.format(buff_coords))
	time.sleep(1)

	#########			
	### FIND COORDS FOR TELEPORT ###
	print('Hover the mouse over the teleport macro, then press enter: ')
	while True:
		if keyboard.is_pressed('return'):
			tele_coords = pa.position()
			print (tele_coords)
			break

	print('Coords set to {0}'.format(tele_coords))
	time.sleep(1)

	#########		
	### FIND COORDS FOR KISHIN ###
	print('Hover the mouse over the kishin macro, then press enter: ')
	while True:
		if keyboard.is_pressed('return'):
			kishin_coords = pa.position()
			print (kishin_coords)
			break

	print('Coords set to {0}'.format(kishin_coords))
	time.sleep(1)

	#########			
	### FIND COORDS FOR DEMON'S FURY ###
	print('Hover the mouse over the demon force macro, then press enter: ')
	while True:
		if keyboard.is_pressed('return'):
			df_coords = pa.position()
			print (df_coords)
			break
			
	print('Coords set to {0}'.format(df_coords))
	save_coords(buff_coords, tele_coords, kishin_coords, df_coords)
	run_bot(buff_coords, tele_coords, kishin_coords, df_coords)