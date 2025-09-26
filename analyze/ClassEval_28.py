import sqlite3
import pandas as pd


class DatabaseProcessor:

    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            self._execute_query(cursor, f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {key1} TEXT, {key2} INTEGER)")

    def insert_into_database(self, table_name, data):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            for item in data:
                self._execute_query(cursor, f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", (item['name'], item['age']))

    def search_database(self, table_name, name):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            result = self._fetch_query(cursor, f"SELECT * FROM {table_name} WHERE name = ?", (name,))
            return result if result else None

    def delete_from_database(self, table_name, name):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            self._execute_query(cursor, f"DELETE FROM {table_name} WHERE name = ?", (name,))

    def _execute_query(self, cursor, query, params=None):
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

    def _fetch_query(self, cursor, query, params=None):
        if params:
            cursor.execute(query, params)
            return cursor.fetchall()
        else:
            cursor.execute(query)
            return cursor.fetchall()