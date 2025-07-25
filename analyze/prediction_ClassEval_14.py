import sqlite3

class BookManagementDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                available INTEGER
            )
        ''')
        self.connection.commit()

    def add_book(self, title, author):
        self._execute_query('''
            INSERT INTO books (title, author, available)
            VALUES (?, ?, ?)
        ''', (title, author, 1))

    def remove_book(self, book_id):
        self._execute_query('''
            DELETE FROM books WHERE id = ?
        ''', (book_id,))

    def borrow_book(self, book_id):
        self._execute_query('''
            UPDATE books SET available = ? WHERE id = ?
        ''', (0, book_id))

    def return_book(self, book_id):
        self._execute_query('''
            UPDATE books SET available = ? WHERE id = ?
        ''', (1, book_id))

    def search_books(self):
        self.cursor.execute('''
            SELECT * FROM books
        ''')
        return self.cursor.fetchall()

    def _execute_query(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()