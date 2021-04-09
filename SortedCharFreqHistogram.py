from os import strerror

charfreq = {}
char = []

try:
    fw = open('test','wt')
    fw.write("anhdrsjxdmaaj")
    fw.close()
    
except IOError as ie:
    print(strerr(ie.errno))
    
srcname = input("Enter File Name : ")
try:
    fr = open(srcname,'rt')
    ch = fr.read(1)
    
    while ch!= '':
        if ch not in char:
            char.append(ch)
            charfreq[ch] = 1
            ch = fr.read(1)
        elif ch in char:
            charfreq[ch] += 1
            ch = fr.read(1)
    fr.close()
            
except FileNotFoundError as fe:
    print(strerr(fe.errno))

for key, value in sorted(charfreq.items(),key = lambda x : x[1], reverse = True):
    print(key,"->",value)
    fw = open(srcname+".hist",'wt')
    fw.write(str(key)+"->"+str(value)+"\n")
fw.close()
        