def delete_from_database(self, table_name, name):
        """
        निर्दिष्ट तालिका से डेटाबेस में मेल खाने वाले नाम के साथ पंक्तियाँ हटाएँ।
        :param table_name: str, पंक्तियाँ हटाने के लिए तालिका का नाम।
        :param name: str, हटाने के लिए मेल खाने वाला नाम।
        >>> db.delete_from_database('user', 'John')
        """
        
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        delete_query = f"DELETE FROM {table_name} WHERE name = ?"
        cursor.execute(delete_query, (name,))
        
        conn.commit()
        conn.close()