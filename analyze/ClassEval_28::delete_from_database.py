def delete_from_database(self, table_name, name):
    """
        निर्दिष्ट तालिका से डेटाबेस में मेल खाने वाले नाम के साथ पंक्तियाँ हटाएँ।
        :param table_name: str, पंक्तियाँ हटाने के लिए तालिका का नाम।
        :param name: str, हटाने के लिए मेल खाने वाला नाम।
        >>> db.delete_from_database('user', 'John')
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f'PRAGMA table_info({table_name})')
    columns_info = cursor.fetchall()
    name_column = None
    for col_info in columns_info:
        if col_info[2] == 'TEXT':
            name_column = col_info[1]
            break
    if name_column:
        delete_query = f'DELETE FROM {table_name} WHERE {name_column} = ?'
        cursor.execute(delete_query, (name,))
    elif len(columns_info) > 1:
        name_column = columns_info[1][1]
        delete_query = f'DELETE FROM {table_name} WHERE {name_column} = ?'
        cursor.execute(delete_query, (name,))
    conn.commit()
    conn.close()