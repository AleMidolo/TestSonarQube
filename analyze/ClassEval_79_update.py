def update(self, data, condition):
    """
    दिए गए डेटा और स्थिति के आधार पर एक UPDATE SQL कथन उत्पन्न करता है।
    :param data: dict. अपडेट किया जाने वाला डेटा, डिक्शनरी रूप में जहाँ कुंजी फ़ील्ड नाम हैं और मान नए फ़ील्ड मान हैं।
    :param condition: str. अपडेट के लिए स्थिति अभिव्यक्ति।
    :return: str. उत्पन्न SQL कथन।
    >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
    "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
    """
    # Build the SET clause
    set_clauses = []
    for field, value in data.items():
        # Add quotes around string values
        if isinstance(value, str):
            set_clauses.append(f"{field} = '{value}'")
        else:
            set_clauses.append(f"{field} = {value}")
    
    set_clause = ", ".join(set_clauses)
    
    # Build the complete UPDATE statement
    sql_statement = f"UPDATE {self.table} SET {set_clause} WHERE {condition};"
    
    return sql_statement