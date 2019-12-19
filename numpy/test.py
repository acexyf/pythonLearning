import re
str1 = 'South Korea: 136 分钟'
str2 = '115分钟(巴西)'
str7 = 'USA: 103 分钟(asqwe)'
str8 = "105min/119 min (unrated director's cut)"

str3 = '98分钟'
str4 = '98 分钟'
str5 = '128min'
str6 = '128 min'
str9 = '128 mins'
str10 = '128mins'
str11 = 'Hong Kong: 101 分钟'
str12 = '99 分钟(Hollywood Film Festival)'
str13 = 'USA: 84 分钟'
str14 = '1:37:42 (h:m:s)'

str15 = '110 Minutes'
str16 = '119 Mins'
str18 = '14:07'
str12 = '89'

def getDurationNum(strs):
    lists = re.findall(r'\d', strs)
    return ''.join(lists)

def parseInt(str):
    num = 0
    try:
        num = int(str)
    except:
        pass
    return num



matchObj1 = re.match(r'^[\w|\s]*\:?\s?\d+\s?[min|Min|mins|Mins|minutes|Minutes|分钟|].*$',str12)

matchObj2 = re.match(r'\d+:\d+:?\d+',str12)


match_str = matchObj2.group()

match_list = match_str.split(':')

print(matchObj1)
print(matchObj2)