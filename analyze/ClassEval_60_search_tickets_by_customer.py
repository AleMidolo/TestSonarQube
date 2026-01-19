def search_tickets_by_customer(self, customer_name):
    """
        "tickets" तालिका में ग्राहक के नाम द्वारा टिकटों की खोज करता है।
        :param customer_name: str, ग्राहक का नाम जिसे खोजा जाना है।
        :return: ट्यूपल की सूची, "tickets" तालिका की वे पंक्तियाँ जो खोज मानदंड से मेल खाती हैं।
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> result = ticket_db.search_tickets_by_customer("John Doe")
        len(result) = 1
        """
    self.cursor.execute('\n                SELECT * FROM tickets WHERE customer_name = ?\n            ', (customer_name,))
    return self.cursor.fetchall()