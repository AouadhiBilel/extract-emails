from urllib.request import urlopen



filepath = 'new_list.txt'
fp= open("newresults.txt","w+")

with open(filepath, 'r') as f:
    for cnt, line in enumerate(f):
        print(("Now cheking website: {0}").format(line))
        #if line==" \n":
        #    print("space")
        #print(line.strip('\n'))
        if line==" \n":
            print("newline")
            continue
        #strip_line = line.strip('\n')
        #strip_line = strip_line.strip()
        print(line+" ---------------")
        http = "http://"
        https = "https://"
        newline = http + line
        print(newline)
        #code = urlopen(newline).getcode()
        try:
           code = urlopen(http+line).getcode()
           print("code is " + str(code))
           if code==200:
               print("this site is cool: {0}".format(line))
               fp.write(http+line)
        except:
            print("code in except is "+str(code))
            fp.write(https+line)
        """
        if urlopen(newline).getcode()==403:
            #fp.write(("Error with this website: {0}"+"\n").format(line))
            print(https+line)
            code= urlopen(http + line).getcode()
            if code==200:
                fp.write(("This website seems to be working: {0}"+"\n").format(line))    
            else:
                fp.write(("This website seems to be working: {0}"+"\n").format(line))
        try:
                newline = https + line
                code = urlopen(newline).getcode()
            except:
                if code!=200:
                    fp.write(("Error with this website: {0}"+"\n").format(line))
                elif code==200:
                    fp.write(("This website seems to be working: {0}"+"\n").format(line))
            """




fp.close()
