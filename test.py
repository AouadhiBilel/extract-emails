from webscraping import download, alg

Dobj = download.Download()
html = Dobj.get("http://www.sharing55tories.blogspot.com/",max_depth=1000, max_urls=None, max_emails=None)

emails = alg.extract_emails(html)

print emails
