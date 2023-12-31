from . import CURSOR 
from . import CONN

class Highscore:

    # --------- CLASS METHODS ---------- #
    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS highscores (
        id INTEGER PRIMARY KEY,
        name TEXT
        score INTEGER
        )
        """
        CURSOR.execute(sql)

    def __init__(self, name, score, id):
        self.name = name
        self.score = score
        self.id = id
        Highscore.create_table()

    def __repr__(self):
        return f"Highscore(id={self.id} name={self.name}, score={self.score})"
    
    def add_score(self):
        sql="""INSERT INTO highscores (name, score)
        VALUES (?, ?)
        """
        CURSOR.execute(sql, [self.name, self.score])
        CONN.commit()
        self.id = CONN.commit().lastrowid()