class SQLGenerator:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        fields = self._get_fields(fields)
        sql = f"SELECT {fields} FROM {self.table_name}"
        if condition is not None:
            sql += f" WHERE {condition}"
        return self._finalize_query(sql)

    def insert(self, data):
        fields = ", ".join(data.keys())
        values = self._format_values(data.values())
        sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({values})"
        return self._finalize_query(sql)

    def update(self, data, condition):
        set_clause = self._format_set_clause(data)
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}"
        return self._finalize_query(sql)

    def delete(self, condition):
        sql = f"DELETE FROM {self.table_name} WHERE {condition}"
        return self._finalize_query(sql)

    def select_female_under_age(self, age):
        condition = self._get_female_under_age_condition(age)
        return self.select(condition=condition)

    def select_by_age_range(self, min_age, max_age):
        condition = self._get_age_range_condition(min_age, max_age)
        return self.select(condition=condition)

    def _get_fields(self, fields):
        return "*" if fields is None else ", ".join(fields)

    def _format_values(self, values):
        return ", ".join([f"'{value}'" for value in values])

    def _format_set_clause(self, data):
        return ", ".join([f"{field} = '{value}'" for field, value in data.items()])

    def _finalize_query(self, sql):
        return sql + ";"

    def _get_female_under_age_condition(self, age):
        return f"age < {age} AND gender = 'female'"

    def _get_age_range_condition(self, min_age, max_age):
        return f"age BETWEEN {min_age} AND {max_age}"