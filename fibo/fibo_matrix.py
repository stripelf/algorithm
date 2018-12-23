def multi(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
    return c
def power(m,n):
    if n==1:
        return m
    if n>1 and n%2==1:
        tmp=power(m,n//2)
        return multi(multi(tmp,tmp),m)
    if n>1 and n%2==0:
        tmp=power(m,n//2)
        return multi(tmp,tmp)

def fibo(n):
    if n==0 or n==1:
        return n
    if n>1:
        m=[[1,1],[1,0]]
        tmp=power(m,n)
        return tmp[0][1]


print fibo(35)
       
      
