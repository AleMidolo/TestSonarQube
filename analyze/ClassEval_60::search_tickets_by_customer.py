def search_tickets_by_customer(self, customer_name):
    """
    根据顾客名称在“tickets”表中搜索票据。
    :param customer_name: str，要搜索的顾客名称。
    :return: 元组列表，符合搜索条件的“tickets”表中的行。
    >>> ticket_db = MovieTicketDB("ticket_database.db")
    >>> ticket_db.create_table()
    >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
    >>> result = ticket_db.search_tickets_by_customer("John Doe")
    len(result) == 1
    """
    self.cursor.execute('\n            SELECT * FROM tickets WHERE customer_name = ?\n        ', (customer_name,))
    return self.cursor.fetchall()