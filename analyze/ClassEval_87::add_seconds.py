def add_seconds(self, seconds):
        """
        Aggiungi il numero specificato di secondi all'ora corrente
        :param seconds: int, numero di secondi da aggiungere
        :return: stringa, ora dopo aver aggiunto il numero specificato di secondi nel formato '%H:%M:%S'
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """
        new_time = self.datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime("%H:%M:%S")