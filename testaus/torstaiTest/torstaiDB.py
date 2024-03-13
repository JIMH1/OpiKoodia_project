import sqlite3

connection = sqlite3.connect('torstai.db')
cursor = connection.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS torstai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    points INTEGER,
    gameID INTEGER,
    date TEXT
  );
''')


def savePlayer(name, score, gameID, datum):
  cursor.execute('INSERT INTO torstai (name, points, gameID, date) VALUES (?, ?, ?, ?)', (name, score, gameID, datum))
  connection.commit()

def getPlayer(name):
  cursor.execute('SELECT * FROM scores WHERE name = ?', (name,))#ei toimi, jos ei oo tuota commaa tossa
  playerData = cursor.fetchone()
  return playerData

connection.close()