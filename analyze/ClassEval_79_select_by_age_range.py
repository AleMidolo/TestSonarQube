def select_by_age_range(self, min_age, max_age):
    """
    निर्दिष्ट आयु सीमा के भीतर रिकॉर्ड चुनने के लिए एक SQL कथन उत्पन्न करता है।
    :param min_age: int. न्यूनतम आयु।
    :param max_age: int. अधिकतम आयु।
    :return: str. उत्पन्न SQL कथन।
    >>> sql.select_by_age_range(20, 30)
    'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
    """
    return f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"