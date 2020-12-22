def get_insert_sql(table_name, objs):
    key_list = objs.keys()
    value_list = objs.values()

    value_arr = []

    for item in value_list:
        if type(item) == int:
            value_arr.append('%d' %item) 
        elif type(item) == str:
            value_arr.append('"%s"' % item) 

    sqls = 'insert into %s (%s) values (%s)' % (table_name, ','.join(key_list), ','.join(value_arr))
    return sqls

def get_update_sql(table_name, objs, where_field = ''):
    value_arr = []
    where_sql = ''

    if where_field != '':
        field_val = objs[where_field]
        del objs[where_field]
        if type(field_val) == int:
            where_sql = 'where %s = %d' % (where_field, field_val)
        elif type(field_val) == str:
            where_sql = 'where %s = "%s"' % (where_field, field_val)

    for key,val in objs.items():
        if type(val) == int:
            value_arr.append('%s=%d' % (key, val))
        elif type(val) == str:
            value_arr.append('%s="%s"' % (key, val))

    if where_sql != '':
        sqls = 'update %s set %s %s' % (table_name, ','.join(value_arr), where_sql)
    else:
        sqls = 'update %s set %s' % (table_name, ','.join(value_arr))
    return sqls

print(get_update_sql('sql_db', {'id':'5',"name": 'ace',"age":10}, ''))

