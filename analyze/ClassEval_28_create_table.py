def create_table(self, table_name, key1, key2):
    """
    यदि डेटाबेस में तालिका मौजूद नहीं है तो एक नई तालिका बनाएं।
    और id (INTEGER) को PRIMARY KEY बनाएं, key1 को TEXT बनाएं, key2 को INTEGER बनाएं।
    :param table_name: str, बनाने के लिए तालिका का नाम।
    :param key1: str, तालिका में पहले कॉलम का नाम।
    :param key2: str, तालिका में दूसरे कॉलम का नाम।
    >>> db.create_table('user', 'name', 'age')
    """
    cursor = self.connection.cursor()
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        {key1} TEXT,
        {key2} INTEGER
    )
    """
    cursor.execute(create_table_query)
    self.connection.commit()