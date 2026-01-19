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
    
    # Create placeholders for values
    placeholders = ', '.join(['?' for _ in columns])
    
    # Prepare the INSERT SQL statement
    sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    
    # Extract values from each dictionary in the same order as columns
    values_list = []
    for row in data:
        values = tuple(row[col] for col in columns)
        values_list.append(values)
    
    # Execute the insert operation
    if hasattr(self, 'cursor') and hasattr(self, 'connection'):
        # For multiple rows
        self.cursor.executemany(sql, values_list)
        self.connection.commit()
    elif hasattr(self, 'conn'):
        # Alternative connection attribute name
        cursor = self.conn.cursor()
        cursor.executemany(sql, values_list)
        self.conn.commit()