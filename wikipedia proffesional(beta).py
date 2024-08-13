import requests
from bs4 import BeautifulSoup
import webbrowser as w
from selenium import webdriver
while (True):
 if __name__=="__main__":
   b="ru"
   i=input("Wikipedia proffesional command,active language:ru,console=con, language:en=english,ru=russian,ge=german")
   url=f"https://{b}.wikipedia.org/wiki/{i}"
   web=webdriver.Firefox()
   web.get(url)
   web2 = webdriver.Firefox()
   web1 = webdriver.Firefox()

 if i=="":
    print("Error safe mode")
    web.close()
 if i=="en":
    web.close()
    web2.close()
    v="en"
    g1 = input("Wikipedia proffesional command,active language:en,console=con, language:en=english,ru=russian,ge=german")
    url1 = f"https://{v}.wikipedia.org/wiki/{g1}"
    web1.get(url1)
if i=="ru":
    web.close()
    web1.close()
    v1="ru"
    g2 = input("Wikipedia proffesional firefox  command,active language:ru,console=con, language:en=english,ru=russian,ge=german")
    url11 = f"https://{v1}.wikipedia.org/wiki/{g2}"
    web2.get(url11)











