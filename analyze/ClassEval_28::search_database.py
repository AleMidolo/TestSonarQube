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
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        search_query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(search_query, (name,))
        results = cursor.fetchall()

        conn.close()
        return results if results else None