def select_female_under_age(self, age):
    """
    Generates a SQL statement to select females under a specified age.
    :param age: int. The specified age.
    :return: str. The generated SQL statement.
    >>> sql.select_female_under_age(30)
    "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
    """
    return f"SELECT * FROM table1 WHERE age < {age} AND gender = 'female';"