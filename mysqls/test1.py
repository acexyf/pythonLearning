import time
import re

class Handler():
    def parseFloat(self, str):
        num = 0.0
        try:
            num = float(str)
        except:
            pass
        return num
    
    def parseInt(self, str):
        num = 0
        try:
            num = int(str)
        except:
            pass
        return num
    
    # 获取string中的数字
    def getInt(self, strs):
        lists = re.findall(r'\d', strs)
        return ''.join(lists)
    
    # 解析duration中的数字
    def getDurationNum(self, dura_pre):
        result = ''
        matchObj = re.match(r'^[\w|\s]*\:?\s?\d+\s?[min|Min|mins|Mins|minutes|Minutes|分钟|].*$',dura_pre)
        matchObj1 = re.match(r'\d+:\d+:?\d+',dura_pre)
        matchObj2 = re.match(r'^\d+$',dura_pre)
        if matchObj2 != None:
            result = self.getInt(dura_pre)
        elif matchObj != None:
            result = self.getInt(dura_pre)
        elif matchObj1 != None:
            match_str = matchObj1.group()
            match_list = match_str.split(':')
            if len(match_list) == 2:
                result = match_list[0]
            elif len(match_list) == 3:
                parse_num = self.parseInt(match_list[0]) * 60 + self.parseInt(match_list[1])
                result = str(parse_num)
                
        return result
    

myobj = Handler()


print(myobj.getDurationNum('128mins'))

