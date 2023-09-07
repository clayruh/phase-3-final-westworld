import sqlite3

CONN = sqlite3.connect('./lib/db/highscores.db')
CURSOR = CONN.cursor()