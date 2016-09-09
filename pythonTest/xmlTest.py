from bs4 import BeautifulSoup
import urllib.request as REQ

url = 'http://rss.joins.com/joins_news_list.xml'
weather = 'http://web.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'
response= REQ.urlopen(weather)

soup = BeautifulSoup(response, 'html.parser')
# print(soup)
for itemElem in soup.findAll('location'):
    print(itemElem.city.string)
    print(10*'=')
    for d in itemElem.findAll('data'):
        print('날짜:', d.tmef.string)
        print('날씨:', d.wf.string)
        print('최저:', d.tmn.string)
        print('최고:', d.tmx.string)
        print(10*'-')
    

# fp = open('song.xml','r',encoding='utf-8')
# soup = BeautifulSoup(fp, "html.parser")
# # print (soup)
# chanElem = soup.find('channel')
# songElem = soup.new_tag('song', sname='sname4') #{'sname':'sname4', 'aa':'aaa'}
# titleElem = soup.new_tag('title')
# titleElem.string='song4'
# singerElem = soup.new_tag('singer')
# singerElem.string='singer4'
# 
# songElem.append(titleElem)
# songElem.append(singerElem)
# chanElem.append(songElem)
# 
# print(soup.prettify())

# for songElem in soup.findAll('song'):
#     print(songElem['sname'])
#     print(songElem.title.string)
#     print(songElem.singer.string)