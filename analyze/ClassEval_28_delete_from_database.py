def delete_from_database(self, table_name, name):
    """
    निर्दिष्ट तालिका से डेटाबेस में मेल खाने वाले नाम के साथ पंक्तियाँ हटाएँ।
    :param table_name: str, पंक्तियाँ हटाने के लिए तालिका का नाम।
    :param name: str, हटाने के लिए मेल खाने वाला नाम।
    >>> db.delete_from_database('user', 'John')
    """
    query = f"DELETE FROM {table_name} WHERE name = ?"
    self.cursor.execute(query, (name,))
    self.connection.commit()