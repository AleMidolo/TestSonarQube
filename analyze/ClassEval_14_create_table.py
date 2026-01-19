def create_table(self):
    """
        यदि पुस्तक तालिका पहले से मौजूद नहीं है, तो डेटाबेस में पुस्तक तालिका बनाता है।
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS books (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                title TEXT NOT NULL,\n                author TEXT NOT NULL,\n                available INTEGER NOT NULL\n            )\n        ')
    self.connection.commit()