import os
import time

# serialNum = '10.101.160.116:5555'
serialNum = '1dd5a009'

serialStr = ''

if serialNum != '':
    serialStr = '-s ' + serialNum


def connect():
    os.system('adb connect ' + serialNum)

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


def checkDevice():
    deviceCode = myDevice()
    if deviceCode == 0:
        connect()
    elif deviceCode == 2:
        os.system('adb kill-server')
        os.system('adb start-server')
        # os.system('adb remount')

def saveImg(imgName = 's1.png'):
    # 截屏保存的文件目录
    dirPath = './'
    
    os.system('adb ' + serialStr + ' shell screencap -p /sdcard/' + imgName)
    os.system('adb ' + serialStr + ' pull /sdcard/' + imgName + ' ' + dirPath)

def tapPoint(point):
    x = point[0]
    y = point[1]
    os.system('adb ' + serialStr + ' shell input tap ' + str(x) + ' ' + str(y))



# 点亮屏幕
def lightUp():
    os.system('adb ' + serialStr + ' shell input keyevent 224')

# 点击home键
def clickHome():
    os.system('adb ' + serialStr + ' shell input keyevent 3')

# 切换应用
def changeApp():
    os.system('adb ' + serialStr + ' shell input keyevent 187')

# 点击返回按钮
def clickBack():
    os.system('adb ' + serialStr + ' shell input keyevent 4')

# 解锁屏幕
def unlockScreen():
    os.system('adb ' + serialStr + ' shell input swipe 300 1130 300 600')

# 翻页
def nextPage():
    os.system('adb ' + serialStr + ' shell input swipe 600 700 60 700')


# 清空应用
def clearApp():
    changeApp()
    tapPoint((70, 1165))
    time.sleep(5)
    clickHome()

# 打开app
def openApp():
    tapPoint((100, 125))
    time.sleep(8)

# 点击我的
def clickMy():
    tapPoint((650, 1200))
    time.sleep(5)

# 点击一行
def clickPunchLine():
    tapPoint((600, 440))
    time.sleep(8)

# 点击按钮
def clickPunchBtn():
    tapPoint((360, 940))
    time.sleep(8)


checkDevice()
lightUp()
unlockScreen()
clearApp()
clickHome()
nextPage()
nextPage()
nextPage()
nextPage()
nextPage()
openApp()
clickMy()
clickPunchLine()
# saveImg()
# clickPunchBtn()
# clickBack()
# clickBack()
# clickBack()
# clickBack()




