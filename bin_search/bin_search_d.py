def bin_search(arr,low,high,t):
    mid=low+(high-low)//2
    if t==arr[mid]:
       return mid
    if t>arr[mid]:
       return bin_search(arr,mid+1,high,t)
    elif t<arr[mid]:
       return bin_search(arr,low,mid+1,t)

test=[8,9,6,4,5,10,18,89]
print bin_search(test,0,len(test),18)

