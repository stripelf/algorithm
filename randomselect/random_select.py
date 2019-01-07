def rand_select(array,p,q,i):
    if p==q:
        return A[p]
    r=partition(array,p,q)
    k=r-p+1
    if i==k:
        return array[k]
    if i<k:
        return rand_select(array,p,r-1,i)
    if i>k:
        return rand_select(array,r+1,q,i-k)  
    


def partition(array,p,q):
    key=array[p]
    i=p
    for j in range(p+1,q+1):
        if key>=array[j]:
           i=i+1
           array[i],array[j]=array[j],array[i]
    array[p],array[i]=array[i],array[p]
    return i


test = [5,2,4, 6, 1, 3]
print rand_select(test,0,len(test)-1,3)
print test
