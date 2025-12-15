def select_female_under_age(self, age):
        """
        Genera un'istruzione SQL per selezionare le femmine sotto un'età specificata.
        :param age: int. L'età specificata.
        :return: str. L'istruzione SQL generata.
        >>> sql.select_female_under_age(30)
        "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        """
        condition = f"age < {age} AND gender = 'female'"
        return self.select(condition=condition)