from itertools import groupby
s = str(input())
itm = [] 
occ = []
y = [list(g) for k, g in groupby(s)] 

for x in y:
    itm.append(int(x[0]))
    occ.append(len(x))
    
t = zip(occ,itm)
print(*t)
    
