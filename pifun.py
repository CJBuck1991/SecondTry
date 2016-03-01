import math # needed for square root function

def pifun(n): # Euler series
    pisqest=0.000 # initialize cumulative sum for pi^2
    for i in range(1,n+1): # sum level of series requested
        pisqest+=6/(i*i) # add each series term
    return math.sqrt(pisqest) # take square root
    
def piintfun(n):
    pisqest=0;
    for i in range(1,n+1):
        pisqest+=6000000000000000000000//(i*i)
    return pisqest    
    
if __name__ == "__main__":
    print("Number_of_Terms   Estimate")
    for n in (100,200,500,1000,2000,5000,10000,20000,50000,100000):
        print("%10u          %13.11f" % (n,pifun(n)))   
    print(" ")
    print("system value of pi is")
    print("%13.11f" % math.pi)
    print("system value of pi-squared is")
    print("%23.21f" % pi*pi)
    print(" ")
    print("Comparing 10000000 terms for Pisquare using integer vs float")
    z=pifun(10000000)
    zz=piintfun(10000000)
    print("%23.21f       \n%22u" % (z*z,zz))
