from webscraping import download, alg
#filepath = 'listofsites.txt'
filepath = 'newresults.txt'

emails = []
#fp=open('results.txt','w+')
fp = open('results2.txt', 'w+')

with open(filepath,'r') as f:
    for cnt, line in enumerate(f):
        #print("Line {0}: {1}").format(cnt,line)
        print("Now scraping: "+line)
        chomped_line = line.strip('\n')
        Dobj = download.Download()
        html_page = Dobj.get(chomped_line, max_depth=200, max_urls=None, max_emails= None)
        new_emails = alg.extract_emails(html_page) 
        if len(new_emails)==0:
            print("no emails were found in this site: " + chomped_line + "\n")
        else:
            print(str(len(new_emails))+" email(s) were found in this site: " + chomped_line)
            print("writing new found emails in the results file")
            for item in new_emails:
                fp.write(item+"\n")
        #emails = emails + new_emails
        



fp.close()







