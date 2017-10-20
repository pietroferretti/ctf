# coding: utf-8
s = open('ctfcoco.html').read()
len(s)
s
len(s)
s.split('style')
len(s.split('style'))
len(s.split('style')[1])
style = s.split('style')[1]
style.split(';}.')
len(style.split(';}.'))
cocos = [x.split('{')[0] for x in style.split(';}.')]
len(cocos)
cocos
cocos_n = [int(x[4:]) for x in cocos]
cocos[0]
cocos[1]
cocos = cocos[1:]
cocos_n = [int(x[4:]) for x in cocos]
len(cocos_n)
len(set(cocos_n))
max(cocos_n)
min(cocos_n)
for x in range(57785):
    if x not in cocos_n:
        print x
        
style.split(';}.')
colors = [x[-7:] for x in style.split(';}.')]
colors
colors[0]
len(colors)
len(cocos_n)
cocos_n = [54901] + cocos_n
len(cocos_n)
cocodic = {}
for i in range(len(cocos_n)):
    cocodic[cocos_n[i]] = colors[i]
    
cocodic
import pickle
pickle.save
help(pickle)
f = open('cocodicc', 'w')
pickle.dump(cocodic, f)
f.close()
s
s.split('table')[1]
s.split('table')[2]
len(s.split('table')[2])
table = s.split('table')[2]
table.split('class=')
table.split('class="')
tablecocos = [x.split('"')[0] for x in table.split('class="')]
tablecocos
len(tablecocos)
set(tablecocos)
len(set(tablecocos))
len(cocos_n)
tablecocos_n = [int(x[4:]) for x in set(tablecocos)]
table.split('class="')
for x in table.split('class="'):
    if len(x.split('"')) != 2 or ' ' in x.split('"')[0]:
        print x
        
l = []
for x in table.split('class="'):
    if len(x.split('"')) != 2 or ' ' in x.split('"')[0]:
        l.append(x)
        
        
len(l)
exccocos_n = [int(x.split(' ')[0][4:]) for x in l]
l[0]
l = l[1:]
exccocos_n = [int(x.split(' ')[0][4:]) for x in l]
exccocos_n
len(exccocos_n)
set(exccocos_n)
len(exccocos_n)
len(set(exccocos_n))
for x in exccocos_n:
    print cocodic[x]
    
s.split('"')[0]
z = s.split('"')[0]
s.split('"')[-1]
for piece in s.split('"')[1:]:
    z += '"'
    if 'CoCo' in piece and not ' Co' in piece:
        z += 'CoCo0'    # null out
    else:
        z += piece      # keep
        
g = open('newcoco.html', 'w')
g.write(z)
g.close()
