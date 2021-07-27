from primes import prime
from math import log,sqrt
def per(n,step):
    print(n)
    if len(str(n))==1:
        print(step)
        return n
    newn=1
    for i in str(n):
        newn*=int(i)
    step+=1
    return per(newn,step)
def factors(n):
    for i in range(int(sqrt(n)),1,-1):
        if n%i==0:
            a=int(log(n,i))
            n/=(i**a)
            print(str(i)*a,end=" ")
if __name__=="__main__":
    per(27887,0)
    print(prime(79))
    factors(27887)