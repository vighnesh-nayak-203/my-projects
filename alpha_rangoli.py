import time
def alpha_rangoli(n):
    l=[chr(i) for i in range(96+n,96,-1)]
    for i in range(1,2*n):
        time.sleep(0.5)
        a=[l[j] for j in range(n-abs(n-i))]
        c=[" " for j in range(abs(n-i))]
        b=a[:n-abs(n-i)-1]
        b.reverse()
        print(" ".join(c+a+b+c))
if __name__=="__main__":
    alpha_rangoli(7)