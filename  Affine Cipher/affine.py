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

def afencode (text,a,b):
    crypstr=""
    for i in text:
        if ord( i ) >= ord( 'a' ) and ord( i ) <= ord( 'z' ):
            x= ord(i)-ord( 'a' )
            y=(a*x+b)%26
            xc= chr(y+ord('a'))
        elif ord( i ) >= ord( 'A' ) and ord( i ) <= ord( 'Z' ):    
            x= ord(i)-ord( 'A' )
            y=(a*x+b)%26
            xc=chr(y+ord('A'))
        else:
            xc=i
        crypstr=crypstr+xc  
        
    return crypstr  
    
def afdecode(cipher,a,b):
    crypstr=""
    for i in cipher:
        if ord( i ) >= ord( 'a' ) and ord( i ) <= ord( 'z' ):
            x= ord(i)-ord( 'a' )
            y= mInverse(a,26)*(x-b)%26
            xc=chr(y+ord('a'))
        elif ord( i ) >= ord( 'A' ) and ord( i ) <= ord( 'Z' ):    
            x= ord(i)-ord( 'A' )
            y=mInverse(a,26)*(x-b)%26
            xc=chr(y+ord('A'))
        else:
            xc=i
        crypstr=crypstr+xc    
    return crypstr    
        
    
    