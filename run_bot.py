import pyautogui as pa
import keyboard
import time
import bot

bot.test_import()

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

#### RUN THE BOT ####

bot.run_bot(buff_coords, tele_coords, kishin_coords, df_coords)

