from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json

class Core_Base:
    def __init__(self):
        self.word = ""
        self.part = ""
        self.arr = []
        self.mean =[]
        self.data = {}
        self.trg = ""
        self.ind = ""
        self.p = ""

    #checks for every word using loop
    def words_p(self):
        # self.alpha = "abcdefghijklmnopqrstuvwxyz- "
        # for i in range(0,46):
        #     for j in range (0,i):

        # self.word = input("Enter a word:")
        self.format ="https://en.oxforddictionaries.com/definition/" + self.word
        try:
            html = urlopen(self.format)
        except HTTPError as e:
            return None 
        
        ch = self.check()
        if(ch == True):
            self.search_for_meaning(self.format)
        else:
            print("Not Valid")

    def pass_words(self):
        
        self.alpha = "abcdefghijklmnopqrstuvwxyz- "
        for i in self.alpha:
            self.__init__()
            self.word = i
            self.words_p()

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

        self.data[self.word] = []                                   #initialise the data[] for the particular word
        #collects the meaning of the word from the web
        for i in self.section:
            self.span = i.find_all("span",{"class" : "pos"})
            for name in self.span:
                self.part = name.get_text()
                # self.mean.append(name.get_text())
            self.trg = i.find_all("div", {"class":"trg"})
            for j in self.trg:
                self.p = j.find_all("p")
                for k in self.p:
                    self.ind = k.find_all("span", {"class": "ind"})
                    # print(self.ind)
                    for details in self.ind:
                        self.mean.append(details.get_text())
            self.arr.append(self.mean)

            self.data[self.word].append({                           #append the data[] with different meanings
                self.part: self.mean
            })
            self.mean = []
        print(self.data)
        with open('test.txt', 'a') as outfile:
            json.dump(self.data, outfile) 
            outfile.write('\n')



obj = Core_Base()
obj.pass_words()










