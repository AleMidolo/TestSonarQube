def select_by_age_range(self, min_age, max_age):
        """
        Genera un'istruzione SQL per selezionare record all'interno di un intervallo di età specificato.
        :param min_age: int. L'età minima.
        :param max_age: int. L'età massima.
        :return: str. L'istruzione SQL generata.
        >>> sql.select_by_age_range(20, 30)
        'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
        """
        condition = f"age BETWEEN {min_age} AND {max_age}"
        return self.select(condition=condition)