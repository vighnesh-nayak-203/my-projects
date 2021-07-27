import time
def pascals_row(arr):
    ret_arr=[0]
    for i in range(len(arr)-2):
        ret_arr.append(arr[i]+arr[i+2])
    ret_arr.append(0)
    return ret_arr
def prnt(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            print(" ",end=" ")
        else:
            print(arr[i],end=" ")
    print()
def pascal(n):
    a=[0 for i in range((2*n)+1)]
    a[n]=1
    prnt(a)
    for i in range(n-1):
        time.sleep(0.5)
        a=pascals_row(a)
        prnt(a)
if __name__=="__main__":
    pascal(7)