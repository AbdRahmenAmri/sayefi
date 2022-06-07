import requests
from bs4 import BeautifulSoup

class Thumb():
    def __init__(self,url) -> None:
        self.url = url
        self.loadPage()
    
    def loadPage(self) -> None:
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.getTitle()
        self.getThumb()
        self.getDescription()
    
    def getTitle(self) -> None:
        self.title = self.soup.title.text
    
    def getThumb(self) -> None:
        if(self.soup.find('meta',property="og:image")):
            self.thumb = self.soup.find('meta',property="og:image")["content"]
        elif (self.soup.find('meta',name="twitter:image")):
            self.thumb = self.soup.find('meta',name="twitter:image")["content"]
            
    def getDescription(self) -> None:
        if(self.soup.find('meta',property="og:description")):
            self.description = self.soup.find('meta',property="og:description")["content"]
        elif (self.soup.find('meta',name="twitter:description")):
            self.description = self.soup.find('meta',name="twitter:description")["content"]
        elif (self.soup.find('meta',name="description")):
            self.description = self.soup.find('meta',name="description")["content"]
        
    def get(self) -> dict:
        return {
            "url":self.url,
            "image":self.thumb,
            "title":self.title,
            "descripton":self.description
        }

    