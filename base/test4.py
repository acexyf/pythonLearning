import re

import pymysql



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



print(handleDate('2012-30-12'),int('30'))

conn = pymysql.connect(
    host="localhost",
    user="xyf",password="xyf930808",
    database="xyf_db",
    charset="utf8"
)


sql = 'select * from 80s_film_spider'

cursor = conn.cursor()

rowcount = cursor.execute(sql)



# for i in range(rowcount):
#     data = cursor.fetchone()
#     release_time = handleDate(data[12])
#     newsql = 'update 80s_film_spider set release_time="%s" where id=%d' % (release_time, data[0])
#     print(newsql)
#     newCursor = conn.cursor()
#     newCursor.execute(newsql)


# cursor.close()

# conn.close()


