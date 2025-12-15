def get_minutes(self, string_time1, string_time2):
    """
    Calcola quanti minuti sono passati tra due orari e arrotonda il risultato al numero intero più vicino.
    :return: int, il numero di minuti tra due orari, arrotondato
    >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    60
    """
    
    dt1 = self.string_to_datetime(string_time1)
    dt2 = self.string_to_datetime(string_time2)
    delta = dt2 - dt1
    return round(delta.total_seconds() / 60)