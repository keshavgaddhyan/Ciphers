def mInverse( a, n ):
    r0, r1, t0, t1 = n, a, 0, 1
    while r1 > 1:
        q = r0 // r1
        r2 = r0 - r1 * q
        t2 = t0 - t1 * q
        r0, r1 = r1, r2
        t0, t1 = t1, t2
 
    if r1 == 1:
        return t1 % n
    return 0

def rsaencrypt(value,n,e):
    return pow(value,e,n)
    
def rsadecrypt(value,n,d):
    return pow(value,d,n)
    
def rsahack(n,e):
    for i in range(1,n):
        if n%i==0:
            x=i
            y=n//i
    fact=(x-1)*(y-1)    
    return mInverse(e,fact)
    