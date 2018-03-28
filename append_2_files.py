import re
import dns.resolver as resolve
filepath1 = 'results.txt'
filepath2 = 'final_results.txt'


with open(filepath1, "r") as f:
    with open(filepath2, "w") as fp:
        for cnt, line in  enumerate(f):
            print("line{0}, now looking at email {1}".format(cnt, line))
            #match = re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', line)
            #if match == None:
            #    print("Bad syntax")
            records = resolve.query(line, 'MX')
            #print(records)
            #mxRecord = records[0].exchange
            #mxRecord = str(mxRecord)
