from tkinter import *
import os
from tkinter import messagebox
import speech_recognition as sr
import tkinter.scrolledtext as tkst
import tkinter as tk
from tkinter.scrolledtext import *
import subprocess

def About_us():
    subprocess.call("About us.html", shell=True)

def Call_me():
	answer = messagebox.askquestion("Exit", "Do you really want to exit")
	if answer == 'yes':
		root.quit()

def dis_play():
	if os.path.isfile('live.txt'):
		for line in open("live.txt", "r").readlines():
			editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
			editArea.insert(tk.INSERT,line)
	else:
		print ("File not exist")

root = tk.Tk()
root.geometry("800x400")
root.title("CloudX")

main_menu = Menu(root)
root.config(menu=main_menu)
fileMenu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label = "About", menu = fileMenu)
fileMenu.add_command(label="Developer", command=About_us)

root = tk.Frame(
    master = root,
    bg = '#135206235'
)

root.pack(fill='both', expand='yes')
editArea = tkst.ScrolledText(
    master = root,
    wrap   = tk.WORD,
    width  = 10,
    height = 0
)

dis_play()

b2 = Button(root, text="Close window", command=Call_me)
b2.place(x=1250,y=660)

root.mainloop()
