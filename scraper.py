from os import write
from bs4 import BeautifulSoup
import requests
import csv

def markscard(a):
    n=a[0]
    d=a[1]
    m=a[2]
    y=a[3]
    url="https://karresults.nic.in/res_sslc_kar21.asp"
    page=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"},verify=False,data={"frm_tokens":"0.1186334","InputRegno":str(n),"ddlday":str(d),"ddlmon":str(m) ,"ddlyear":str(y)})
    soup=BeautifulSoup(page.content,"html5lib")
    b=soup.find_all("td",attrs={"class":"textright"})
    a=soup.find_all("span",attrs={"style":"font-weight: bold"})
    m=[]
    for i in a[:2]:
        m.append(i.text.strip())
    for i in range(1,int((len(b)-1)/4)+1):    
        s=b[4*i-2].text.strip()
        m.append(s)
    # m.append(b[len(b)-1].text.strip())
    return m
def find():
    s=20210132000
    k=[]
    while s<=20210132200:
        print(s)
        a=markscard([s,"01","03","2005"])
        if a!=[]:
            print(a)
            k.append(a)
        s+=1
    print(k)
    print("ok")
"""   
699S    
f=open("markslist.csv","a")
w=csv.writer(f)
#while True:
n=str(input("reg no:"))
d=str(input("day"))
m=str(input("m"))
y=str(input("y"))
print(markscard([n,"01","03","2005"]))
w.writerow(markscard([n,d,m,y]))
f.close()
"""
find()