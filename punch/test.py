import os

# serialNum = '10.101.160.116:5555'
serialNum = '1dd5a009'

serialStr = ''

if serialNum != '':
    serialStr = '-s ' + serialNum


def myDevice():
    deviceLists = os.popen('adb devices').readlines()
    print(deviceLists)
    # 0没有设备 1 device 2 offline
    status = 0

    for item in deviceLists:
        if serialNum in item:
            if 'device' in item:
                status = 1
            if 'offline' in item:
                status = 2

    return status


def connect():
    os.system('adb connect ' + serialNum)



code = myDevice()
print(code,'code')

# if code == 2:

#     os.system('adb kill-server')
#     os.system('adb start-server')
#     os.system('adb remount')
#     connect()


# if code == 0:
#     connect()