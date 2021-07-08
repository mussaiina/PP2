handler = open('a.txt', 'r')
words = handler.read().split()
handler.close()
mp = {}

for i in words:
    if i not in mp:
        mp[i]=1
    else:
        mp[i]+=1

ss=list(mp.items()) 
ss.sort(key = lambda x : x[1],  reverse=True ) 
for  x  in  ss:
   print (x[0])