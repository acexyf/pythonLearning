import re

dicts = {
    "str1":'2019-12-23',
    "str2":'2019',
    "str3":'2019-01',
    "str4":'2004-07-16(美国)',
    "str5":'2004-07-16 (美 国)',
    "str6":'2012年10月12日',
    "str7":'2011-11-11(美国/中国大陆)',
    "str8":'2012年',
    "str9":'2012年8月9日（美国）',
    "str10":'2012-11-01 / 2013-1-25（鹿特丹国际电影节）',
    "str11":'2012-01-21（圣丹斯电影节）/2012-09-14（美国）',
    "str12":'2012年8月（美国）',
    "str13":'2019-6',
    "str14": ''
}



lists = ['201','','234']
listss = [not x for x in lists]
print(listss)

def handleDate(strs):
    result = ''
    # 替换一些没用的字符
    strs = strs.replace(' ','').replace('（','(').replace('）',')').replace('年','-').replace('月','-').replace('日','')
    # 提取日期字符串
    find_list = re.findall(r'^\d{4}-*[0-9]*-*[0-9]*',strs)
    if len(find_list) != 0:
        # 把最后一个-去掉
        if find_list[0][-1] == '-':
            find_list[0] = find_list[0][:-1]
        # 按照-分隔
        data_list = find_list[0].split('-')
        if len(data_list) == 1:
            result = data_list[0]+'-01-01'
        elif len(data_list) == 2:
            data_list[1] = data_list[1].rjust(2, '0')
            result = data_list[0]+'-'+data_list[1]+'-01'
        elif len(data_list) == 3:
            data_list[1] = data_list[1].rjust(2, '0')
            data_list[2] = data_list[2].rjust(2, '0')
            result = data_list[0]+'-'+data_list[1]+'-'+data_list[2]
    else:
        result = '1900-01-01'
    return result



for i in range(1,15):
    print(dicts['str'+str(i)]+'  =>  '+handleDate(dicts['str'+str(i)]))
    pass


print()