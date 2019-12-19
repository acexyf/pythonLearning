import MySQLdb
import re
import time


table_name = '80s_film_pre'


db = MySQLdb.connect("127.0.0.1", "root", "root", "xyf_db", charset='utf8' )

cursor = db.cursor()

cursor.execute("SELECT id,duration,duration_pre FROM "+table_name+" WHERE duration = 0 and duration_pre != ''")



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

print(cursor.rowcount, 'rowcount')

for index in range(cursor.rowcount):

    film_tuple = cursor.fetchone()
    ids = film_tuple[0]
    dura_pre = film_tuple[2]
    matchObj = re.match(r'^[\w|\s]*\:?\s?\d+\s?[min|Min|mins|Mins|minutes|Minutes|分钟|].*$',dura_pre)
    matchObj1 = re.match(r'\d+:\d+:?\d+',dura_pre)
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if matchObj != None:
        parse_dura = parseInt(getDurationNum(dura_pre))
        print('ids:'+str(ids)+' '+str(dura_pre)+' => '+str(parse_dura))
        sql = 'update '+table_name+' set duration=%d,update_time="%s" where id=%d' % (parse_dura, now, ids)
        print(sql)
        cur1 = db.cursor()
        try:
            cur1.execute(sql)
            db.commit()
        except:
            db.rollback()
            pass
    elif matchObj1 != None:
        match_str = matchObj1.group()
        match_list = match_str.split(':')
        parse_dura = 0
        if len(match_list) == 2:
            parse_dura = parseInt(match_list[0])
        elif len(match_list) == 3:
            parse_dura = parseInt(match_list[0]) * 60 + parseInt(match_list[1])

        print('ids:'+str(ids)+' '+str(dura_pre)+' => '+str(parse_dura))

        sql = 'update '+table_name+' set duration=%d,update_time="%s" where id=%d' % (parse_dura, now, ids)
        print(sql)
        cur1 = db.cursor()
        try:
            cur1.execute(sql)
            db.commit()
        except:
            db.rollback()
            pass

db.close()



