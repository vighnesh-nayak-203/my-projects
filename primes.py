from math import sqrt
def prime(n):
    if n==1:
        return False
    a=True
    k=0
    check=[j for j in range(2,int(sqrt(n))+1)]
    while k<len(check):
        i=check[k]
        if n%i==0:
            a=False
            break
        k+=1
    return a
def main():
    t=int(input("No. Test Cases:"))
    for i in range(t):
        p=prime(int(input("Case"+str(i+1)+":")))
        if p:
            print("Prime")
        else:
            print("Not prime")
if __name__=="__main__":    
    main()
