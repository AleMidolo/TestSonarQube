def select_female_under_age(self, age):
    """
    生成一个 SQL 语句以选择指定年龄以下的女性。
    :param age: int. 指定的年龄。
    :return: str. 生成的 SQL 语句。
    >>> sql.select_female_under_age(30)
    "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
    """
    return f"SELECT * FROM table1 WHERE age < {age} AND gender = 'female';"