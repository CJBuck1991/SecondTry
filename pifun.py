import module math

def pifun(n): # Euler series
    pisqest=0.000
    for i in range(1,n+1):
        pisqest+=6/(i*i)
    return math.sqrt(pisqest)
    
