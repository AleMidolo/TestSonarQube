def select_female_under_age(self, age):
        """
        एक SQL कथन उत्पन्न करता है जो निर्दिष्ट आयु से कम महिलाओं का चयन करता है।
        :param age: int. निर्दिष्ट आयु।
        :return: str. उत्पन्न SQL कथन।
        >>> sql.select_female_under_age(30)
        "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        """
        condition = f"age < {age} AND gender = 'female'"
        return self.select(condition=condition)