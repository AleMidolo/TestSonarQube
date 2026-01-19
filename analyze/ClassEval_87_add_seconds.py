def add_seconds(self, seconds):
    """
    Aggiungi il numero specificato di secondi all'ora corrente
    :param seconds: int, numero di secondi da aggiungere
    :return: stringa, ora dopo aver aggiunto il numero specificato di secondi nel formato '%H:%M:%S'
    >>> timeutils.add_seconds(600)
    "19:29:22"
    """
    from datetime import datetime, timedelta
    
    # Get current time
    current_time = datetime.now()
    
    # Add the specified seconds
    new_time = current_time + timedelta(seconds=seconds)
    
    # Return formatted time string
    return new_time.strftime('%H:%M:%S')