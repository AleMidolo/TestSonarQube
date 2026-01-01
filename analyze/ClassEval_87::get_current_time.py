def get_current_time(self):
    """
        Restituisce l'ora corrente nel formato '%H:%M:%S'
        :return: stringa
        >>> timeutils = TimeUtils()
        >>> timeutils.get_current_time()
        "19:19:22"
        """
    format = '%H:%M:%S'
    return self.datetime.strftime(format)