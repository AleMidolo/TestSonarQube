def update(self, data, condition):
        """
        दिए गए डेटा और स्थिति के आधार पर एक UPDATE SQL कथन उत्पन्न करता है।
        :param data: dict. अपडेट किया जाने वाला डेटा, डिक्शनरी रूप में जहाँ कुंजी फ़ील्ड नाम हैं और मान नए फ़ील्ड मान हैं।
        :param condition: str. अपडेट के लिए स्थिति अभिव्यक्ति।
        :return: str. उत्पन्न SQL कथन।
        >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
        "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        """
        
        set_clause = ", ".join([f"{key} = '{value}'" for key, value in data.items()])
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}"
        return sql + ";"