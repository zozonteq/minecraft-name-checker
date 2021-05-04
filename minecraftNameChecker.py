import requests
from bs4 import BeautifulSoup
import random
import time

words = "qwertyuioopasdfghjklzxcvbnm1234567890"
url = "https://ja.namemc.com/search?q="

while True:
    wd = words[random.randint(0,len(words)-1)]
    wd = wd +words[random.randint(0,len(words)-1)]
    wd = wd +words[random.randint(0,len(words)-1)]
    
    r = requests.get(url+wd)
    soup = BeautifulSoup(r.content, "html.parser")

    res = soup.find("div",class_="my-1")
    if(res!=None) :
        //通常の処理
        print(res.text)
        print('"'+wd+'"'+"調査完了")
    else :
        //アクセスのし過ぎで、IPアドレスが一時的に制限された時の処理です。
        time.sleep(5)
        r = requests.get(url+wd)
        soup = BeautifulSoup(r.content, "html.parser")

        res = soup.find("div",class_="my-1")
        if(res!=None) :
            print(res.text)
            print('"'+wd+'"'+"調査完了")


    


