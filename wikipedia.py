import requests as rq
from bs4 import BeautifulSoup
import webbrowser as wb
import os
r="ru"
while (True):

 i=input("Добро пожаловать в википедию напишите вопрос на русккий=1 или поменяйте язык на английский=2,3=секретная клавиша,4=exit")
 url=f'https://{r}.wikipedia.org/wiki/{i}'
 req=rq.get(url)
 b=BeautifulSoup(req.content,"html.parser")
 print(f"Вот что нашлось на {i}")
 print(b.text)
 wb.open_new(url)
 if i=="2":
     v="en"
     i = input("Добро пожаловать в википедию напишите вопрос английский=2")
     url = f'https://{v}.wikipedia.org/wiki/{i}'
     req = rq.get(url)
     b = BeautifulSoup(req.content, "html.parser")
     print(f"Вот что нашлось на {i}")
     print(b.text)
     wb.open_new_tab(url)
 if i=="3":
     cmd="notepad"
     os.system(cmd)
 if i=="4":
     exit()