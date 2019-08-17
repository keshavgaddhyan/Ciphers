
from rsa import *
value = 529
n = 493                                                                  
e = 11                                                                         
code = rsaencrypt( value, n, e )
print( value, "=>", code )