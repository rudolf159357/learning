from eng_words import  english
from de_words import german


gk = []
gv = []
ek = []
ev = []


for k,v in german.items():
    gk.append(k)
    gv.append(v)

for k,v in english.items():
    ek.append(k)
    ev.append(v)


q = input('choose lang(de/en): ')

if q == 'de':
    c = input('training/learning?: ')
    if c == 'training':
        for k,v in zip(gk, gv): 
            x = input(f'{k}: ')
            if x == v:
                print(f'Right, {k} - {v}')
            elif x == 'quit':
                break
            else:
                print(f'Wrong! its {k} - {v} ')
    elif c == 'learning':
        for k,v in zip(gk, gv):
            print(f'{k} - {v}')
        e = input('want end?: ')
        if e == 'yes' or 'y':
            quit
        else:
            quit
    else:
        quit
    
elif q == 'en':
    c = input('training/learning?: ')
    if c == 'training':
        for k,v in zip(ek, ev): 
            x = input(f'{k}: ')
            if x == v:
                print(f'Right, {k} - {v}')
            elif x == 'quit':
                break 
            else:
                print(f'Wrong! its {k} - {v} ')
    elif c == 'learning':
        for k,v in zip(ek, ev):
            print(f'{k} - {v}')
        e = input('want end?: ')
        if e == 'yes' or 'y':
            quit        
        else:
            quit
                
    else:
        quit
else:
    quit
