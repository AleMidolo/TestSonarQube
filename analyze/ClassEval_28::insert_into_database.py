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
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    for entry in data:
        insert_query = f"INSERT INTO {table_name} ({', '.join(entry.keys())}) VALUES ({', '.join(['?' for _ in entry.values()])})"
        cursor.execute(insert_query, tuple(entry.values()))
    conn.commit()
    conn.close()