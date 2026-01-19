def create_table(self, table_name, key1, key2):
    """
        यदि डेटाबेस में तालिका मौजूद नहीं है तो एक नई तालिका बनाएं।
        और id (INTEGER) को PRIMARY KEY बनाएं, key1 को TEXT बनाएं, key2 को INTEGER बनाएं।
        :param table_name: str, बनाने के लिए तालिका का नाम।
        :param key1: str, तालिका में पहले कॉलम का नाम।
        :param key2: str, तालिका में दूसरे कॉलम का नाम।
        >>> db.create_table('user', 'name', 'age')
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    create_table_query = f'\n        CREATE TABLE IF NOT EXISTS {table_name} (\n            id INTEGER PRIMARY KEY,\n            {key1} TEXT,\n            {key2} INTEGER\n        )\n        '
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()