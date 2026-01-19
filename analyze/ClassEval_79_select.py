def select(self, fields=None, condition=None):
    """
    निर्दिष्ट फ़ील्ड और शर्तों के आधार पर एक SELECT SQL कथन उत्पन्न करता है।
    :param fields: सूची, वैकल्पिक। डिफ़ॉल्ट None है। क्वेरी किए जाने वाले फ़ील्ड की सूची।
    :param condition: str, वैकल्पिक। डिफ़ॉल्ट None है। क्वेरी के लिए शर्त अभिव्यक्ति।
    :return: str। उत्पन्न SQL कथन।
    >>> sql = SQLGenerator('table1')
    >>> sql.select(['field1', 'field2'], 'filed3 = value1')
    'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
    """
    # Determine which fields to select
    if fields is None or len(fields) == 0:
        field_str = '*'
    else:
        field_str = ', '.join(fields)
    
    # Build the base SELECT statement
    sql = f'SELECT {field_str} FROM {self.table_name}'
    
    # Add WHERE clause if condition is provided
    if condition is not None and condition != '':
        sql += f' WHERE {condition}'
    
    # Add semicolon at the end
    sql += ';'
    
    return sql