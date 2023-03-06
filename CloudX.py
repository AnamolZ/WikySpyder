import requests
from bs4 import BeautifulSoup
import customtkinter as ctk

def search_wiki():
    last_word = entry.get().split()[-1]
    url = "https://en.wikipedia.org/wiki/" + last_word
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = ""
    for i in range(len(soup.findAll('p'))):
        one_a_tag = soup.findAll('p')[i]
        text += one_a_tag.text
    output.delete('1.0', ctk.END)
    output.insert(ctk.END, text)

window = ctk.CTk()
window.title("Wikipedia Search")
window.geometry("500x500")

label = ctk.CTkLabel(window, text="WIKY Search:", font=("Helvetica", 14))
label.pack(pady=10)

entry = ctk.CTkEntry(window, font=("Helvetica", 14), width=100,height=10)
entry.pack(pady=10)

button = ctk.CTkButton(window, text="Search", font=("Helvetica", 14), command=search_wiki)
button.pack(pady=10)

output = ctk.CTkTextbox(window, font=("Helvetica", 12))
output.pack(pady=10, fill="both", expand=True)

window.mainloop()
