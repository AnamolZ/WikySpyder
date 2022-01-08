import winsound
import os
import sys
import time
import speech_recognition as sr
import playsound

def play():
	playsound.playsound('ask.mp3', True)

time.sleep(3)

filename = 'live.mp3'
winsound.PlaySound(filename, winsound.SND_FILENAME)
play()
r = sr.Recognizer()
r.pause_threshold = 1.0
r.phrase_threshold = 1.0
r.non_speaking_duration = 1.0
with sr.Microphone() as source:
	while True:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		try:
			a = r.recognize_google(audio)
			print(a)
			if a == "exit":
				os.system('TASKKILL /F /IM CloudXI.exe')
				os.remove("live.txt")
				os.remove("live.mp3")
				os.system('TASKKILL /F /IM CloudXz.exe')
				print("..Closed Go For The Next One..")
			else:
				print("..Manually Reading Mod ON..")
				os.remove("live.txt")
				os.remove("live.mp3")
				os.system('TASKKILL /F /IM CloudXz.exe')
		except Exception as e:
			print(":( error !")
			os.remove("live.txt")
			os.remove("live.mp3")