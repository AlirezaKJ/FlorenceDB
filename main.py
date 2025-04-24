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


initdb()
print(dbfcontent)
print(type(dbfcontent))
changekey("temp", {"boom": 1, "boombamm": [1, 2, 3]})
print(dbfcontent)
print(type(dbfcontent))