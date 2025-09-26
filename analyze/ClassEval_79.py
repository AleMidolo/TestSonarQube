class SQLGenerator:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        fields = self._get_fields(fields)
        sql = f"SELECT {fields} FROM {self.table_name}"
        if condition is not None:
            sql += f" WHERE {condition}"
        return sql + ";"

    def _get_fields(self, fields):
        return "*" if fields is None else ", ".join(fields)

    def insert(self, data):
        fields = self._get_fields_from_data(data)
        values = self._get_values_from_data(data)
        sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({values})"
        return sql + ";"

    def _get_fields_from_data(self, data):
        return ", ".join(data.keys())

    def _get_values_from_data(self, data):
        return ", ".join([f"'{value}'" for value in data.values()])

    def update(self, data, condition):
        set_clause = self._get_set_clause(data)
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}"
        return sql + ";"

    def _get_set_clause(self, data):
        return ", ".join([f"{field} = '{value}'" for field, value in data.items()])

    def delete(self, condition):
        sql = f"DELETE FROM {self.table_name} WHERE {condition}"
        return sql + ";"

    def select_female_under_age(self, age):
        condition = self._get_female_under_age_condition(age)
        return self.select(condition=condition)

    def _get_female_under_age_condition(self, age):
        return f"age < {age} AND gender = 'female'"

    def select_by_age_range(self, min_age, max_age):
        condition = self._get_age_range_condition(min_age, max_age)
        return self.select(condition=condition)

    def _get_age_range_condition(self, min_age, max_age):
        return f"age BETWEEN {min_age} AND {max_age}"