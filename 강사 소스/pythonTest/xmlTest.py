from bs4 import BeautifulSoup
import urllib.request as REQ

# jUrl='http://rss.joins.com/joins_news_list.xml'
kUrl = 'http://web.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'
response =REQ.urlopen(kUrl)
soup = BeautifulSoup( response, "html.parser" )
# print( soup )
for locElm in soup.findAll("location"):
    print(locElm.city.string)
    print('-'*30)
    for dataElm in locElm.findAll('data'):
        print('시간:', dataElm.tmef.string)
        print('날씨:', dataElm.wf.string)
        print('최저기온:', dataElm.tmn.string)
        print('최고기온:', dataElm.tmx.string)
        print('신뢰도:', dataElm.reliability.string)
    print('\n')



# for itemElm in soup.findAll('item'):
#     print("기사제목:", itemElm.title.string)
#     print("기사내용:", itemElm.description.string)
    
    
    
    
# fp = open("song.xml","r", encoding='utf-8')
# soup = BeautifulSoup( fp, "html.parser" )
# # print( soup )
# chanElm = soup.find('channel')
# songElm = soup.new_tag('song', sname='sname4') #{'sname':'sname4','aa':'aaa'}
# titleElm = soup.new_tag('title')
# titleElm.string ='노래4'
# singerElm = soup.new_tag('singer')
# singerElm.string ='singer4'
# songElm.append(titleElm)
# songElm.append(singerElm)
# chanElm.append(songElm)
# print( soup.prettify() )

# for songElm in soup.findAll('song'):
#     print( songElm['sname'] )
#     print(songElm.title.string)
#     print(songElm.singer.string)





