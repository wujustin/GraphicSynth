from collections import Counter
import pickle

cnt=0
filename ='data/newsgroup/new_game.txt'

with open(filename) as f:
    c = Counter()
    for x in f:
        x=x.decode('utf-8')
        c += Counter(x.strip())
        cnt += len(x.strip())
        #print c
print cnt

for key in c:
    c[key]=float(c[key])/cnt
    print key,c[key]
     
d = dict(c)
#print d
with open("data/models/char_freq.cp",'wb') as f:
    pickle.dump(d, f)
