import sqlite3

connection = sqlite3.connect('scores.db')
cursor = connection.cursor()

#guard clause
#kannattaisko olla useampi filu tietokantaa varten vai kaikki yhteen?
cursor.execute('''
  CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    points INTEGER,
    gameID INTEGER
  );
''')

def savePlayer(name, score, gameID):
  cursor.execute('INSERT INTO scores (name, points, gameID) VALUES (?, ?, ?)', (name, score, gameID))
  connection.commit()

def getPlayer(name):
  cursor.execute('SELECT * FROM scores WHERE name = ?', (name,))#ei toimi, jos ei oo tuota commaa tossa
  playerData = cursor.fetchone()
  return playerData

def getHighScore():#tää hakis kaikki tiedot kannasta, sorttaa sen pelin ja ennenkaikkea pisteiden kautta, sit valitsee sieltä vaikka top10 printattavaks
  pass

def makeTestData():
  #("AKU", 100, 1),
  players = [
    ("AKU", 100, 1),
    ("TUPU", 101, 1),
    ("HUPU", 102, 1),
    ("LUPU", 103, 1),
    ("ROOPE", 104, 1),
    ("MIKKI", 105, 1),
    ("HESSU", 106, 1),
    ("IINES", 107, 1),
    ("KEKSIJÄ", 108, 1),
    ("MATAMI MIMMI", 109, 1),
    ("AKUN NAAPURI", 110, 1),
    ("KARHUKOPLA", 111, 1),
  ]

  for player in players:
    savePlayer(player[0], player[1], player[2])

def resetDB():
  pass


makeTestData()
akuData = getPlayer("AKU")
print(akuData)

#TODO testaa hakea kaikki tiedot
#

connection.close()
