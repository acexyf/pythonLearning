def get_insert_sql(table_name, objs):
    key_list = objs.keys()
    value_list = objs.values()

    value_arr = []
    val_arr = []

    for item in value_list:
        if type(item) == int:
            val_arr.append(item)
            value_arr.append('%s') 
        elif type(item) == str:
            val_arr.append(item)
            value_arr.append('%s') 
        elif item == None: 
            value_arr.append('NULL') 

    sqls = 'insert into %s (%s) values (%s)' % (table_name, ','.join(key_list), ','.join(value_arr))
    return (sqls, tuple(val_arr))



def get_update_sql(table_name, objs, where_field = ''):
    value_arr = []
    where_sql = ''
    clone_obj = objs.copy()
    field_val = clone_obj[where_field]
    val_arr = []

    if where_field != '':
        del clone_obj[where_field]

    for key,val in clone_obj.items():
        if type(val) == int:
            value_arr.append(key + '=%s')
            val_arr.append(val)
        elif type(val) == str:
            value_arr.append(key + '=%s')
            val_arr.append(val)
        elif val == None:
            value_arr.append('%s=NULL' % key)

    if where_field != '':
        val_arr.append(field_val)
        if type(field_val) == int:
            where_sql = 'where '+where_field+' = %s' 
        elif type(field_val) == str:
            where_sql = 'where '+where_field+' = %s'

    if where_sql != '':
        sqls = 'update %s set %s %s' % (table_name, ','.join(value_arr), where_sql)
    else:
        sqls = 'update %s set %s' % (table_name, ','.join(value_arr))
    return (sqls, tuple(val_arr))


obj = {'id':5,"name": 'ace',"age":10, 'time': None,'skill': 'sdf"asd"'}
sqls = get_update_sql('sql_db', obj, 'id')
print(sqls)

