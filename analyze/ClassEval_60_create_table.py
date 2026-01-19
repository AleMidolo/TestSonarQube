def create_table(self):
    """
    यदि "tickets" तालिका पहले से मौजूद नहीं है, तो डेटाबेस में "tickets" तालिका बनाता है। फ़ील्ड में ID (int प्रकार), फ़िल्म का नाम (str प्रकार), थिएटर का नाम (str प्रकार), सीट नंबर (str प्रकार), और ग्राहक का नाम (str प्रकार) शामिल हैं।
    :return: None
    """
    cursor = self.conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            film_name TEXT NOT NULL,
            theater_name TEXT NOT NULL,
            seat_number TEXT NOT NULL,
            customer_name TEXT NOT NULL
        )
    ''')
    self.conn.commit()