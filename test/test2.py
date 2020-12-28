import re
import time
# urls = 'https://www.dy2018.com/sdf'


# urlpattern ='www.dy2018.com/i/\d+'


# matchObj = re.search(urlpattern, urls)


# print(matchObj)


now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

item_url4 = "javascript:window.external.addFavorite('https://www.dy2018.com/','dy2018.com-电影天堂')"
item_url1 = 'https://www.dy2018.com/i/102682.html'
item_url2 = 'https://www.dy2018.com/html/zongyi2013/index.html'
item_url3 = 'ftp://dygod1:dygod1@d174.dygod.org:1016/%E6%B3%A1%E6%B2%AB%E4%B9%8B%E5%A4%8F/[%E7%94%B5%E5%BD%B1%E5%A4%A9%E5%A0%82www.dygod.org]%E6%B3%A1%E6%B2%AB%E4%B9%8B%E5%A4%8F08.rmvb'
item_url5 = 'https://www.jianpian.com/'
item_url6 = "https://www.dy2018.com/4/index.html"
item_url7 = 'https://www.dy2018.com/html/gndy/dyzz/index_2.html'


item_url = item_url7

url_pattern = 'https://www.dy2018.com\/.*'

detail_pattern ='https://www.dy2018.com/i/\d+'

urlObj = re.match(url_pattern, item_url)
detailObj = re.match(detail_pattern, item_url)

if urlObj != None:
    if detailObj == None:
        print('not detail')
    else:
        print('detail')
else:
    print('not this site')
# print(now)