import datetime

def d(message):
    return "{} - DEBUG: {}".format(str(datetime.datetime.now()), message)


def w(message):
    return "{} - WARNNING: {}".format(str(datetime.datetime.now()), message)


def e(message):
    return "{} - ERROR: {}".format(str(datetime.datetime.now()), message)


def v(message):
    return "{} - VERBOSE: {}".format(str(datetime.datetime.now()), message)


def i(message):
    return "{} - INFO: {}".format(str(datetime.datetime.now()), message)

