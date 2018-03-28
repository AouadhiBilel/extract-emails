filepath = 'listofsites.txt'
fp=open('new_list.txt','w+')


with open(filepath, 'r') as f:
    for cnt, line in enumerate(f):
        print(('Line{0}: site: {1}  \n').format(cnt, line))
        if line.startswith('www'):
            fp.write(line+" \n")



fp.close()
        

