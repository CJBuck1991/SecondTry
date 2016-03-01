import module math # needed for square root function

def pifun(n): # Euler series
    pisqest=0.000 # initialize cumulative sum for pi^2
    for i in range(1,n+1): # sum level of series requested
        pisqest+=6/(i*i) # add each series term
    return math.sqrt(pisqest) # take square root
    
if __name__ == "__main__"":
    print("Number_of_Terms   Estimate")
    for n in (100,200,500,1000,2000,5000,10000,20000,50000,100000):
        print("10u%          13.11f%" % (n,pifun(n))   
