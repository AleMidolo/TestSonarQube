def select_by_age_range(self, min_age, max_age):
    """
    Generates a SQL statement to select records within a specified age range.
    :param min_age: int. The minimum age.
    :param max_age: int. The maximum age.
    :return: str. The generated SQL statement.
    >>> sql = SQLGenerator('table1')
    >>> sql.select_by_age_range(20, 30)
    'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
    """
    
    condition = f"age BETWEEN {min_age} AND {max_age}"
    return self.select(condition=condition)