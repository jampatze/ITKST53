from debug import *
from zoodb import *
import rpclib

socket = '/authsvc/sock'

def login(username, password):
    with rpclib.client_connect('/authsvc/sock') as c:
        ret = c.call('login', username=username, password=password)
        return ret    

def register(username, password):
    with rpclib.client_connect('/authsvc/sock') as c:
        ret = c.call('register', username=username, password=password)
        return ret

def check_token(username, token):
    with rpclib.client_connect('/authsvc/sock') as c:
        ret = c.call('check_token', username=username, token=token)
        return ret
