import math

def hash(key,m):
    A=111
    return (key*A%pow(2,7))>>(7-int(math.log(m,2)))
    
def insert(key,hashtable):
    addr=hash(key,len(hashtable))
    while hashtable[addr]:
        addr+=1
        addr=addr%len(hashtable)
    hashtable[addr]=key

def search(key,hashtable):
    addr=hash(key,len(hashtable))
    while hashtable[addr] and hashtable[addr]!=key:
        addr+=1
        addr=addr%len(hashtable)
    if hashtable[addr]==None:
        return None
    return addr

def delete(key,hashtable):
    addr=search(key,hashtable)
    if addr:
        hashtable[addr]=None       

hashtable=[None for i in range(1,17)]

insert(7,hashtable)
print hashtable
print search(7,hashtable)

insert(18,hashtable)
print hashtable
print search(18,hashtable)

delete(18,hashtable)
print hashtable

