def create_table(self):
    """
    यदि पुस्तक तालिका पहले से मौजूद नहीं है, तो डेटाबेस में पुस्तक तालिका बनाता है।
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.create_table()
    """
    cursor = self.connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE,
            publication_year INTEGER,
            quantity INTEGER DEFAULT 0
        )
    ''')
    self.connection.commit()