import json
DBPATH = "db.json"


def initdb():
  dbf = open(DBPATH, "r")
  global dbfcontent
  dbfcontent = json.load(dbf)
  dbf.close()


def savedb():
  dbf = open(DBPATH, "w")
  json.dump(dbfcontent, dbf, indent=4)
  dbf.close()


def changekey(key, value):
  dbfcontent[key] = value
  savedb()


def getkey(key):
  try:
    return dbfcontent[key]
  except:
    return None