def select_by_age_range(self, min_age, max_age):
    """
        生成一个 SQL 语句以选择指定年龄范围内的记录。
        :param min_age: int. 最小年龄。
        :param max_age: int. 最大年龄。
        :return: str. 生成的 SQL 语句。
        >>> sql.select_by_age_range(20, 30)
        'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
        """
    condition = f'age BETWEEN {min_age} AND {max_age}'
    return self.select(condition=condition)