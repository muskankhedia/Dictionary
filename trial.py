from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def gettitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None 
    try:
        bsobj = BeautifulSoup(html.read(), 'lxml')
        title = bsobj.title
        all_headings = bsobj.find_all("h2")
        # for link in all_headings:
        #     span_ele = link.find_all('span')
        #     str_span = str(span_ele)
        #     cleantext = BeautifulSoup(str_span, "lxml").get_text()
        #     print(cleantext) 
        namelist = bsobj.findAll("span", {"class": "pos"})
        for name in namelist:
            print(name.get_text())

    except AttributeError as e:
        return None
    return title

title = gettitle('https://en.oxforddictionaries.com/definition/mobile')
if title == None:
    print("Title could not be found")
else:
    print(title)

