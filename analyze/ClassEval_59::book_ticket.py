from datetime import datetime
import numpy as np

class MovieBookingSystem: 
    def __init__(self):
        """
        Initialize movies contains the information about movies
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        movie = {
            'name': name,
            'price': price,
            'start_time': datetime.strptime(start_time, '%H:%M'),
            'end_time': datetime.strptime(end_time, '%H:%M'),
            'seats': np.zeros((n, n))
        }
        self.movies.append(movie)

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')

        available_movies = []
        for movie in self.movies:
            if start_time <= movie['start_time'] and movie['end_time'] <= end_time:
                available_movies.append(movie['name'])

        return available_movies

    def book_ticket(self, name, seats_to_book):
        """
        Prenota i biglietti per un film. Cambia il valore dei posti in self.movies se la prenotazione ha successo.
        :param name: str, nome del film
        :param seats_to_book: lista di tuple, che rappresentano i posti da prenotare [(riga1, colonna1), (riga2, colonna2), ...]
        :return: str, messaggio di stato della prenotazione. "Film non trovato." se non esiste un film del genere.
                "Prenotazione riuscita." per una prenotazione avvenuta con successo, o "Prenotazione fallita." altrimenti
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
        'Prenotazione riuscita.'
        >>> system.book_ticket('Batman', [(0, 0)])
        'Prenotazione fallita.'
        >>> system.book_ticket('batman', [(0, 0)])
        'Film non trovato.'
        """
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                for seat in seats_to_book:
                    row, col = seat
                    if movie['seats'][row, col] == 0:
                        movie['seats'][row, col] = 1  # Mark seat as booked
                    else:
                        return 'Prenotazione fallita.'
                return 'Prenotazione riuscita.'
        return 'Film non trovato.'