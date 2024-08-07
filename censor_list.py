
def censor(words):
    print('start')
    w = None
    while True:
        word = yield w
        
        if word not in words:
            w = word
        else:
            w = '*' * len(word)
            
            
g = censor(['cow','donkey','monkey'])

next(g)

print(g.send('ali'))                 
print(g.send('sara'))                 
print(g.send('donkey'))                 
print(g.send('yara'))                 
print(g.send('monkey'))                 
print(g.send('john'))                 
print(g.send('cow'))


                 
            
    