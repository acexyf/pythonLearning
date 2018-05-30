def _private1(name):
    return 'Hello, %s' % name


def _private2(name):
    return 'Hi, %s' % name


def greet(name):
    if len(name) >3:
        return _private1(name)
    else:
        return _private2(name)


print(__name__)