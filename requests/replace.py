import re

strs = '基本内镜手术：<input type="checkbox" value="" name="hxnj1" id="hxnj11" checked="checked">支气管镜肺泡灌洗（BAL）<input type="checkbox" value="" name="hxnj2" id="hxnj12" checked="checked">经支气管镜透壁肺活检（TBLB）<input type="checkbox" value="" name="hxnj3" id="hxnj13" checked="checked">经气管镜超声引导下针吸活检（EBUS-TBNA）<input type="checkbox" value="" name="hxnj4" id="hxnj14" checked="checked">床旁气管镜应用危重病人诊治<br><span style="display:inline-block;width:93px"></span><input type="checkbox" value="" name="hxnj5" id="hxnj15" checked="checked">经气管镜超声引导下经鞘管活检（EBUS-GS）<input type="checkbox" value="" name="hxnj6" id="hxnj16" checked="checked">气道异物钳取术<input type="checkbox" value="" name="hxnj7" id="hxnj7">外周病灶小超声引导下经气管镜肺活检'

strs = re.sub(r'<span.*?>|<br>', '', strs)


result_list = []

checked_id = '3,6,7,14'

checked_id = ','+checked_id+','

ids = "hxnj"

print(strs, 'checked_id')

for item in re.finditer(r'id="'+ids+'\w*"', strs):
    id_str = item.group()

    find_id = re.search(r'\d{1,2}', id_str).group()


    if checked_id.find(','+find_id+',') != -1:

        str_start = strs.find('>', item.end())
        str_end = strs.find('<input', str_start)

        if str_end == -1:
            sub_str = strs[str_start+1:]
        else:
            sub_str = strs[str_start+1:str_end]

        print(sub_str, 'sub_str')





