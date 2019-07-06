from zoodb import *
from debug import *

import time

def transfer(sender, recipient, zoobars):
    bankdb = bank_setup()
    sender = bankdb.query(Bank).get(sender)
    recipient = bankdb.query(Bank).get(recipient)

    sender_balance = sender.zoobars - zoobars
    recipient_balance = recipient.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    sender.zoobars = sender_balance
    recipient.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender.username
    transfer.recipient = recipient.username
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    db = bank_setup()
    bank = db.query(Bank).get(username)
    return bank.zoobars

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username, Transfer.recipient==username))

def newAccount(username):
    db = bank_setup()
    bank = Bank()
    bank.username = username
    db.add(bank)
    db.commit()
