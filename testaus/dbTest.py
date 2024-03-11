import sqlite3

connection = sqlite3.connect('scores.db')
cursor = connection.cursor()

def savePlayer(name, score):
  cursor.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (name, score))
  connection.commit()

def getPlayer(name):
  cursor.execute('SELECT * FROM scores WHERE name = ?', (name,))
  playerData = cursor.fetchone()
  return playerData

connection.close()
