def quick_sort(array,p,q):
    if p<q:
        r = partition(array,p,q)
        quick_sort(array,p,r-1)
        quick_sort(array,r+1,q)

def partition(array,p,q):
    key=array[p]
    i=p
    for j in range(p+1,q+1):
        if key>=array[j]:
           i=i+1
           tmp=array[j]
           array[j]=array[i]
           array[i]=tmp
    tmp=array[i]
    array[i]=key
    array[p]=tmp
    return i

test = [5,2,4, 6, 1, 3]
quick_sort(test,0,len(test)-1)
print test
