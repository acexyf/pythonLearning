import json

strs = '|file|[人人电影网：www.renrendianyingwang.cn]人兽杂交.Splice.2009.BD720P.中英双字.rmvb|1410927331|9F500CF4BEAF02A8460FB84DB073B8E8|h=4NRG2WMD6YSE4YMU4ASMKOVOEUZTUJDH|'

nums = []

nums.append({
    "name": "asd",
    "age": "15"
})

jsons = json.dumps(nums)

print(type(jsons))