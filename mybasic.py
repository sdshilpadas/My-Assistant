import os
import pyttsx3

pyttsx3.speak("Welcome")

while True:
	print("What do you want to open?:" , end= " ")
	p = input()

	if ("run" in p)  and ("chrome" in p):
		os.system("google-chrome")

	elif (("run" in p) or ("start" in p)) and ("camera" in p):
		os.system('cheese')

	elif (("run" in p) or  ("execute" in p )) and  (("sublime" in p) or ("text editor" in p) ):
		os.system("subl")

	elif ("run" in p)  and (("video player" in p) or ("media" in p) or ("vlc" in p)):
		os.system("vlc")

	elif ("run" in p) and ("firefox" in p):
		os.system("firefox")

	elif  ("run" in p) and ("virtual box" in p):
		os.system("virtualbox")

	elif  ("show" in p) and ("calendar" in p):
		os.system("cal")

	elif  ("show" in p) and ("date and time" in p):
		os.system("date")

	elif  ("run" in p) and ("jupyter notebook" in p):
		os.system("jupyter notebook")

	elif ("start" in p) and (("r in p") or ("R" in p)):
		os.system("R")
		

	elif  ("exit" in p)  or ("quit" in p):
		break

	else:
		print('dont support')
		
		
		
		
		