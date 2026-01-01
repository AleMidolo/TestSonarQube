def create_table(self):
    """
        यदि "tickets" तालिका पहले से मौजूद नहीं है, तो डेटाबेस में "tickets" तालिका बनाता है। फ़ील्ड में ID (int प्रकार), फ़िल्म का नाम (str प्रकार), थिएटर का नाम (str प्रकार), सीट नंबर (str प्रकार), और ग्राहक का नाम (str प्रकार) शामिल हैं।
        :return: None
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS tickets (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                movie_name TEXT NOT NULL,\n                theater_name TEXT NOT NULL,\n                seat_number TEXT NOT NULL,\n                customer_name TEXT NOT NULL\n            )\n        ')
    self.connection.commit()