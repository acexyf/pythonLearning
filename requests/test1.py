# import time, os ,threading

# print(os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0'))





from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time



def tick():
    print('run now')

scheduler = BlockingScheduler()
scheduler.add_job(tick, 'cron', hour=10,minute=37)


try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
