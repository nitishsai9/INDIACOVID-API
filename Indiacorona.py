from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ur
import requests
import json

URL='https://www.mohfw.gov.in/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page=requests.get(URL,headers=headers)
soup=bs(page.content,'html.parser')

tables=soup.find('tbody')
rows = tables.find_all('tr')
r=[]
must=[]
for row in rows:
    s=row.find_all('td')
    must.append([x.text.strip() for x in s])
c=0


links=[]
for row in rows:
    cold=row.find('a')['href']
    links.append(cold)







##############################################################################################
mains=soup.findAll("div", {"class": "content newtab"} )
for row in mains:
    cols=row.find_all('td')
    z=['0' if v.text.strip() == "" else v.text.strip() for v in cols]
x=z[:-5]
last=z[-5:]
chunks = [x[i:i+5] for i in range(0, len(x), 5)]
print(chunks)
#print(last)
#print(chunks)
#############################################################################################
#####ICON BLOCKS##############
l=[]
icon_main=soup.find_all("div",{"class":"information_block"})
for i in icon_main:
  counter=i.find_all("div",{"class":"iblock_text"})
  for j in counter:
    l.append(j.text.strip())
m=[]
for k in l:
  m.append(k.split('\n'))
t=[]
for k in range(len(m)):
  t.append(m[k][0])


d={
    "Stats":[]
    }
f={
    "StateWise":[]
}
est={
    "News":[]
    
}

air,act,cur,ded,mig=t
d["Stats"].append(
    {
        "Screend":air,
     "ActiveIndia":act,
     "Cured":cur,
     "Death":ded,
     "migration":mig
    }
)




for i in chunks:
    if len(i)==5:
        sno,st,conf,dis,deds=i
        f["StateWise"].append({
      "State":st,
      "confirm":conf,
      "Discharged":dis,
      "Deaths":deds
  }
      
  )

for i in range(len(must)):
  est["News"].append(
      {
      "date":must[i][0],
     "news":must[i][1],
     "Links":links[i],
      }
  )


