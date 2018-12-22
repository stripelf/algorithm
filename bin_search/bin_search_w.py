def bin_search(arr,t):
    low = 0 
    high = len(arr) - 1
    while (low <= high):
       mid=(low+high)//2
       if t<arr[mid]:
           high=mid+1
       elif t>arr[mid]:
           low=mid
       else:
           return mid

test=[8,9,6,4,5,10,18,89]
print bin_search(test,18)  
