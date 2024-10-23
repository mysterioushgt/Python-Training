import requests
from bs4 import BeautifulSoup
import pandas as pad

url ='https://www.icicibank.com/'
reqs= requests.get(url) #We are trying to open with the wesite
soup =BeautifulSoup(reqs.text,'html.parser')  #html.parser enables the 
alllinks=[]

fv=open("E:\\Website.Txt","a")  
for link in soup.find_all('a'):   #Any link <A Href ="XXX">
    print(link.get('href'))
    alllinks.append(link)
    
for x in alllinks:
    fv.write(str(x) + "\n")    
    
fv.close()    