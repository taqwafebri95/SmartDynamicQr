# -*- coding: utf-8 -*-
"""SmartQr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hbw0xd-a9jGrbVYf9dBTVC61wHXcl-QD
"""

!pip3 install requests

!pip install qrcode[pil]

!pip install gtts

!pip install prettytable

!pip install pytrends

import requests
API_KEY = "AIzaSyDJ2YM7V81X-iLanfEA3w03X6HYlE349XA"
SEARCH_ENGINE_ID = "2a3a1dab97dfd9253"

query = input("Anda Mau Cari apa? : ")
page = 1
start = (page - 1) * 10+ 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

data = requests.get(url).json()

search_items = data.get("items")
for i, search_item in enumerate(search_items, start=1):
    title = search_item.get("title")
    snippet = search_item.get("snippet")
    html_snippet = search_item.get("htmlSnippet")
    link = search_item.get("link")
    print("="*10,f" Heres i got for the Trends #{i+start-1}", "="*10)
    print("Title:", title)
    print("Description:", snippet)
    print(":", link, "\n")

from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = [query]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') 

data = pytrends.interest_over_time() 
import plotly.express as px
fig = px.line(data, y=[query], title='Ini adalah Trends berdasarkan Pencarian yang anda cari')
fig.show()

from prettytable import PrettyTable

myTable = PrettyTable(["Title","Description", "link"])
print(f"Ini Adalah Pencarian Terbaik Untuk anda : ")
myTable.add_row([title, snippet, link])
print(myTable)

import qrcode
from gtts import gTTS 
from IPython.display import Audio 
img = qrcode.make(link)
type(img)
tts = gTTS('here that i found, enjoy your Smart QR, and i said LOVE YOU, thanks for using our program best regrads ATM') 
tts.save('1.wav')
sound_file = '1.wav'
img.save("Hasil_qr.png")  
Audio(sound_file, autoplay=True)

"""Data Yang diperoleh dalam bentuk QR dinamis

Created By ATM team's 2022
# Azzahra, Taqwa, Mahendra


```
# This is formatted as code
```
"""