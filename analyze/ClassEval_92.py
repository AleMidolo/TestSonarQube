import sqlite3


class UserLoginDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def insert_user(self, username, password):
        self._execute_insert_user(username, password)

    def _execute_insert_user(self, username, password):
        self.cursor.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        ''', (username, password))
        self.connection.commit()

    def search_user_by_username(self, username):
        return self._fetch_user_by_username(username)

    def _fetch_user_by_username(self, username):
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self.cursor.fetchone()

    def delete_user_by_username(self, username):
        self._execute_delete_user(username)

    def _execute_delete_user(self, username):
        self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
        self.connection.commit()

    def validate_user_login(self, username, password):
        user = self.search_user_by_username(username)
        return self._is_valid_user(user, password)

    def _is_valid_user(self, user, password):
        return user is not None and user[1] == password