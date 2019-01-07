import random
def counting_sort(a,k):
    b=[0 for i in range(0,len(a))]
    c=[0 for i in range(0,k+1)]
    for i in a:
        c[i]+=1
    for i in range(1,k+1):
        c[i]=c[i]+c[i-1]
    for i in a:
        b[c[i]-1]=i
        c[i]-=1
    return b

a=[random.randint(0,12) for i in range(0,20)]
print counting_sort(a,12)
