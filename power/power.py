def power(x,n):
    if n==1:
        return x
    if n%2==1:
        tmp=power(x,n//2)
        return tmp*tmp*x
    if n%2==0:
        tmp=power(x,n//2)
        return tmp*tmp

print power(2,5)
