# from lib import CURSOR # can't find lib?

class Highscore:

    # --------- CLASS METHODS ---------- #
    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS highscores(
        id INTEGER PRIMARY KEY,
        name TEXT
        )
        """
        CURSOR.execute(sql)

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Highscore(id={self.id} name={self.name})"