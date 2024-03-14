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


def savePlayer(name, score):
  cursor.execute('INSERT INTO torstai (name, points) VALUES (?, ?)', (name, score))
  connection.commit()

def getPlayer(name):
  cursor.execute('SELECT * FROM torstai WHERE name = ?', (name,))#ei toimi, jos ei oo tuota commaa tossa
  playerData = cursor.fetchone()
  return playerData

connection.close()