def insert_into_database(self, table_name, data):
    """
    निर्दिष्ट तालिका में डेटा डालें।
    :param table_name: str, उस तालिका का नाम जिसमें डेटा डालना है।
    :param data: list, शब्दकोशों की एक सूची जहाँ प्रत्येक शब्दकोश डेटा की एक पंक्ति का प्रतिनिधित्व करता है।
    >>> db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
    """
    if not data:
        return
    
    # Get column names from the first dictionary
    columns = list(data[0].keys())
    column_names = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in columns])
    
    # Prepare the SQL INSERT statement
    sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    
    # Prepare the values for each row
    values_list = []
    for row in data:
        values = tuple(row[col] for col in columns)
        values_list.append(values)
    
    # Execute the insert operation
    cursor = self.connection.cursor()
    cursor.executemany(sql, values_list)
    self.connection.commit()