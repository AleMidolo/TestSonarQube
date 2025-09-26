import sqlite3

class BookManagementDB:
    AVAILABLE = 1
    UNAVAILABLE = 0

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
        ''', (title, author, self.AVAILABLE))

    def remove_book(self, book_id):
        self._execute_query('''
            DELETE FROM books WHERE id = ?
        ''', (book_id,))

    def borrow_book(self, book_id):
        self._update_availability(book_id, self.UNAVAILABLE)

    def return_book(self, book_id):
        self._update_availability(book_id, self.AVAILABLE)

    def search_books(self):
        self.cursor.execute('''
            SELECT * FROM books
        ''')
        return self.cursor.fetchall()

    def _update_availability(self, book_id, availability):
        self._execute_query('''
            UPDATE books SET available = ? WHERE id = ?
        ''', (availability, book_id))

    def _execute_query(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()