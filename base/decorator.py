def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper



@log #now = log(now)
def now():
    print('2018-05-29')

f = now

f()

print(now.__name__, f.__name__)


