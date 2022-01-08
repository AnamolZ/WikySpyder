import speech_recognition as sr
import urllib.request
from bs4 import BeautifulSoup
import os
import requests
import sys
from gtts import gTTS
import comtypes.client
from threading import Thread
import subprocess

def func1():
    subprocess.call("CloudXI.exe", shell=True)

def func2():
    subprocess.call("CloudXz.exe", shell=True)

r = sr.Recognizer()
r.pause_threshold = 1.0
r.phrase_threshold = 1.0
r.non_speaking_duration = 1.0
keyWord = 'hey'
with sr.Microphone() as source:
    while True:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            a = r.recognize_google(audio)
            if keyWord.lower() in a.lower():
                text = a
                first, *middle, last = text.split()
                print(last)
                url = "https://en.wikipedia.org/wiki/" + last
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                for i in range(len(soup.findAll('p'))):
                    one_a_tag = soup.findAll('p')[i]
                    with open('live.txt', 'a+', errors='ignore') as f:
                        print(one_a_tag.text, file=f)
                text=""
                speak = comtypes.client.CreateObject("SAPI.SpVoice")
                filestream = comtypes.client.CreateObject("SAPI.spFileStream")
                filestream.open("live.mp3", 3, False)
                with open("live.txt","r") as file:
                    for line in file:
                        text=text + line
                speak.AudioOutputStream = filestream 
                speak.Speak(text)
                filestream.close()
                if __name__ == '__main__':
                	Thread(target = func1).start()
                	Thread(target = func2).start()
                print("Finished")
        except Exception as e:
            print()