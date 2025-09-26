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
        ''', (title, author, self._available_status()))

    def remove_book(self, book_id):
        self._execute_query('''
            DELETE FROM books WHERE id = ?
        ''', (book_id,))

    def borrow_book(self, book_id):
        self._update_availability(book_id, 0)

    def return_book(self, book_id):
        self._update_availability(book_id, 1)

    def search_books(self):
        self.cursor.execute('''
            SELECT * FROM books
        ''')
        return self.cursor.fetchall()

    def _update_availability(self, book_id, status):
        self._execute_query('''
            UPDATE books SET available = ? WHERE id = ?
        ''', (status, book_id))

    def _execute_query(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()

    def _available_status(self):
        return 1