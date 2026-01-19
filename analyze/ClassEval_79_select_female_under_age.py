def select_female_under_age(self, age):
    """
    Genera una declaración SQL para seleccionar mujeres menores de una edad especificada.
    :param age: int. La edad especificada.
    :return: str. La declaración SQL generada.
    >>> sql.select_female_under_age(30)
    "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
    """
    return f"SELECT * FROM table1 WHERE age < {age} AND gender = 'female';"