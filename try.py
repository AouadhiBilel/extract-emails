from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
 


def getAllUrl(url):
urlList = []
try:
    page = uReq( url ).read()
    soup = bs(page)
    soup.prettify()
    for anchor in soup.findAll('a', href=True):
        if not 'http://' in anchor['href']:
            if urlparse.urljoin('http://bobthemac.com', anchor['href']) not in urlList:
                urlList.append(urlparse.urljoin('http://bobthemac.com', anchor['href']))
        else:
            if anchor['href'] not in urlList:
                urlList.append(anchor['href'])

    return urlList

except urllib2.HTTPError, e:
    urlList.append( e )

if __name__ == "__main__":
urls = getAllUrl('http://bobthemac.com')

fullList = []

for x in urls:
    listUrls = list
    listUrls = getAllUrl(x)
    try:
        for i in listUrls:
            if not i in fullList:
                fullList.append(i)
    except TypeError, e:
        print 'Woops wrong content passed'

for i in fullList:
    print i

