
def hash(key,m):
    return key%m

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

hashtable=[None for i in range(1,18)]

insert(23,hashtable)
print hashtable
print search(23,hashtable)

insert(159,hashtable)
print hashtable
print search(159,hashtable)

delete(159,hashtable)
print hashtable

