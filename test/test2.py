import re
urls = 'https://www.dy2018.com/sdf'


urlpattern ='www.dy2018.com/i/\d+'


matchObj = re.search(urlpattern, urls)


print(matchObj)
