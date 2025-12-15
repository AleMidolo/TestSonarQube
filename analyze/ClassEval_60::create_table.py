import sqlite3

class MovieTicketDB: 
    def __init__(self, db_name):
        """
        Initializes the MovieTicketDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :param movie_name: str, the name of the movie.
        :param theater_name: str, the name of the theater.
        :param seat_number: str, the seat number.
        :param customer_name: str, the name of the customer.
        :return: None
        """
        self.cursor.execute('''
                INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
                VALUES (?, ?, ?, ?)
            ''', (movie_name, theater_name, seat_number, customer_name))
        self.connection.commit()
    
    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> result = ticket_db.search_tickets_by_customer("John Doe")
        len(result) = 1
        """
        self.cursor.execute('''
                SELECT * FROM tickets WHERE customer_name = ?
            ''', (customer_name,))
        tickets = self.cursor.fetchall()
        return tickets
    
    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to delete.
        :return: None
        """
        self.cursor.execute('''
                DELETE FROM tickets WHERE id = ?
            ''', (ticket_id,))
        self.connection.commit()
    
    def create_table(self):
        """
        Crea una tabella "tickets" nel database se non esiste già. I campi includono ID di tipo int, nome del film di tipo str, nome del teatro di tipo str, numero del posto di tipo str e nome del cliente di tipo str.
        :return: None
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_name TEXT NOT NULL,
                theater_name TEXT NOT NULL,
                seat_number TEXT NOT NULL,
                customer_name TEXT NOT NULL
            )
        ''')
        self.connection.commit()