def search_database(self, table_name, name):
    """
    निर्दिष्ट तालिका को डेटाबेस में उन पंक्तियों के लिए खोजें जिनका नाम मेल खाता है।
    :param table_name: str, खोजने के लिए तालिका का नाम।
    :param name: str, खोजने के लिए नाम।
    :return: list, मेल खाते नाम वाली पंक्तियों का प्रतिनिधित्व करने वाले ट्यूपल की सूची, यदि कोई हो;
                अन्यथा, None लौटाता है।
    >>> db.search_database('user', 'John')
    [(1, 'John', 25)]
    """
    try:
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(query, (name,))
        results = cursor.fetchall()
        
        if results:
            return results
        else:
            return None
    except Exception as e:
        return None