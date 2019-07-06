from zoodb import *
from debug import *

import hashlib
import random

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    if cred.password == password:
        return newtoken(db, cred)
    else:
        return None

def register(username, password):
    db_person = person_setup()
    db_cred = cred_setup()

    person = db_person.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newperson.username = username

    newcred = Cred()
    newcred.username = username
    newcred.password = password

    db_person.add(newperson)
    db_person.commit()
    db_cred.add(newcred)
    db_cred.commit()
    return newtoken(db_cred, newcred)

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

