def get_minutes(self, string_time1, string_time2):
    """
    Calcola quanti minuti sono passati tra due orari e arrotonda il risultato al numero intero più vicino.
    :return: int, il numero di minuti tra due orari, arrotondato
    >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    60
    """
    from datetime import datetime
    
    # Parse the time strings into datetime objects
    time1 = datetime.strptime(string_time1, "%Y-%m-%d %H:%M:%S")
    time2 = datetime.strptime(string_time2, "%Y-%m-%d %H:%M:%S")
    
    # Calculate the difference in seconds
    time_diff = abs((time2 - time1).total_seconds())
    
    # Convert to minutes and round to nearest integer
    minutes = round(time_diff / 60)
    
    return minutes