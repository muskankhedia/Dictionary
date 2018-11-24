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
        self.mean =""
        self.trg = ""
        self.ind = ""
        self.p = ""
        self.ex = ""
        self.example =""
        self.mean_ex = {}
        self.subsense =""
        self.submean = ""
        self.subex = ""
        self.submean_ex = {}
        self.sub_len = 0

    #checks for every word using loop
    def words_p(self):
        self.format ="https://en.oxforddictionaries.com/definition/" + self.word
        try:
            self.search_for_meaning(self.format)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print("the server could not be found")
        else:
            print(self.count)
        

    def pass_words(self):

        self.file_name = input("Enter the file name: ")
        self.file_json = self.file_name + ".json"
        self.file_name = self.file_name + ".txt"
        file = open(self.file_name, "r")
        self.count = 0
        self.data = {}

        for line in file:
            self.__init__()
            self.word = line
            self.length = len(self.word)
            self.word = self.word[0:self.length-1]
            self.count += 1
            self.words_p()
            time.sleep(3)
        
        with open(self.file_json, 'a') as outfile:
            json.dump(self.data, outfile) 
            outfile.close()
            print("Reached")
        file.close()
    
    #searches and stores the meaning of the particular word
    def search_for_meaning(self,url):
        html = urlopen(url)
        bsobj = BeautifulSoup(html.read(), 'lxml')
        self.section = bsobj.findAll("section", {"class": "gramb"})

        self.data[self.word] = [] 
                                                       
        #collects the meaning of the word from the web
        for i in self.section:
            self.span = i.find_all("span",{"class" : "pos"})
            for name in self.span:
                self.part = name.get_text()
                # self.mean.append(name.get_text())
            self.trg = i.find_all("div", {"class":"trg"})
            self.mean_ex[self.part] = []
            for j in self.trg:
                self.p = j.find_all("p")
                self.mean = ""
                for k in self.p:
                    self.ex =""
                    self.ind = k.find_all("span", {"class": "ind"})
                    # print(self.ind)
                    for details in self.ind:
                        self.mean = (details.get_text())
                    self.ex = j.find("li", {"class" : "ex"})
                    self.example = str(self.ex)       
                    self.example = self.example[21:-12] 

                    if(len(self.example) == 0):
                        self.ex = j.find("div", {"class" : "ex"})
                        self.example = str(self.ex)       
                        self.example = self.example[22:-12]  
                    
                    self.mean_ex[self.part].append({                           
                        "meaning": self.mean,
                        "example": self.example
                    })
                    self.ex = ""
                    self.submean_ex[self.part] = []
                    self.subsense = j.find_all("li", {"class" : "subSense"})
                    for details in self.subsense:
                        self.submean = details.find("span", {"class" : "ind"})
                        self.submean = str(self.submean)
                        self.submean = self.submean[18:-7]
                        self.ex = details.find("li", {"class" : "ex"})
                        self.subex = str(self.ex)
                        self.subex = self.subex[21:-12]

                        if(len(self.subex) == 0):
                            self.ex = details.find("div", {"class" : "ex"})
                            self.subex = str(self.ex)
                            self.subex = self.subex[22:-12]

                        if(len(self.submean) !=0 and len(self.subex) != 0):
                            self.submean_ex[self.part].append({
                                "subMeaning": self.submean,
                                "subExample": self.subex
                            })
                    self.sub_len = (len(self.submean_ex[self.part]))    
                    if(self.sub_len != 0):
                        self.mean_ex[self.part].append(self.submean_ex[self.part])
                
                self.mean = ""
        self.data[self.word].append(self.mean_ex)                           
                
        self.data_len = len(self.data[self.word])
        # print(self.data_len)
        if self.data_len < 1:
            del self.data[self.word]



obj = Core_Base()
obj.pass_words()