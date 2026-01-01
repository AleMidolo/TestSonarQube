def get_current_date(self):
    """
        Restituisce la data corrente nel formato "%Y-%m-%d"
        :return: stringa
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
    return self.datetime.strftime('%Y-%m-%d')