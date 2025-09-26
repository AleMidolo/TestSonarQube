import sqlite3


class UserLoginDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def insert_user(self, username, password):
        self._execute_query('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        ''', (username, password))

    def search_user_by_username(self, username):
        return self._fetch_one('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))

    def delete_user_by_username(self, username):
        self._execute_query('''
            DELETE FROM users WHERE username = ?
        ''', (username,))

    def validate_user_login(self, username, password):
        user = self.search_user_by_username(username)
        return self._is_valid_user(user, password)

    def _execute_query(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()

    def _fetch_one(self, query, params):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def _is_valid_user(self, user, password):
        return user is not None and user[1] == password