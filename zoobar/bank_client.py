from debug import *
from zoodb import *
import rpclib

socket = '/banksvc/sock'
client = rpclib.client_connect(socket)

def validate(sender, token):
    with rpclib.client_connect('/authsvc/sock') as c:
        return c.call('check_token', username=sender, token=token)

def transfer(sender, token,  recipient, zoobars):
    if validate(sender, token):
        return client.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars)

def balance(username):
    return client.call('balance', username=username)    

def get_log(username):
    return client.call('get_log', username=username)

def newAccount(username):
    return client.call('newAccount', username=username)
