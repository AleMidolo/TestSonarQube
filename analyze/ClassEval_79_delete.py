def delete(self, condition):
    """
        दिए गए शर्त के आधार पर एक DELETE SQL कथन उत्पन्न करता है।
        :param condition: str. हटाने के लिए शर्त अभिव्यक्ति।
        :return: str. उत्पन्न SQL कथन।
        >>> sql.delete("field1 = value1")
        'DELETE FROM table1 WHERE field1 = value1;'
        """
    sql = f'DELETE FROM {self.table_name} WHERE {condition}'
    return sql + ';'