def __init__(self, db_name):
    self.db_name = db_name
    self.connection = sqlite3.connect(db_name)
    self.cursor = self.connection.cursor()