import webbrowser as wb
from requests import*
from bs4 import*
i=input("добро пожаловать википедию свободную энциклапедию какую может редактировать каждый,напишите старт")
while (True):
    if i=="старт":
        i1=input("Окей давай определимся с языком напиши 1 если на русской 2 если на англиской 3 на белоруском")
        if i1=="1":
            i2=input("Вопрос выводитя на русский")
            url=f"https://ru.wikipedia.org/wiki/{i2}"
            wb.open_new_tab(url)
            print(f"Вот что нашлось на вопрос {i2}")
            c = get(url)
            bn=BeautifulSoup(c.content,"html.parser")
            print(bn.text)

        if i1=="2":
            i2=input("the question is translated into English")
            url=f"https://en.wikipedia.org/wiki/{i2}"
            wb.open_new_tab(url)
            print(f"Here's what we found in response to the question {i2}")
            c = get(url)
            bn=BeautifulSoup(c.content,"html.parser")
            print(bn.text)
        if i1=="3":
            i2=input("пытанне выводзіцца на беларускай мове")
            url=f"https://be.wikipedia.org/wiki/{i2}"
            wb.open_new_tab(url)
            print(f"Вось што знайшлося на пытанне {i2}")
            c = get(url)
            bn=BeautifulSoup(c.content,"html.parser")
            print(bn.text)

