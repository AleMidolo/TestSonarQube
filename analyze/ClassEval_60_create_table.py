def __init__(self, db_name='tickets.db'):
    self.db_name = db_name
    self.conn = None
    self.cursor = None