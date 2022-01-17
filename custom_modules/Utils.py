import os


def cls(): return os.system('clear')


def log(arg=''): print('{}'.format(arg))


def bind_event(target, event, method):
    if type(target) != None and type(event) == str and type(method) != None:
        target.bind("<{}>".format(event), method)


be = bind_event

SERVER_BASE = {
    "syoutube": "https://www.youtube.com",
    "oyoutube": "http://www.youtube.com",
    "syt": "https://wwww.youtube.com",
    "oyt": "http://www.youtube.com"
}
