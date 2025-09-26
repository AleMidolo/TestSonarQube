import sqlite3
import pandas as pd


class DatabaseProcessor:

    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            create_table_query = self._build_create_table_query(table_name, key1, key2)
            cursor.execute(create_table_query)

    def insert_into_database(self, table_name, data):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            for item in data:
                self._insert_item(cursor, table_name, item)

    def search_database(self, table_name, name):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            return self._fetch_results(cursor, table_name, name)

    def delete_from_database(self, table_name, name):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            self._delete_item(cursor, table_name, name)

    def _build_create_table_query(self, table_name, key1, key2):
        return f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {key1} TEXT, {key2} INTEGER)"

    def _insert_item(self, cursor, table_name, item):
        insert_query = f"INSERT INTO {table_name} (name, age) VALUES (?, ?)"
        cursor.execute(insert_query, (item['name'], item['age']))

    def _fetch_results(self, cursor, table_name, name):
        select_query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(select_query, (name,))
        result = cursor.fetchall()
        return result if result else None

    def _delete_item(self, cursor, table_name, name):
        delete_query = f"DELETE FROM {table_name} WHERE name = ?"
        cursor.execute(delete_query, (name,))