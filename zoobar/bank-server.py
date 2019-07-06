#!/usr/bin/python

import rpclib
import sys
import bank
from debug import *
from sqlalchemy.orm import class_mapper

def serialize(model):
  columns = [c.key for c in class_mapper(model.__class__).columns]
  return dict((c, getattr(model, c)) for c in columns)

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, sender, recipient, zoobars):
        return bank.transfer(sender, recipient, zoobars)
    def rpc_balance(self, username):
        return bank.balance(username)
    def rpc_get_log(self, username):
        transfers = [
  	   serialize(row)
  	   for row in bank.get_log(username)
	]
        return transfers
    def rpc_newAccount(self, username):
        return bank.newAccount(username)

(_, dummy_zookld_fd, sockpath) = sys.argv 
s = BankRpcServer()
s.run_sockpath_fork(sockpath)
