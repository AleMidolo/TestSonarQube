class SQLQueryBuilder:

    @staticmethod
    def select(table, columns='*', where=None):
        columns = SQLQueryBuilder._format_columns(columns)
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += SQLQueryBuilder._format_where(where)
        return query

    @staticmethod
    def insert(table, data):
        keys = ', '.join(data.keys())
        values = SQLQueryBuilder._format_values(data.values())
        return f"INSERT INTO {table} ({keys}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        query = f"DELETE FROM {table}"
        if where:
            query += SQLQueryBuilder._format_where(where)
        return query

    @staticmethod
    def update(table, data, where=None):
        update_str = ', '.join(f"{k}='{v}'" for k, v in data.items())
        query = f"UPDATE {table} SET {update_str}"
        if where:
            query += SQLQueryBuilder._format_where(where)
        return query

    @staticmethod
    def _format_columns(columns):
        return ', '.join(columns) if columns != '*' else '*'

    @staticmethod
    def _format_values(values):
        return ', '.join(f"'{v}'" for v in values)

    @staticmethod
    def _format_where(where):
        return " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())