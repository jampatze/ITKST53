## This module wraps SQLalchemy's methods to be friendly to
## symbolic / concolic execution.

import fuzzy
import sqlalchemy.orm

oldget = sqlalchemy.orm.query.Query.get

def newget(query, primary_key):
  ## Exercise 5: your code here.
  ##
  ## Find the object with the primary key "primary_key" in SQLalchemy
  ## query object "query", and do so in a symbolic-friendly way.
  ##
  ## Hint: given a SQLalchemy row object r, you can find the name of
  ## its primary key using r.__table__.primary_key.columns.keys()[0]
  for r in query:
    if (primary_key == getattr(r, r.__table__.primary_key.columns.keys()[0])):
      return r

sqlalchemy.orm.query.Query.get = newget
