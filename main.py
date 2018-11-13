from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


class Core_Base:
    def __init__(self):
        self.word = ""
        self.part = ""
        self.arr = []
        self.mean =[]
        
    #checks for every word using loop
    def words(self):
        # self.alpha = "abcdefghijklmnopqrstuvwxyz- "
        # for i in self.alpha:
        self.word = input("Enter a word:")
        self.format ="https://en.oxforddictionaries.com/definition/" + self.word
        # ch = self.check()
        # if(ch == "True"):
        self.search_for_meaning(self.format)

    #checks if the word starts or ends with space or hypen
    def check(self):
        w_len = len(self.word)
        if self.word[0] == ' ' or self.word[0] == '-' or self.word[w_len-1] == ' ' or self.word[w_len-1] == '-':
            return False
        else:
            return True
    
    #searches and stores the meaning of the particular word
    def search_for_meaning(self,url):
        html = urlopen(url)
        bsobj = BeautifulSoup(html.read(), 'lxml')
        self.arr.append(self.word) 
        self.section = bsobj.findAll("section", {"class": "gramb"})
        for i in self.section:
            self.span = i.find_all("span",{"class" : "pos"})
            for name in self.span:
                self.mean.append(name.get_text())
            self.trg = i.find_all("div", {"class":"trg"})
            for j in self.trg:
                self.ind = j.find_all("span", {"class": "ind"})
                for details in self.ind:
                    self.mean.append(details.get_text())
        self.arr.append(self.mean)
        mean = []
        print(self.arr)

obj = Core_Base()
obj.words()










