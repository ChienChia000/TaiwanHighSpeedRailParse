import requests
from bs4 import BeautifulSoup

theDay=input("幾號要搭車: ")
start=input("出發站： ")
if start=='南港':
	startStation='2f940836-cedc-41ef-8e28-c2336ac8fe68'
elif start=='台北':
    startStation='977abb69-413a-4ccf-a109-0272c24fd490'
elif start=='板橋':
    startStation='e6e26e66-7dc1-458f-b2f3-71ce65fdc95f'
elif start=='桃園':
    startStation='fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'
elif start=='新竹':
    startStation='a7a04c89-900b-4798-95a3-c01c455622f4'
elif start=='苗栗':
    startStation='e8fc2123-2aaf-46ff-ad79-51d4002a1ef3'
elif start=='台中':
    startStation='3301e395-46b8-47aa-aa37-139e15708779'
elif start=='彰化':
    startStation='38b8c40b-aef0-4d66-b257-da96ec51620e'
elif start=='雲林':
    startStation='5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f'
elif start=='嘉義':
    startStation='60831846-f0e4-47f6-9b5b-46323ebdcef7'
elif start=='台南':
    startStation='9c5ac6ca-ec89-48f8-aab0-41b738cb1814'
elif start=='左營':
    startStation='f2519629-5973-4d08-913b-479cce78a356'

end=input("目的站： ")
if end=='南港':
	endStation='2f940836-cedc-41ef-8e28-c2336ac8fe68'
elif end=='台北':
    endStation='977abb69-413a-4ccf-a109-0272c24fd490'
elif end=='板橋':
    endStation='e6e26e66-7dc1-458f-b2f3-71ce65fdc95f'
elif end=='桃園':
    endStation='fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'
elif end=='新竹':
    endStation='a7a04c89-900b-4798-95a3-c01c455622f4'
elif end=='苗栗':
    endStation='e8fc2123-2aaf-46ff-ad79-51d4002a1ef3'
elif end=='台中':
    endStation='3301e395-46b8-47aa-aa37-139e15708779'
elif end=='彰化':
    endStation='38b8c40b-aef0-4d66-b257-da96ec51620e'
elif end=='雲林':
    endStation='5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f'
elif end=='嘉義':
    endStation='60831846-f0e4-47f6-9b5b-46323ebdcef7'
elif end=='台南':
    endStation='9c5ac6ca-ec89-48f8-aab0-41b738cb1814'
elif end=='左營':
    endStation='f2519629-5973-4d08-913b-479cce78a356'

timeSelect=input("幾點出發： ")

#print(timeSelect[2])

#startStation='977abb69-413a-4ccf-a109-0272c24fd490'
#endStation='9c5ac6ca-ec89-48f8-aab0-41b738cb1814'
#theDay='2018/12/13'
#timeSelect='06:00'

print(theDay, start, end, timeSelect)
payload = {
    'startStation':startStation,
    'endStation':endStation,
    'theDay':theDay,
    'timeSelect':timeSelect,
    'waySelect':'DepartureInMandarin'
}

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}

res = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResult",data=payload,headers=headers)


#print(res.text)

soup=BeautifulSoup(res.text,features="html.parser")

#print(soup)

trainData=[]
flag=0

divs = soup.find_all('a', 'ui-block-a')
for d in divs:
    #print(d.find('div').string.lstrip())
    trainData.append(d.find('div').string.lstrip())
    flag+=1

flag=0
divs = soup.find_all('a', 'ui-block-b')
for d in divs:
    #print(d.find('div').string.lstrip())
    trainData[flag]+=" "
    trainData[flag]+=(d.find('div').string.lstrip())
    flag+=1

flag=0
divs = soup.find_all('a', 'ui-block-c')
for d in divs:
    #print(d.find('div').string.lstrip())
    trainData[flag]+=" "
    trainData[flag]+=(d.find('div').string.lstrip())
    #trainData[flag]+="\n"
    flag+=1

for i in trainData:
    print(i)
