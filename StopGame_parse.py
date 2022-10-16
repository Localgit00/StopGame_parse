import requests
from bs4 import BeautifulSoup as bs

max_page = 10 
pages=[]
def get_review():
    for x in range(1, max_page+1):
        pages.append(requests.get('https://stopgame.ru/review/new/stopchoice/p' + str(x))).text
    for page in pages:
        soup = bs(page, features="lxml")

        element=soup.select('body > div.page-layout > div > div > div > section:nth-child(4) > div') 

        for div in element:
            soup = bs(div.text, features="lxml")
            div=div.select('div.article-description > div.caption.caption-bold > a')
            for reviw in div:
                print(reviw.text)
            
if __name__ == '__main__':
    get_review()
