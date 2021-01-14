def function1(x,y):
    
    if ( y <= x ):
        return function1( x-y, y ) + 1
    else:
        return 1
        
def function2(n,r):
    
    if (n > 0 and r > 0 ):
        return function2( n-1, r ) + function2( n-1, r-1 )
    else:
        return 1

def function3(n):
    
    if ( n > 1 ):
        return function3(n/2) + 1
        
    else:
        return 1
        
def function4(m,n):
    
   if ( m == 0 or m >= n and n >= 1 ):
       return 1
   else:
       return function4( m-1, n ) + function4( m-1, n-1 )
        
def function5(m,x):
    
    def factorial(n):
        mul = 1
        for i in range(1,n+1):
           mul = mul * i
            
        return mul
        
    
    if ( m > x ):
        return factorial(m) / ( factorial(x) * factorial(m-x) )
    elif ( x == 0 ):
        return 1
    else:
        return function5( m, x-1 ) * ( ( m - x + 1 ) / x )
  
