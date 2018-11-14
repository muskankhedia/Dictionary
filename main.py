from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import json
import time

class Core_Base:
    def __init__(self):
        self.word = ""
        self.part = ""
        self.arr = []
        self.mean =[]
        self.trg = ""
        self.ind = ""
        self.p = ""

    #checks for every word using loop
    def words_p(self):
        self.format ="https://en.oxforddictionaries.com/definition/" + self.word
        try:
            html = urlopen(self.format)
            self.search_for_meaning(self.format)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print("the server could not be found")
        else:
            print("It worked !")
        

    def pass_words(self):

        file = open("wordss.txt", "r")
        self.count = 0
        self.data = {}

        for line in file:
            self.__init__()
            self.word = line
            self.length = len(self.word)
            self.word = self.word[0:self.length-1]
            self.count += 1
            print(self.count)
            self.words_p()
            time.sleep(3)
        with open('test.json', 'a') as outfile:
            json.dump(self.data, outfile) 
            outfile.close()
            print("Reached")
        file.close()
    
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
        self.arr_len = len(self.arr)
        # print(self.data)
        self.data_len = len(self.data[self.word])
        # print(self.data_len)
        if self.data_len < 1:
            del self.data[self.word]



obj = Core_Base()
obj.pass_words()











