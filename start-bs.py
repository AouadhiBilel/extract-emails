from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import re 

my_url = 'http://www.amysbookishlife.blogspot.co.uk/'
uClient = uReq(my_url)
page_html = uClient.read().decode('utf-8')


uClient.close()

page_soup = bs(page_html, "html.parser")

#container = page_soup.findAll("div", {"class": "single-article single-article-small-pic"})

#print(len(container))

print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",str(page_soup)))
#print(len(container))
