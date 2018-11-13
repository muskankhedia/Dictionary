from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# def gettitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None 
#     try:
#         bsobj = BeautifulSoup(html.read(), 'lxml')
#         title = bsobj.title
#         x = bsobj.h2.span
#         all_headings = bsobj.find_all("h2")
#         for link in all_headings:
#             span_ele = link.find_all('span')
#             str_span = str(span_ele)
#             cleantext = BeautifulSoup(str_span, "lxml").get_text()
#             print(cleantext) 

#     except AttributeError as e:
#         return None
#     return title

# title = gettitle('https://en.oxforddictionaries.com/definition/processor')
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)


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
        self.word = input()
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
        print(self.arr)
        self.section = bsobj.findAll("section", {"class": "gramb"})
        for i in self.section:
            self.span = i.find_all("span",{"class" : "pos"})
            self.trg = i.find_all("div", {"class":"trg"})
            self.mean.append(self.span)
            for j in self.trg:
                self.ind = j.find_all("span", {"class": "ind"})
                for k in self.ind:
                    self.mean.append(k.get_text())
                self.arr.append(self.mean)
                print(self.arr)

obj = Core_Base()
obj.words()










