from primes import prime
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
if __name__=="__main__":
    per(277,0)