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
  cursor.execute('INSERT INTO scores (name, score, gameID) VALUES (?, ?, ?)', (name, score, gameID))
  connection.commit()

def getPlayer(name, gameID):
  cursor.execute('SELECT * FROM scores WHERE name = ?', (name,))
  playerData = cursor.fetchone()
  return playerData

def getHighScore():#tää hakis kaikki tiedot kannasta, sorttaa sen pelin ja ennenkaikkea pisteiden kautta, sit valitsee sieltä vaikka top10 printattavaks
  pass

connection.close()
