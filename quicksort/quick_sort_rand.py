import random
def quick_sort(array,p,q):
    if p<q:
        r = partition(array,p,q)
        quick_sort(array,p,r-1)
        quick_sort(array,r+1,q)

def partition(array,p,q):
    r=random.randint(p,q)
    array[p],array[r]=array[r],array[p]
    key=array[p]
    i=p
    for j in range(p+1,q+1):
        if key>=array[j]:
           i=i+1
           array[i],array[j]=array[j],array[i]
    array[p],array[i]=array[i],array[p]
    return i

test = [5,2,4, 6, 1, 3]
quick_sort(test,0,len(test)-1)
print test
