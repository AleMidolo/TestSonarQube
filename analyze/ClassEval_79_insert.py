def insert(self, data):
    """
        दिए गए डेटा के आधार पर एक INSERT SQL कथन उत्पन्न करता है।
        :param data: dict. डेटा जो डिक्शनरी रूप में डाला जाएगा जहाँ कुंजी फ़ील्ड नाम हैं और मान फ़ील्ड मान हैं।
        :return: str. उत्पन्न SQL कथन।
        >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
        "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
        """
    columns = ', '.join(data.keys())
    values = ', '.join([f"'{value}'" for value in data.values()])
    sql = f'INSERT INTO {self.table_name} ({columns}) VALUES ({values})'
    return sql + ';'